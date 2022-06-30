# dictionary 
user = {
    "name" : "samuel",
    "age" : 19,
    "country" : "Egypt",
    "programer" : True
}
# how to access .
print(user)
print(user["country"])
print(user.get("programer"))

# to print just all keys .
print(user.keys())

# to print just all values .
print(user.values())

print("-"*69)

# two dimentional dict .
MyKnowledg = {
    "fav_games":"lol",
 
    "languges" : {
        "one" : "english",
        "two" : "germany",
    },
    "skills" : { 
        "one" : "programing",
        "two" : "problem solving",
        "three" : "fast typing",
    }
}
# access 
print(MyKnowledg["languges"]["one"])
print(len(MyKnowledg))
print(len(MyKnowledg["skills"]))
print(MyKnowledg.keys())
print("-"*69)


friend1 ={
    "name" : "peter",
    "age" : 19,

}
friend2 ={
    "name" : "mena",
    "age" : 19,

}
friend3 ={
    "name" : "joseph",
    "age" : 19,

}
allFriends = {
    "1" : friend1,
    "2" : friend2,
    "3" : friend3,
}
print(allFriends["1"]["name"])

print("-"*69)

# dict methods

# clear()
friend3 ={
    "name" : "joseph",
    "age" : 19,
}
friend3.clear()
print(friend3)

# update()
skills = {
    "languge" : 'english',
    "programing" : "python",
}
skills ["fast typing"] = "20%"
print(skills)
skills.update({"v games":"80%"})
print(skills)

print("-"*69)

# copy()
skills = {
    "languge" : 'english',
    "programing" : "python",
}
a = skills.copy() # ---> take copy for one time that mean that any update or edit in orginal dict will not be contained in this copy .
print(a)
skills.update({"lol" : 11})
skills["ww"] = 99
print(skills)
print(a)

print("-"*69)

# setdefult()
skills = {
    "languge" : 'english',
    "programing" : "python",
}

print(skills)
print(skills.setdefault("language","german")) # if this method didn't found languge variable it will edit what u write if it found a languge variable it will not edit it .
print(skills.setdefault("skill","fast typng"))

print("-"*69)

# popitem()
skills = {
    "languge" : 'english',
    "programing" : "python",
}
skills.update({"lol" : 11})
print(skills)
print(skills.popitem())

print("-"*69)

# items()
skills = {
    "languge" : 'english',
    "programing" : "python",
}
allSkills = skills.items() # it also can contain all updates not like copy().
print(allSkills)
skills["lol"] = 99
print(allSkills)

print("-"*69)

# fromkeys()
a = ("ss", "vv", "ll")
e = "s"
print(dict.fromkeys(a,e))

print("-"*69)

# true values
print(bool(1))
print(bool(1.1))
print(bool("sasa"))
print(bool(True))
print(bool([1,3,4,5,6]))

print("-"*69)

print(bool(0))
print(bool(""))
print(bool(''))
print(bool({}))
print(bool([]))
print(bool(()))
print(bool(None))
print(bool(False))

print("-"*69)

# type conversion
str()
int()
float()
complex()
tuple()
list()
set()
dict()
# cant't convert str and set to a dict
# lists and tubles must be 2 dimentions or nested to convert it to a dict
a = [["one",1],["two",2]]
print(dict(a))
w = (("one",1),("two",2))
print(dict(w))






















