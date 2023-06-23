import os

import pygame

from tools import *


class Lives:
	def __init__(self, screen, settings, stats):
		self.screen = screen
		self.screenRect = self.screen.get_rect()
		self.files = [
			os.path.join("lives", "1_mrp.png"),
			os.path.join("lives", "2_200.png"),
			os.path.join("lives", "3_202.png"),
			os.path.join("lives", "4_mrpRfilter.png"),
			os.path.join("lives", "5_mrpGBkeep.png")]
		self.settings = settings
		self.stats = stats
		if len(self.files) < self.settings.lifenum:
			raise ValueError("Lives not enough according to settings!")
		self.images = [pygame.image.load(i) for i in self.files[:self.settings.lifenum]]
		
		self.livesImage = self.settings.font.render(
			"Lives: %2s" % self.stats.lives, True, 
			self.settings.textColor, self.settings.bgColor)
		self.livesRect = self.livesImage.get_rect()
		self.livesRect.top = 10
		self.livesRect.left = 10
		
		self.curImage = self.images[-self.stats.lives]
		self.curRect = self.curImage.get_rect()
		self.curRect.top = self.livesRect.bottom + 10
		self.curRect.left = 10	
	
	def addLives(self, n):
		'''更改血量'''
		if self.stats.lives + n <= 0:
			endGame()
		else:
			self.stats.addLives(n)
		
		self.livesImage = self.settings.font.render(
			"Lives: %2s" % self.stats.lives, True, 
			self.settings.textColor, self.settings.bgColor)
		self.livesRect = self.livesImage.get_rect()
		self.livesRect.top = 10
		self.livesRect.left = 10
		
		self.curImage = self.images[-self.stats.lives]
		self.curRect = self.curImage.get_rect()
		self.curRect.top = self.livesRect.bottom + 10
		self.curRect.left = 10	

	def render(self):
		self.screen.blit(self.curImage, self.curRect)
		self.screen.blit(self.livesImage, self.livesRect)
