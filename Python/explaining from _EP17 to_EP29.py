#------------------------
#------------------------
#--- string formating ---
#------------------------
#------------------------


# %s ---> for holding a palce to str .
# %d ---> for holding a palce to int .
# %f ---> for holding a place to float .
# %.num f ---> to manage the number of zeros .
# can also do it with %.num s .

name = "samuel"
age = 19
rank = 10.1
print("your age is:-", age ,"and your name is:-", name)
print(f"your age is:- {age:,}")
print("hi %s" % name)
print("hi : %s ,ur age is: %d ,and ur rank is : %.1f point" % (name,age,rank))
print("hi %.3s" % name)

#format()
name = "samuel"
print("hi : {} ,ur age is: {} ,and ur rank is : {} points".format(name,age,rank))
print("hi : {:.3s} ,ur age is: {:d} ,and ur rank is : {:.1f} points".format(name,age,rank))

# formate numbers
my_money = 5000000000
print("my mony in the bank is : {:,}".format(my_money))

print("-"*69)

# reArrange items 
a, b , c = 1 , 2, 3
print("hi {1},{2},{0}".format(a,b,c))
print("hi {1:.2F},{2:d},{0:.2f}".format(a,b,c))

# complex numder .
a = 2+5j
print("real part is : {}".format(a.real))
print("imaginary part is : {}".format(a.imag))

# can convert any type of nums to another type except complex type .
q = 11
print(float(q))
print(int(q))
print(complex(q))
q = 11+99j
# print(int(q)) # ---> error: can't convert complex number to another number's types .

print("-"*69)

# {+} addition .
# {-} suptraction .
# {*} multiplication .
# {%} modulus .
print(22%5) # ---> 2 Because the nearest number that can be divided by five and gives an integer value is 20 and the muduls is(20 - 22)
print(20%5) # ---> 0 Because 20 can be dvided by 5 and gives integar value so muduls is 0
# {/} devision .
# {**} exponent .
# {//} floor devision .
print(100//20)
print(120//20)

print("-"*69)

# edit a list
a = ["sasa","lol",1,22.1]
a[1] = "py"
print(a)
a[:3] = []
print(a)
q = ["python", "java", "c++"]
q[:2] = ["hi","pu"]
print(q)

# append()
MyFriend = ["mena", "jojo","peter"]
MyFriend.append("marten")
print(MyFriend)
oldFriend=["keroles","samuel"]
MyFriend.append(oldFriend)
print(MyFriend)
print(MyFriend[-1][0])

print("-"*69)

# extand()
nums=[1,2,3,4]
alpha=["a","g","t","u"]
nums.extend(alpha)
print(nums)

# remove()
hi = ["sasa","peter","sasa"]
hi.remove("sasa")
print(hi)

# sort()
num = [1,33,10,1222,-90]
num.sort()
print(num)
num.sort(reverse=True)
print(num)
alpha = ["a","c","b"]
alpha.sort()
print(alpha)
# alpha = [12,"w","a"]
# alpha.sort() ---> error

# reverse()
num = [1,2,4,5,"lol"]
num.reverse()
print(num)

print("-"*69)

# clear()
a = [1,2,3,4,]
a.clear()
print(a)

# coby()
a = [1,2,3,4]
c = a.copy() # just take a coby for onr time .
a.append(11)
print(c , a)

# count()
a = [1,2,3,3,3,3,3,3,3,]
print(a.count(3))

# index() ----> access to the index of a character .
hi = ["sasa","peter","sasa"]
print(hi.index("sasa"))

# insert()
hi = ["sasa","peter","sasa"]
hi.insert(0,"yoyoyo")
hi.insert(-1,"yoyoyo")
print(hi)

# pop()
hi = ["sasa","peter","lol"]
print(hi.pop())
print(hi.pop(1))

print("-"*69)

a=("sasa",)
print(type(a))
# to merge two tubles or more .
c = (1, 2,45,5)
b = c + a + ("a", 1,True)
print(b)

# to repeat list,tuble or str * .
mystr = "sasa,"
mylist = [1,2,3,45,6]
mytuble = (1,2,3,4,4,8)
print(mystr*6)
print(mytuble*6)
print(mylist*6)

# to ignore an element .
a =(1,2,3,5)
q,w,e,_ = a
print(q,w,e)

print("-"*69)

# set 

# we can use a lot of mythods we used before with tubels and lists .
myset = {1,2,"sasa",(1,23,4)}
print(myset) # set is not ordered 
# print(myset[0]) ---> you cannt access the index of any element in set and cannt slicing .
myset = {1,1,1,2,2,"sasa",(1,23,4)} # items are uniqe .
print(myset)

print("-"*69)

# union
myset = {1,2,"sasa",(1,23,4)}
a = {4,6,7,"lol"}
x = {9,0}
print(myset.union(a,x))

# remove()
myset = {1,2,"sasa",(1,23,4)}
myset.remove(1)
# myset.remove(222) ---> error .

# diacard()
myset = {1,2,"sasa",(1,23,4)}
myset.discard(1)
myset.discard(222) # --->will not give a error .
print(myset)

# pop() with set will give a random element .
myset = {1,2,"sasa",(1,23,4)}
print(myset.pop())

# update()
myset = {1,2,"sasa",(1,23,4)}
a = {4,6,7,"lol"}
myset.update(a)
yy = ["ww",99 ,123]
myset.update(yy)
print(myset)

print("-"*69)

# difference()
myset = {1,2,"sasa",(1,23,4)}
a = {1,4,6,7,"lol"}
print(myset.difference(a))
print(myset)

print("-"*69)

# difference_update()
myset = {1,2,"sasa",(1,23,4)}
a = {1,4,6,7,"lol"}
myset.difference_update(a)
print(myset)

print("-"*69)

# intersection() != difference()
myset = {1,2,"sasa",(1,23,4)}
a = {1,4,6,7,"lol",(1,23,4)}
print(myset.intersection(a)) # gives the rebeated elements .

print("-"*69)

# intersection_update()
myset = {1,2,"sasa",(1,23,4)}
a = {1,4,6,7,"lol",(1,23,4)}
print(myset)
myset.intersection_update(a)
print(myset)

print("-"*69)

# symmetric_difference()
myset = {1,2,"sasa",(1,23,4),"lol"}
a = {1,4,6,7,"lol"}
print(myset)
print(myset.symmetric_difference(a))

print("-"*69)

# symmetric_difference_update()
myset = {1,2,"sasa",(1,23,4),"lol"}
a = {1,4,6,7,"lol"}
print(myset)
myset.symmetric_difference_update(a)
print(myset)

print("-"*69)

# issuperset()
myset = {"sasa","lol",1,2,4,6,7}
a = {1,4,6,7,"lol"}
print(myset.issuperset(a)) # tell u if the set contain all elements in a nother set like .
print(a.issuperset(myset)) # false beceause set"a"don't have all elements of set "myset" .

print("-"*69)

# issubset()
myset = {"sasa","lol",1,2,4,6,7}
a = {1,4,6,7,"lol"}
print(myset.issubset(a)) # tell u if all elements of the orginal set "myset" is in the another set "a" .
print(a.issubset(myset)) # true becease all elements of "a" is in "mylist"

print("-"*69)

# isdisjoint()
a = {1,2,3,4}
c = {1,3,4,5}
f = {1}
d = {11,44,66,8,0}
print(a.isdisjoint(c)) # false becease it tells u if there is no elements in a set are in another set .
print(c.isdisjoint(a)) # false becease there is "1,2,3,4" .
print(c.isdisjoint(f)) # false becease there is "1" .
print(a.isdisjoint(d)) # true becease there is no elements in any set of those sets "a" and "d" is contained in another .

print("-"*69)