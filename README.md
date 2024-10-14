# form-filler

pdf-form-filler fills pdf text forms from a csv


# installation

```
pip install git+https://github.com/alexhalpin/form-filler
```

# usage

pdf-form-filler is designed for ease of use by non-developers without the command line and thus requires some file-system setup before using.

#

pdf-form-filler needs 2 main files to work:

1. the input table (csv)
    - the input table contains the information that we want to fill into the pdf
2. the pdf form template (pdf)
    - the pdf form template is a pdf file with text form fields that we will fill in



the columns in the input table that align with the form field names in the template pdf will be used to fill in the repsective form fields.

NOTE:
the table must be a csv and must have 1 mandatory column, `file_name`, which will be used to name the output pdf

e.g.

say our input table, `table.csv`, contains the following information

| file_name  | field_1   | field_2   |
|------------|------------|------------|
| output file 1 | value1 | value2|
| output file 2| value3 | value4 |


if our pdf template, `template.pdf`, contains 2 fields,`field_1` and `field_2`, pdf-form-filler will output 2 files: `output_file_1.pdf` and `output_file_2.pdf`

`field_1` in `output_file_1.pdf` will contain value `value1`, `field_2` with `value2` and so on for `output_file_2.pdf`.

#

### directory preparation

#

1. choose a directory (folder) on your machine that you will be working in, let's call this `main` (but you can name it whatever you want)

2. in this `main` directory create 3 sub-directories (these subdirectories must have the following names exactly):
    
    a. `input_table`

    b. `input_pdf_template`

    c. `filled_pdfs`

3. copy `run.bat` into main

#

at this point your folder structure should look like this

```
main/
├── input_table/
├── input_pdf_template/
├── filled_pdfs/
└── run.bat
```

#

4. place youre template pdf into the `input_pdf_template` directory (can be named anything, must be .pdf)
5. place youre input table into the `input_table` folder (can be named anything, must be .csv)

#

```
main/
├── input_table/
├──── input_table.csv <-
├── input_pdf_template/
├──── pdf_template.pdf <-
├── filled_pdfs/
└── run.bat
```

# 

now, if on windows, launch `run.bat`

if on mac, launch `run.command`

