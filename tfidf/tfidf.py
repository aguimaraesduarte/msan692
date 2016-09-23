from sklearn.feature_extraction.text import TfidfVectorizer
from common import *
import os

def filelist(root):
	"""Return a fully-qualified list of filenames under root directory"""
	files = []
	for dirname, dirnames, filenames in os.walk(root):
		for filename in filenames:
			files.append(os.path.join(dirname, filename))
	return files

def tokenizer(text):
	words = tokenize(text)
	stems = stemwords(words)
	return stems

files = filelist(sys.argv[1])
file = sys.argv[2]

vectorizer = TfidfVectorizer(input='filename', # argument to transform() is list of files
						analyzer='word',
						preprocessor=gettext, # convert xml to text
						tokenizer=tokenizer,  # tokenize, stem
						stop_words='english', # strip out stop words
						decode_error='ignore')

matrix = vectorizer.fit(files).transform([file])
word_indices = matrix.nonzero()[1]

tfidf = [(vectorizer.get_feature_names()[i], matrix[0, i]) for i in word_indices if matrix[0, i] >= 0.09]
sorted_tfidf = sorted(tfidf, key=lambda x: x[1], reverse=True)
for tup in sorted_tfidf:
	print tup[0], format(tup[1], ".3f")
