#!/usr/bin/python

from string import punctuation
from string import maketrans
from os import listdir
from gensim.models import Word2Vec

# load doc into memory
def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text

# turn a doc into clean tokens
def doc_to_clean_lines(doc, vocab):
	clean_lines = list()
	lines = doc.splitlines()
	for line in lines:
		# split into tokens by white space
		tokens = line.split()
		table = maketrans('', '')
    tokens = [w.translate(table) for w in tokens]
    tokens = [word for word in tokens if len(word) > 1]
		clean_lines.append(tokens)
	return clean_lines

# load all docs in a directory
def process_docs(directory, vocab, is_trian):
	lines = list()
	# walk through all files in the folder
	for filename in listdir(directory):
		path = directory + '/' + filename
		# load and clean the doc
		doc = load_doc(path)
		doc_lines = doc_to_clean_lines(doc, vocab)
		# add lines to list
		lines += doc_lines
	return lines

# load the vocabulary
vocab_filename = 'vocab.txt'
vocab = load_doc(vocab_filename)
vocab = vocab.split()
vocab = set(vocab)

april = process_docs('../Datasets/April', vocab, True)
march = process_docs('../Datasets/March', vocab, True)
may = process_docs('../Datasets/May', vocab, True)

sentences = april + march + may

print('Total training sentences: %d' % len(sentences))