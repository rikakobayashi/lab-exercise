from exercise1 import reverse_complement

def is_reverse_complement(seq1, seq2):
  if reverse_complement(str.upper(seq1)) == str.upper(seq2):
    return True
  else:
    return False
