from sklearn.feature_extraction.text import TfidfVectorizer
from common import *

def tokenizer():
	tokenize("")
	stemwords([""])

tfidf = TfidfVectorizer(input='filename', # argument to transform() is list of files
						analyzer='word',
						preprocessor=gettext, # convert xml to text
						tokenizer=tokenizer,  # tokenize, stem
						stop_words='english') # strip out stop words