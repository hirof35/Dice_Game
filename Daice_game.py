import sys
import pygame
import random as ran
from pygame.locals import *

pygame.init()
SURFACE = pygame.display.set_mode((600, 600))
FPSCLOCK = pygame.time.Clock()

def Main():
    pos_x, pos_y = 300, 300
    screen = pygame.display.get_surface()

    # サイコロの画像をロード
    dice_images = [
        pygame.image.load(f"さいころ{i}.png").convert_alpha() for i in range(1, 7)
    ]

    # 各サイコロ画像のrect設定
    dice_rects = [img.get_rect(center=(pos_x, pos_y)) for img in dice_images]

    # 初期値
    current_dice = 0  

    while True:
        SURFACE.fill((0, 0, 0))  # 画面クリア

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    current_dice = ran.randint(0, 5)  # 0~5 のランダムな数を取得

        # 選ばれたサイコロの画像を描画
        SURFACE.blit(dice_images[current_dice], dice_rects[current_dice])

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == "__main__":
    Main()
