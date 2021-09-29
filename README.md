# Keyword extractor
Scripts keyword extractions of Zotero database.  This script obtains a text file for each file in ../Zotero/storage/. It is meant to be put inside a folder nested in the same folder that Zotero/ is.
### tree_reader.sh
- First, it generates a file named pdflist.txt containing all pdf files found recursively searching inside storage/.
- Then, it extracts the text of each pdf file using pdftotext from poppler-utils; the resulting text files are stored in Corpora/.
- Finally, it feeds each of this files to yake_kw_extractor.py
### yake_kw_extractor.py
- It gets Zotero id of a register from the relative path of files logged in pdflist.txt
- Keywords are extracted using yake
- A json is built with the id and keywords and it is stored in keywords/
---
# Contributors
This development was made as a part of my social services for obtaining a B. Sc. in Biology at the Sciences Faculty of the National Autonomous University of Mexico. I'm Isaac Pardo Granillo and I did this under the tutelage of David Suárez Pascal.