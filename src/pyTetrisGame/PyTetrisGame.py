# -*- coding: utf-8 -*-

import pygame
import threading

#import Constants
from pyTetrisGame.Constants import Constants
from pyTetrisGame.EventManager import EventManager
from Patterns.ObserverPattern import *
from pyTetrisGame.KeyListenerSubject import KeyListenerSubject


class PyTetrisGame(Observer):
    
    def __init__(self):
        
        self.running = True
        self.paused = False
        self.game_over = False
        self.bgColor = (0,0,0)

        #Iniciamos pygame
        pygame.init()
        pygame.display.set_caption( Constants.DEFAULT_SCREEN_TITLE )
        self.screen = pygame.display.set_mode((Constants.DEFAULT_WINDOW_WIDTH, Constants.DEFAULT_WINDOW_HEIGHT))
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(self.bgColor)
        self.draw_grid()
        #This make blitting faster.
        self.background = self.background.convert()

        self.eventManager = EventManager(self)

        self.threadEventManager=threading.Thread(target=self.eventManager.run)
        self.threadGraphicsManager = None
        self.threadSoundManager = None

    def update(self, subject: Subject) -> None:
        print("Hola!!") 
        if isinstance( subject, KeyListenerSubject ):
            keyListenerSubject = subject
            keyListenerSubject.__class__ = KeyListenerSubject
            print("tipo: " + str( keyListenerSubject._action ) + " key: " + str( keyListenerSubject._key) )
            if keyListenerSubject._action == pygame.KEYDOWN:
                pass
            if keyListenerSubject._action == pygame.KEYUP:
                if keyListenerSubject._key == pygame.K_p:
                    self.paused = not self.paused
                    return
                if keyListenerSubject._key == pygame.K_q:
                    self.quit()
                    return
                    

    def run(self):
        self.threadEventManager.start()
        while( self.running ):
            self.screen.blit(self.background, (0,0))
            pygame.display.flip()    


    def quit(self):
        self.running = False
        self.eventManager.stop()

    def draw_grid(self):
        #Dibujamos el grid.
        self.grid_color = ( 50,50,50 )
        #Dibujamos los tiles...
        #vertical lines.
        for i in range(11):
            x = Constants.DEFAULT_TILE_SIZE * i
            pygame.draw.line(self.background, 
                             self.grid_color,
                             (x,0),
                             (x,Constants.DEFAULT_GRID_HEIGHT)
                             )
        #Horizontal lines.
        for i in range(21):
            y = Constants.DEFAULT_TILE_SIZE * i
            pygame.draw.line(self.background, 
                             self.grid_color,
                             (0,y),
                             (Constants.DEFAULT_GRID_WIDTH,y)
                             )