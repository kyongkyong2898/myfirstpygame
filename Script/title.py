import pygame

import UI
import design

import inputfunction as iff

import var

import start

def manage():
    display()

def display():
    var.screen.fill(design.Color.white)

    var.screen.blit(design.Font.title.render('Dessert Card RPG', True, design.Color.black), UI.title_text)
    
    pygame.draw.rect(var.screen, design.Color.black, UI.Title.new_game_button, 2)
    pygame.draw.rect(var.screen, design.Color.black, UI.Title.load_game_button, 2)

    pygame.display.flip()

def mouse_up_handle():
    mouse = pygame.mouse.get_pos()

    if iff.point_inside_rect(mouse[0], mouse[1], UI.Title.new_game_button[0], UI.Title.new_game_button[1], UI.Title.new_game_button[2], UI.Title.new_game_button[3]):
        start.start_field()
