def h():  
  print('Wen Chuan')
  yield "xxasdfdf"
  yield "bbasdfdf"
c = h()  
print(c.__class__)
a = next(c)
print(a)
#b = next(c)
#print(a,b)
