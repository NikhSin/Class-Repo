#. 6 Write a program to separate odd and even keys from a dictionary. 
#Also count the total number of odd keys and even keys. 
def fun(d):
    even=[]
    odd=[]
    for keys,value in d.items():
        if keys%2==0:
            even.append(keys)
        else:
            odd.append(keys)
    return even,odd

d={1:1,2:2,3:3,4:4,5:5}
res=fun(d)
print(res)