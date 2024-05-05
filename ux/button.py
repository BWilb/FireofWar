import pygame

class Button():
    def __init__(self, x, y, image, scale):
        width = int(image.get_width())
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

class AnimatedButton:
    def __init__(self, screen, font, text, width, height, pos):
        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = "#475F77"
        # core attributes
        self.pressed = False

        self.text_surf = font.render(text, True, "#FFFFFF")
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
        self.nation = text
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.top_color, self.top_rect, border_radius=12)
        self.screen.blit(self.text_surf, self.text_rect)
        self.check_if_clicked()

    def check_if_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        if left_click and self.top_rect.collidepoint(mouse_pos):
            self.pressed = True
            if self.pressed:
                self.pressed = False
        else:
            print(self.pressed)
            if self.pressed:
                self.pressed = False
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
                if not pygame.mouse.get_pressed()[0]:
                    if self.pressed:
                        print("HI")
                        self.pressed = False