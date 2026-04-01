import pygame
import sys
import os
import webbrowser
import random

# Handle PyInstaller bundled resources
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.is_animating = False
        self.sprites = []
        # Load and scale button frames
        for i in range(1, 7):
            img_path = os.path.join(base_path, f"graphics/button {i}.png")
            img = pygame.image.load(img_path)
            self.sprites.append(pygame.transform.scale(img, (x, y)))
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()

    def animate(self):
        self.is_animating = True

    def update(self, speed):
        # Update position to keep centered (updated each frame)
        self.rect.center = (pygame.display.get_surface().get_size()[0] // 2,
                            pygame.display.get_surface().get_size()[1] // 2)

        if self.is_animating:
            self.current_sprite += speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]

    def draw_clicks(self, clicks, screen):
        font = pygame.font.SysFont("jetbrains mono", 50)
        txt_surface = font.render(f"Clicks: {clicks}", True, (255, 255, 255))
        txt_rect = txt_surface.get_rect(topleft=(10, 10))
        screen.blit(txt_surface, txt_rect)

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Screen setup
screen_width = 900
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Bored Button")

weird_websites = [
    "https://theuselessweb.com",
    "https://eelslap.com",
    "https://zombo.com",
    "https://staggeringbeauty.com",
    "https://pointerpointer.com",
    "https://findtheinvisiblecow.com",
    "https://koalastothemax.com",
    "https://www.700horses.com",
    "https://www.burymewithmymoney.com",
    "https://www.screamintothevoid.com",
    "https://www.noooooooooooooo.com",
    "https://www.papertoilet.com",
    "https://www.he-man-4nonblondes.com",
    "https://www.endless.horse",
    "https://www.isitchristmas.com",
    "https://www.tane.us",
    "https://www.rainymood.com",
    "https://www.patience-is-a-virtue.org",
    "https://www.procatinator.com",
    "https://www.cornify.com",
    "https://boredbutton.com",
    "https://neal.fun",
    "https://neave.com",
    "https://wikiroulette.co",
    "https://mapcrunch.com",
    "https://thesecretdoor.com",
    "https://alwaysjudgeabookbyitscover.com",
    "https://web.archive.org",
    "https://heeeeeeeey.com",
    "https://cat-bounce.com",
    "https://longdogechallenge.com",
    "https://corndog.io",
    "https://make-everything-ok.com",
    "https://isitfridayyet.net",
    "https://zoomquilt.org",
    "https://zoomquilt2.com",
    "https://fallingfalling.com",
    "https://thisissand.com",
    "https://weavesilk.com",
    "https://patatap.com",
    "https://theinternetmap.net",
    "https://thewildernessdowntown.com",
    "https://coolbackgrounds.io",
    "https://autodraw.com",
    "https://csszengarden.com",
    "https://pudding.cool",
    "https://informationisbeautiful.net",
    "https://thetruesize.com",
    "https://scaleofuniverse.com",
    "https://everytimezone.com",
    "https://nullisland.com",
    "https://nyan.cat",
    "https://asoftmurmur.com",
    "https://incredibox.com",
    "https://radio.garden",
    "https://thezen.zone",
    "https://pixelthoughts.co",
    "https://window-swap.com",
    "https://thenicestplace.net",
    "https://music-map.com",
    "https://gnoosic.com",
    "https://hackertyper.com",
    "https://thewikigame.com",
    "https://littlealchemy2.com",
    "https://geoguessr.com",
    "https://playingcards.io",
    "https://akinator.com"
]   

# Set window icon
icon_path = os.path.join(base_path, "graphics/icon.png")
icon = pygame.image.load(icon_path)
pygame.display.set_icon(icon)  # Use set_icon(), not set_caption()

# Load sounds
click_sound = pygame.mixer.Sound(os.path.join(base_path, "sounds/click.mp3"))
pygame.mixer.music.load(os.path.join(base_path, "sounds/backround.mp3"))
pygame.mixer.music.play(-1)

# Create sprite group and button
moving_sprites = pygame.sprite.Group()
button = Button(400, 400)
moving_sprites.add(button)

clicks = 0
clock = pygame.time.Clock()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and button.rect.collidepoint(pygame.mouse.get_pos()):
                button.animate()
                webbrowser.open_new_tab(weird_websites[random.randint(0, len(weird_websites) - 1)])   
                click_sound.play()
                clicks += 1

    screen.fill((10, 10, 10))
    button.draw_clicks(clicks, screen)
    moving_sprites.draw(screen)
    moving_sprites.update(0.5)
    pygame.display.flip()
    clock.tick(60)   
