"""import pygame, sys

class Button:
    def __init__(self, text, width, height, pos):
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = "#475F77"

        self.text_surf = gui_font.render(text, True, "#FFFFFF")
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        pygame.draw.rect(screen, self.top_color, self.top_rect)
        screen.blit(self.text_surf, self.text_rect)

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("GUI MENU")
gui_font = pygame.font.Font(None, 30)
x = 40
for i in range(0, 19):
    button1 = Button("Hello", 200, x, (200, 250))
    x += 20

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("#DCDDD8")
    #button1.draw()

    pygame.display.update()"""