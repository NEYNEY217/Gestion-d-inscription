class Course: #Creation de la classe Course pour le cours
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}"
