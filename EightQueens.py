# Bart Shaughnessy 2016
#Solves Eight Queen Placement problem


import math
from array import array
from sys import stdout

class chessboard:
	def __init__(self, length, width):
		self.width = width
		self.length = length
		self.spaces = [[0 for x in range(self.length)] for x in range(self.width)]
		self.placements = []

	def placeQueen(self, row, col):
		if self.spaces[row][col] != 0:
			print "invalid selection!"
			return

		self.spaces[row][col] = 1

#now update the rest of the board to eliminate spaces the newly placed queen can capture
		for i in range(0, self.width):
			if self.spaces[i][col] != 1:
				self.spaces[i][col] = 'X'
			if self.spaces[row][i] != 1:
				self.spaces[row][i] = 'X'
		
		#dumb way to handle diagonals. To be improved in final version			
		rowIndex = row
		colIndex = col

		while rowIndex>0 and colIndex>0:
			rowIndex -= 1
			colIndex -= 1

		while colIndex<self.width and rowIndex<self.length:
			if self.spaces[rowIndex][colIndex] != 1:
				self.spaces[rowIndex][colIndex] = 'X'
			rowIndex += 1
			colIndex += 1

		rowIndex = row
		colIndex = col

		while rowIndex>0 and colIndex<self.width-1:
			rowIndex -= 1
			colIndex += 1

		while colIndex>=0 and rowIndex<self.length:
			if self.spaces[rowIndex][colIndex] != 1:
				self.spaces[rowIndex][colIndex] = 'X'
			rowIndex += 1
			colIndex -= 1

		self.placements.append([row,col])

	def findPlacements(self, x, y):  #takes x and y coordinates of a Queen on the board. 
		next_x = 0
		last_board_state = self.saveLastBoardState()
		self.placeQueen(x, y)

		if len(self.placements) == 8:
			self.printBoard()
			self.resetBoard()
			return "DONE"

		if x > self.length-1:
			return "Row index not valid"

		next_x = (x+1)%8

		moves = []
		for i in range(self.length):
			if self.spaces[next_x][i] == 0:
				moves.append(i)

		moves_count = len(moves)  #this seems better for keeping track of a loop. Instead we'd have to call len every time
		while moves_count !=0:
			y = moves.pop()
			result = self.findPlacements(next_x, y)

			if result == "DONE":
				return "DONE"
			if result == "No Moves Left":
				return "No Moves Left"
			moves_count -= 1

		if (moves_count == 0) and (len(self.placements)==1):
		 	print "No solution for that selection"
		 	return "No Moves Left"

		self.spaces = list(last_board_state)
		self.placements.pop()
		return
		
	def printBoard(self):
		for i in range(0, self.width):
			for j in range(0, self.length):
				print self.spaces[i][j]," ",
			print "\n"

		for i in range(len(self.placements)):
			print self.placements[i], " ", 
		print ""
		return

	def resetBoard(self):
		for i in range(0, self.width):
			for j in range(0, self.length):
				self.spaces[i][j] = 0
		self.last_placements = self.placements
		self.placements = []

	# lol why did I bother writing an accessor for a Python class
	def getLastPlacements(self):
		print self.last_placements

	def saveLastBoardState(self):
		last_board_state = [[0 for x in range(self.length)] for x in range(self.width)]
		for i in range(0, self.width):
			for j in range(0, self.length):
				last_board_state[i][j] = self.spaces[i][j]
		return last_board_state

	def masterTest(self):
		for i in range(0, self.width):
			for j in range(0, self.length):
				result = self.findPlacements(i, j)
				if result != 'DONE':
					print "No ", 
				print "Solution for ", i, " : ", j







	
