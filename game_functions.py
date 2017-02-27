import pygame;
import sys;
import os;
from hero import Hero;
from pygame.sprite import Group, groupcollide;
from enemy import Enemy;
from bullet import Bullet;


def check_events(screen, hero,start_button,game_settings,bullets,enemies):
	for event in pygame.event.get():
		# user clicked on red X
		if event.type == pygame.QUIT:
			sys.exit();
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos();
			if start_button.rect.collidepoint(mouse_x,mouse_y):
				game_settings.game_active = True;
				bg_music = pygame.mixer.Sound('boom.wav');
				os.system("say START!");
				bg_music.play();
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				hero.moving_right = True;
			elif event.key == pygame.K_LEFT:
				hero.moving_left = True;
			elif event.key == pygame.K_UP:
				hero.moving_up = True;
			elif event.key == pygame.K_DOWN:
				hero.moving_down = True;
			elif event.key == pygame.K_w:
				new_bullet = Bullet(screen,hero,game_settings, "up", "vert");
				bullets.add(new_bullet);
				hero.image = pygame.image.load('john-wick_up.png');
				hero.image = pygame.transform.scale(hero.image,(128,128));
			elif event.key == pygame.K_s:
				new_bullet = Bullet(screen,hero,game_settings, "down", "vert");
				bullets.add(new_bullet);
				hero.image = pygame.image.load('john-wick_down.png');
				hero.image = pygame.transform.scale(hero.image,(128,128));
			elif event.key == pygame.K_d:
				new_bullet = Bullet(screen,hero,game_settings, "right", "horiz");
				bullets.add(new_bullet);
				hero.image = pygame.image.load('john-wick_right.png');
				hero.image = pygame.transform.scale(hero.image,(128,128));
			elif event.key == pygame.K_a:
				new_bullet = Bullet(screen,hero,game_settings, "left", "horiz");
				bullets.add(new_bullet);
				hero.image = pygame.image.load('john-wick_left.png');
				hero.image = pygame.transform.scale(hero.image,(128,128));
			# print event.key;
		elif event.type == pygame.KEYUP:
			hero.image = pygame.image.load('john-wick_down.png');
			hero.image = pygame.transform.scale(hero.image,(128,128));
			if event.key == pygame.K_RIGHT:
				hero.moving_right = False;
			elif event.key == pygame.K_LEFT:
				hero.moving_left = False;
			elif event.key == pygame.K_UP:
				hero.moving_up = False;
			elif event.key == pygame.K_DOWN:
				hero.moving_down = False;

def update_screen(screen,hero,hero_group,start_button,game_settings,bullets,enemies):
	hero.draw_me();
	for bullet in bullets.sprites():
		bullet.update();
		bullet.draw_bullet();
	

	for enemy in enemies.sprites():
		if game_settings.game_active:
			enemy.update_me(hero);
		enemy.draw_me();

	for hero in hero_group.sprites():
		if game_settings.game_active:
			hero.update_me();

	enemy_died = groupcollide(bullets, enemies, True, True);
	if enemy_died:
		print "HIT";

	hero_died = groupcollide(hero_group, enemies, True, True);
	if hero_died:
		loser_sound = pygame.mixer.Sound('lose.wav');
		loser_sound.play();
		print "GAME OVER";
		game_settings.game_active = False;
		
	if game_settings.game_active == False:
		start_button.draw_button();

	pygame.display.flip();