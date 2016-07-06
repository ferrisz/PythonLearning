# _*_ coding:utf-8 _*_

name = [ "abc","Tina","yp","ddssa" ]
print type(name)
print len(name)
print id(name)


print name[0] #indexError

name.append(4)
name.append("xiaoqi")
name.append("xuefeng")
print len(name)
name.insert(6,"Rose")
print name
print name[-3][:4]
name.pop(5)
print name
print name[3:]
print ">"*50
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print power(5)