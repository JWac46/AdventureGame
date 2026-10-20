import numpy as np
import pygame as game
import pytmx

from scripts.TileSet import Tileset
from scripts.Player import Player
from scripts.Camera import Camera

TILE_SIZE = 32
ROWS = 14
COLS = 22

SCREEN_WIDTH = COLS * TILE_SIZE
SCREEN_HEIGHT = ROWS * TILE_SIZE

screen = game.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = game.time.Clock()

tiled_map = pytmx.load_pygame("assets/Adventure Game Map.tmx", pixelalpha=True)

#overWorld_tileset = Tileset("assets/TILESET_V1.png", TILE_SIZE, TILE_SIZE)

def create_tilemap():
    tilemap = np.zeros((ROWS, COLS), dtype=int)
    for row in range(ROWS):
        for col in range(COLS):
            if row == 0 or row == ROWS - 1 or col == 0 or col == COLS - 1:
                tilemap[row][col] = 1
            else:
                tilemap[row][col] = 0
    return tilemap

TEXTURE_MAPPING = {
 #   0: overWorld_tileset.get_tile(1, 6),  # Grass
  #  1: overWorld_tileset.get_tile(0, 0),  # Wall
}

# Create entities once before the loop
fixed_tilemap = create_tilemap()
player = Player("Player", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

running = True
while running:
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False

    # 1. Handle Input & Update Player First
    pressed_keys = game.key.get_pressed()      
    player.move(dx=4, dy=4, pressed_keys=pressed_keys) 

    # 2. Update Camera to follow the player
    camera.update(player, SCREEN_WIDTH, SCREEN_HEIGHT)

    # 3. Clear Screen
    screen.fill((0, 0, 123))

    # 4. Draw Tiles (WITH camera offset applied so they scroll!)
    for layer in tiled_map.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile_image = tiled_map.get_tile_image_by_gid(gid)
                if tile_image:
                # Apply your camera offset and blit!
                    screen.blit(tile_image, camera.apply((x * TILE_SIZE, y * TILE_SIZE)))

    # 5. Draw Player (Player class handles its own camera offset)
    player.draw(screen, camera)

    game.display.flip()
    clock.tick(60)

game.quit()