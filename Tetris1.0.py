from block_class import *
import threading
class handle_:
    def __init__(self):
        user = block()
        state = threading.Thread(target = user.down())
        self.auto_down()
    def new_block(self):
        self.del_block()
        while True:
            if line_check() == 'clear':
                break
        self.user = block()
        self.auto_down()
    def del_block(self):
        del self.user
    def auto_down(self):
        while self.user != None:
            self.state.start()
        self.state.join()
    
    
K_DOWN = 274
K_UP = 273
K_LEFT = 276
K_RIGHT = 275
def main():
    global handle
    pygame.init()
    run = True
    key = None
    handle = handle_()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                key = event.key
        
        if key:
            #if pygame.key.name(key) == 'a':
            #    handle = block()
            #    key = None
            if pygame.key.name(key) == 'space':
                e = handle.space()
                if e == 'new':
                    handle.new_block()
                key = None
            elif key == K_DOWN:
                if handle.down() == 'new':
                    handle.new_block()
                key = None
            elif key == K_UP:
                handle.user.turn()
                key = None
            elif key == K_RIGHT:
                handle.user.right()
                key = None
            elif key == K_LEFT:
                handle.user.left()
                key = None
        
        pygame.display.flip()
    pygame.quit()
main()
