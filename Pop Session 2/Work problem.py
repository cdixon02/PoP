#initialisation


start = 0
end = 13
step = 2
sum = 0
#position = 1

#logic
##for x in range(start,end,step):
  ##  if position % 2 != 0:
   ##     sum += x
  ##  print(position, 'value =', x)
   ## position += 1
  
flag = True
for x in range(start,end,step):
    if flag:
        sum += x
    flag = not flag
#output
print(sum)

assert sum == 24
