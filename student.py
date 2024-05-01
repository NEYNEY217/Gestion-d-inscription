class Student: #Creation de la classe Student pour l'eleve
    def __init__(self, student_id, prenom, nom, age, grade, courses=None):
        self.student_id = student_id
        self.prenom = prenom
        self.nom = nom
        self.age = age
        self.grade = grade
        self.courses = {} if courses is None else courses

    def __str__(self):
        return f"ID: {self.student_id}, Prenom: {self.prenom}, Nom: {self.nom}, Age: {self.age}, Grade: {self.grade}"

    def enroll_course(self, course): #Fonction qui permet de s'inscrire dans un cours
        if course.course_id not in self.courses:
            self.courses[course.course_id] = course
            return True
        else:
            return False

    def drop_course(self, course_id): #Fonction qui permet de quitter un cours
        if course_id in self.courses:
            del self.courses[course_id]
            return True
        else:
            return False

    def display_courses(self): #fonction pour afficher le cours
        if self.courses:
            return "\n".join([str(course) for course in self.courses.values()])
        else:
            return "No courses enrolled"
