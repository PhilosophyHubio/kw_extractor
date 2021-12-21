# On demand keyword extractor for Zotero

This tool is meant to read the text of a pdf, using tools available via the textract module (pdftotext for pdf files with embedded text, and tesseract for OCR), and dumps a json with keywords extracted using yake module.

### About this "new version"

This new "flavour" of the original tree_reader extractor (still available in this repository inside kw_extractor/batch) is a remake following a completely different logic. While the original tree_reader was made as a batch processing tool (for all pdf's in Zotero's storage), this new development does so on demand, only for the pdf files that can be found inside a given Zotero id folder. Also, the script was fully written in python to focus in the maintenance and interoperability aspects, rather than execution time or general optimization.

## Dependencies

In order for this tool to work properly, several dependencies are needed

- yake: This module is used for the keyword extraction process; further tuning is needed and the helpfulness of this tool should be reviewed accordingly. It can be installed using ```pip install yake```
- textract: This module is used for extracting text from pdf files. At least, it also needs to have poppler-utils and tesseract-ocr in the OS to function, besides executing ```pip install textract```; it is highly recommended to review the [installation for this module](https://textract.readthedocs.io/en/stable/installation.html).