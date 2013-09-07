word1 = "abcd"
word2 = "abcde"

def _reverse(word):
  chars = list(word)
  word_len = len(word)
  for i in xrange(word_len/2):
    chars[i], chars[word_len-i-1] = chars[word_len-i-1], chars[i]
  print "".join(chars)

_reverse(word1)
_reverse(word2)
