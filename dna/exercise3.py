def calc_gc_content(file_name):
  gc_num = 0
  all_num = 0

  f = open(file_name, "r")
  for line in f.readlines():
    if line[0] != '>':
      gc_num += line.count("C") + line.count("G")
      all_num += line.count("A") + line.count("T") + line.count("C") + line.count("G")

  f.close()
  
  return gc_num / all_num

file_name  = "NT_113952.1.fasta"
print(calc_gc_content(file_name))