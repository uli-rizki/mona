#!/usr/bin/python

from string import maketrans
from string import punctuation
from os import listdir
from collections import Counter
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()

# Kalimat
# kalimat = 'Dengan Menggunakan Python dan Library Sastrawi saya dapat melakukan proses Stopword Removal'
# stop = stopword.remove(kalimat)
# print(stop)

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
def clean_doc(doc):
  tokens = doc.split()
  table = maketrans('', '')
  tokens = [w.translate(table) for w in tokens]
  tokens = [word for word in tokens if len(word) > 1]
  return tokens

# save list to file
def save_list(lines, filename):
	# convert lines to a single blob of text
	data = '\n'.join(lines)
	# open file
	file = open(filename, 'w')
	# write text
	file.write(data)
	# close file
	file.close()

# load doc and add to vocab
def add_doc_to_vocab(filename, vocab):
	# load doc
	doc = load_doc(filename)
	# clean doc
	tokens = clean_doc(doc)
	# update counts
	vocab.update(tokens)

# load all docs in a directory
def process_docs(directory, vocab, is_trian):
	# walk through all files in the folder
	for filename in listdir(directory):
		# create the full path of the file to open
		path = directory + '/' + filename
		# add doc to vocab
		add_doc_to_vocab(path, vocab)

# load all coversation

vocab = Counter()
process_docs('../Datasets/April', vocab, True)
process_docs('../Datasets/March', vocab, True)
process_docs('../Datasets/May', vocab, True)

# keep tokens with a min occurrence
min_occurane = 2
tokens = [k for k,c in vocab.items() if c >= min_occurane]
# print(len(tokens))
save_list(tokens, 'vocab.txt')

# # load the document
# filename = '../Datasets/April'
# text = load_doc(filename)
# tokens = clean_doc(text)

# # save tokens to a vocabulary file
# save_list(vocab, 'vocab.txt')