def reverse_complement(seq):
  table = str.maketrans({
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
  })

  return str.upper(seq).translate(table)
