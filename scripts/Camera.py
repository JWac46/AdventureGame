import pygame

class Camera:
    def __init__(self, width, height):
        self.camera_rect = pygame.Rect(0, 0, width, height)

    def apply(self, entity_or_pos):
        """Offsets a position or rect based on camera location"""
        if isinstance(entity_or_pos, pygame.Rect):
            return entity_or_pos.move(-self.camera_rect.x, -self.camera_rect.y)
        return (entity_or_pos[0] - self.camera_rect.x, entity_or_pos[1] - self.camera_rect.y)

    def update(self, target, screen_width, screen_height):
        """Centers the camera on the target (player) safely"""
        # Check if target has a rect, otherwise use position
        if hasattr(target, 'rect'):
            target_x = target.rect.centerx
            target_y = target.rect.centery
        else:
            target_x, target_y = target.position

        x = target_x - int(screen_width / 2)
        y = target_y - int(screen_height / 2)
        
        self.camera_rect.topleft = (x, y)