sudoku = []
box = [[] for _ in range(9)]
def getBoxIndex(i,j):
  return ((i//3) * 3) + j//3

for i in range(9):
  r = list(map(int,list(input())))
  sudoku.append(r)
  for j in range(9):
    idx = getBoxIndex(i,j)
    box[idx].append(r[j])

mx = 0
idx = 0
for i in range(9):
  if mx <= len(box[i]):
    idx = i
    mx = len(box[i])
print()