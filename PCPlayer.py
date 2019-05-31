# -*- coding: utf-8 -*-
from random import random, choice

class PCPlayer:

	# Probabilidad de realizar jugada perfecta según grado de dificultad
	FACTORS = {
		'Fácil'  : 0.2,
		'Medio'  : 0.6,
		'Difícil': 1,
	}

	center  = (5,)
	corners = (7, 9, 1, 3)
	others  = (8, 4, 6, 2)

	# Estilo de juego según grado de dificultad
	STRATEGIES = {
		'Fácil'  : [others, center, corners],
		'Medio'  : [center, corners, others],
		'Difícil': [corners, center, others],
	}

	def __init__(self, **kwargs):
		self.letter = kwargs['letter']
		self.user_letter = kwargs['user_letter']
		self.board = kwargs['board']
		self.factor = self.FACTORS[kwargs['difficulty']]
		self.strategy = self.STRATEGIES[kwargs['difficulty']]

	def writeLetter(self, pos):
		self.board.writeLetter(self.letter, pos)

	def canWin(self):
		return self.board.playerCanWin(self.letter)

	def opponentCanWin(self):
		return self.board.playerCanWin(self.user_letter)

	def doMovement(self):
		if self.canWin():
			self.tryToWin()
		elif self.opponentCanWin():
			self.tryToBlock()
		else:
			self.doRandomMovement()

	def tryToWin(self):
		""" El jugador intentará ganar, con probabilidad de éxito según dificultad """
		if random() <= self.factor:
			victory_pos = self.board.victoryPosition(self.letter)
			self.writeLetter(victory_pos)
		else:
			self.doRandomMovement()

	def tryToBlock(self):
		""" 
			El jugador intentará bloquear la línea ganadora del oponente,
			con probabilidad de éxito según dificultad
		"""
		if random() <= self.factor:
			block_pos = self.board.victoryPosition(self.user_letter)
			self.writeLetter(block_pos)
		else:
			self.doRandomMovement()

	def doRandomMovement(self):
		""" 
			Realiza un movimiento aleatorio siguiendo la prioridad determinada
			por el nivel de dificultad.
			Eventualmente, esto puede implicar ganar o bloquear una victoria.
		"""
		positions = self.board.getFreePositions()
		for group in self.strategy:
			possibilities = [pos for pos in group if pos in positions]
			if possibilities:
				self.writeLetter(choice(possibilities))
				break
