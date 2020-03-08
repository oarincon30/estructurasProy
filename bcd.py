from xml.dom import minidom
docXML = minidom.parse("pruebaxml.xml")
doc2 = minidom.parse("transmilenio.xml")

nombre = docXML.getElementsByTagName("username")[0]
print("Nombre: ", nombre.firstChild.data)

nombre = docXML.getElementsByTagName("nombre")[1]
print("Nombre: ", nombre.firstChild.data)

estacion = doc2.getElementsByTagName("nombre")[0]
print("estacion: ", estacion.firstChild.data)

todosEmp = docXML.getElementsByTagName("empleado")
print()
print("-----")
print("lista de emp: ")
print()

for empleado in todosEmp:
    numId = empleado.getAttribute("id")
    username=empleado.getElementsByTagName("username")[0]
    password = empleado.getElementsByTagName("password")[0]
    num2=int(numId)
    print("id: %s"% numId)
    print("username: %s"% username.firstChild.data)
    print("username: %s"% password.firstChild.data)
    print(type(numId))
    print(num2)
    print(type(num2))
