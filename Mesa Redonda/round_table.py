chairs = [0, 1, 2]

def scan_integer(range):
  A = int(input())
  if (A < range and A >= 1):
    return A
  else:
    A = int(input("Insira um número entre 1 e {}: ".format(range)))
    return A

def chair_select(chairs, sort):
  counter = 0
  for i in range(0, sort):
    if counter + 1 < 3:
      counter += 1
    else:
      counter = 0
  return (chairs[counter])

chairs_selected = []

A = scan_integer(1000)
chairs_selected.append(chair_select(chairs, A))

B = scan_integer(1000)

if (chair_select(chairs, B) in chairs_selected):
  if (chair_select(chairs, B) == 2):
    chairs_selected.append(0)
  else:
    chairs_selected.append((chair_select(chairs, B) + 1))
else:
  chairs_selected.append(chair_select(chairs, B))

chairs.remove(chairs_selected[0])
chairs.remove(chairs_selected[1])

print(chairs[0])
