import sys
import os
import textract
import yake
import json


def extract_kw (text):
    """"Returns a list of tuples with keywords and their scores"""

    #TODO: tuning to extraction parameters
    #TODO: how to deal with other languages?

    kw_tuples = yake.KeywordExtractor (lan = 'es', n = 2, dedupLim = 0.9, top = 100).extract_keywords (text)
    return kw_tuples


def pdf_to_kw (id, folder, pdf_list):
    """Extracts the text of a pdf file, and dumps a json with extracted keywords
    
    In case the pdf has embedded text, it is read directly; if no text can be found
    tesseract OCR is used to read text from it
    """
    
    #TODO: test behavior with pdf lists rather than single files

    for pdf in pdf_list:
        #print(f'reading file {pdf}')
        pdf_file = folder + '/' + pdf
        text = ''
        kw_tuples = []
        text += textract.process (pdf_file, method = 'pdftotext').decode ('utf-8')
        if text != '':
            #print ('text extracted directly from pdf')
            kw_tuples += extract_kw(text)
        
        #TODO: test how tesseract handles real pdf documents with no text

        else:
            #print ('extracting text from pdf using tesseract')

            #TODO: how to deal with other languages?

            text += textract.process (pdf_file, method = 'tesseract', language = 'spa').decode ('utf-8')
            kw_tuples += extract_kw(text)
        payload = json.dumps (
            {
                'id': id,
                'keywords': kw_tuples
            }
        )
        print (payload)      


def main (zotero_id):
    """looks for folder with given ids in Zotero's storage path; then looks for pdf files"""
    ZOTERO_STORAGE_PATH = '../../Zotero/storage/'
    folder = ZOTERO_STORAGE_PATH + zotero_id
    #print (f'looking for path {folder}')
    if os.path.exists (folder):
        #print (f'looking for pdf associated to entry with zotero id {zotero_id}')
        pdf_list = [f for f in os.listdir(folder) if f.endswith('.pdf')]

        #TODO: add more file types as needed

        if len (pdf_list) == 0:
            print (f'no pdf files found for entry with id {zotero_id}')
        else:
            #print (f'found {len(pdf_list)} pdf file(s)')
            pdf_to_kw (zotero_id, folder, pdf_list)
    else:
        print(f'no folder for entry with zotero id {zotero_id} found')
    



if __name__ == "__main__":
    if len (sys.argv) == 1:
        print('please specify at least one zotero id to read')
    else:
        for i in range (1, len (sys.argv)):
            main (sys.argv[i])