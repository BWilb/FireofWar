import pygame
import pyautogui
from ux import button
import sys

pygame.init()


# initialization of pygame screen done outside of class
class OpeningMenu:
    def __init__(self):
        self.HEIGHT = pyautogui.size().height * 0.9
        self.WIDTH = pyautogui.size().width
        # initial width and height will be 90% size of computer screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.flare_background = \
            pygame.transform.scale(pygame.image.load("C:/Users/wilbu/pythonProjects/FireofWar/ux/opening_menu_ux/background.jpg").convert_alpha(),
                                   (self.WIDTH, self.HEIGHT))
        # define fonts
        self.font = pygame.font.SysFont("Arial-Black", 40)
        # define colour
        self.text_col = (0, 0, 0)
        pygame.display.set_caption("Main Menu")
        self.is_running = True
        self.game_paused = False
        """constraint on while loop that will control primary function of class"""
        self.menu_state = "main"
        # menu state controls which piece of the menu you are looking at
        self.time_chosen = ""
        self.nation_chosen = ""
        """region chosen variable will aid in primary while loop function
        time and nation chosen variables will aid in kickstarting game
        """

    def draw_text(self, text, font, text_col, x, y):
        """function of opening menu class draws text"""
        # draws the text on screen
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def update_menu(self):
        """updates screen"""
        pygame.display.update()

    def primary_menu(self):
        """welcoming screen"""
        start_img = pygame.image.load("C:/Users/wilbu/pythonProjects/FireofWar/ux/opening_menu_ux/start_button.jpg").convert_alpha()
        options_img = pygame.image.load("C:/Users/wilbu/pythonProjects/FireofWar/ux/opening_menu_ux/options_butt.jpg").convert_alpha()
        quit_img = pygame.image.load("C:/Users/wilbu/pythonProjects/FireofWar/ux/opening_menu_ux/quit_butt.jpg").convert_alpha()
        start_button = button.Button(self.WIDTH * 0.48, self.HEIGHT * 0.25, start_img, 0.25)
        options_button = button.Button(self.WIDTH * 0.48, self.HEIGHT * 0.5, options_img, 0.25)
        quit_button = button.Button(self.WIDTH * 0.48, self.HEIGHT * 0.75, quit_img, 0.25)
        """Primary images and buttons for main menu of game"""
        self.draw_text("Welcome to Fire and War", self.font, self.text_col,
                       (self.WIDTH * 0.425) - len("Fire and War"), 100)
        if start_button.draw(self.screen):
            self.menu_state = "time"
        elif options_button.draw(self.screen):
            self.menu_state = "options"
        elif quit_button.draw(self.screen):
            pygame.quit()

    def time_menu(self):
        # game directs user to select specific time frame in this part of the menu
        """time button images"""
        img_1950 = pygame.image.load("C:/Users/wilbu/pythonProjects/FireofWar/ux/opening_menu_ux/time_buttons/1950_button.jpg").convert_alpha()
        img_1953 = pygame.image.load("C:/Users/wilbu/pythonProjects/FireofWar/ux/opening_menu_ux/time_buttons/1953_button.jpg").convert_alpha()
        img_1960 = pygame.image.load("C:/Users/wilbu/pythonProjects/FireofWar/ux/opening_menu_ux/time_buttons/1953_button.jpg").convert_alpha()
        img_1963 = pygame.image.load("C:/Users/wilbu/pythonProjects/FireofWar/ux/opening_menu_ux/time_buttons/1953_button.jpg").convert_alpha()
        img_1969 = pygame.image.load("C:/Users/wilbu/pythonProjects/FireofWar/ux/opening_menu_ux/time_buttons/1953_button.jpg").convert_alpha()
        img_1980 = pygame.image.load("C:/Users/wilbu/pythonProjects/FireofWar/ux/opening_menu_ux/time_buttons/1953_button.jpg").convert_alpha()
        img_1989 = pygame.image.load("C:/Users/wilbu/pythonProjects/FireofWar/ux/opening_menu_ux/time_buttons/1953_button.jpg").convert_alpha()
        """time buttons"""
        button_1950 = button.Button(self.WIDTH * 0.20, 300, img_1950, 0.25)
        button_1953 = button.Button(self.WIDTH * 0.20, 500, img_1953, 0.25)
        button_1960 = button.Button(self.WIDTH * 0.20, 700, img_1960, 0.25)
        button_1963 = button.Button(self.WIDTH * 0.65, 300, img_1963, 0.25)
        button_1969 = button.Button(self.WIDTH * 0.65, 500, img_1969, 0.25)
        button_1980 = button.Button(self.WIDTH * 0.65, 700, img_1980, 0.25)
        button_1989 = button.Button(self.WIDTH * 0.65, 700, img_1989, 0.25)
        self.draw_text("Choose your timeframe!", self.font, self.text_col, self.WIDTH * 0.375, 100)
        if button_1910.draw(self.screen):
            self.time_chosen = "1910"
            self.menu_state = "region"
        if button_1914.draw(self.screen):
            self.time_chosen = "1914"
            self.menu_state = "region"
        if button_1918.draw(self.screen):
            self.time_chosen = "1918"
            self.menu_state = "region"
        if button_1932.draw(self.screen):
            self.time_chosen = "1932"
            self.menu_state = "region"
        if button_1936.draw(self.screen):
            self.time_chosen = "1936"
            self.menu_state = "region"
        if button_1939.draw(self.screen):
            self.time_chosen = "1939"
            self.menu_state = "region"
        """if back_button.draw(self.screen):
            self.menu_state = "main"""

    def region_menu(self):
        # function directs user to specific region that they select
        """
        img_asia = pygame.image.load("buttons/region/asia/asia_button.jpg").convert_alpha()
        img_africa = pygame.image.load("buttons/region/africa/africa_button.jpg").convert_alpha()
        img_na = pygame.image.load("buttons/region/n_a/na_button.jpg").convert_alpha()
        img_sa = pygame.image.load("buttons/region/s_a/sa_button.jpg").convert_alpha()
        img_europe = pygame.image.load("buttons/region/europe/europe_button.jpg").convert_alpha()
        """
        """
        europe_button = button.Button(self.WIDTH * 0.20, 250, img_europe, 0.25)
        asia_button = button.Button(self.WIDTH * 0.20, 450, img_asia, 0.25)
        na_button = button.Button(self.WIDTH * 0.65, 250, img_na, 0.25)
        sa_button = button.Button(self.WIDTH * 0.65, 450, img_sa, 0.25)
        africa_button = button.Button(self.WIDTH * 0.425, 650, img_africa, 0.25)
        """
        if

    def main_menu(self):
        """main menu that controls user process of navigating opening menu"""
        #self.background_music()
        self.is_running = True
        while self.is_running:
            if not self.game_paused:
                self.screen.fill((0, 0, 0))
                self.screen.blit(self.flare_background, (0, 0))
                # sets background image
                # self.background_music()
                if self.menu_state == "main":
                    self.primary_menu()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # pushing of space key
                    if event.key == pygame.K_SPACE:
                        if self.game_paused:
                            self.game_paused = False

                        else:
                            self.game_paused = True

                if event.type == pygame.QUIT:
                    self.is_running = False
                    sys.exit()

            self.update_menu()
        pygame.quit()


menu = OpeningMenu()
menu.main_menu()