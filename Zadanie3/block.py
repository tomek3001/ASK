import numpy as np


class Block:
    def __init__(self, block_id, block_x, block_y, block_type, skin=1):
        self.blocks = []
        self.block_id = block_id
        self.drawable = True
        self.chosen = False
        self.block_type = block_type
        if block_type == 0:
            self.blocks.append((block_x, block_y))
            self.blocks.append((block_x + 1, block_y))
            self.blocks.append((block_x + 2, block_y))
            self.blocks.append((block_x + 1, block_y + 1))
            if skin == 1:
                self.colour = (142, 61, 65)
            elif skin == 2:
                self.colour = (255, 234, 108)
            else:
                self.colour = (255, 0, 0)
        elif block_type == 1:
            self.blocks.append((block_x, block_y))
            self.blocks.append((block_x + 1, block_y))
            self.blocks.append((block_x + 1, block_y + 1))
            self.blocks.append((block_x + 2, block_y + 1))
            if skin == 1:
                self.colour = (150, 107, 45)
            elif skin == 2:
                self.colour = (255, 154, 85)
            else:
                self.colour = (255, 127, 0)
        elif block_type == 2:
            self.blocks.append((block_x, block_y))
            self.blocks.append((block_x + 1, block_y))
            self.blocks.append((block_x + 2, block_y))
            self.blocks.append((block_x + 2, block_y + 1))
            if skin == 1:
                self.colour = (154, 155, 66)
            elif skin == 2:
                self.colour = (84, 255, 251)
            else:
                self.colour = (255, 255, 0)
        elif block_type == 3:
            self.blocks.append((block_x, block_y))
            self.blocks.append((block_x + 1, block_y))
            self.blocks.append((block_x + 2, block_y))
            self.blocks.append((block_x + 3, block_y))
            if skin == 1:
                self.colour = (62, 138, 70)
            elif skin == 2:
                self.colour = (231, 178, 255)
            else:
                self.colour = (0, 255, 0)
        elif block_type == 4:
            self.blocks.append((block_x, block_y+1))
            self.blocks.append((block_x + 1, block_y+1))
            self.blocks.append((block_x + 2, block_y+1))
            self.blocks.append((block_x + 2, block_y))
            if skin == 1:
                self.colour = (53, 105, 134)
            elif skin == 2:
                self.colour = (137, 255, 204)
            else:
                self.colour = (0, 0, 255)
        elif block_type == 5:
            self.blocks.append((block_x, block_y))
            self.blocks.append((block_x + 1, block_y))
            self.blocks.append((block_x + 1, block_y + 1))
            self.blocks.append((block_x, block_y + 1))
            if skin == 1:
                self.colour = (96, 123, 145)
            elif skin == 2:
                self.colour = (140, 255, 31)
            else:
                self.colour = (96, 153, 145)
        elif block_type == 6:
            self.blocks.append((block_x, block_y+1))
            self.blocks.append((block_x + 1, block_y + 1))
            self.blocks.append((block_x + 1, block_y))
            self.blocks.append((block_x + 2, block_y))
            if skin == 1:
                self.colour = (64, 55, 128)
            elif skin == 2:
                self.colour = (0, 198, 204)
            else:
                self.colour = (139, 0, 255)
        else:
            print("Błędny typ klocka.")
            quit()

    def left(self):
        for coord, _ in enumerate(self.blocks):
            (tempx, tempy) = self.blocks[coord]
            self.blocks[coord] = (tempx - 1, tempy)

    def right(self):
        for coord, _ in enumerate(self.blocks):
            (tempx, tempy) = self.blocks[coord]
            self.blocks[coord] = (tempx + 1, tempy)

    def up(self):
        for coord, _ in enumerate(self.blocks):
            (tempx, tempy) = self.blocks[coord]
            self.blocks[coord] = (tempx, tempy - 1)

    def down(self):
        for coord, _ in enumerate(self.blocks):
            (tempx, tempy) = self.blocks[coord]
            self.blocks[coord] = (tempx, tempy + 1)


class SingleBlock():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color