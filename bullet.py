import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

	def __init__(self, settings, screen, shotBullets, mrp, xMove, yMove):
		super().__init__()
		self.mrp = mrp
		self.settings = settings
		self.image = pygame.transform.rotate(
			pygame.image.load("images/chromosome.png"), self.mrp.angle)
		self.rect = self.image.get_rect()
		self.mrpRect = self.mrp.newRect
		self.screen = screen
		self.screenRect = self.screen.get_rect()

		self.rect.centerx = self.mrpRect.centerx
		self.rect.top = self.mrpRect.top

		self.xMove = xMove
		self.yMove = yMove

	def render(self): 
		self.screen.blit(self.image, self.rect.center)
	
	def shoot(self):
		self.rect.centerx += self.xMove
		self.rect.centery -= self.yMove
