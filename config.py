import os

import pygame


class Settings:

		def __init__(self):
			self.screenSize = (1280, 720)
			self.title = "听话的矿工挖得多"
			self.bgColor = (255, 255, 255)
			self.mrpSpeed = 3 # MRP移动速度, 像素/次
			self.bulletSpeed = 10 #子弹移动速度, 像素/次
			self.maxExistBullets = 25 # 最大子弹数量
			self.maxExistTargets = 20 # 最大目标数量
			
			self.rotateSpeed = 3 # MRP旋转速度, 度/次
			self.rotateAngle = 90 #MRP最大旋转角度（两边）
			
			self.lifenum = 5 # 生命数
			
			self.textColor = (30, 30, 30)
			self.font = pygame.font.SysFont(None, 72)
			
			self.targetTypes = os.listdir(os.path.join("images", "targetTypes"))
			self.nonMRPTargetTypes = [i for i in self.targetTypes if i[-7:-4] != "mrp"]
			self.targetDict = {
				"chromosome": 1,
				"cell": 2
			} # 目标得分字典
			self.mrpImages = os.listdir(os.path.join("images", "mrpImages"))
			
			self.clearMRPsRate = 0.2 # 重置MRP时，MRP在目标中所占数量比

			self.addLife = 10 # 分数每增加一定值，恢复1条命

			self.mrpXMoveInitialSpeed = 1 # MRP在x轴移动初始速度
			self.mrpXMoveSpeed = 1 # MRP在x轴移动速度（这两个同步）
			self.mrpXMoveSpeedIncreaseRate = 0.05 # MRP在X轴移动速度随分数增长率
			self.mrpXMoveInitialDistance = 10 # MRP在x轴移动初始距离（双向）
			self.mrpXMoveDistance = 10# MRP在x轴距离
			self.mrpXMoveDistanceIncreaseRate = 0.5 # MRP在Y轴移动距离随分数增长率
			
			self.mrpYMoveInitialSpeed = 1
			self.mrpYMoveSpeed = 1
			self.mrpYMoveSpeedIncreaseRate = 0.05
			self.mrpYMoveInitialDistance = 10
			self.mrpYMoveDistance = 10
			self.mrpYMoveDistanceIncreaseRate = 0.5
	
class Stats:
	def __init__(self, settings):
		self.score = 0
		self.activeScore = 0 # 分数板上的分数
		self.settings = settings
		self.lives = self.settings.lifenum
	
	def addLives(self, n):
		self.lives += n

	def addScore(self, n):
		self.score += n
	
	def addActiveScore(self, n):
		self.activeScore += n
	
	def resetActiveScore(self):
		self.activeScore = 0