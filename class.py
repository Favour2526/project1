# write a python program to create an instance of a specified class and display the namespace of 
# the said instance
class Python():
    
    def __init__(self,name,age,hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def display(self):
        print(f'My name is {self.name}, i am {self.age} yrs old, my hobby is {self.hobby}')

details = Python('amarachi',17,'eating')
details.display()

# write a python class named student with two class attributes student_name,marks.modify the attr values of 
# the said class and print the original and modified values of the said attr

class Student():

    student_name = 'amarachi'
    marks = 90

    def __init__(self,name,mark):
        self.name = name
        self.mark = mark

    def display(self):
        print(f'Student name = {self.name}\nMark = {self.mark}')

    def repr(self):
        return (f'Student name = {self.name}\nMark = {self.mark}')

item1 = Student('amarachi',90)
item2 = Student('favour',75)
item3 =Student('chinonso',88)

item1.display()
item2.display()
item3.display()



# write a python class named student with two attr student_id,student_name.add new attr student class.
# create a function to display the entire attr and their values in student class


class Student():

    student_id = []
    student_name = []

    def __init__(self,Id,name,level):
        self.Id = Id
        self.name = name
        self.level = level

    def display(self):
        print(f'student Id = {self.Id}\nstudent name = {self.name}\nstudent level = level{self.level}')

student1 = Student('id','favour',100)
student2 = Student('Id','amara',300)

student1.display()
student2.display()


# write a python class which has two methods get_string and print_string.
# get_string accept a string from the user and print string prints the string in upper case

class String():
    def __init__(self,word):
        self.word = word

    def get_string(self):
        print(f'sentence = {self.word}')

    def print_string(self):
        print(self.word.upper())

word = String (input('enter any sentence\n'))

word.get_string()
word.print_string()
