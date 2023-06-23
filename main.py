import os
import random

import pygame

from config import *
from mrp import MRP
from target import Target
from bullet import Bullet
from scoreboard import Scoreboard
from tools import *
from lives import Lives


def main():
	pygame.init()
	settings = Settings()
	stats = Stats(settings)
	screen = pygame.display.set_mode(settings.screenSize)
	screenRect = screen.get_rect()
	pygame.display.set_caption(settings.title)

	mrp = MRP(settings, screen)
	shotBullets = pygame.sprite.Group()

	targets = pygame.sprite.Group()
	
	board = Scoreboard(screen, settings, stats)
	lives = Lives(screen, settings, stats)

	while True:
		check_events(settings, screen, mrp, shotBullets)

		mrp.move()
		mrp.rotate()

		# 检测碰撞
		check_collisions(shotBullets, targets, settings, stats, lives, board)

		# 检测子弹数量是否超过最大值
		for i in shotBullets:
			if i.rect.top > screenRect.height or i.rect.left > screenRect.width or i.rect.right < 0:
				shotBullets.remove(i)
		
		# 布局目标
		if len(targets) < settings.maxExistTargets:
			newTarget = Target(settings, targets, 
				os.path.join("images", "targetTypes", random.choice(settings.targetTypes)), 
				screen, mrp)
			targets.add(newTarget)
		
		# 检测重置超额数量MRP
		targets = clearMRPs(targets, settings)

		# 更新画面
		update_screen(settings.bgColor, screen, mrp, targets, shotBullets, board, lives)

main() 