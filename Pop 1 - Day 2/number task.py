'''read in a list of numbers, one a time, using a prompt.
if the number is 0 then stop. OTherwise, add the number to a running total.
prints out a runnning total'''
#print("A number please:", end = " ")
#number = int(input())
#count = 0
#while number != 0:
   # count += number
  #  print("A number please:", end = " ")
   # number = int(input())
#print(count)

#total = 0
#while True:
   # print("A number please:", end = " ")
   # number = int(input())
   # if number == 0:
   #     break
  #  total += number
#print(total)

total = 0
finished = False
while not finished:
    print("A number please:", end = " ")
    number = int(input())
    if number == 0:
        finished = True
    else:
            total += number
print(total)
