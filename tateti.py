# -*- coding: utf-8 -*-
from PCPlayer import PCPlayer
from gameboard import GameBoard, PositionError
from random import randint

class Tateti:

	LETTERS = ("X", "O")
	DIFFICULTIES = {
		'1': 'Fácil',
		'2': 'Medio',
		'3': 'Difícil',
	}

	def run(self):
		self.welcome()
		self.chooseDifficulty()
		self.chooseLetter()
		self.initVars()
		self.showFirstPlayer()
		while not self.gameIsOver():
			self.turn_nr += 1
			self.board.show()
			self.showInfo()
			self.makeMovement()
		self.board.show()
		self.finishGame()

	def welcome(self):
		print "¡Bienvenido al Tateti!\n"

	def chooseDifficulty(self):
		print "Seleccioná la dificultad del juego escribiendo el número correspondiente."
		for nr, mode in sorted(self.DIFFICULTIES.items()):
			print "%s - %s" % (nr, mode)
		selection = raw_input()
		if selection in self.DIFFICULTIES:
			self.difficulty = self.DIFFICULTIES[selection]
			print "Elegiste jugar en modo %s.\n" % (self.difficulty)
		else:
			print "Esa dificultad no existe. Intentá de nuevo."
			self.chooseDifficulty()

	def chooseLetter(self):
		letter = raw_input("¿Vas a jugar con X o O?\n").upper()
		if letter in self.LETTERS:
			self.user_letter = letter
			self.pc_letter = filter(lambda l: l != self.user_letter, self.LETTERS)[0]
		else:
			print "Letra no válida. Intentá de nuevo."
			self.chooseLetter()
	
	def initVars(self):
		self.winner = False
		self.tie = False
		self.first_player = self.LETTERS[randint(0,1)]
		self.last_player = None
		self.turn_nr = 0
		self.board = GameBoard()
		kwargs = {'difficulty': self.difficulty,
				  'board': self.board,
				  'letter': self.pc_letter,
				  'user_letter': self.user_letter}
		self.pc_player = PCPlayer(**kwargs)

	def showFirstPlayer(self):
		print "Sorteando quién juega primero..."
		if self.first_player == self.user_letter:
			print "¡Excelente! Jugás primero."
		else:
			print "Mala suerte. Empieza la computadora."

	def showInfo(self):
		if self.getNextPlayer() == self.user_letter:
			print "Turno %i. Te toca." % self.turn_nr
		else:
			print "Turno %i. Juega la computadora." % self.turn_nr

	def makeMovement(self):
		next_player = self.getNextPlayer()
		if next_player == self.user_letter:
			self.doPlayerMovement()
			self.last_player = self.user_letter
		else:
			self.pc_player.doMovement()
			self.last_player = self.pc_letter		

	def getNextPlayer(self):
		if self.last_player:
			if self.last_player != self.LETTERS[0]:
				next_player = self.LETTERS[0]
			else:
				next_player = self.LETTERS[1]
		else:
			next_player = self.first_player
		return next_player

	def doPlayerMovement(self):
		try:
			pos = int(raw_input("¿En qué posición vas a anotar?\n"))
			self.board.writeLetter(self.user_letter, pos)			
		except (ValueError, PositionError):
			print "Posición no válida. Intentá de nuevo con un número entre 1 y 9."
			self.doPlayerMovement()

	def gameIsOver(self):
		""" 
			Evalúa si terminó el juego, ya sea porque algún jugador realizó
			ta-te-tí o porque no hay más espacio disponible. 
		"""
		is_over = False
		winner_letter = self.board.getWinnerLetter(self.LETTERS)
		if winner_letter:
			is_over = True
			self.winner = winner_letter == self.user_letter
		elif self.board.isFull():
			is_over = True
			self.tie = True
		return is_over

	def finishGame(self):
		if self.winner:
			print "¡Felicitaciones, ganaste!"
		elif self.tie:
			print "¡Es un empate!"
		else:
			print "Qué lastima, perdiste."
		print "Fin del juego."


game = Tateti()
game.run()