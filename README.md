# TrainLogger
Log the training of a neural network

This should be used to write important training information to file at regular intervals, such as every batch or every epoch. Because it logs during training, the logged information can be viewed and visualized during training to check on the progress of learning. You don't need to wait until the training has ended to see if the run was a success. 

You can log loss along with other metrics. The log can also include the current epoch, batch, and timestamps. These will be logged to a CSV file, which can then be used in a plot to visualize progress (using matplotlib or seaborn, for example).
