import pygame;
from settings import Settings;
from hero import Hero;
from game_functions import check_events;
from pygame.sprite import Group, groupcollide;
from enemy import Enemy;
from start_button import Start_Button;

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

enemies = Group();
enemies.add(Enemy(screen,game_settings));

start_button = Start_Button(screen);


while 1:
	check_events(hero,start_button,game_settings);

	screen.fill(game_settings.bg_color);
	for hero in hero_group.sprites():
		if game_settings.game_active:
			hero.update_me();
		hero.draw_me();

	for enemy in enemies.sprites():
		if game_settings.game_active:
			enemy.update_me(hero);
		enemy.draw_me();

	hero_died = groupcollide(hero_group, enemies, True, True);
	if hero_died:
		loser_sound = pygame.mixer.Sound('lose.wav');
		loser_sound.play();
		print "GAME OVER";
		game_settings.game_active = False;
		
	if game_settings.game_active == False:
		start_button.draw_button();
	pygame.display.flip();