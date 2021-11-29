import pygame
import img

import UI
import design

import var
import carddata as cd

def place_animation_handle():
    if var.Animation.place_box == True:
        var.Animation.place_box_tick += 1
        
        if var.Animation.place_box_tick > 0 and var.Animation.place_box_tick <= 1 * var.FPS :
            var.Animation.place_box_rect[1] += 160 / var.FPS

        if var.Animation.place_box_tick > 2 * var.FPS and var.Animation.place_box_tick <= 3 * var.FPS:
            var.Animation.place_box_rect[1] -= 160 / var.FPS

        if var.Animation.place_box_tick == 3 * var.FPS:
            var.Animation.place_box = False
            var.Animation.place_box_tick = 0
            var.Animation.place_box_rect = [40, -120, 240, 80]

def place_display():
    pygame.draw.rect(var.screen, design.Color.white, var.Animation.place_box_rect)
    pygame.draw.rect(var.screen, design.Color.black, var.Animation.place_box_rect, 2)
    var.screen.blit(design.Font.place.render(var.Field.place, True, design.Color.black), [var.Animation.place_box_rect[0] + 2, var.Animation.place_box_rect[1] + 20])

def terrain_display():
    var.screen.blit(img.place[var.Field.place], [0 - var.Camera.x, 0 - var.Camera.y])

def player_display():
    var.screen.blit(img.hero[var.Player_Field.face], [var.Player_Field.position[0] - var.Camera.x, var.Player_Field.position[1] - var.Camera.y])

def enemy_display():
    for i in range(len(var.Field.enemy)):
        var.screen.blit(img.enemy['enemy'], [var.Field.enemy[i][0][0] - var.Camera.x, var.Field.enemy[i][0][1] - var.Camera.y])

def draw_card(card, position):
    var.screen.blit(img.card['card_frame'], position)

    var.screen.blit(design.Font.card_energy.render(str(card['energy']), True, design.Color.black), [position[0] + UI.Card.energy_text[0], position[1] + UI.Card.energy_text[1]])
    var.screen.blit(design.Font.card_name.render(str(card['name']), True, design.Color.black), [position[0] + UI.Card.name_text[0], position[1] + UI.Card.name_text[1]])
    var.screen.blit(design.Font.card_description.render(str(card['description']), True, design.Color.black), [position[0] + UI.Card.description_text[0], position[1] + UI.Card.description_text[1]])
    var.screen.blit(design.Font.card_stat.render(str(card['stat'][0]) + '/' + str(card['stat'][1]), True, design.Color.black), [position[0] + UI.Card.stat_text[0], position[1] + UI.Card.stat_text[1]])

def inventory_display():
    pygame.draw.rect(var.screen, design.Color.white, UI.Field.Inventory.player_info)
    pygame.draw.rect(var.screen, design.Color.black, UI.Field.Inventory.player_info, 2)

    var.screen.blit(img.inventory_tab['skill'], UI.Field.Inventory.skill_tab)
    var.screen.blit(img.inventory_tab['card'], UI.Field.Inventory.card_tab)
    var.screen.blit(img.inventory_tab['deck'], UI.Field.Inventory.deck_tab)
    var.screen.blit(img.inventory_tab['equip'], UI.Field.Inventory.equip_tab)
    var.screen.blit(img.inventory_tab['item'], UI.Field.Inventory.item_tab)

    pygame.draw.rect(var.screen, design.Color.white, UI.Field.Inventory.content)
    pygame.draw.rect(var.screen, design.Color.black, UI.Field.Inventory.content, 2)

    if var.state_inventory == 'card':
        inventory_card_display()

    elif var.state_inventory == 'deck':
        inventory_deck_display()

def inventory_card_display():
    for i in range(8):
        if var.inventory_page * 8 + i < len(var.Player_Info.Inventory.card):
            tmp_ID = var.Player_Info.Inventory.card[var.inventory_page * 8 + i][0]
            tmp_card = {'ID' : var.Player_Info.Inventory.card[var.inventory_page * 8 + i][0],
                        'name' : cd.card[tmp_ID]['name'],
                        'type' : cd.card[tmp_ID]['type'],
                        'element' : cd.card[tmp_ID]['element'],
                        'rarity' : cd.card[tmp_ID]['rarity'],
                        'energy' : cd.card[tmp_ID]['energy'],
                        'stat' : [cd.card[tmp_ID]['stat'][0], cd.card[tmp_ID]['stat'][1]],
                        'effect' : cd.card[tmp_ID]['effect'],
                        'description' : cd.card_description[tmp_ID],
                        'play' : [cd.card[tmp_ID]['play'][0], cd.card[tmp_ID]['play'][1], cd.card[tmp_ID]['play'][2]]}
            draw_card(tmp_card, UI.Field.Inventory.card_list[i][:2])

def inventory_deck_display():
    for i in range(8):
        if i < len(var.Player_Info.deck):
            var.screen.blit(img.card_back[var.Player_Info.deck[i]['back']], UI.Field.Inventory.card_list[i][:2])
            var.screen.blit(design.Font.card_name.render(var.Player_Info.deck[i]['name'], True, design.Color.black), UI.Field.Inventory.deck_text[i])

def battle_start_display():
    pygame.draw.rect(var.screen, design.Color.white, UI.Battle.Start.rect)
    pygame.draw.rect(var.screen, design.Color.black, UI.Battle.Start.rect, 2)

def battle_field_display():
    for i in range(14):
        pygame.draw.rect(var.screen, design.Color.black, UI.Battle.Field.cell_list[i], 2)

def battle_hand_display():
    pass
