# CMD Timepass
import os
import time
from random import randint

baseGrid = [" " * 50 for x in range(25)]
for x in range(len(baseGrid)):
	baseGrid[x] = "#" + baseGrid[x][1:len(baseGrid[x]) - 1] + "#"
baseGrid[0] = baseGrid[-1] = "#" * 50

frames = [
r"""    _____  
   /     \ 
  (  O  O )
   \  -  / 
    -----  
     /|\   
    / | \  
      |    
     / \   
    /   \  
""",
r"""    _____  
   /     \ 
  (  O  O )
   \  -  / 
    -----  
     /|\   
    / | =/ 
      |    
     / \   
    /   \  
"""
,r"""    _____  
   /     \ 
  (  O  O )
   \  -  / 
    -----  
     /|\ / 
    / | =  
      |    
     / \   
    /   \  
"""
,r"""    _____  
   /     \ 
  (  -  - )
   \  -  / 
    ----- /
     /|==/ 
    / |    
      |    
     / \   
    /   \  
"""
,r"""    _____  
   /     \ 
  (  O  O )
   \  -  / 
    -----\ 
     /|==/ 
    / |    
      |    
     / \   
    /   \  
"""
,r"""    _____  
   /     \ 
  (  O  O )
   \  -  / 
    ----- /
     /|==/ 
    / |    
      |    
     / \   
    /   \  
"""
,r"""    _____  
   /     \ 
  (  O  O )
   \  -  / 
    -----\ 
     /|==/ 
    / |    
      |    
     / \   
    /   \  
"""
,r"""    _____  
   /     \ 
  (  -  - )
   \  -  / 
    ----- /
     /|==/ 
    / |    
      |    
     / \   
    /   \  
"""
,r"""    _____  
   /     \ 
  (  O  O )
   \  -  / 
    -----  
     /|\ / 
    / | =  
      |    
     / \   
    /   \  
"""
,r"""    _____  
   /     \ 
  (  O  O )
   \  -  / 
    -----  
     /|\   
    / | =/ 
      |    
     / \   
    /   \  
"""
,r"""    _____  
   /     \ 
  (  O  O )
   \  -  / 
    -----  
     /|\   
    / | \  
      |    
     / \   
    /   \  
"""]

helloSign =r""" /============\ 
| Hello, You   |
| Are Amazing. |
| How you doin?|
\   Me? Good.  / 
 \____________/  
"""

grid = [" " * 50 for x in range(25)]

for x in range(len(grid)):
	grid[x] = "#" + grid[x][1:len(grid[x]) - 1] + "#"
grid[0] = grid[-1] = "#" * 50

class Dot:
	def __init__(self, pos = [0, 0], velocity = [1, 0]):
		self.pos = pos
		self.velocity = velocity
		self.master = None

	def update(self):
		self.pos[0] += self.velocity[0]
		self.pos[1] += self.velocity[1]

		

		return self.pos[0], self.pos[1]

dots = [Dot(pos = [0, randint(1, 48)]) for x in range(10)]
for x in dots:
	x.master = dots

global currentPlayerFrame
currentPlayerFrame = 0
def renderPlayer(pos = [19, 17]):
	global currentPlayerFrame
	if pos[0] >= len(grid) - len(frames[currentPlayerFrame].split("\n")):
		pos[0] = len(grid) - len(frames[currentPlayerFrame].split("\n"))

	for y, row in enumerate(frames[currentPlayerFrame].split("\n")):
		try:
			grid[pos[0] + y] = grid[pos[0] + y][:pos[1]] + row + grid[pos[0] + y][pos[1] + len(row):]
		except IndexError:
			print(y, row)
			print(f"grid[{pos[0] + y}] = grid[{pos[0] + y}][:{pos[1]}] + row + grid[{pos[0] + y}][{pos[1] + len(row)}:]")
			exit()
	currentPlayerFrame += 1
	if currentPlayerFrame >= len(frames):
		currentPlayerFrame -= currentPlayerFrame

def renderFigure(pos = [0, 0], frame = None):
	if pos[0] >= len(grid) - len(frame.split("\n")):
		pos[0] = len(grid) - len(frame.split("\n"))

	for y, row in enumerate(frame.split("\n")):
		try:
			grid[pos[0] + y] = grid[pos[0] + y][:pos[1]] + row + grid[pos[0] + y][pos[1] + len(row):]
		except IndexError:
			print(y, row)
			print(f"grid[{pos[0] + y}] = grid[{pos[0] + y}][:{pos[1]}] + row + grid[{pos[0] + y}][{pos[1] + len(row)}:]")
			exit()



while True:
	os.system("cls")
	grid = baseGrid[:]
	for dot in dots:
		x, y = dot.update()
		if x >= len(grid) - 1:
			del dot
			continue
		grid[x] = grid[x][:y] + "." + grid[x][y+1:]
	for x in range(3):dots.append(Dot(pos = [0, randint(1, 48)]))

	renderPlayer()
	renderFigure(frame = helloSign, pos = [7 ,15])
	for row in grid:
		print(row)

	time.sleep(0.166)