def check_sequence(stack):
  sec = []
  conta=0
  contb=0
  contc=0
  cond1=True
  for j in stack:
      sec.append (j)
  for i in sec:
      if i =="(":
          conta=conta+1
      elif i ==")":
          conta=conta-1
          if conta<0:
              cond1=False
      elif i=="[":
          contb=contb+1
      elif i==']':
          contb=contb-1
          if contb<0:
              cond1=False
      elif i=='{':
          contc=contc+1
      elif i=='}':
          contc=contc-1
          if contc<0:
              cond1=False

  if cond1==False or conta!=0 or contb!=0 or contc!=0:
        return "No es balanceado"
  if cond1==True and conta==0 and contb==0 and contc==0:
        return "Es balanceado"



seq = "{[]{()}}"
print(seq,"-", check_sequence(seq))

seq = "[{}{})(]"
print(seq,"-", check_sequence(seq))
