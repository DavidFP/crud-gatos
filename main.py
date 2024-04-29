from repository.crud import crud
from models.animal import animal
from tabulate import tabulate
import random
import webbrowser
import subprocess
import os
import platform

def display_animal(animalico):
    """
    The function `display_animal` takes a dictionary `animalico` as input and prints out each key-value
    pair in the dictionary.
    
    :param animalico: It looks like the function `display_animal` takes a dictionary `animalico` as a
    parameter and then iterates over its key-value pairs to display them in the format "key : value"
    """
    for key, value in animalico.items():
        print(f"{key} : {value}")

def get_random_cat():
    """
    The function `get_random_cat` returns a randomly generated cat with a name, age, color, and cuteness
    level.
    :return: A random cat object with a randomly selected name, age, color, and number of lives.
    """
    names =["chispa","bola de nieve","bola de nieve 2", "pequeño santa claus"]
    colors =["rubio","negro","rayado","fuego"]
    randAnimal = animal(random.choice(names),random.randint(0,10),random.choice(colors), random.randint(1,6))
    return randAnimal   

# This block of code is the main logic of your Python script. Let's break it down:
if __name__=="__main__":
    crud = crud()
    action = -1
    animal_id = 0
    mi_gato = get_random_cat()

    while action != 0:
        print(f"\n 1- Create \n 2- Get all \n 3- Update \n 4-Delete \n 5-Table format  \n 6- View Results in Web \n 99-Crear DB en docker \n 0- Exit")
        action = int(input("¿Qué deseas hacer?"))    
        if action==1:
            mi_gato = get_random_cat()
            animal_id = crud.create(mi_gato)
            print(f"Creado: {animal_id} Gato:{crud.get(animal_id)}")
        if action ==2:
            animals = crud.getAll()
            print("-----------------------------------------------")
            for animal in animals:
                if animal:
                    current_animal_index = list(animals).index(animal)
                    print(f"######### Animal ID:{current_animal_index}###############")
                    display_animal(animal)
                    print(f"######### Animal ID:{current_animal_index}###############")
        if action == 3: 
            crud.update(animal_id, get_random_cat())
            print(f"Updated: {crud.get(animal_id)}")
        if action == 4:
            idToDelete = int(input("¿Cúal es ID del animal a borrar?"))
            toDelete = crud.get(idToDelete)
            if toDelete:
                crud.delete(idToDelete)
            print(f"Deleted ID:{idToDelete} Animal: {crud.get(idToDelete)}")
        if action == 5:
            animals = crud.getAll()
            headers = animals[0].keys()
            rows = [list(animal.values()) for animal in animals]
            print(tabulate(rows, headers, tablefmt="grid"))
        if action == 6:
            animals = crud.getAll()
            headers = animals[0].keys()
            rows = [list(animal.values()) for animal in animals]
            table = tabulate(rows, headers, tablefmt="html")
            print(os.path)
            
            with open("template_animals.html","r") as template:
                html_template = template.read()
            
            html_content = html_template.replace("<!--DynamicTableContent-->", table)
            output_path = "current_animals.html"
            with open(output_path,"w+") as file:
                file.write(html_content)
                if platform.system() == "Darwin":
                    os.system(f"open ./{output_path}")
                else:    
                    webbrowser.open_new_tab(output_path)
                print("Open new tab")
        if action == 99:
            print("Esta acción obtendrá la imagen de redis a docker y lo expone en el puerto por defecto 6379")
            docker_command = ["docker", "run", "--name", "redis-gatos", "-d", "-p", "6379:6379", "redis"]
            subprocess.run(docker_command)