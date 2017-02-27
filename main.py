import pygame;
import time;
from settings import Settings;
from hero import Hero;
from game_functions import check_events, update_screen;
from pygame.sprite import Group, groupcollide;
from enemy import Enemy;
from start_button import Start_Button;
from bullet import Bullet;


pygame.init();
# screen_size = (1000,800);
# bg_color = (82,111,53);
# add a caption and status bar
pygame.display.set_caption('Monster Attack!');

game_settings = Settings();
screen = pygame.display.set_mode(game_settings.screen_size);
hero_group = Group();
hero = Hero(screen);
hero_group.add(hero);
bullets = Group();
# new_bullet = Bullet(screen,hero,game_settings);
# bullets.add(new_bullet);
game_start_time = time.time();

enemies = Group();
enemies.add(Enemy(screen,game_settings));

start_button = Start_Button(screen);


while 1:
	screen.fill(game_settings.bg_color);

	game_settings.timer = (time.time() - game_start_time);
	if int(game_settings.timer) % 5 == 0:
		game_settings.timer = 0;
		game_settings.enemy_count += 1;
		# print game_settings.enemy_count;
	if game_settings.enemy_count == 25:
		game_settings.enemy_count = 0;
		game_settings.timer = 0;
		enemies.add(Enemy(screen,game_settings));
		
	check_events(screen,hero,start_button,game_settings,bullets,enemies);
	update_screen(screen,hero,hero_group,start_button,game_settings,bullets,enemies);
	
	