class Item():
  def __init__(self, obj):
    self.item = obj
    self.nxt = None

class ListDynamic(object):

  def __init__(self):
    self.head = None
    self.size = 0

  def add_element(self, ele):
    new_item = Item(ele)
    if self.size == 0:
      self.head = new_item
    else:
      aux = self.head
      while(aux.nxt != None):
        aux = aux.nxt
      aux.nxt = new_item
    self.size += 1

  def remove_tail(self):
      if self.size < 1:
          pass
      else:
          aux = self.head
          aux2 =self.size -2
          for i in range(aux2):
              aux = aux.nxt
          aux.nxt=None
          self.size -=1

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

          if (s>1)and(s<self.size):
            s2=s-2
            for i in range(s2):
                aux=aux.nxt
            aux.nxt=aux2.nxt
            aux2.nxt=None
            self.size-=1
          elif s==self.size:
              lista.remove_tail()
          elif s==1:
              aux2=aux2.nxt
              self.head=aux2

      else:
          print("NO esta en la lista")


  def print_list(self):
    item = self.head
    print("\n")
    for i in range(self.size):
      print(item.item)
      item =  item.nxt
    print("-------------------\n")


lista = ListDynamic()
#lista.size

op=0
while ((op < 1) or (op > 5)):
    print("\n 1) Agregar nuevo elemento \n 2) Elimina el ultimo elemento\n 3) Buscar y eliminar elemento\n 4) Imprimir lista\n 5)Salir")
    op=int(input("\n  -Escoge una opcion: "))
    if op==1:
        entrada=int(input("\n Escribe elemento a ingresar: "))
        lista.add_element(entrada)
        op=0
    if op==2:
        lista.remove_tail()
        op=0
    if op==3:
        eliminar=int(input("\n Escribe elemento a eliminar: "))
        lista.remove_element(eliminar)
        op=0
    if op==4:
        lista.print_list()
        op=0
