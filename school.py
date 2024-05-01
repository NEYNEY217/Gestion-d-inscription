from student import Student
from course import Course
import csv #Import de la librairie de CSV

class School: #Creation de la classe School pour l'éecole
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.load_students()
        self.load_courses()

    def load_students(self): #Fonction qui permet d'utiliser des fichiers CSV
        try:
            with open('students.csv', mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None)  
                for row in reader:
                    student_id, prenom, nom, age, grade = row
                    self.students[student_id] = Student(student_id, prenom, nom, int(age), int(grade))
        except FileNotFoundError:
            self.students = {}

    def save_students(self): #Fonction qui stock les donnees des eleves sur le fichier CSV
        with open('students.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['student_id', 'prenom', 'nom', 'age', 'grade'])
            for student in self.students.values():
                writer.writerow([student.student_id, student.prenom, student.nom, student.age, student.grade])

    def load_courses(self): #Fonction qui stock les cours sur le fichier CSV
        try:
            with open('courses.csv', mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip the header
                for row in reader:
                    course_id, name = row
                    self.courses[course_id] = Course(course_id, name)
        except FileNotFoundError:
            self.courses = {}

    def save_courses(self): #Fonction pour enregistrer tout les cours sur le fichier CSV
        with open('courses.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['course_id', 'name'])
            for course in self.courses.values():
                writer.writerow([course.course_id, course.name])

    def add_student(self, student_id, prenom, nom, age, grade): #Fonction pour enregistrer les eleves sur le fichier CSV
        if student_id not in self.students:
            student = Student(student_id, prenom, nom, age, grade)
            self.students[student_id] = student
            self.save_students()
            return True
        else:
            return False

    def remove_student(self, student_id): #Fonction pour supprimer les donnees des eleves
        if student_id in self.students:
            del self.students[student_id]
            self.save_students()
            return True
        else:
            return False

    def add_course(self, course_id, name): #Fonction pour ajouter un cours
        if course_id not in self.courses:
            course = Course(course_id, name)
            self.courses[course_id] = course
            self.save_courses()
            return True
        else:
            return False

    def remove_course(self, course_id): #Fonction pour supprimer un cours
        if course_id in self.courses:
            del self.courses[course_id]
            for student in self.students.values():
                student.drop_course(course_id)
            self.save_courses()
            return True
        else:
            return False

    def enroll_student_in_course(self, student_id, course_id):  #Fonction pour enregistrer les eleves d'un cours
        if student_id in self.students and course_id in self.courses:
            student = self.students[student_id]
            course = self.courses[course_id]
            if student.enroll_course(course):
                self.save_students()  
                return True
        return False

    def display_students(self): #Fonction pour afficher 
        if self.students:
            return "\n".join([str(student) for student in self.students.values()])
        else:
            return "Aucun eleve n'est enregistrer"

    def display_courses(self):
        if self.courses:
            return "\n".join([str(course) for course in self.courses.values()])
        else:
            return "Aucun cours n'est enregistre"

    def display_student_courses(self, student_id):
        if student_id in self.students:
            return self.students[student_id].display_courses()
        else:
            return "Aucun n'eleve n'a ete trouvé"
