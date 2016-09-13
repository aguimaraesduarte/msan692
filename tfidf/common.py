import xml.etree.cElementTree as ET
import sys
import collections

def gettext(xmltext):
	"""
	Parse xmltext and return the text from <title> and <text> tags
	"""
	return

def tokenize(text):
	"""
	Tokenize text and return a non-unique list of tokenized words
	found in the text. Normalize to lowercase, strip punctuation,
	remove stop words, drop words of length < 3.
	"""
	return

def stemwords(words):
	"""
	Given a list of tokens/words, return a new list with each word
	stemmed using a PorterStemmer.
	"""
	return

if __name__=="__main__":
	"""
	xmltext = ... text from filename in sys.argv[1] ...
	text = gettext(xmltext)
	...
	counts = Counter(tokens)
	...
	"""
	print