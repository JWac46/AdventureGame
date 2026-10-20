import pygame

input_mapping = {
    'up': pygame.K_w,
    'down': pygame.K_s,
    'left': pygame.K_a,
    'right': pygame.K_d
}

class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = list(position)  # Make it mutable [x, y]
        
        # Create a Pygame Rect for positioning, drawing, and future collisions!
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))  # Red color for the player
        self.rect = self.image.get_rect(topleft=position)

    def draw(self, surface, camera):
        """Draws the player adjusted by the camera position"""
        # camera.apply(self.rect) handles rectangles perfectly!
        surface.blit(self.image, camera.apply(self.rect))
         
    def move(self, dx, dy, pressed_keys):
        # Update raw position and sync the rect
        if pressed_keys[input_mapping['up']]:
            self.position[1] -= dy
        if pressed_keys[input_mapping['down']]:
            self.position[1] += dy
        if pressed_keys[input_mapping['left']]:
            self.position[0] -= dx
        if pressed_keys[input_mapping['right']]:
            self.position[0] += dx

        # Keep the rect updated so the camera and collisions know where the player is
        self.rect.topleft = (self.position[0], self.position[1])