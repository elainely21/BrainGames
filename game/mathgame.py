from game import boolgame
import pyglet
from utils import maths


class MathGame(boolgame.BoolGame):

	comparators = ['==', '<']
	operators = ['+', '-', '*', '/']


	def __init__(self, width, height):

		self.negative = -10 # tryin to be fair

		super().__init__('Math Game', width, height, description='Check if the expression is true or not')

		self.lblExp = pyglet.text.Label('2 < 4', font_size=20, x = self.width//2, y = self.description.y - 100, anchor_x = 'center', anchor_y = 'center')
		self.lblExp.draw()
		# self.window.push_handlers(on_draw = self.pyglet_on_draw)


	def game_on_draw(self):
		'''
		Default on_draw event for the game
		'''
		self.window.clear()
		self.lblExp.draw()


	def addNew(self):

		self.syncKey = True

		exp = self.genExpression()
		self.lblExp.text = exp[0]
		self.lblExp.draw()
		self.answer = exp[1]

		self.syncKey = False


	def genExpression(self):
		'''
		Generates a random expression for this game
		'''
		chComparator = maths.weightedRandomIndex([0.24, 0.76])
		leftSize = maths.weightedRandomIndex([0.15, 0.75]) + 1
		rightSize = maths.weightedRandomIndex([0.2, 0.8]) + 1

		oprPDF = [0.35, 0.20, 0.30, 0.15]
		numRange = [(1,1) , (1,9) , (9,15) , (15,25)]
		numPDF = [0.01, 0.69, 0.27, 0.03]

		lhs = ''
		for i in range(leftSize):
			lhs += ' ' + str( round(maths.weightedRandomRange(numPDF, numRange)) ) + ' '
			lhs += self.operators[ maths.weightedRandomIndex(oprPDF) ]
		rhs = ''
		for i in range(rightSize):
			rhs += ' ' + str( round(maths.weightedRandomRange(numPDF, numRange)) ) + ' '
			rhs += self.operators[ maths.weightedRandomIndex(oprPDF) ]

		lhs = lhs[:-1].strip()
		rhs = rhs[:-1].strip()

		ans = eval( '(' + lhs.replace('^','**') + ')' + 
					self.comparators[chComparator] +
					'(' + rhs.replace('^', '**') + ')' 
				)

		return (lhs + '  ' + self.comparators[chComparator] + '  ' + rhs , ans)
