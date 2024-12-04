file = open("2016/inputi/day1.txt", "r")
line = file.read().split(', ')

print("***** PART 1 *****")

path = [0, 0]
dir = 'N'

next_move = {
  ('N', 'R'): 'E',
  ('N', 'L'): 'W',
  ('S', 'R'): 'W',
  ('S', 'L'): 'E',
  ('E', 'R'): 'S',
  ('E', 'L'): 'N',
  ('W', 'R'): 'N',
  ('W', 'L'): 'S'
}

movements = {
  'N': (0, 1),
  'S': (0, -1),
  'E': (1, 0),
  'W': (-1 ,0)
}

for instruction in line:
  direction, length = instruction[0], int(instruction[1:])
  dir = next_move[dir, direction]

  movex, movey = movements[dir]
  for _ in range(length):
    path[0] += movex
    path[1] += movey

print(abs(path[0]) + abs(path[1]))

print("***** PART 2 *****")

dir = 'N'
path = [0, 0]
visited = set()
visited.add(tuple(path))
revisited = False

for instruction in line:
  if revisited:
    break
  direction, length = instruction[0], int(instruction[1:])
  dir = next_move[dir, direction]

  movex, movey = movements[dir]
  for _ in range(length):
    path[0] += movex
    path[1] += movey

    if (tuple(path) in visited):
      revisited = True
      break
    visited.add(tuple(path))

print(abs(path[0]) + abs(path[1]))
