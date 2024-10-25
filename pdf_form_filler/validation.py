from pdf_form_filler.errors import ValidationError
from typing import List
import os
import re
import warnings

# PDF Fields


# def validate_for_duplicate_text_fields(writer: PdfWriter):
#     fields = writer.get_fields()

#     dupe_fields = {}
#     for name, field in fields.items():
#         kids = field["/Kids"]

#         if len(kids) > 1:
#             if name in dupe_fields:
#                 dupe_fields[name] += len(kids)
#             else:
#                 dupe_fields[name] = len(kids)

#     if len(dupe_fields) > 0:
#         raise ValidationError(f"pdf contains duplicate text fields: {dupe_fields}")


# Table Columns


def validate_for_duplicate_columns(columns: List[str]):

    # check empty cols
    if len(columns) == 0:
        raise ValidationError("received an empty column list")

    # check actual duplicates
    col_set = set({})
    true_duplicate_col_set = set({})
    for col in columns:
        if col not in col_set:
            col_set.add(col)
        else:
            true_duplicate_col_set.add(col)

    if len(true_duplicate_col_set) > 0:
        raise ValidationError(f"input table contains duplicate column(s): {sorted(list(true_duplicate_col_set))}")

    # check duplicates renamed by pandas read_csv
    dupe_column_pattern = r"(.*)\.\d*$"
    potential_duplicate_columns = []
    for col in columns:
        m = re.match(dupe_column_pattern, col)
        if m is not None:
            potential_duplicate_columns.append(col)

    if len(potential_duplicate_columns) > 0:
        raise ValidationError(
            f"input table contains potential duplicate column(s): {sorted(list(potential_duplicate_columns))}. if the column is NOT supposed to contain the .NUM suffix, then the root column is a duplicate. if it is supposed to, rename it."
        )


def validate_file_name_column(columns: List[str]):
    if "file_name" not in columns:
        raise ValidationError(f"file_name column missing from input table.")


# Both


def validate_fields_and_columns(fields: List[str], columns: List[str]):

    field_set = set(fields)
    col_set = set(columns)

    fields_not_in_cols = field_set.difference(col_set)
    cols_not_in_fields = col_set.difference(field_set)

    if len(fields_not_in_cols) > 0:
        warnings.warn(f"The following pdf field names do not have a corresponding table column: {sorted(list(fields_not_in_cols))}.")

    if len(cols_not_in_fields) > 0:
        warnings.warn(f"The following table columns do not have a corresponding pdf field name: {sorted(list(cols_not_in_fields))}.")


# Directory Structure


def validate_directory_structure():
    cwd = os.getcwd()

    subfolders = set([os.path.basename(f) for f in os.scandir(cwd) if f.is_dir()])

    # input table folder
    if "input_table" not in subfolders:
        raise ValidationError(
            f"input_table directory not found in current working directory: {cwd}. to proceed, create an input_table folder and place your table in it."
        )

    ## input table file
    input_table_dir = os.path.join(cwd, "input_table")
    input_table_files = os.listdir(input_table_dir)
    if len(input_table_files) == 0:
        raise ValidationError(f"no input table found in input_table directory")
    if len(input_table_files) > 1:
        raise ValidationError(f"expected 1 file in input_table directory, found {len(input_table_files)}: {input_table_files}")

    ### file ext
    input_table_file = input_table_files[0]
    input_table_ext = os.path.splitext(input_table_file)[1]
    if input_table_ext != ".csv":
        raise ValidationError(f"input_table file extension must be .csv, got: {input_table_ext}")

    # input pdf template folder
    if "input_pdf_template" not in subfolders:
        raise ValidationError(
            f"input_pdf_template directory not found in current working directory: {cwd}. to proceed, create an input_pdf_template folder and place your template in it."
        )

    ## input pdf template file
    input_template_dir = os.path.join(cwd, "input_pdf_template")
    input_template_files = os.listdir(input_template_dir)
    if len(input_template_files) == 0:
        raise ValidationError(f"no input template found in input_pdf_template directory")
    if len(input_template_files) > 1:
        raise ValidationError(f"expected 1 file in input_pdf_template directory, found {len(input_template_files)}: {input_template_files}")

    ### file ext
    input_template_file = input_template_files[0]
    input_template_ext = os.path.splitext(input_template_file)[1]
    if input_template_ext != ".pdf":
        raise ValidationError(f"input_pdf_template file extension must be .pdf, got: {input_template_ext}")


def validate_output_folder() -> bool:
    cwd = os.getcwd()

    subfolders = set([os.path.basename(f) for f in os.scandir(cwd) if f.is_dir()])

    if "filled_pdfs" not in subfolders:
        print("no output folder found, creating one")
        output_dir_path = os.path.join(cwd, "filled_pdfs")
        os.makedirs(output_dir_path)


#####
