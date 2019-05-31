# -*- coding: utf-8 -*-

class GameBoard:

	VICTORY_LINES = [
		(7, 8, 9),	  # horizontales
		(4, 5, 6),
		(1, 2, 3),
		(7, 4, 1),	  # verticales
		(8, 5, 2),
		(9, 6, 3),
		(7, 5, 3),	  # diagonales
		(9, 5, 1),
	] 

	def __init__(self):
		self.table = [""] * 10	# La primera posición es sólo para facilitar el manejo de índices	

	def show(self):
		def getRowValues(rowNr):
			""" 
				Devuelve una tupla con las letras o espacios en la fila solicitada.
				Si el tablero está vacío, devuelve los números del cuadrante.
			"""
			if not any(self.table):
				if rowNr == 1:
					tup = (7,8,9)
				elif rowNr == 2:
					tup = (4,5,6)
				else:
					tup = (1,2,3)
			else:
				if rowNr == 1:
					tup = (self.table[7] or " ", self.table[8] or " ", self.table[9] or " ")
				elif rowNr == 2:
					tup = (self.table[4] or " ", self.table[5] or " ", self.table[6] or " ")
				else:
					tup = (self.table[1] or " ", self.table[2] or " ", self.table[3] or " ")
			return tup
		print ""
		print "***** Tablero de juego *****"
		print "       |       |       "
		print "   %s   |   %s   |   %s   " % getRowValues(1)
		print "       |       |       "
		print "-----------------------"
		print "       |       |       "
		print "   %s   |   %s   |   %s   " % getRowValues(2)
		print "       |       |       "
		print "-----------------------"
		print "       |       |       "
		print "   %s   |   %s   |   %s   " % getRowValues(3)
		print "       |       |       "
		print ""

	def writeLetter(self, letter, pos):		
		if not self.validPosition(pos): raise PositionError
		self.table[pos] = letter

	def validPosition(self, pos):
		""" Evalúa si la posición está disponible en el tablero de juego. """
		return pos in range(1, 10) and not self.table[pos]

	def getFreePositions(self):
		return [pos for pos, value in enumerate(self.table[1:], start=1) if not value]

	def isFull(self):
		return not self.getFreePositions()

	def playerCanWin(self, letter):
		"""
			Evalúa si el jugador puede ganar con la siguiente jugada.
			Puede ganar si tiene dos letras en al menos una línea de victoria.
			Si existe, retorna posición de victoria.
		"""
		return self.victoryPosition(letter)

	def victoryPosition(self, letter):
		victory_pos = None
		for line in self.VICTORY_LINES:
			count = len([pos for pos in line if self.table[pos] == letter])
			free_pos = 	[pos for pos in line if self.table[pos] == ""]
			if count == 2 and free_pos:
				victory_pos = free_pos[0]
				break
		return victory_pos

	def getWinnerLetter(self, letters):
		winner = None
		for letter in letters:
			for line in self.VICTORY_LINES:
				count = len([pos for pos in line if self.table[pos] == letter])
				if count == 3:
					winner = letter
					break
		return winner


class PositionError(Exception):
	pass
		