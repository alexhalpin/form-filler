from setuptools import setup, find_packages

setup(
    name="pdf-form-filler",  # Name of your package
    version="0.1.0",  # Package version
    packages=find_packages(),  # Automatically find packages
    install_requires=[
        "pandas",
        "re",
        "os",
        "pypdf",
    ],  # List of dependencies
    entry_points={  # Define the entry point
        "console_scripts": [
            "pdf-form-filler=pdf_form_filler.main:main",  # Command 'foo' runs foo.main.main()
        ],
    },
    author="Alexander Halpin",
    author_email="alexhalpin00@gmail.com",
    url="https://github.com/alexhalpin/form-filler",  # Your GitHub URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version
)
