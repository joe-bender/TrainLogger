class Logger:
    def __init__(self, filename):
        self.f = open(filename, 'w')
    
    def log(self, loss):
        self.f.write(str(loss) + '\n')

    def close(self):
        self.f.close()
