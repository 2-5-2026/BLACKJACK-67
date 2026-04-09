import random
import tkinter as tk
import pygame

karte = {'2H': 2, '2T': 2, '2P': 2, '2K': 2,
    '3H': 3, '3T': 3, '3P': 3, '3K': 3,
    '4H': 4, '4T': 4, '4P': 4, '4K': 4,
    '5H': 5, '5T': 5, '5P': 5, '5K': 5,
    '6H': 6, '6T': 6, '6P': 6, '6K': 6,
    '7H': 7, '7T': 7, '7P': 7, '7K': 7,
    '8H': 8, '8T': 8, '8P': 8, '8K': 8,
    '9H': 9, '9T': 9, '9P': 9, '9K': 9,
    'JH': 10, 'JT': 10, 'JP': 10, 'JK': 10,
    'QH': 10, 'QT': 10, 'QP': 10, 'QK': 10,
    'KH': 10, 'KT': 10, 'KP': 10, 'KK': 10,
    'AH': 11, 'AT': 11, 'AP': 11, 'AK': 11}

vrijednosti = []
zb = 0
bra = 0
ruke = []

zbk = 0
brak = 0
ruke_diler = []

novac = 100
ulog = 0
