class Person:
    def __init__(self, firstname, lastname, idnum):
        self.firstname = firstname
        self.lastname = lastname
        self.idnum = idnum
    
    def printPerson(self):
        print("Name: ", self.firstname, self.lastname)
        print("ID Number: ", self.idnum)


class Student(Person):
    def __init__(self, fname, lname, idnum, scores):
        Person.__init__(self, fname, lname, idnum)
        self.scores = scores
    
    def calculate(self):
        sum = 0 
        for score in self.scores:
            sum += score
        average = sum/len(self.scores)
        if average < 40:
            return 'T'
        elif average < 55:
            return 'D'
        elif average <70:
            return 'P'
        elif average < 80:
            return 'A'
        elif average < 90:
            return 'E'
        else:
            return '0'

if __name__  == "__main__":
    line = input().split()
    first_name = line[0]
    last_name = line[1]
    id_num = line[2]
    a = [100, 70, 80, 50, 67, 90, 100, 80, 80, 90]
    scores = list(map(int, a))
    s = Student(first_name, last_name, id_num, scores)
    s.printPerson()
    print('Grade:', s.calculate())
