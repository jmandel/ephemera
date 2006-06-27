import os
import sys


def main(file):
  words = open(file).readlines()
  outfile = open("%s-defined"%(file),'w')
#  sys.stdout = outfile
  for w in words:
    wp = w[:-1].split(" ")[0]
    print w
    defnn = os.popen("dict -d wn %s"%(wp)).readlines()
    for l in defnn:
      print l[:-1]
    print "-----------------------------------\n"
  outfile.close()

if __name__ == "__main__":
  main(sys.argv[1])
