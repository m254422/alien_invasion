import pygame
import time
from settings2 import Settings

pygame.init()
ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption("Alien Invasion")

image = pygame.image.load('images/ship.bmp')
rect = image.get_rect()
screen_rect = screen.get_rect()

rect.centery = screen_rect.centery
rect.bottom = screen_rect.centery

screen.fill(ai_settings.bg_color)
screen.blit(image,rect)

pygame.display.flip()
time.sleep(2)
