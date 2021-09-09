import sys
import yake
import json

def extract_kw(text_file):
    text = open(text_file,"r").read()
    lang = "es"
    max_ngram = 2
    dedup_lim = 0.9
    max_num_kw = 100
    kw_tuples = yake.KeywordExtractor(lan=lang,n=max_ngram,dedupLim=dedup_lim,top=max_num_kw).extract_keywords(text)
    kw_output = "{keyword-tuples="+str(kw_tuples)+"}"
    kw_file = text_file[:-4]+"_kw.json"
    print(f"creating {kw_file}")
    open(kw_file,"w").write(kw_output)  


if __name__ == "__main__":
    text_file = sys.argv[1]
    print(f"extracting keywords from {text_file}")
    extract_kw(text_file)