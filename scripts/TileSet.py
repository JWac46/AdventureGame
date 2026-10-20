import pygame

class Tileset:
    def __init__(self, filename, tile_width, tile_height):
        # Load the tileset image and keep transparency
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.tile_width = tile_width
        self.tile_height = tile_height

    def get_tile(self, col, row):
        """
        Extracts a single tile based on its column and row index 
        (0-indexed: col 0, row 0 is the top-left tile).
        """
        # Calculate pixel coordinates on the sheet
        x = col * self.tile_width
        y = row * self.tile_height

        # Create a blank surface for the tile with transparency support
        image = pygame.Surface((self.tile_width, self.tile_height), pygame.SRCALPHA)
        
        # Blit the specific section of the tileset onto the new surface
        image.blit(self.sheet, (0, 0), (x, y, self.tile_width, self.tile_height))
        
        return image