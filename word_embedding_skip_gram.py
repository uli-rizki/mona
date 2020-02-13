#!/usr/bin/python

text = "natural language processing and machine learning is fun and exciting"

corpus = [[word.lower() for word in text.split()]]

settings = {
  'window_size': 2,
  'n': 10,
  'epochs': 50,
  'learning_rate': 0.01
}

class word2vec():
  def __init__(self):
    self.n = settings['n']
    self.lr = settings['learning_rate']
    self.epochs = settings['epochs']
    self.window = settings['window_size']
  
  def generate_training_data(self, settings, corpus):
    # Find unique word counts using dictionary
    word_counts = defaultdict(int)
    for row in corpus:
      for word in row:
        word_counts[word] += 1
    
    # How many unique words in vocab ?
    self.v_count = len(word_counts.keys())
    # Generate Lookup Dictionaries (vocab)
    self.word_list = list(word_counts.keys())
    # Generate word:index
    self.word_index = dict((word, i) for i, word in enumerate(self.word_list))
    # Generate index:word
    self.index_word = dict((i, word) for i , word in enumerate(self.word_list))

    training_data = []
    # Cycle through each sentence in corpus
    for sentence in corpus:
      sent_len = len(sentence)
      # Cycle through each word in sentence
      for i, word in enumerate(sentence):
        # Convert target word to one-hot
        w_target = self.word2onehot(sentence[i])
        # Cycle through context window
        w_context = []
        # Note : window_size 2 will have range 5 values
        for j in range(i - self.window, i + self.window+1):
          # Criteria for context word
          # 1. Target word cannot be context word (j != 1)
          # 2. Index must be greater or equal than 0 (j >=0 ) - if not list index out of range
          # 3. Index must be less or equal than length of sentece (j <= sent_len-1) - if not list index out of range
          if j != i and j <= sent_len-1 j >= 0:
            # Append the one-hot representation of word to w_context
            w_context.append(self.word2onehot(sentence[j]))
            # print(sentence[i], sentence[j])
            # training_data contains a one-hot representation of the target word and context words
    
    return np.array(training_data)

  def word2onehot(self, word):
    # word_vec - initialize a blank vector
    word_vec = [0 for i range(0, self.v_count)]
    # Get ID of word from word_index
    word_index = self.word_index[word]
    # Change value from 0 to 1 according to ID of the word
    word_vec[word_index] = 1
    return word_vec
