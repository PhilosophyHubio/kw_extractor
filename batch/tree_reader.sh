#! /bin/bash

if [[ -z "${ZOTERO_STORAGE}" ]]; then
  ZOTERO_STORAGE="../../Zotero/test_storage/"
else
  ZOTERO_STORAGE="${ZOTERO_STORAGE}"
fi

echo "updating pdf list with relative paths inside Zotero storage"
find $ZOTERO_STORAGE -iname "*.pdf" > pdflist.txt
echo -e "\nnumber of pdf files found:" && echo "$var" | wc -l pdflist.txt
PDF_REL_PATHS="pdflist.txt"
echo -e "\nchecking for text in pdf list"
if [ ! -d corpora ]; then
        mkdir corpora
        echo "creating corpora folder"
fi
if [ ! -d keywords ]; then
        mkdir keywords
        echo "creating keywords folder"
fi    
while read -r line; do
    pdf_file=$line
    echo -e "\nprocessing file $pdf_file"
    path_base=${pdf_file%.pdf}
    filename_base=${path_base##*/}
    text_file="corpora/$filename_base.txt"
    if [ ! -f "$text_file" ]; then
        echo -e "$text_file not found; creating it"
        pdftotext "$pdf_file" "$text_file"
    else
        echo "$text_file found"
    fi
    kw_file_ext="_kw.json"
    kw_file="keywords/$filename_base$kw_file_ext"
    if [ ! -f "$kw_file" ]; then
        python3 yake_kw_extractor.py "$text_file" "$pdf_file"
    else
        echo "$kw_file found"
    fi
done < "$PDF_REL_PATHS"
