import pyfiglet as fg

def banner_pagga(texto):
    letra = fg.figlet_format(texto, font="pagga")
    return letra

def banner_future(texto):
    letra = fg.figlet_format(texto, font="future")
    return letra