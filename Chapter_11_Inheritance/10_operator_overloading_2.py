class Student:
    def __init__(self, marks):
        self.marks = marks

    def __len__(self):
        return len(self.marks)

s = Student([85, 90, 95])
print(len(s))      # calls s.__len__()

#this prints 3 as it it takes list as an object which acts as string

#so len function looks for the number of elements in the list --> and ;len(s) call the __len__() which has
#gives returns the vakue len(self.marks)


