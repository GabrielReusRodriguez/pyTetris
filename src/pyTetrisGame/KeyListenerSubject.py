# -*- coding: utf-8 -*-

import pygame
from typing import List

from Patterns.ObserverPattern import *


class KeyListenerSubject(Subject):
    
    #Constantes
    MOVEMENT_KEYS =  ( pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP )
    GAME_KEYS =  ( pygame.K_p )

    #Variables staticas
    _state: int = None
    _observers: List[Observer] = []

    def __init__(self):
        self._action = None
        self._key = None

    def setData(self,action: int,key: int):
        self._action = action
        self._key = key

    def clearData(self):
        self._action = None
        self._key = None

    def attach(self, observer: Observer ) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer ) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)
        self.clearData()