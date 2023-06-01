# -*- coding: utf-8 -*-

from __future__ import annotations
from abc import ABC, abstractmethod


class Event:
    
    @abstractmethod    
    def __init__(self):
        self._tipo = None

