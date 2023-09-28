class job():
  
  def __init__(self, name, salary, hours):
    self.name = name
    self.salary = salary
    self.hours = hours
  
  def printer(self):
    print(f'''
Job type: {self.name}
Salary: {self.salary}
Hours worked: {self.hours}
    ''')

class doctor(job):
  def __init__(self, specialty, experience):
    self.name = 'Doctor'
    self.salary = 'Very Huge'
    self.hours = '45'
    self.specialty = specialty
    self.experience = experience
    
  def printer(self):
    print(f'''
Job type: {self.name}
Salary: {self.salary}
Hours worked: {self.hours}
Speciality: {self.specialty}
Years of Experience: {self.experience}
''')

class teacher(job):
  
  def __init__(self, subject, position):
    self.name = 'Teacher'
    self.salary = 'Very very poor'
    self.hours = '100'
    self.subject = subject
    self.position = position

  def printer(self):
    print(f'''
Job type: {self.name}
Salary: {self.salary}
Hours worked: {self.hours}
Subject: {self.subject}
Position: {self.position}
''')

Lawyer = job('Lawyer', '$200,000', '60')
print(Lawyer.printer())
print()

Teacher = teacher('Computer Science', 'Vice Principal')
print(Teacher.printer())

Doctor = doctor('Pediatric Consultant', '7')
print(Doctor.printer())