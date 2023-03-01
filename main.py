import pygame
from utils import load_image, terminate, generate_level, load_level
from startscreen import start_screen

FPS = 50
SIZE = WIDTH, HEIGHT = 600, 400
TILE_WIDTH = TILE_HEIGHT = 50
BACKGROUND_COLOR = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('ЗАСТАВКА')
player = None
clock = pygame.time.Clock()


tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('mario.png')


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, vars):
        super().__init__(vars['tiles_group'], vars['all_sprites'])
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            TILE_WIDTH * pos_x, TILE_HEIGHT * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, vars):
        super().__init__(vars['player_group'], vars['all_sprites'])
        self.image = player_image
        self.rect = self.image.get_rect().move(
            TILE_WIDTH * pos_x + (TILE_WIDTH - self.image.get_width()) // 2,
            TILE_HEIGHT * pos_y + (TILE_HEIGHT - self.image.get_height()) // 2
        )


def main():
    global player, level_x, level_y, all_sprites, tiles_group, player_group

    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    start_screen(screen)
    player, level_x, level_y = generate_level(load_level('map.txt'), globals())
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.rect.x -= TILE_WIDTH
                elif event.key == pygame.K_RIGHT:
                    player.rect.x += TILE_WIDTH
                elif event.key == pygame.K_UP:
                    player.rect.y -= TILE_HEIGHT
                elif event.key == pygame.K_DOWN:
                    player.rect.y += TILE_HEIGHT
        screen.fill(BACKGROUND_COLOR)
        tiles_group.draw(screen)
        player_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    terminate()


if __name__ == '__main__':
    main()
