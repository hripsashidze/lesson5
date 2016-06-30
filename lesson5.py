ff = open("example.txt")
#for line in open("example.txt"):
 #   if '3 lines' in line:
 #       print(line)

ontent = ff.read()
ff.close()
return len(ontent)