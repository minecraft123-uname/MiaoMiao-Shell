import os
import random

import pygame
from pygame.sprite import Sprite


class Target(Sprite):

	def __init__(self, settings, targets, image, screen, mrp):
		super().__init__()
		self.settings = settings
		self.tType = image.split(os.sep)[-1][:-4]
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.center = self.rect.center
		self.screen = screen
		self.screenRect = self.screen.get_rect()
		self.mrpRect = mrp.rect
		self.size  = [None, None]
		self.rect.left = random.randint(0, self.screenRect.width - self.rect.width)
		self.rect.top= random.randint(self.mrpRect.bottom + 10, self.screenRect.height - self.rect.height)
		# 若目标为MRP，则随机重置颜色
		if self.tType == "mrp":
			self.changeType(random.choice(self.settings.mrpImages), True)
			self.tType = "mrp"
		
		self.autoMoveAxis = random.choice([0, 1])
		self.autoMoveDirection = random.choice([0, 1])
		self.autoXMovedDistance = 0
		self.autoYMovedDistance = 0

	def render(self):
		self.screen.blit(self.image, self.rect)
	
	def changeType(self, new, isMRP):
		rawcenter = self.rect.center
		if isMRP:
			self.image = pygame.image.load(
				os.path.join("images", "mrpImages", new))
		else:
			self.image = pygame.image.load(
				os.path.join("images","targetTypes", new))
		self.rect = self.image.get_rect(center=rawcenter)
		self.tType = new.split("/")[-1][:-4]
	
	def autoXMove(self):
		'''X轴上自动移动'''
		if -self.settings.mrpXMoveDistance < self.autoXMovedDistance  < self.settings.mrpXMoveDistance:
			if self.autoMoveDirection:
				self.rect.centerx += self.settings.mrpXMoveSpeed
				self.autoXMovedDistance += self.settings.mrpXMoveSpeed
			else:
				self.rect.centerx -= self.settings.mrpXMoveSpeed
				self.autoXMovedDistance -= self.settings.mrpXMoveSpeed
		elif self.autoXMovedDistance >= self.settings.mrpXMoveDistance:
			self.autoMoveDirection = 0
			self.rect.centerx -= self.settings.mrpXMoveSpeed
			self.autoXMovedDistance -= self.settings.mrpXMoveSpeed
		elif self.autoXMovedDistance <= -self.settings.mrpXMoveDistance:
			self.autoMoveDirection = 1
			self.rect.centerx += self.settings.mrpXMoveSpeed
			self.autoXMovedDistance += self.settings.mrpXMoveSpeed
	
	def autoYMove(self):
		'''Y轴上自动移动'''
		if -self.settings.mrpYMoveDistance < self.autoYMovedDistance  < self.settings.mrpYMoveDistance:
			if self.autoMoveDirection:
				self.rect.centery += self.settings.mrpYMoveSpeed
				self.autoYMovedDistance += self.settings.mrpYMoveSpeed
			else:
				self.rect.centery -= self.settings.mrpYMoveSpeed
				self.autoYMovedDistance -= self.settings.mrpYMoveSpeed
		elif self.autoYMovedDistance >= self.settings.mrpYMoveDistance:
			self.autoMoveDirection = 0
			self.rect.centery -= self.settings.mrpYMoveSpeed
			self.autoYMovedDistance -= self.settings.mrpYMoveSpeed
		elif self.autoYMovedDistance <= -self.settings.mrpYMoveDistance:
			self.autoMoveDirection = 1
			self.rect.centery += self.settings.mrpXMoveSpeed
			self.autoYMovedDistance += self.settings.mrpYMoveSpeed
