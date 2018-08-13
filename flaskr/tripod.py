
class Tripod(object):

    def __init__(self):
        self.horizontal = 0
        self.vertical = 0
        self.step_size = 5

    def left(self):
        if (-85 < self.horizontal):
            self.horizontal = self.horizontal - self.step_size
        print('moving left ' + str(self.horizontal))

    def right(self):
        if (self.horizontal < 85):
            self.horizontal = self.horizontal + self.step_size
        print('moving right ' + str(self.horizontal))

    def up(self):
        if (-85 < self.vertical):
            self.vertical = self.vertical - self.step_size
        print('moving up ' + str(self.vertical))

    def down(self):
        if (self.vertical < 85):
            self.vertical = self.vertical + self.step_size
        print('moving down ' + str(self.vertical))