#can we have a set with 18 (aas int ) and '18' as a string as value in it?

s = set()

num = int(input("Enter a number: "))

s.add(num)

char = input("Enter number as string: ")
s.add(char)
print(s)

# Enter a number: 18
# Enter number as string: 18
# {'18', 18}
#as we know that set is also unordered in nature it is showing in random way

#Yes we can have a set with value 18  as int and value 18 as string

