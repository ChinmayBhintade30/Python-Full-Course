# Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.

#we have to create a folder for 13 year old boy, which has 2 to 20 tables files in it



def generateTable(n):
    table = ""

    #empty string as variable table


    for i in range (1, 11):
        #creates mutliplication of every  number from 1 to 10


        table += f"{n} X {i} = {n*i}\n"


        #string of n X i = n*i in f string
    with open(f"tables/table_{n}", "w") as f:

        #write mode
        #tables/table{n} opens every single number file like table2, table 3, table4 in tables folder

        f.write(table)




for i in range(2,21):
    #this for loop generates the table from 2 to 20 
    generateTable(i)


    