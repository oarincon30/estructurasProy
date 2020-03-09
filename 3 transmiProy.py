from xml.dom import minidom
doc = minidom.parse("transmilenio.xml")
estacion = doc.getElementsByTagName("nombre")[14]
print("estacion: ", estacion.firstChild.data)
print("estacion: ", estacion.firstChild.data)

class Item():
  def __init__(self, obj, obj2, obj3, obj4, obj5):
    self.item = obj
    self.geoLat = obj2
    self.geoLong = obj3
    self.tipo = obj4
    self.troncal = obj5
    self.nxtc = None
    self.prvc = None
    self.nxtd = None
    self.prvd = None

class ListDynamic(object):
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def add_element(self, ele, b, c, d, e):
    new_item = Item(ele, b, c, d, e)
    if self.size == 0:
      self.head = new_item
      self.tail=new_item
      aux = self.head
      aux.nxtc=self.tail
      aux2 = self.tail
      aux2.prvc=self.head
    elif self.size == 1:
      self.tail = new_item
      aux=self.head
      aux2=self.tail
      aux.nxtc=self.tail
      aux2.prvc=self.head
    else:
      aux3 = self.head
      while(aux3.nxtc != None):
        aux3 = aux3.nxtc
      self.tail = new_item
      aux3.nxtc = self.tail
      aux2=self.tail
      aux2.prvc=aux3

    self.size += 1

  def print_list(self):
    item = self.head
    g=0
    if self.size > 0:
        g=self.size
    for i in range(g):
      print(item.item)
      print(item.geoLat)
      print(item.geoLong)
      print(item.tipo)
      print(item.troncal)
      print("--")
      item =  item.nxtc
    print("-------------------\n")

  def printinv_list(self):
    item = self.tail
    g=0
    if self.size > 0:
        g=self.size
    for i in range(g):
      print(item.item)
      print(item.geoLat)
      print(item.geoLong)
      print(item.tipo)
      print(item.troncal)
      print("--")
      item =  item.prvc
    print("-------------------\n")

lista = ListDynamic()

todasEst = doc.getElementsByTagName("estacion")
print("-----")
for estacion in todasEst:
    nombre=estacion.getElementsByTagName("nombre")[0]
    latitud = estacion.getElementsByTagName("latitud")[0]
    longitud = estacion.getElementsByTagName("longitud")[0]
    tipo=estacion.getElementsByTagName("tipo")[0]
    troncal=estacion.getElementsByTagName("troncal")[0]
    a = nombre.firstChild.data
    b = latitud.firstChild.data
    c = longitud.firstChild.data
    b=float(b)
    c=float(c)
    d = tipo.firstChild.data
    e = troncal.firstChild.data
    #troncal=estacion
    lista.add_element(a, b, c, d, e)
    #print(a)
    #print(b)
    #print(c)
    #print(type(b))
    #print(type(c))
    #print()



#lista.add_element(entrada)

op=0
while ((op < 1) or (op > 5)):
    print("\n 3) Imprimir lista\n 4) Imprimir invertida\n 5) Salir")
    op=int(input("\n--Escoge una opcion: "))
    if op==1:
        op=0
    if op==2:
        op=0
    if op==3:
        lista.print_list()
        op=0
    if op==4:
        lista.printinv_list()
        op=0
