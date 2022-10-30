
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

def find_collision_rect(rect1, rect2):
    pass