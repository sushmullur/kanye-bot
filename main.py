from urllib.request import urlopen
txt = open("processed-lyrics.txt").read().split("\n")
print("Our dataset contains {} lines".format(len(txt)))
everything = set([w for s in txt for w in s.split()])
print("and {} lexical types".format(len(everything)))

import spacy
nlp = spacy.load("en_core_web_sm", disable=["parser","tagger","ner","textcat"])

txt = [nlp(s) for s in txt]

txt = [ ["<s>"] + [str(w) for w in s] + ["</s>"] for s in txt]

train = txt[:-5]
valid = txt[-5:]
train = [w for s in train for w in s if not w.isspace()]
valid = [w for s in valid for w in s if not w.isspace()]