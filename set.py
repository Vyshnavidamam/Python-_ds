s1={1,1,2,2,4,4}
s2={1,4,3,5,1}
print(s1)
print(type(s1))

s1.add("vyshu")
print(s1)

s1.remove(1)
print(s1)
print (s1.difference(s2))


l1=[1,1,2,2,3,4,5,5,6]
print(l1)
print(type (l1))
l2=set (l1)
print(l2)
print(type(l2))

a=input(" enter the string")
b=set(a)
c={'a','e','i','o','u'}
d=b.intersection(c)
print("vowles present in given string are",d)