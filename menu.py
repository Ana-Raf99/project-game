import pygame
import pygame_menu
import sys

def set_difficulty(value, difficulty):
    global difficulty_level
    difficulty_level = difficulty
    print(f"Сложность изменена на: {value}")

def start_the_game():
    print("Игра запущена со сложностью:", difficulty_level)

CYBERPUNK_THEME = pygame_menu.Theme(
    background_color=(5, 5, 15),
    title_background_color=(255, 20, 147),
    title_font_color=(0, 255, 255),
    widget_font_color=(0, 255, 180),

    selection_color=(255, 0, 255),    # неоновая подсветка строки

    widget_selection_effect=pygame_menu.widgets.SimpleSelection(),

    widget_background_color=(20, 0, 30),
    title_font_size=55,
    widget_font_size=32,
    cursor_color=(0, 255, 255),
    cursor_switch_ms=400,

    widget_padding=15,
    widget_border_color=(0, 255, 255),
    widget_border_width=2
)

def run():
    
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Крестики нолики")
    icon = pygame.image.load("C:/Users/anast/Desktop/project game/image/pixil-frame-0.png")
    pygame.display.set_icon(icon)
    bg_color = (255, 255, 255)
    menu = pygame_menu.Menu(
        'Welcome', 400, 300,
        theme=CYBERPUNK_THEME
)

    menu.add.text_input('Name :', default='John Doe')
    menu.add.selector('Difficulty :', [("Hard", 1), ("Medium", 2), ("Easy", 3)], onchange=set_difficulty)
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        pygame.display.flip()

run()
