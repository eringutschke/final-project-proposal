import pygame
from sprites import *
from config import *
import sys

#class Sound:
#    pygame.mixer.init()

#    channel1 = pygame.mixer.Channel(0)
#    channel2 = pygame.mixer.Channel(1)
#    background_sound = pygame.mixer.Sound('audio/chode-to-dub-step.wav')
#    channel1.play(background_sound, -1)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Mini RPG")
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font('Font/MONO.ttf', 32)

        self.Isa = Spritesheet('img/Isa2.png')
        self.Pepper = Spritesheet('img/Pepper2.png')
        self.terrain = Spritesheet('img/rock.png')
        self.bg = Spritesheet('img/bg.png')
        self.intro = pygame.image.load('./img/intro.png')
        self.map = pygame.image.load('img/map.png')


    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    Player(self, j, i)

    def new(self):
        # a new game starts
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()

        self.createTilemap()

    def events(self):
        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        # game loop updates
        self.all_sprites.update()
        
    def draw(self):
        # game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        # game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):
        intro = True

        title = self.font.render('MINI RPG', True, WHITE)
        title_rect = title.get_rect(x=10, y=10)

        play_button = Button(10, 80, 100, 100, WHITE, BLACK, 'Play', 32)


        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False

            self.screen.blit(self.intro, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
  
            self.clock.tick(FPS)
            pygame.display.update()

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()