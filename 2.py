'''
l=[1,2,3]
print(l[3])
'''
#IndexError: list index out of range

l=[1,2,3]
try:
    print(l[3])
except:
    print("list index out of range")
