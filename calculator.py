import tkinter as tk

class Main(tk.Tk):
	def __init__(self, width = 300, height = 500):
		super().__init__()
		self.width = width
		self.height = height
		self.geometry(f"{int(width * 4/4)}x{height}")
		self.title("Calculator")
		self.resizable(False, False)
		self.signs = ["+", "-", "/", "*", '.']
		buttonCharacters = """123+D
456-)
789X(
.0/C=""" 
		buttonCharacters = [x for x in buttonCharacters.split("\n")]
		self.buttons = []

		for i, row in enumerate(buttonCharacters):
			for j, character in enumerate(row):
				self.buttons.append(tk.Button(master = self, text = character, font = "Calibri 25", bd = 0,
					command = self.actionFunction(character)))
				self.buttons[-1].place(x = j * self.width / 5, width = self.width / 5,
									   y = i * self.height / 5 + self.height / 5, height = self.height / 5)


		self.displayVal = tk.StringVar()
		self.equation = ""
		self.display = tk.Label(master = self, textvariable = self.displayVal, font = "Calibri 16", anchor = "w", wraplength = self.width * 3/5)
		self.display.place(x = 0, y = 0, width = self.width * 3/5 , height = self.height / 5)

		self.resultVal = tk.StringVar()
		self.resultDisplay = tk.Label(master = self, textvariable = self.resultVal, wraplength = self.width * 2/5, font = "calibri 15")
		self.resultDisplay.place(x = self.width * 3/5, y = 0, width = self.width *2/ 5, height = self.height / 5, )

		self.display['bg'] = "white"
		
		self.nightMode()

	def actionFunction(self, character):
		def a():
			c = character
			if c == "X":
				c = "*"
			self.updateDisplay(c)
		return a 

	def updateDisplay(self, character):
		#print(character)
		
		if character == "D":
			self.equation = ""
		
		elif character == "C":
			self.equation = self.equation[:-1]
		
		elif character == "(":
			if (self.equation != "") and not self.equation[-1] in self.signs:
				self.equation += "*"
				#print("afnashd jisah sjiah di")
			self.equation += character
		
		elif character == ")":
			rightCount = 0
			leftCount = 0
			for x in self.equation:
				if x == ")":
					rightCount += 1
			for x in self.equation:
				if x == "(":
					leftCount += 1
			if rightCount < leftCount:
				self.equation += character
			else:
				pass

		elif character != "=":
			if self.equation != "":
				if not (character in self.signs and self.equation[-1] == character):
					self.equation += character
				else:
					return
			else:
				if not (character in self.signs):
					self.equation += character
		else:
			pass
		result = ""
		try:
			result = eval(self.equation)
		except SyntaxError as e:
			result = ""
			print(str(e))
		except ZeroDivisionError:
			result = "Divided\nBy\nZero"
		except Exception as e:
			print(str(e))
		self.displayVal.set(self.equation)
		self.resultVal.set(str(result))
		#print(result)

	def nightMode(self):
		if self.display['bg'] == "white": 
			for b in self.buttons:
				self["bg"] = self.resultDisplay["bg"] =  self.display["bg"] = b["bg"] = "black"
				self.display["fg"] = self.resultDisplay["fg"] = b["fg"] = "white"

		else:
			for b in self.buttons:
				self["bg"] = self.resultDisplay["bg"] = self.display["bg"] = b["bg"] = "white"
				self.display["fg"] = self.resultDisplay["fg"] = b["fg"] = "black"

main = Main()
main.mainloop()
