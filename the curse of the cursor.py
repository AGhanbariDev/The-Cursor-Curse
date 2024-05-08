import pygame, sys, os, random, time

os.chdir("C:\\Users\\aydip\\Desktop\\Programming\\Python\\The Cursor's Curse\\assets")

# IMAGES
class Background(pygame.sprite.Sprite):
    def __init__(self,back_pos_x,back_pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load("background1.png"))
        self.sprites.append(pygame.image.load("background2.png"))
        self.sprites.append(pygame.image.load("background3.png"))
        self.sprites.append(pygame.image.load("background4.png"))
        self.sprites.append(pygame.image.load("background5.png"))
        self.sprites.append(pygame.image.load("background6.png"))
        self.sprites.append(pygame.image.load("background7.png"))
        self.sprites.append(pygame.image.load("background8.png"))  
        self.sprites.append(pygame.image.load("background9.png"))
        self.sprites.append(pygame.image.load("background10.png"))
        self.sprites.append(pygame.image.load("background11.png"))
        self.sprites.append(pygame.image.load("background12.png"))
        self.sprites.append(pygame.image.load("background13.png"))
        self.sprites.append(pygame.image.load("background14.png"))
        self.sprites.append(pygame.image.load("background15.png"))
        self.sprites.append(pygame.image.load("background16.png"))
        self.sprites.append(pygame.image.load("background17.png"))
        self.sprites.append(pygame.image.load("background18.png"))
        self.sprites.append(pygame.image.load("background19.png"))
        self.sprites.append(pygame.image.load("background20.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [back_pos_x,back_pos_y]

    def update(self):
        self.current_sprite += 0.1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]
        


class Button:
    def __init__(self,text,width,height,pos,elevation):
        # core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        
        # top rectangle
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_colour = '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(width,elevation))
        self.bottom_colour = '#354B5E'

        # text
        self.text_surf = gui_font.render(text,False,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

# START
    def draw_start(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen,self.bottom_colour,self.bottom_rect,border_radius=100)
        pygame.draw.rect(screen,self.top_colour,self.top_rect,border_radius=100)
        screen.blit(self.text_surf,self.text_rect)
        self.check_click_start()


    def check_click_start(self):
        
        mouse_pos = pygame.mouse.get_pos()

        if self.top_rect.collidepoint(mouse_pos):
            self.top_colour = "#D74B4B"

            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True

            else:
                if self.pressed == True:
                    game_start()
                    self.pressed = False

        else:
            self.dynamic_elevation = self.elevation
            self.top_colour = '#475F77'

# EXIT
    def draw_exit(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen,self.bottom_colour,self.bottom_rect,border_radius=100)
        pygame.draw.rect(screen,self.top_colour,self.top_rect,border_radius=100)
        screen.blit(self.text_surf,self.text_rect)
        self.check_click_exit()


    def check_click_exit(self):
         
        mouse_pos = pygame.mouse.get_pos()

        if self.top_rect.collidepoint(mouse_pos):
            self.top_colour = "#D74B4B"

            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True

            else:
                if self.pressed == True:
                    pygame.quit()
                    sys.exit()
        

        else:
            self.dynamic_elevation = self.elevation
            self.top_colour = '#475F77'

# OPTIONS
    def draw_options(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen,self.bottom_colour,self.bottom_rect,border_radius=100)
        pygame.draw.rect(screen,self.top_colour,self.top_rect,border_radius=100)
        screen.blit(self.text_surf,self.text_rect)
        self.check_click_options()


    def check_click_options(self):
         
        mouse_pos = pygame.mouse.get_pos()

        if self.top_rect.collidepoint(mouse_pos):
            self.top_colour = "#D74B4B"

            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True

            else:
                if self.pressed == True:
                    options_menu()
                    self.pressed = False
        
        else:
            self.dynamic_elevation = self.elevation
            self.top_colour = '#475F77'

# CREDITS
    def draw_credits(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen,self.bottom_colour,self.bottom_rect,border_radius=100)
        pygame.draw.rect(screen,self.top_colour,self.top_rect,border_radius=100)
        screen.blit(self.text_surf,self.text_rect)
        self.check_click_credits()


    def check_click_credits(self):
         
        mouse_pos = pygame.mouse.get_pos()

        if self.top_rect.collidepoint(mouse_pos):
            self.top_colour = "#D74B4B"

            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True

            else:
                if self.pressed == True:
                    credits_menu()
                    self.pressed = False
        
        else:
            self.dynamic_elevation = self.elevation
            self.top_colour = '#475F77'

# STATS
    def draw_stats(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen,self.bottom_colour,self.bottom_rect,border_radius=100)
        pygame.draw.rect(screen,self.top_colour,self.top_rect,border_radius=100)
        screen.blit(self.text_surf,self.text_rect)
        self.check_click_stats()


    def check_click_stats(self):
         
        mouse_pos = pygame.mouse.get_pos()

        if self.top_rect.collidepoint(mouse_pos):
            self.top_colour = "#D74B4B"

            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True

            else:
                if self.pressed == True:
                    stats_menu()
                    self.pressed = False
        
        else:
            self.dynamic_elevation = self.elevation
            self.top_colour = '#475F77'


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load("cursor ring 1.png"))
        self.sprites.append(pygame.image.load("cursor ring 2.png"))
        self.sprites.append(pygame.image.load("cursor ring 3.png"))
        self.sprites.append(pygame.image.load("cursor ring 4.png"))
        self.sprites.append(pygame.image.load("cursor ring 5.png"))
        self.sprites.append(pygame.image.load("cursor ring 6.png"))
        self.sprites.append(pygame.image.load("cursor ring 7.png"))
        self.sprites.append(pygame.image.load("cursor ring 8.png"))
        self.sprites.append(pygame.image.load("cursor ring 9.png"))
        self.sprites.append(pygame.image.load("cursor ring 10.png"))
        self.sprites.append(pygame.image.load("cursor ring 11.png"))
        self.sprites.append(pygame.image.load("cursor ring 12.png"))
        self.sprites.append(pygame.image.load("cursor ring 13.png"))
        self.sprites.append(pygame.image.load("cursor ring 14.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        
        self.health = 5
        self.health_bar = 300
        
        


    def update(self):

        self.current_sprite += 0.2

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

        pos_list = list(pygame.mouse.get_pos())

        player_pos_x = pos_list[0]
        player_pos_y = pos_list[1]

        self.rect.center = (player_pos_x,player_pos_y)
        
        self.mask = pygame.mask.from_surface(self.image)

        
        # RED
        pygame.draw.rect(screen,(255,0,0),((1280/2 - 150, 720 - 25 - 15),(300,25)))
        # GREEN
        pygame.draw.rect(screen,(0,255,0),((1280/2 - 150, 720 - 25 - 15),(self.health_bar,25)))

        if pygame.sprite.spritecollide(self,bullet_group,True,pygame.sprite.collide_mask):
            self.health -= 1
            self.health_bar -= 60

            if self.health <= 0:
                # MAKE A GAME OVER SCREEN THAT WILL RETURN TO MAIN MENU AFTER A CERTAIN PERIOD OF TIME AND INCLUDE AUDIO 
                main_menu()


    def create_bullet(self):
        return Bullet(random.randint(1,1280), -100)



class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.image.load("projectile.png")
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
        

    def update(self):
        self.rect.y += 10

        if self.rect.y >= 720-30:
            self.kill()
        

bullet_group = pygame.sprite.Group()

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("The Cursor's Curse")
screen = pygame.display.set_mode((1280,720), pygame.FULLSCREEN)
gui_font = pygame.font.Font(None,50)

butt_size_x = 215
butt_size_y = 75



def main_menu():
    # MUSIC PLAYER
    pygame.mixer.init()
    pygame.mixer.music.load("music.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.02)
    # pygame.mixer.music.stop()

    start_game_button = Button('Play', butt_size_x , butt_size_y,((1280 / 2) - (butt_size_x / 2), (720 - 575) - (butt_size_y / 2)), 16)
    exit_game_button = Button('Exit', butt_size_x , butt_size_y,((1280 / 2) - (butt_size_x / 2), (720 - 175) - (butt_size_y / 2)), 16)
    options_game_button = Button('Options', butt_size_x , butt_size_y,((1280 / 2) - (butt_size_x / 2), (720 - 475) - (butt_size_y / 2)), 16)
    stats_game_button = Button('Statistics', butt_size_x , butt_size_y,((1280 / 2) - (butt_size_x / 2), (720 - 375) - (butt_size_y / 2)), 16)
    credits_game_button = Button('Credits', butt_size_x , butt_size_y,((1280 / 2) - (butt_size_x / 2), (720 - 275) - (butt_size_y / 2)), 16)
    
    pygame.mouse.set_visible(True)
    moving_sprites = pygame.sprite.Group()
    mainmenu_back = Background(0,0)
    moving_sprites.add(mainmenu_back)

    while True:   
        
        moving_sprites.draw(screen)
        moving_sprites.update()

        start_game_button.draw_start()
        exit_game_button.draw_exit()
        options_game_button.draw_options()
        stats_game_button.draw_stats()
        credits_game_button.draw_credits()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        mainClock.tick(60)



def game_start():
    running = True

    # Timer Start
    time_start = time.time()
    seconds = 0
    level = 1
    rand_nums= 50
    score = 0

    # MAKE A WORKING CLOCK AND ADD IT AT THE TOP MIDDLE OF THE SCREEN

    # Player init
    player = Player()
    player_group = pygame.sprite.Group()
    player_group.add(player)

    pygame.mouse.set_visible(False)

    pygame.mixer.music.stop()

    bullet_sound = pygame.mixer.Sound("lazer sound effect.wav")
    bullet_sound.set_volume(0.02)

    while running:
        screen.fill((0,0,50))

        player_group.draw(screen)
        player_group.update()


        bullet_group.draw(screen)
        bullet_group.update()

        seconds = int(time.time() - time_start)

        shoot_proj = random.randint(1,rand_nums)
        
        # Projectile was shot
        if shoot_proj == 1:
            bullet_group.add(player.create_bullet())
            bullet_sound.play()
            score += 1
        
        if seconds == 10:
            rand_nums = 40
            level = 1

        elif seconds == 20:
            rand_nums = 30
            level = 2

        elif seconds == 30:
            rand_nums = 20
            level = 3

        elif seconds == 40:
            rand_nums = 10
            level = 4

        elif seconds == 60:
            rand_nums = 2
            level = 5

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    pygame.mixer.music.play(-1)
                    pygame.mouse.set_visible(True)
                    time.time()

        level_text_str = f"Level: {level}"
        level_text = gui_font.render(level_text_str,False,'#FFFFFF')
        screen.blit(level_text,(10,10))

        score_text_str = f"Score: {score}"
        score_text = gui_font.render(score_text_str,False,'#FFFFFF')
        screen.blit(score_text,(1280 - score_text.get_width() - 10,10))

        pygame.display.update()
        mainClock.tick(60)



def options_menu():
    running = True
    
    while running:
        screen.fill((0,0,250))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)



def credits_menu():
    running = True
    
    while running:
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)



def stats_menu():
    running = True
    
    while running:
        screen.fill((250,0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()