from pdf_form_filler.utils import PDFFiller, load_input_table
import pandas as pd
import re

from pdf_form_filler.validation import (
    validate_directory_structure,
    validate_for_duplicate_columns,
    validate_fields_and_columns,
    validate_output_folder,
    validate_file_name_column,
)


def _clean_filename(input_string):
    cleaned_string = re.sub(r"[^a-zA-Z0-9\s]", "", input_string)
    cleaned_string = cleaned_string.replace(" ", "_")
    cleaned_string = cleaned_string.lower()

    return cleaned_string


def fill_forms(table: pd.DataFrame, pdf_filler: PDFFiller, clean_filename=False):

    for ri, row in table.iterrows():
        row = row.to_dict()

        file_name = str(row["file_name"])
        row.pop("file_name")

        if clean_filename:
            file_name = _clean_filename(file_name)

        pdf_filler.fill(file_name, **row)


def main():

    validate_directory_structure()
    # validate_for_duplicate_text_fields(PDF_FILLER.writer)

    table = load_input_table()
    PDF_FILLER = PDFFiller()

    columns = list(table.columns)
    fields = PDF_FILLER.unique_field_names

    validate_file_name_column(columns)
    columns.remove("file_name")

    validate_for_duplicate_columns(columns)
    validate_fields_and_columns(fields, columns)
    validate_output_folder()

    fill_forms(table, PDF_FILLER, clean_filename=True)


if __name__ == "__main__":
    main()
