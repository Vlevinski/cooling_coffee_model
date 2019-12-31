# copy the list from pdf like
#          fodselsNummer,firstName,lastName,age,email,programmingCourse
#    create record file Student Records.txt

class Student():
    def __int__(self,sN,fN,lN,age,email,pCourse):
        self.sN =sN
        self.fN =fN
        self.lN= lN
        self.age= age
        self.email=email
        self.pCourse=pCourse

    def DisplayName(self):
        print(self.fN, self.lN)

student = Student()
student.sN = "123456"
student.fN = "Nick"
student.lN = "Pann"
student.age = 33
student.email ="nick@yahoo.com"

student.DisplayName()
