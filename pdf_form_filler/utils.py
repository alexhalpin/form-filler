import os
import pandas as pd
from pypdf import PdfReader, PdfWriter
from typing import Dict
from pdf_form_filler.errors import ValidationError


cwd = os.getcwd()


def load_input_table() -> pd.DataFrame:

    input_dir = os.path.join(cwd, "input_table")
    input_table_basename = os.listdir(input_dir)[0]
    input_table_path = os.path.join(input_dir, input_table_basename)

    try:
        input_df = pd.read_csv(input_table_path, index_col=False)
    except Exception as e:
        raise ValidationError(f"error reading input table, is it a valid csv? ERROR: {e}")

    return input_df


class PDFFiller:

    def __init__(self):

        template_dir = os.path.join(cwd, "input_pdf_template")
        template_basename = os.listdir(template_dir)[0]
        template_path = os.path.join(template_dir, template_basename)

        self.reader = PdfReader(template_path)

        self.unique_field_names = list(self.reader.get_fields().keys())

        self.output_dir = os.path.join(cwd, "filled_pdfs")

    def fill(self, output_pdf_name, **fields):

        file_extension = os.path.splitext(output_pdf_name)[1]
        if file_extension == "":
            output_pdf_name += ".pdf"

        writer = PdfWriter()
        writer.clone_reader_document_root(self.reader)
        writer.set_need_appearances_writer(True)

        fields = {k: str(v) for k, v in fields.items()}

        writer.update_page_form_field_values(
            None,
            fields=fields,
        )

        output_pdf_path = os.path.join(self.output_dir, output_pdf_name)

        with open(output_pdf_path, "wb") as output_stream:
            writer.write(output_stream)
