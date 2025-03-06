import pygame
import numpy as np

class Lever:
    def __init__(self):
        self.state = True

    def flip(self):
        self.state = not self.state


class Door:
    def __init__(self, pos, state):
        self.pos = pos
        self.state = state

    def open(self):
        self.state = True

    def close(self):
        self.state = False

    def is_open(self):
        return self.state


class MovableObject:
    def __init__(self, pos, size, color, speed, left_limit, right_limit):
        self.pos = pos
        self.size = size
        self.color = color
        self.speed = speed
        self.left_limit = left_limit
        self.right_limit = right_limit
        self.direction = 1

    def move(self):
        # Move a plataforma na direção atual
        self.pos.x += self.speed * self.direction

        # Verifica se a plataforma atingiu um dos limites
        if self.pos.x <= self.left_limit:  # Se atingiu o limite esquerdo
            self.pos.x = self.left_limit   # Corrige a posição
            self.direction = 1             # Inverte a direção (move para a direita)
        elif self.pos.x >= self.right_limit:  # Se atingiu o limite direito
            self.pos.x = self.right_limit     # Corrige a posição
            self.direction = -1              # Inverte a direção (move para a esquerda)
