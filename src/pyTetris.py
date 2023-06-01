#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" python3 -m pip  install pygame
    pyTetris v0.1 by Gabriel Reus
    Versión de Gabriel del Tetris clásico 

"""

#https://recursospython.com/codigos-de-fuente/tetris-pygame/

#import pyTetrisGame.pyTetrisGame
from pyTetrisGame.PyTetrisGame import PyTetrisGame

game = PyTetrisGame()

game.run()