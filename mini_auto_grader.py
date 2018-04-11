import ID3, parse, random
from ID3 import CHOOSE_ATTRIBUTE
from ID3 import split
from ID3 import majority

def mini_grader():

  # data = [dict(a=1, b=0, Class=1), dict(a=1, b=1, Class=1)]
  #
  # try:
  #   tree = ID3.ID3(data, 0)
  #   if tree != None:
  #     ans = ID3.evaluate(tree, dict(a=1, b=0))
  #     if ans != 1:
  #       print "ID3 test 1 failed."
  #     else:
  #       print "ID3 test 1 succeeded."
  #   else:
  #     print "ID3 test 1 failed -- no tree returned"
  # except Exception:
  #   print 'ID3 test 1 failed runtime error'
  #
  data = [dict(a=1, b=0, Class=0), dict(a=1, b=1, Class=1)]

  try:
    tree = ID3.ID3(data, 0)
    if tree != None:
      ans = ID3.evaluate(tree, dict(a=1, b=0))
      if ans != 0:
        print "ID3 test 2 failed."
      else:
        print "ID3 test 2 succeeded."
    else:
      print "ID3 test 2 failed -- no tree returned"
  except Exception:
    print 'ID3 test 2 failed runtime error'

################TRY by XWX

  # data = [dict(a=1, b=0, Class=2), dict(a=1, b=1, Class=1),
  #         dict(a=1, b=0, Class=2), dict(a=3, b=1, Class=3),
  #         dict(a=3, b=0, Class=1), dict(a=3, b=1, Class=3)]
  #
  # try:
  #   tree = ID3.ID3(data, 0)
  #   if tree != None:
  #     ans = ID3.evaluate(tree, dict(a=1, b=0))
  #     if ans != 2:
  #       print "ID3 test 3-1 failed."
  #     else:
  #       print "ID3 test 3-1 succeeded."
  #     ans = ID3.evaluate(tree, dict(a=1, b=1))
  #     if ans != 1:
  #       print "ID3 test 3-2 failed."
  #     else:
  #       print "ID3 test 3-2 succeeded."
  #   else:
  #     print "ID3 test 3 failed -- no tree returned"
  # except Exception:
  #   print 'ID3 test 3 failed runtime error'

###############################################################

  data = [dict(a=1, b=0, Class=2), dict(a=1, b=1, Class=1),
          dict(a=2, b=0, Class=2), dict(a=2, b=1, Class=3),
          dict(a=3, b=0, Class=1), dict(a=3, b=1, Class=3)]

  try:
    tree = ID3.ID3(data, 0)
    if tree != None:
      ans = ID3.evaluate(tree, dict(a=1, b=0))
      if ans != 2:
        print "ID3 test 3-1 failed."
      else:
        print "ID3 test 3-1 succeeded."
      ans = ID3.evaluate(tree, dict(a=1, b=1))
      if ans != 1:
        print "ID3 test 3-2 failed."
      else:
        print "ID3 test 3-2 succeeded."
    else:
      print "ID3 test 3 failed -- no tree returned"
  except Exception:
    print 'ID3 test 3 failed runtime error'
  #
  # data = [dict(a=1, b=0, c='?', Class=1), dict(a=1, b=3, c=2, Class=1),
  #        dict(a=2, b='?', c=1, Class=2), dict(a=2, b=1, c=3, Class=2),
  #        dict(a=3, b=0, c=1, Class=3), dict(a=3, b=2, c='?', Class=3)]
  #
  # try:
  #   tree = ID3.ID3(data, 0)
  #   if tree != None:
  #     ans = ID3.evaluate(tree, dict(a=1, b=1, c=1))
  #     if ans != 1:
  #       print "ID3 test 4-1 failed."
  #     else:
  #       print "ID3 test 4-1 succeeded."
  #     ans = ID3.evaluate(tree, dict(a=2, b=0, c=0))
  #     if ans != 2:
  #       print "ID3 test 4-2 failed."
  #     else:
  #       print "ID3 test 4-2 succeeded."
  #   else:
  #     print "ID3 test 4 failed -- no tree returned"
  # except Exception:
  #   print 'ID3 test 4 failed runtime error'

if __name__ == "__main__":
# #    mini_grader()
#   data = [dict(L= 's', F= 's',H='no' , Class='no'),
#           dict(L='s', F='l', H='yes', Class='yes'),
#           dict(L='l', F='m', H='yes', Class='yes'),
#           dict(L='m', F='m', H='yes', Class='yes'),
#           dict(L='l', F='m', H='yes', Class='yes'),
#           dict(L='m', F='l', H='no', Class='yes'),
#           dict(L='m', F='s', H='no', Class='no'),
#           dict(L='l', F='m', H='no', Class='yes'),
#           dict(L='m', F='s', H='no', Class='yes'),
#           dict(L='s', F='s', H='yes', Class='no')]
# #   data = [dict(a=1, b=0, Class=2), dict(a=1, b=1, Class=1),
# #         dict(a=2, b=0, Class=2), dict(a=2, b=1, Class=3),
# #         dict(a=3, b=0, Class=1), dict(a=3, b=1, Class=3)]
#   a = CHOOSE_ATTRIBUTE(data)
#   b = ID3.split(data,'a',1)
#   print b
#   print data
  mini_grader()
#   data = [dict(Class = 2),dict(Class = 2),dict(Class = 2),dict(Class = 1),dict(Class = 3),dict(Class = 4),dict(Class = 0)]
#   majority(data)
