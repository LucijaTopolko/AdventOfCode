file = open("2016/inputi/day2.txt", "r")
lines = file.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].split("\n")[0]

print("***** PART 1 *****")

movements = {
  'U': -3,
  'D': 3,
  'L': -1,
  'R': 1
}

seq = ''
button = 5

forbidden = [(3, 1), (6,1), (4, -1), (7, -1)]

for line in lines:
  for char in line:
    move = movements[char]
    if 1 <= button+move <= 9 and (button, move) not in forbidden:
      button = button + move
  seq += str(button)

print(seq)


print("***** PART 2 *****")

keypad = [
  ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
  ['x', 'x', 'x', '1', 'x', 'x', 'x'],
  ['x', 'x', '2', '3', '4', 'x', 'x'],
  ['x', '5', '6', '7', '8', '9', 'x'],
  ['x', 'x', 'A', 'B', 'C', 'x', 'x'],
  ['x', 'x', 'x', 'D', 'x', 'x', 'x'],
  ['x', 'x', 'x', 'x', 'x', 'x', 'x']
]

seq = ''
pos = [3, 1]

movements = {
  'U': (-1, 0),
  'D': (1, 0),
  'L': (0, -1),
  'R': (0, 1)
}

for line in lines:
  for char in line:
    movex, movey = movements[char]
    if keypad[pos[0] + movex][pos[1] + movey] != 'x':
      pos[0] = pos[0] + movex
      pos[1] = pos[1] + movey
  seq += keypad[pos[0]][pos[1]]

print(seq)