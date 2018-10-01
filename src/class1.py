import json

class gradebook():
    data = []

    def __init__(self):

        with open(r'C:\Users\Mike\Desktop\CS551\hw3\cs451-551-analytics-engine\data\grade-data.json') as f:
            self.data = json.loads(f.read())
            #print(self.data)

    def m_students(self):
        bros=0
        for i in range(len(self.data)):
            if(self.data[i][1]=="M"):
                bros +=1
        print("this many bros: ",bros)


    def f_students(self):
        sis=0
        for i in range(len(self.data)):
            if (self.data[i][1]=="F"):
                sis +=1
        print("this many sis: ",sis)

    def grade_count(self):
        grade_a=0
        grade_b=0
        grade_c=0
        grade_d=0
        grade_f=0

        for i in range(len(self.data)):
            if(self.data[i][3] =="A"):
                grade_a += 1
            if(self.data[i][3] =="B"):
                grade_b += 1
            if(self.data[i][3] =="C"):
                grade_c += 1
            if(self.data[i][3] =="D"):
                grade_d += 1
            if(self.data[i][3] =="F"):
                grade_f += 1
        print("this many A's",grade_a)
        print("this many B's",grade_b)
        print("this many C's",grade_c)
        print("this many D's",grade_d)
        print("this many F's",grade_f)

    def avg_grade(self):
        grades = 0
        amount_grades = 0
        for i in (range(len(self.data))):
            if(self.data[i][3] =="A"):
                grades += 4
                amount_grades +=1
            if(self.data[i][3] =="B"):
                grades += 3
                amount_grades +=1

            if(self.data[i][3] =="C"):
                grades += 2
                amount_grades +=1
            if(self.data[i][3] =="D"):
                grades += 1
                amount_grades +=1
            if(self.data[i][3] =="F"):
                grades += 0
                amount_grades +=1
            if(self.data[i][2] =="A"):
                grades += 4
                amount_grades +=1
            if(self.data[i][2] =="B"):
                grades += 3
                amount_grades +=1
            if(self.data[i][2] =="C"):
                grades += 2
                amount_grades +=1
            if(self.data[i][2] =="D"):
                grades += 1
                amount_grades +=1
            if(self.data[i][2] =="F"):
                grades += 0
                amount_grades +=1
        print(amount_grades)
        avg_gr = (float((grades)) / (amount_grades))
        print(grades)
        print(avg_gr)
if __name__ == '__main__':
    gradebook().m_students()
    gradebook().f_students()
    gradebook().grade_count()
    gradebook().avg_grade()
