#!coding: utf-8 
def test():
  str1 = "t"
  str2 = "T"
  ustr1 = str1.decode('utf8')
  ustr2 = str2.decode('utf8')
  print ustr1 == ustr2

if __name__ == "__main__":
  test()