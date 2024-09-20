
import re

#num=input("enter a number: ")
#pattern = "^[6-9]\d*{9}$"
#result = re.findall(pattern,num)
#if result:
 #   print(f" {num} sucesfulle nterdd")
#else:
 #   print("invalid")

#. -> match with any character (alphabets, digits, special char etc....)
#[a-z]->  match lower case char.
#[A-Z]-> match upper case char
#[0-9]-> match digits
# when we .char & .digits class , it will match only single character
#(like single alphabet, single digit)
#when we put [a-z],[A-Z] it is matching single chaarctr.

#+ ->means atleast one
# *-> zero or more
# if we want multple occurences to be matched then use + or *
# when we +,*char & +,*digits class , it will match multiple characters

#[a-z]+ -> it will match atleast one alphabet and max anything.
#[a-z]* -> it will match zero or more.

#the total no.of occurences it accepts is zero or max anything.


#------------
#^ -> match something at the start of the string.
#$ -> match something at the end of the string.

# ?-specify something as optional
#[a-z]{4} -> means there should be 4 characters atleast.
##[a-z]{2,4}-> here it can accept min 2 aplhabets and max 4.
#if we specify more/less than that , then it is not acceptable.
s="12-02-1999"
p=re.compile("^(?P<date>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})$")
l=re.search(p,s)
print(l)
if l:
    print(l.group("year"))
else:
    print("invalid match")

s="AAABCDE1234A"
r=re.compile("[A-Z]{5}[0-9]{4}[A-Z]")
l=re.findall(r,s)
print(l)

s="ABCDE1234A"
r=re.compile("^[A-Z]{5}[0-9]{4}[A-Z]")
l=re.findall(r,s)
print(l)

s="9867334840"
r=re.compile("^[6-9]{1}[0-9]{9}$")
l=re.findall(r,s)
print(l)


#dd-mm-yy
s="12-02-1999"
r=re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
l=re.findall(r,s)
print(l)

mob="8867334740"
r=re.compile("^[6-9]{1}[0-9]{9}$")
l=re.findall(r,mob)
print(l)

s="12-02-1999"
r=re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
l=re.search(r,s)
print(l)
print(l.group())
#search:- it will try to seacrh this pattern ("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
# in this string s="12-02-1999" and give first occurrence of it.
#if pattern exist it will return "Match object"
# else it will return none.

# if we want to fetch the value of match string, then use method: "group"

#Note:(findall) it will try to search all the occurences of this pattern "^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
#in this striing s="12-02-1999"

s="12-02-199"
r=re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
l=re.search(r,s)
print(l)
if l:
    print(l.group())
else:
    print("pattern not found")
    

#if i want to search group by group
s="12-02-1999"
r=re.compile("^([0-9]{2})-([0-9]{2})-([0-9]{4})$")
l=re.search(r,s)
print(l)
if l:
    print(l.group(1))
    print(l.group(2))
    print(l.group(3))
else:
    print("pattern not found")

s="12-02-1999"
p=re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
l=re.findall(p,s)
print(l)
if l:
    print(l.group())
else:
    print("invalid match")


#now suppose if we have 10-20 groups , so its difficult to remenver as per the
    #index , for this python provides "Named Groups"


s="12-02-1999"
r=re.compile("^(?P<date>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})$")
l=re.search(r,s)
print(l)
if l:
    print(l.group("date"))
    print(l.group("month"))
    print(l.group("year"))
else:
    print("pattern not found")

#here we need to specify +91 as optional
    #(+91)? -> means +91\s is optional
    #for sppace -> we use \s
mob="8867334740"
r=re.compile("(\+91\s)?[6-9]{1}[0-9]{9}")
l=re.search(r,mob)
if l:
    print(l.group())
else:
    print("pattern not found")

    #it will show an error , because it is considering "+" as atleast one char
    #so we use \+


#now i want only 10 digir number
    #(\+91\s)-> spscify this as non-capturing group, so my group will not
    #capture that particular value
mob="+91 8867334740"
r=re.compile("(?:\+91\s)?([6-9]{1}[0-9]{9})")
l=re.search(r,mob)
if l:
    print(l.group(1))
    #print(l.group(2))
else:
    print("pattern not found")


#if i want everything other than digits
    #[^0-9] \D

#match alphanumeric values
#[a-zA-Z0-9] \w

#match anything other than alphanumeric values
#[^a-zA-Z0-9] \W

#match space: \s
#match anything other than space \S

s="9867334740"
r=re.compile("^(\+91\s)?[6-9][0-9]{9}$")
l=re.search(r,s)
print(l.group())



s="12-09-1999"
r=re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
l=re.search(r,s)
print(l.group())




s="24-02-1999"
r=re.compile("^([0-9]{2})-([0-9]{2})-([0-9]{4})$")
l=re.search(r,s)
if l:
    print(l.group(1))
    print(l.group(2))
    print(l.group(3))
else:
    print("pattern not found")


s="24-02-1999"
r=re.compile("^(?P<date>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})$")
l=re.search(r,s)
if l:
    print(l.group("date"))
    print(l.group("year"))
    print(l.group("month"))
else:
    print("pattern not found")









