class Item():
  def __init__(self, obj):
    self.item = obj
    self.nxt = None
    self.prv = None

class ListDynamic(object):

  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def add_element(self, ele):
    new_item = Item(ele)
    if self.size == 0:
      self.head = new_item
      self.tail=new_item
      aux = self.head
      aux.nxt=self.tail
      aux.prv=self.tail
      aux2 = self.tail
      aux2.nxt=self.head
      aux2.prv=self.head
    elif self.size == 1:
      self.tail = new_item
      aux=self.head
      aux2=self.tail
      aux.nxt=self.tail
      aux.prv=self.tail
      aux2.nxt=self.head
      aux2.prv=self.head

    else:
      aux = self.head
      while(aux.nxt != self.head):
        aux = aux.nxt
      j=self.size-2
      aux4=self.head
      for i in range(j):
            aux4=aux4.nxt
      aux.nxt = new_item
      new_item.prv=aux4
      new_item.nxt=self.head
    self.size += 1


  def remove_element(self, val):
      elim=val
      aux = self.head
      aux2=self.head
      s=1
      t=0
      for i in range(self.size):
          if aux2.item==elim:
              t+=1
              break
          else:
              aux2 = aux2.nxt
              s+=1
      if (t>0):
          print("Esta en la lista"+str(s))

          if (s>1):
            s2=s-2
            for i in range(s2):
                aux=aux.nxt
            aux.nxt=aux2.nxt
            aux2.nxt=None
            aux3=aux.nxt
            aux3.prv=aux
            self.size-=1
          elif s==1:
            g=self.size-1
            for i in range(g):
                aux2=aux2.nxt
            aux3=aux.nxt
            self.head=aux3
            aux2.nxt=self.head
            aux3.prv=aux2


            self.size-=1

      else:
          print("NO esta en la lista")


  def print_list(self):
    item = self.head
    print("\n")
    g=self.size+2
    for i in range(g):
      print(item.item)
      item =  item.nxt
    print("-------------------\n")

  def printinv_list(self):
    item = self.tail
    print("\n")
    g=self.size+2
    for i in range(g):
      print(item.item)
      item =  item.prv
    print("-------------------\n")




lista = ListDynamic()
#lista.size

op=0
while ((op < 1) or (op > 5)):
    print("\n 1) Agregar nuevo elemento \n 2) Buscar y eliminar elemento\n 3) Imprimir lista\n 4) Imprimir invertida\n 5)Salir")
    op=int(input("\n  -Escoge una opcion: "))
    if op==1:
        entrada=int(input("\n Escribe elemento a ingresar: "))
        lista.add_element(entrada)
        op=0
    if op==2:
        eliminar=int(input("\n Escribe elemento a eliminar: "))
        lista.remove_element(eliminar)
        op=0
    if op==3:
        lista.print_list()
        op=0
    if op==4:
        lista.printinv_list()
        op=0
