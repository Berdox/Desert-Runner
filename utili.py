
def redraw(image):
    image.parent_screen.blit(image.loc, (image.x, image.y))
    
def find_collision_window(item, width, height):
    rect = item.loc.get_rect()
    rect.x = item.x
    rect.y = item.y
    print(rect)
    if rect.right >= width or rect.left <= 0:
        return True
    if rect.left >= height or rect.top <= 0:
        return True

collision_tolerance = 10
def find_collision_rect(player, zombies):
    prect = player.loc.get_rect()
    prect.x = player.x
    prect.y = player.y
    zrect = zombies.loc.get_rect()
    zrect.x = zombies.x
    zrect.y = zombies.y
    if prect.colliderect(zrect):
        if abs(prect.top - zrect.bottom) < collision_tolerance:
            return True
        if abs(zrect.bottom - zrect.top) < collision_tolerance:
            return True
        if abs(prect.right - zrect.left) < collision_tolerance:
            return True
        if abs(prect.left - zrect.right) < collision_tolerance:
            return True
        