n= int(input("Enter numebr of students: "))
record={}
maxi=-1
id = ""
for i in range(n):
    name=str(input("Enter student's name: "))
    marks=int(input("Enter marks: "))
    record[name]=marks
    if(marks>maxi):
        maxi=marks
        id=name
print("Student with Highest marks (%i) is %s"%(marks,id))