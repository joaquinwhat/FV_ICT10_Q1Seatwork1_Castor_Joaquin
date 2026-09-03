from pyscript import document, display

name = "Joaquin" #String
age = 14 #integer
height1 = 167.5 #float
countries_to_visit = ["Netherlands", "America", "Brazil"] #list
student_type = True #boolean
student_info = {
    "color": "Black",
    "car_brand": "Ferrari",
    "shoe_size": 10.5,
    "best_friend": "Benedict Baldoria"
}
fruits = {"Mango", "Melon", "Strawberry"} #set
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday") #tuple

display("Name:", name, target="output")
display("Age:", age, target="output")
display("Height:", height1, target="output")
display("Countries to Visit:", countries_to_visit, target="output")
display("Student:", student_type, target="output")
display("Student Info:", student_info, target="output")
display("Favorite Fruits:", fruits, target="output")
display("Days in a week:", days, target="output")

def calculate(e):
    document.getElementById("output").innerHTML = ""

    num1 = float(document.getElementById("input1").value)
    num2 = float(document.getElementById("input2").value)

    addition = num1 + num2
    subtraction = num1 - num2

    display(f"Addition: {addition}", target="output")
    display(f"Subtraction: {subtraction}", target="output")
