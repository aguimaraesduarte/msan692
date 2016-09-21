import xml.etree.cElementTree as ET
import sys
import collections
import nltk
import string
from sklearn.feature_extraction import text as sktext
import re

def gettext(xmltext):
	"""
	Parse xmltext and return the text from <title> and <text> tags
	"""
	root = ET.fromstring(xmltext)
	text = root[0].text
	for elem in root.iterfind('.//text/*'):
		text += elem.text
	return text

def tokenize(text):
	"""
	Tokenize text and return a non-unique list of tokenized words
	found in the text. Normalize to lowercase, strip punctuation,
	remove stop words, drop words of length < 3.
	"""
	strippedText = text.lower()
	reg = re.compile('[%s]' % (string.punctuation + "0-9\\r\\t\\n"))
	strippedText = reg.sub(" ", strippedText)
	strippedText = ' '.join(strippedText.split())
	token = nltk.word_tokenize(strippedText)
	token = [i for i in token if len(i)>=3]
	token = [i for i in token if i not in sktext.ENGLISH_STOP_WORDS]
	return token

def stemwords(words):
	"""
	Given a list of tokens/words, return a new list with each word
	stemmed using a PorterStemmer.
	"""
	stemmer = nltk.stem.porter.PorterStemmer()
	stemmedWords = [stemmer.stem(i).encode('ascii', 'ignore') for i in words]
	return stemmedWords

if __name__=="__main__":
	f = open(sys.argv[1], 'r')
	xmltext = f.read()
	f.close()
	text = gettext(xmltext)
	words = tokenize(text)
	stems = stemwords(words)

	counts = collections.Counter(stems)
	for tup in counts.most_common(10):
		print tup[0], tup[1]
	