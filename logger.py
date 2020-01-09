class Logger:
    def __init__(self, filename):
        self.f = open(filename, 'w')
    
    def log(self, epoch, batch, train_loss, val_loss, train_metric, val_metric):
        self.f.write("{},{},{},{},{},{}\n".format(epoch, batch, train_loss, val_loss, train_metric, val_metric))

    def close(self):
        self.f.close()
