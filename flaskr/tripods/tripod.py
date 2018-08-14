import pantilthat

class Tripod(object):

    def __init__(self):
        self.horizontal = 0
        self.vertical = 0
        self.step_size = 5
        pantilthat.pan(0)
        pantilthat.tilt(0)

    def left(self):
        if (-80 < self.horizontal):
            self.horizontal = self.horizontal - self.step_size
        print('moving left ' + str(self.horizontal))
        pantilthat.pan(self.horizontal)

    def right(self):
        if (self.horizontal < 80):
            self.horizontal = self.horizontal + self.step_size
        print('moving right ' + str(self.horizontal))
        pantilthat.pan(self.horizontal)

    def up(self):
        if (-80 < self.vertical):
            self.vertical = self.vertical - self.step_size
        print('moving up ' + str(self.vertical))
        pantilthat.tilt(self.vertical)

    def down(self):
        if (self.vertical < 80):
            self.vertical = self.vertical + self.step_size
        print('moving down ' + str(self.vertical))
        pantilthat.tilt(self.vertical)