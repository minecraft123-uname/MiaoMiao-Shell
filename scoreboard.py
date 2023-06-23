import pygame


class Scoreboard:
	def __init__(self, screen, settings, stats):
		self.screen = screen
		self.screenRect = self.screen.get_rect()
		self.settings = settings
		self.stats = stats
		
		self.updateScore()
		self.render()
		
	def updateScore(self):
		'''更新分数'''
		self.scoreImage = self.settings.font.render(
			"Score: %6s" % self.stats.activeScore, True, 
			self.settings.textColor, self.settings.bgColor)
		self.scoreRect = self.scoreImage.get_rect()
		self.scoreRect.right = self.screenRect.width - 10
		self.scoreRect.top = 10
	
	def render(self):
		self.screen.blit(self.scoreImage, self.scoreRect)
