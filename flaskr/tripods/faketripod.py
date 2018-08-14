class Faketripod(object):

    def __init__(self):
        self.horizontal = 0
        self.vertical = 0
        self.step_size = 5

    def left(self):
        if (-80 < self.horizontal):
            self.horizontal = self.horizontal - self.step_size
        print('mock: moving left ' + str(self.horizontal))

    def right(self):
        if (self.horizontal < 80):
            self.horizontal = self.horizontal + self.step_size
        print('mock: moving right ' + str(self.horizontal))

    def up(self):
        if (-80 < self.vertical):
            self.vertical = self.vertical - self.step_size
        print('mock: moving up ' + str(self.vertical))

    def down(self):
        if (self.vertical < 80):
            self.vertical = self.vertical + self.step_size
        print('mock: moving down ' + str(self.vertical))
