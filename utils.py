import re  #Import de la librairie re pour faciliter le controle de saisie
from datetime import datetime

def get_input(prompt, data_type=str):  #Fonction pour controler la saisie du choix du menu
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")

def get_valid_date(prompt): #Fonction pour controler la saisie de la date 
    while True:
        date_str = input(prompt)
        date_pattern = r"^(0[1-9]|[1-2][0-9]|3[0-1])-(0[1-9]|1[0-2])-\d{4}$"
        if re.match(date_pattern, date_str):
            return date_str
        else:
            print("Format de date invalide. Veuillez saisir une date au format JJ-MM-AAAA.")



