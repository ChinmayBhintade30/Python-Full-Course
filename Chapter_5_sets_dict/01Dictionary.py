marks = {"harry": 100,
         "shubham": 45,
         "Steve": 67,
         0:"harry"
         }

print(marks,type(marks))

# {'harry': 100, 'shubham': 45, 'Steve': 67} <class 'dict'>

# a = {"key": "value",
#     "harrry": "code",
#     "marks": 100,
#     "list" : [1,2,9]
# }
# print(a["key"])
# print(a["list"])

# value
# [1, 2, 9]


# print(marks.items())
# dict_items([('harry', 100), ('shubham', 45), ('Steve', 67), (0, 'harry')])


#we get a list after items methods and we can key value in form of tuple


# print(marks.keys())
# dict_keys(['harry', 'shubham', 'Steve', 0])


# print(marks.values())
# dict_values([100, 45, 67, 'harry'])

# marks.update({"harry": 99, "renuka": 100})
#new key value pair renuka and 100 is added
# print(marks)

# {'harry': 99, 'shubham': 45, 'Steve': 67, 0: 'harry'}


# {'harry': 99, 'shubham': 45, 'Steve': 67, 0: 'harry', 'renuka': 100}



# print(marks.get("harry"))
# 99

# print(marks.get("shivika"))

# None


# print(marks["shivika"])
#  File "d:\Python_Full_Course\Chapter_5_sets_dict\01Dictionary.py", line 56, in <module>
#     print(marks["shivika"])
#           ~~~~~^^^^^^^^^^^
# KeyError: 'shivika'




print(marks.popitem())


# (0, 'harry')

print(marks.pop("harry"))
# 100

# print(marks.clear())
# print(marks)
# None
# {}

my_dict = {
    "harry": 100,
    "steven": 97,
    "rohan": 45
    
    }
print(my_dict.pop('harry','default value'))
# 100
print(my_dict.pop("shila","default value"))
# default value



