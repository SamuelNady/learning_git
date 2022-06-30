# -------------------------------
# all data in python is object .
# first built in fn is "type()".
# -------------------------------

x = True
print(type("sasa"))
print(type(10.10))
print(type(10))
print(type(x))
print(type([12,"sasa",12,1.18]))
print(type((236,2134,"sasa")))
print(type({"one": 1 , "two": 2 , "three": 3}))

print("------------------------------------------------------------------------------------")

# ------------------------------------------------------------------
# can start a variable with{a-z} , {A-Z or underscore .
# can't start it with a number or spicial character .
# can put what we want after the starting of variable's name .
# every case of variabrl's names are sensitive {"name" is not "Name"} .
# ------------------------------------------------------------------

# can give more than one variables values in just one line
a, b, c = 1, 2, 3

print("-"*69)

# ------------------------------------------------------------------
# escape sequences characters .
# \b make a back space .
# to make a new line in your code not in string .
# ---> ( escabe new line(enter) + \ ) .
# to print back slash(\) you must write one more (\) .
# note --->back slash can escabe any character .
# \n can make a new line in output not in your code
# \r replace that characters befor \r by that characters after \r .
# \t make horizontal tab (6 spaces) .
# ------------------------------------------------------------------

print("helloo\b world")

# it will print ---> hi my name is samuel in one line .
print("hi\
my name\
is\
samuel ")

# it will print one back slash (\) .
print("hi \\ samuel")

# note --->back slash can escabe any character .
print('hi my name is \'samuel\'')
# wite out back slash escaping .
# print('hi my name is 'samuel'') (remove the #) .

# \n can make a new line in output not in your code
print("hi\nsamuel")

# \r replace that characters befor \r by that characters after \r .
print("sasa\r1234")
# \t make horizontal tab (6 spaces) .
print("hi\tsamuel")
# triple """ or ''' will make multable lines in your code and your output LOL :).
# ---> and can also escabe characters like ths back slash .
print("""s
S
---> \ S
S ---> \
S
S
s""")

print("-"*69)

# salicing is --->
a = "samuel nady"
print(a[8]) #----> access a index .
print(a[2:7]) #---> will print (muel na) because end is not included .
print(a[:6]) #---> if you don't write the starting it will start from 0 .
print(a[2:]) #---> if you don't write the ending it will start from the last posion .
print(a[2:-3]) 
#steps
print(a[::2]) #---> it skeps one character after printing what we assign and continue and continue doing it till the end .
print(a[::3]) #---> it skeps 2 character after printing what we assign and continue and continue doing it till the end .

print("-"*69)

# -----------------------
# --- strings methods ---
# -----------------------
a = "()()())()()()())()        samuel nady         )*("
print(len(a))
print(a.strip())
print(len(a)) # strip fun will not change the variabel character numbers .
print(len(a.strip())) #but if we do it like that len will print the lenth with out striped string .
print(a.rstrip()) # will remove spaces from the right side .
print(a.lstrip()) # will remove spaces from the left side .
print(a.strip(")(*")) # strip fun also can remove any thing you want but if you gaved it a parametar .

print("-"*69)

# titel()
a = "samuel loves programing and 3g technology ."
print(a.title())

# capitalize
a = "samuel Loves programing and 3g technOlogy ."
print(a.capitalize())

#zfill
c,v,b = "1", "11", "111"
print(c.zfill(3))
print(v.zfill(3))
print(b.zfill(3))

# upper()
a="sAmUel.upper"
print(a.upper())
# lower()
a="sAmUEl.lower"
print(a.lower())

print("-"*69)

# split() & rsplit() & splitlines()
x = "i love python "
print(x.split()) # it can take two parameters 
# the firs patameter .
x = "i-love-python-.First-Parameter"
print(x.split("-"))
# seconed parameter .
x = "i-love-python-.secound-Parameter"
print(x.split("-",2)) # it will make just 2 strings as a elements in the list and other all string will be just in one element in the list .
# splitlines()
x = "i love python "
print(x.splitlines()) # ---> will make all elementes as a one element in a list .
# rsplit()
x = "i-love-python-and-java script-.rsplit"
print(x.rsplit("-",2)) # dong all what split() fon do but from the right side .

print("-"*69)

# join()
my_list = ["sasa","python","css"]
print("-".join(my_list))
print(" ".join(my_list))

print("-"*69)

# center()
# اول باراميتير اللى هيه الرقم بتعد عدد حروف الفاليو اللى انت عاوز تحط قبلها او بعدها
#  الاضافات ولو مثلا عاوز تحط قبل او بعد الفاليو دى اتنين هاشتاج مثلا من هنا و من هنا بتزود 4 على عدد حروف الفاليو
# و هكذا اعتمادا على عدد الكاراكترز اللى عاوز تزودها قبل وبعد الفاليو باختصار عدد حروف الفاليو + عدد الكركترز
x = "Samuel"
print(x.center(10,)) # spaces and it is the defult
print(x.center(10,"#")) # hashtag
print(x.center(12,"@")) # @

# rjust() ljust() the same like center() but the deffrence is that ljust() do center() work from the left
#  & rjust() do center() work from the right .
# sasa is 4 characters .
a = "sasa"
print(a.ljust(8,"#"))
print(a.rjust(8,"#"))

# count()
x = "i love python beceause python is too easy"
print(x.count("python")) # count how many "python" in this string note (case sensitive) .
print(x.count("python",0,30)) # it can also take posions first num is starting posion and second num is ending posion .

# swapcase()
x = "my NAMe is Samuel"
print(x.swapcase())#--->make small capital and capitall small .

# startswith()
x = "my NAMe is Samuel"
print(x.startswith("m"))
print(x.startswith("S",11,16)) # make sure that posion 11 : 16 starts with S .

print("-"*69)

# endswith
x = "my NAMe is Samuel"
print(x.endswith("m")) # make sure that "my NAMe is Samuel" ends with m ---> false .
print(x.endswith("l",11,)) # make sure that posion 11 : 16 ends with l .
print(x.endswith("e",3,7)) # remember ends is not included .

# index()
a = "hello it's me"
print(a.index("l"))
print(a.index("e",0,11))
# print(a.index("m",0,9)) # ---> it will make error beceause of the position 0:9 is not include "m" .

print("-"*69)

# find()
a = "hello it's me"
print(a.find("m"))
print(a.find("m",0,11)) # it will print -1 beacouse of the position 0:11 is not include "m" .

# expandtabs()
a = "I\tlove\tpython"
print(a.expandtabs(1)) # to control tabs 

#istitel()
x = "Samuel Loves Python"
print(x.istitle()) # check if all first littar in each wors and the littars after nums are capital

print("-"*69)

# isspace()
x = " "
print(x.isspace())
# islower()
x = "i love python"
print(x.islower())
# isupper()
x = "I LOVE PYTHON"
print(x.isupper())
# isalpha()
x = "samuel loves python"
print(x.isalpha()) # it will be false beacouse of spaces .

print("-"*69)

#isalnum()
x = "sasa99"
w = "sasa"
z = "="
print(x.isalnum())
print(w.isalnum())
print(z.isalnum())
# replace()
a = "i'll count one one two three"
print(a.replace("one","1"))
print(a.replace("one","1",1)) # ---> it will replace str "one" for one time .
print(a.replace("one","1").replace("two","2"))
