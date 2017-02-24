import pygame;
from pygame.sprite import Sprite;

class Hero(Sprite):
	def __init__(self, screen):
		super(Hero,self).__init__();
		self.image = pygame.image.load('hero.png');
		self.rect = self.image.get_rect();
		self.screen = screen;
		self.screen_rect = screen.get_rect();
		self.rect.centery = self.screen_rect.centery;
		self.rect.left = self.screen_rect.left;
		self.moving_right = False;
		self.moving_left = False;
		self.moving_up = False;
		self.moving_down = False;
		# self.speed = settings.hero_speed;
	def update_me(self):
		if self.moving_right:
			if self.rect.right <= self.screen_rect.right:
				self.rect.centerx += 10;
		elif self.moving_left:
			if self.rect.left >= self.screen_rect.left:
				self.rect.centerx -= 10;

		if self.moving_down:
			if self.rect.bottom <= self.screen_rect.bottom:
				self.rect.centery += 10;
		elif self.moving_up:
			if self.rect.top >= self.screen_rect.top:
				self.rect.centery -= 10;
	def draw_me(self):
		self.screen.blit(source = self.image, dest = self.rect);

