class Student:
    def __init__(self, name, marks):
        self.name =name
        self.marks=marks
    def avg(self):
        if(len(self.marks)==0):
            return 0
        return sum(self.marks)/len(self.marks)
    
    
s1 = Student("rohit", [23,31,41,51,21])
print("%s scored and average of %.2f marks"%(s1.name,s1.avg()))