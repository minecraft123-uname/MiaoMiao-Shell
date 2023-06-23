from random import choice

import pygame

from pygame.transform import rotate


class MRP:

	def __init__(self, settings, screen):
		self.settings = settings
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.image = pygame.image.load("images/mrp.png")
		self.rect = self.image.get_rect()

		self.rect.top = 6
		self.rect.centerx = int(self.screen_rect.width / 2)
		self.center = self.rect.center
		self.newImage = self.image
		self.newRect = self.newImage.get_rect(center=self.center)
		
		self.X = self.rect.centerx # 中心x坐标固定
		
		self.move_left = False
		self.move_right = False

		self.direction = 1
		self.angle = 0

		self.clock = pygame.time.Clock()

	def render(self):
		self.screen.blit(self.newImage, self.newRect.topleft)

	def move(self):
		'''MRP响应左右键并移动'''
		if self.move_left:
			self.newRect.centerx -= self.settings.mrpSpeed
			self.X -= self.settings.mrpSpeed
		elif self.move_right:
			self.newRect.centerx += self.settings.mrpSpeed
			self.X += self.settings.mrpSpeed
	
	def rotate(self):
		'''MRP旋转'''
		if -self.settings.rotateAngle < self.angle < self.settings.rotateAngle:
			if self.direction == 1:
				self.angle += self.settings.rotateSpeed
			elif self.direction == -1:
				self.angle -= self.settings.rotateSpeed
		elif self.angle >= self.settings.rotateAngle:
			self.direction = -1
			self.angle -= self.settings.rotateSpeed
		elif self.angle <= -self.settings.rotateAngle:
			self.direction = 1
			self.angle += self.settings.rotateSpeed
			
		self.newImage = rotate(self.image, self.angle)
		self.clock.tick(60)
		self.newRect = self.newImage.get_rect(center=(self.X, self.center[1]))