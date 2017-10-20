##Question 2
#a = [int(i) for i in input().split()]
#for elem in a:
#    if elem % 2 == 0:
#        print(elem)
##Question 3
#a = [int(i) for i in input().split()]
#for i in range(1, len(a)):
#    if a[i] > a[i - 1]:
#        print(a[i])
##Question 4
#a = [int(i) for i in input().split()]
#for i in range(1, len(a)):
#    if a[i - 1] * a[i] > 0:
#        print(a[i - 1], a[i])
#        break



#question 8
#a = [int(i) for i in input().split()]
#for i in range(1, len(a), 2):
#    a[i - 1], a[i] = a[i], a[i - 1]
#print(' '.join([str(i) for i in a]))

#a = [int(s) for s in input().split()]
#index_of_min = 0
#index_of_max = 0
#for i in range(1, len(a)):
#    if a[i] > a[index_of_max]:
#        index_of_max = i
#    if a[i] < a[index_of_min]:
#        index_of_min = i
#a[index_of_min], a[index_of_max] = a[index_of_max], a[index_of_min]
#print(' '.join([str(i) for i in a]))

#question 10
#a = [int(s) for s in input().split()]
#counter = 0
#for i in range(len(a)):
#    for j in range(i + 1, len(a)):
#        if a[i] == a[j]:
#            counter += 1
#print(counter)


#question 11
#a = [int(s) for s in input().split()]
#for i in range(len(a)):
#    for j in range(len(a)):
#        if i != j and a[i] == a[j]:
#            break
#    else:
#       print(a[i], end=' ')
