import pygame
from sprites import *
from config import *
import sys

class Sound:
    pygame.mixer.init()

    channel1 = pygame.mixer.Channel(0)
    channel2 = pygame.mixer.Channel(1)
    background_sound = pygame.mixer.Sound('audio/chode-to-dub-step.wav')
    channel1.play(background_sound, -1)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Mini RPG")
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.character_spritesheet = Spritesheet('img/Isa2.png')
        self.character_spritesheet2 = Spritesheet('img/Pepper2.png')
        self.character_spritesheet3 = Spritesheet('img/Hearth2.png')
        self.terrain = Spritesheet('img/rock.png')
        self.bg = Spritesheet('img/bg.png')


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
        pass

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()