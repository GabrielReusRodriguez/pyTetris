# -*- coding: utf-8 -*-

import pygame
from  pyTetrisGame.KeyPressListener import KeyPressListener
from  pyTetrisGame.KeyListenerSubject import KeyListenerSubject
from  Patterns.ObserverPattern import Observer

class EventManager:

    def __init__(self,game : Observer):
        self._run = True
        self._game_over = False
        self._paused = False

        self._keyListener = KeyListenerSubject()
        self._keyListener.attach(game)

#        self._keyPressListener = KeyPressListener()


    def stop(self):
        self._run = False


    def run(self):
        while (self._run == True ):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #self._run = False
                    break
                elif event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                    print("KEY UP "+ str ( event.key))
                    self._keyListener.setData(action = pygame.KEYUP, key = event.key )
                    self._keyListener.notify()
#                    if not self._paused and not self._game_over:
#                        if event.key in KeyPressListener.MOVEMENT_KEYS:
#                            pass
#                            #blocks.stop_moving_current_block()
#                        #elif event.key == pygame.K_UP:
#                        #    pass
#                            #blocks.rotate_current_block()
#                    if event.key == pygame.K_p:
#                        print ( "PAUSA: "+ str( self._paused ) )
#                        self._paused = not self._paused
#            
#                    # Stop moving blocks if the game is over or paused.
#                    if self._game_over or self._paused:
#                        continue
#            
#                elif event.type == pygame.KEYDOWN:
#                    print("KEY DOWN "+ str ( event.key ))
#                    
#                    #blocks.start_moving_current_block(event.key)
#                    pass
#            
#           try:
#               if event.type == EVENT_UPDATE_CURRENT_BLOCK:
#                    blocks.update_current_block()
#               elif event.type == EVENT_MOVE_CURRENT_BLOCK:
#                    blocks.move_current_block()
#           except TopReached:
#               game_over = True

