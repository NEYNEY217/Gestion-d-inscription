from school import School
import utils
import time

def main():
    school = School()

    while True:
        print("\n1. Ajouter un élève")
        print("2. Supprimer un élève")
        print("3. Ajouter un cours")
        print("4. Supprimer un cours")
        print("5. Inscrire un élève à un cours")
        print("6. Afficher la liste des étudiants")
        print("7. Afficher la liste des cours")
        print("8. Afficher les cours d'un étudiant")
        print("9. Quitter")

        choice = utils.get_input("Entrez votre choix: ", int)

        if choice == 1:
            student_id = input("Entrez l'identifiant de l'élève: ")
            prenom = input("Entrez le prénom de l'élève: ")
            nom = input("Entrez le nom de l'étudiant: ")
            date_naiss = utils.get_valid_date("Entrez la date de naissance de l'élève: ")
            grade = utils.get_input("Entrez la note de l'année scolaire précedente: ", int)
            if school.add_student(student_id, prenom, nom, date_naiss, grade):
                print("Ajout de l'élève avec succès")
            else:
                print("Cet élève existe dêja")    
            time.sleep(2)

        elif choice == 2:
            student_id = input("Entrez l'ID de l'élève: ")
            if school.remove_student(student_id):
                print("Eleve supprimé avec succès")
            else:
                print("Eleve introuvable")
            time.sleep(2)

        elif choice == 3:
            course_id = input("Entrez l'ID du cours: ")
            name = input("Entrez le nom du cours: ")
            if school.add_course(course_id, name):
                print("Cours ajouté avec succès")
            else:
                print("Ce cours existe dêjà")
            time.sleep(2)

        elif choice == 4:
            course_id = input("Entrez l'ID du cours: ")
            if school.remove_course(course_id):
                print("Cours supprimé avec succès")
            else:
                print("Ce cours n'existe pas")
            time.sleep(2)

        elif choice == 5:
            student_id = input("Entrez l'ID de l'élève: ")
            course_id = input("Entrez l'ID de ce cours: ")
            if school.enroll_student_in_course(student_id, course_id):
                print("Eleve ajouté dans ce cours avec succès")
            else:
                print("Echec")
            time.sleep(2)

        elif choice == 6:
            print(school.display_students())
            time.sleep(2)

        elif choice == 7:
            print(school.display_courses())
            time.sleep(2)

        elif choice == 8:
            student_id = input("Entrez l'ID de l'élève: ")
            print(school.display_student_courses(student_id))
            time.sleep(2)

        elif choice == 9:
            print("Fermeture du programme...")
            time.sleep(1)
            break
        else:
            print("Choix invalide, réessayez")
            time.sleep(2)


if __name__ == "__main__":
    main()
