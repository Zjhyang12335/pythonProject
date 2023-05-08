class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.sex = sex
        self.age = age

    def personInfo(self):
        print('我叫%s，年龄%s，性别%s'%(self.name, self.age, self.sex))

class Student(Person):
    def __init__(self, name, age, sex, college, banji):
        super().__init__(name, age, sex)
        self.college = college
        self.banji = banji

    def personInfo(self):
        print('我叫%s，年龄%s，性别%s，我是%s的%s班的学生'%(self.name, self.age,self.sex, self.college, self.banji))

class Teacher(Person):
    def __init__(self, name, age, sex, college, professional):
        super().__init__(name, age, sex)
        self.college = college
        self.professional = professional

    def personInfo(self):
        print('我叫%s，年龄%s，性别%s，我是%s的%s讲师'%(self.name, self.age, self.sex, self.college, self.professional))

    def teach(self):
        return '今天讲了如何用面向对象设计程序员必读'
