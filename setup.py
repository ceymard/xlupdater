from setuptools import setup, find_packages

setup(
    name = "HelloWorld",
    version = "0.1",
    # packages = find_packages(),
    scripts = ['xlupdater'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['watchdog'],
    # metadata for upload to PyPI
    author = "Christophe Eymard",
    author_email = "christophe.eymard@gmail.com",
    description = "Excel VB file two-way sync with the file system to edit VB code in an external editor",
    license = "MIT",
    keywords = "excel, editor, sync",
    url = "https://github.com/ceymard/xlupdater/",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)