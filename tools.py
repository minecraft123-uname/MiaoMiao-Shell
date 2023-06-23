import sys
import os
from random import choice

import pygame

from bullet import Bullet
from math import sin, cos, pi


def angleToRad(angle):
	return pi * angle / 180

def check_events(settings, screen, mrp, shotBullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				mrp.move_right = True
			elif event.key == pygame.K_LEFT:
				mrp.move_left = True
			elif event.key == pygame.K_SPACE:
				if len(shotBullets) < settings.maxExistBullets:
					newBullet = Bullet(settings, screen, shotBullets, mrp, 
						settings.bulletSpeed * cos(angleToRad(mrp.angle - 90)), 
						settings.bulletSpeed * sin(angleToRad(mrp.angle - 90)))
					shotBullets.add(newBullet)

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				mrp.move_right = False
			elif event.key == pygame.K_LEFT:
				mrp.move_left = False

def update_screen(bgcolor, screen, mrp, targets, shotBullets, board, lives):
	screen.fill(bgcolor)
	mrp.render()
	for i in targets:
		# 检测MRP种类并移动
		if i.tType == "mrp":
			if i.autoMoveAxis:
				i.autoXMove()
			else:
				i.autoYMove()
		i.render()
	for i in shotBullets:
		i.shoot()
		i.render()
	board.render()
	lives.render()
	pygame.display.flip()
	
def check_collisions(shotBullets, targets, settings, stats, lives, board):
	'''检测碰撞'''
	collisions = pygame.sprite.groupcollide(shotBullets, targets, True, True)
	if collisions:
		mrps = 0
		for i in collisions.values():
			for j in i:
				if j.tType == "mrp":
					mrps += 1
		if mrps == 0:
			for i in collisions.values():
				for j in i:
					before = stats.activeScore // settings.addLife
					stats.addScore(settings.targetDict[j.tType])
					stats.addActiveScore(settings.targetDict[j.tType])
					board.updateScore()
					after = stats.activeScore // settings.addLife
					if after > before and stats.lives < settings.lifenum:
						lives.addLives(1)
			# 更改MRP移动距离、速度
			settings.mrpXMoveSpeed = settings.mrpXMoveInitialSpeed + int(
				settings.mrpXMoveSpeedIncreaseRate * stats.score)
			settings.mrpYMoveSpeed = settings.mrpYMoveInitialSpeed + int(
				settings.mrpYMoveSpeedIncreaseRate * stats.score)
			settings.mrpXMoveDistance = settings.mrpXMoveInitialDistance + int(
				settings.mrpXMoveDistanceIncreaseRate * stats.score)
			settings.mrpYMoveDistance = settings.mrpYMoveInitialDistance + int(
				settings.mrpYMoveDistanceIncreaseRate * stats.score)
		else:
			# 重置Scoreboad分数
			stats.resetActiveScore()
			lives.addLives(-mrps)
			board.updateScore()

def clearMRPs(targets, settings):
	'''
	当MRP在总目标数中占比达到一定值时，
	随机将所有MRP中的一半替换为其他非MRP目标
	'''
	targets_ = targets.copy()
	mrps = []
	nonmrps = []
	for i in targets_:
		if i.tType == "mrp":
			mrps.append(i)
		else:
			nonmrps.append(i)
	toBeReplaceds = []
	if len(mrps) / settings.maxExistTargets >= settings.clearMRPsRate:
		for i in range(int(len(mrps) / 2)):
			cur = choice(mrps)
			toBeReplaceds.append(cur)
			mrps.remove(cur)
	for i in toBeReplaceds:
		i.changeType(choice(settings.nonMRPTargetTypes), False)
	new = pygame.sprite.Group(list(nonmrps) + list(mrps) + list(toBeReplaceds))
	return new

def endGame():
	print("\n\nFUCK YOU THE BITCH! MRP DIED!")
	print("\n\nFUCK YOU THE BITCH! MRP DIED!")
	print("\n\nFUCK YOU THE BITCH! MRP DIED!\n\n")
	os._exit(0)