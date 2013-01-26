#!/usr/bin/python

""" Password Generator Program """

__authors__ = "gerson23 and jbsilva"

import Password as ps
import sys, getopt

class PassGenerator:

  def parse(self, argv):
    # default value
    size = 6
    chars = True
    num = True
    other = True
    # end defaults

    try:
      opts, args = getopt.getopt(argv, "d:lno")
    except getopt.GetoptError:
      print "PassGenerator.py [-d <dim>] [-l] [-n] [-o]"
      sys.exit(2)

    for opt, arg in opts:
      if opt == "-d":
        try:
          size = int(arg)
        except ValueError:
          print "Invalid argument -d ",arg
      elif opt == "-l":
        chars = False
      elif opt == "-n":
        num = False
      elif opt == "-o":
        other = False
      else:
        print "Invalid argument ", opt

    return size, chars, num, other


if __name__ == "__main__":
  pg = PassGenerator()
  size, chars, num, other = pg.parse(sys.argv[1:])
  psw = ps.Password(size, chars, num, other)
  print ">>", psw.get_pass()
