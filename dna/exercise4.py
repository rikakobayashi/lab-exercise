import re
import matplotlib.pyplot as plt
import numpy as np

def calc_gc_content(file_name, window, step):
  gc_num = 0
  seq = ''

  f = open(file_name, "r")
  for line in f.readlines():
    if line[0] != '>':
      seq += re.sub('[^ACTG]', '', line)
  f.close()

  gc_num = seq.count("G") + seq.count("C")
  print("GC含量: {}".format(gc_num / len(seq)))

  x = []
  gc_ratio = []
  index = 0
  while index < len(seq):
    gc_num = seq[index:index+window].count("G") + seq[index:index+window].count("C")
    print("GC含量({}-{}): {}".format(index, index+window-1, gc_num / window))
    x.append(index)
    gc_ratio.append(gc_num / window)
    index += step

  plt.plot(np.array(x), np.array(gc_ratio))
  plt.show()

file_name  = "NT_113952.1.fasta"
print(calc_gc_content(file_name, 1000, 500))