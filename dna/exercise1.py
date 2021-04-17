def reverse_complement(seq):
  table = str.maketrans({
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
  })

  return seq.translate(table)
