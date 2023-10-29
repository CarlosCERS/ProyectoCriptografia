import json

with open("prueba.json","r") as f:
    my_dict=json.load(f)

nombre = my_dict["nombre"]
apellido = my_dict["apellido"]
edad = int(my_dict["edad"])

print (nombre)
print (apellido)
print (edad)
print (edad + 10)