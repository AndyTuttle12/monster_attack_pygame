import pygame;
from pygame.sprite import Sprite;

class Bullet(Sprite):
	def __init__(self,screen,hero,game_settings,direction,bullet_type):
		super(Bullet,self).__init__();
		self.screen = screen;
		if bullet_type == 'vert':
			self.rect = pygame.Rect(0,0,game_settings.bullet_width,game_settings.bullet_height);
		elif bullet_type == 'horiz':
			self.rect = pygame.Rect(0,0,game_settings.bullet_height,game_settings.bullet_width);
		self.rect.centerx = hero.rect.centerx;
		self.rect.centery = hero.rect.centery;
		self.color = game_settings.bullet_color;
		self.speed = game_settings.bullet_speed;
		self.direction = direction;
		self.x = self.rect.x;
		self.y = self.rect.y;

	def draw_bullet(self):
		pygame.draw.rect(self.screen,self.color,self.rect);

	def update(self):
		if self.direction == 'up':
			self.y -= self.speed;
		elif self.direction == 'down':
			self.y += self.speed;
		elif self.direction == 'right':
			self.x += self.speed;
		elif self.direction == 'left':
			self.x -= self.speed;
		self.rect.y = self.y;
		self.rect.x = self.x;



