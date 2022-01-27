


"Taking Inputs From User"


uinput=input("taking input from the user ")

print("input is: " ,uinput)

print(type(int(uinput)))


age=input("Enter Your Birth Year :  ")

age=2022-int(age)

print(age)



nt=int(input("Enter Number"))

print(nt)

print(type(nt))



"Formated Strings"


fir="hello"
las="goodbye"
thi=55

print(fir+las+"my name") #You can not concatinate int with string and our thir val is int

print(fir+" "+las+" "+"my name")

print(fir,las,"my name",thi)

print(f'{fir} {las} my name {thi}')

print("{} {} my name {}".format("hello","goodbye","55"))

s=("{} {} my name {}") #you don't need storing string 1st. See Below eg.

print(s.format(fir,las,thi))

print("{} {} my my name {}".format(fir,las,thi))

"see stringsformat.py for more"



"In Operator" #Gives True False for presence


course = 'Python for beginners'

print('Python' in course)
print('python' in course)

lis=[25,75,88,77]
print(88 in lis)
print(69 in lis)

"Similarly There is noy in too"

print("Python" not in course)
print(69 not in lis)

