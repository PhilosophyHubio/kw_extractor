import sys
import os
import yake
import json


def extract_kw(text_file):
    text = open(text_file,"r").read()
    lang = "es"
    max_ngram = 2
    dedup_lim = 0.9
    max_num_kw = 100
    split_file_addr = text_file.split("/")
    file_id = split_file_addr[3]
    kw_tuples = yake.KeywordExtractor(lan=lang,n=max_ngram,dedupLim=dedup_lim,top=max_num_kw).extract_keywords(text)
    kw_output = {
        "id": file_id,
        "keywords": kw_tuples
    }
    payload = json.dumps(kw_output)
    json_folder = "keywords"
    if not os.path.exists(json_folder):
        print("json folder not found; creating it")
        os.makedirs(json_folder)
    out_filename = split_file_addr[4][:-4]+"kw.json"
    out_full_path = json_folder+"/"+out_filename
    print(f"creating json file with id {file_id}")
    open(out_full_path,"w").write(payload)


if __name__ == "__main__":
    text_file = sys.argv[1]
    print(f"extracting keywords from {text_file}")
    extract_kw(text_file)