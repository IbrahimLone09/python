#Given a List we need to check if it is a palindrome or not
lst=[1,2,1]
copy_lst = lst.copy()
copy_lst.reverse()

if(copy_lst==lst):
    print("Palindrome:")
else:
    print("Not Palindrome:")