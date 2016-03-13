# Bart Shaughnessy 2016
#Solves Eight Queen Placement problem

#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import math
from array import array
from sys import stdout
import time
#import os, sys

class chessboard:
	def __init__(self, length, width):
		self.width = width
		self.length = length
		self.spaces = [[0 for x in range(self.length)] for x in range(self.width)]
		self.placements = []
		self.rank = min(self.length, self.width)

	def placeQueen(self, row, col):
		if self.spaces[row][col] != 0:
			print "invalid selection!"
			return

		self.spaces[row][col] = 1

#now update the rest of the board to eliminate spaces the newly placed queen can capture
		for i in range(0, self.width):
			if self.spaces[i][col] != 1:
				self.spaces[i][col] = '.'
			if self.spaces[row][i] != 1:
				self.spaces[row][i] = '.'
		
		#dumb way to handle diagonals. To be improved in final version			
		rowIndex = row
		colIndex = col

		while rowIndex>0 and colIndex>0:
			rowIndex -= 1
			colIndex -= 1

		while colIndex<self.width and rowIndex<self.length:
			if self.spaces[rowIndex][colIndex] != 1:
				self.spaces[rowIndex][colIndex] = '.'
			rowIndex += 1
			colIndex += 1

		rowIndex = row
		colIndex = col

		while rowIndex>0 and colIndex<self.width-1:
			rowIndex -= 1
			colIndex += 1

		while colIndex>=0 and rowIndex<self.length:
			if self.spaces[rowIndex][colIndex] != 1:
				self.spaces[rowIndex][colIndex] = '.'
			rowIndex += 1
			colIndex -= 1

		self.placements.append([row,col])
		#self.printBoard()

	def findPlacements(self, x, y):  #takes . and y coordinates of a Queen on the board. 
		next_x = 0
		last_board_state = self.saveLastBoardState()
		self.placeQueen(x, y)

		if len(self.placements) == self.rank:
			#self.printBoard()
			self.resetBoard()
			return "DONE"

		if x > self.length-1:
			return "Row index not valid"

		next_x = (x+1)%self.length

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

		#if (moves_count == 0) and (len(self.placements)==1):
		if (moves_count == 0) and (len(self.placements)==0):
		 	print "No solution for that selection"
		 	return "No Moves Left"

		#print "recursing"
		self.spaces = list(last_board_state)
		self.placements.pop()
		return
		
	def printBoard(self):
		for i in range(0, self.width):
			for j in range(0, self.length):
				if self.spaces[i][j] == 1:
					print '\xE2\x99\x9B'," ",
				else:
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
				start_time = time.time()
				result = self.findPlacements(i, j)
				#if self.placements
				if result != 'DONE':
					print "No ", 
				print "Solution for ", i, " : ", j
				end_time = time.time()
				print "Solved in ", end_time-start_time







	
