import pygame,sys
pygame.init()
window=pygame.display.set_mode((1000,600))
#цвета
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
bleck=(0,0,0)
#чистота обновления экрана
FPS=30
clok=pygame.time.Clock()
#основной цикл в котором будут прописыватся события и все действия 
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    clok.tick(FPS)
    pygame.display.update()
    window.fill(red)
    # ниже все действия которые не нужно постоянно проверять
