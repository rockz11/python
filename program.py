# print("Hello INDIA")
# print(type(2))
# a =11
# print(id(a))
# a = 2
# a*= 2
# print(a)
# name = input("Please enter your name: ")
# print(type(name))
# print("Hello," + name)
# a = [1,2,3,4,5, "cloud",'true']
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[5])
# print(a[6])
# print(len(a))
# print("length of the list:", 7)
# print(a,len(a))
# a = [1,2,3,4,5,6,7,8,9] # slicing operation on list
# print(a[-1])
# print(a[len(a) -1])
# print(len(a))
# # print(a[::2])
# a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# print(a[-1::-1])
# print(a[::-1])

#Appending and Extending
# This means appending values to a list 
a = [1,2,3,4,5,6,7]
#Append 8 to the list we use a.append(8)
#a.append(8)  # Append takes one value at time ,two more is not possible
#print(a)
#Extending
a.extend([9,10,11])        #output: [1, 2, 3, 4, 5, 6, 7, 9, 10, 11]
#a.append([9,10,11])  #output: [1, 2, 3, 4, 5, 6, 7, [9, 10, 11]]
print(a)