
f = open('email_list.csv', 'rU')
for line in f:   ## iterates over the lines of the file
  x = line.find('@')
  if x >= 1:
    print line,

f.close()