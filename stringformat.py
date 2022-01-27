''' Formated strings '''

fir="hello"
las="goodbye"
thi=55

print(fir+las+"my name") #You can not concatinate int with string and our thir val is int

print(fir+" "+las+" "+"my name")

print(fir,las,"my name",thi)

print(f'{fir} {las} my name {thi}')

print("{} {} my name {}".format("hello","goodbye","55"))

#   s=("{} {} my name {}") #you don't need storing string 1st. See Below eg.

#   print(s.format(fir,las,thi))

print("{} {} my my name {}".format(fir,las,thi))

first=input("Enter Your Fisrst Name: ")

last=input("Enter Your Last Name: ")

birth=int(input("enter your Year of Birth: "))

birth=2022-birth

#sen="Hello {} it's great to have you aboard. {} {} he will be shortly with you. Currently you are {} years old."

print("Hello {} it's great to have you aboard. {} {} he will be shortly with you. Currently you are {} years old.".format(first,first,last,birth))
