from js import document  

class_list = [
    "Max Ancheta", "Alonso Asuncion", "Enzo Battung", "Vic Buenvenida", 
    "Kayla Casul", "Athena Catapang", "Cade Chua", "Zyan Eusebio", 
    "Radhika Evangelio", "Mara Fado", "Kleiser Fermocil", "Curt Fernando", 
    "Ethan Francia", "Sophia Jimenez", "Javi Mabilog", "AC Mactal", 
    "Lei Magday", "Yanna Moya", "Zoe Mutia", "Luis Nazareno", 
    "Ara Quinto", "Inigo Romero", "Kyler Santos", "Jaedin Sarao", 
    "Briana Sy", "Charlotte Sy", "Jared Udono", "KC Vida"
]

def show_players(event=None):
    student_list = document.getElementById("student")
    student_list.innerHTML = ""  # clear previous list
    for student in class_list:
        li = document.createElement("li")
        li.textContent = student
        li.className = "list-group-item"
        student_list.appendChild(li)
