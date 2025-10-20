#break statement - used to exit the loop in between using if condition in for loop

# for i in range(100):
    #It will print 0 to 100 values  exempting 100 , 0 to 99
    # if(i == 34):
        # break 
        # #Exit the loop right now - 
    #When i will be equal to 34 , exit the loop , 
    #it will print - 0 to 33 values


#it will print upto 33 , after that when i == 34 , it will break the loop and come out of the loop




    # print(i)

"""
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
"""








#Continue statement

# for j in range(10):
#     if(j == 7):
#         continue
#     print(j)


# here continue statement  does exactly opposite of break
#here continue is used to skip the iteration , that is , it will skip i == 7 and print rest of the iterations
#i == 7 is  skipped and continued further the next iteration


"""
0
1
2
3
4
5
6
8
9 
 """   

#pass statement

for i in range(20):
    pass



for i in range(10):
    print(i)

#here I want to print the 2nd loop and work later on 1st loop - so I can write pass statement in body of for loop

#Pass is null statement in Python - which tells to do nothing

#Otherwise it will show an error 

