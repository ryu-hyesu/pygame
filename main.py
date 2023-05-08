import pygame, sys
from settings import *
from level import Level

class Game :
    def __init__(self) -> None:
        pygame.init()
        # creating a display surface & clock
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Sprout land")
        self.clock = pygame.time.Clock()
        self.level = Level()
    
    # most of game is going to run inside of the run method
    # check game loop
    def run(self): 
        while True:
            # close game
            for event in pygame.event.get() :
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() # 게임 종료
                
                # get delta time  
                dt = self.clock.tick(60) / 1000
                self.level.run(dt)
                # update game
                pygame.display.update()

if __name__ == '__main__' :
    game = Game()
    game.run()