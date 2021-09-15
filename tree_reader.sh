#! /bin/bash
echo "generating pdf list with absolute paths"
ZOTERO_STORAGE="../Zotero/test_storage/"
find $ZOTERO_STORAGE -iname "*.pdf" > pdf.list
echo -e "\nnumber of pdf files found:" && echo "$var" | wc -l pdf.list
PDF_ABS_PATHS="pdf.list"
echo -e "\nchecking for text in pdf list"
while read -r line; do
    pdf_file=$line
    echo -e "\nprocessing file $pdf_file"
    filename_base=${pdf_file%.pdf}
    text_file="$filename_base.txt"
    if [ ! -f "$text_file" ]; then
        echo -e "$text_file not found; creating it"
        pdftotext "$pdf_file" "$text_file"
    else
        echo "$text_file found"
    fi
    kw_file_ext="_kw.json"
    kw_file="$filename_base$kw_file_ext"
    if [ ! -f "$kw_file" ]; then
        python3 yake_kw_extractor.py "$text_file"
    else
        echo "$kw_file found"
    fi
done < "$PDF_ABS_PATHS"
