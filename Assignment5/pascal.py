import mystuff as my

for y in range(6):
     for x in range(y):
          if (x == 0 or x == y - 1):
              print(1,end=' ')
          else:
              value = my.pascal_number(y,x)
              value -= 1
              print(value,end=' ')
     print()
