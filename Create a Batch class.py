class Batch:
    def __init__(self, batch_name, timing):
        self.batch_name = batch_name
        self.timing = timing
    def display(self):
        print("Batch Name:", self.batch_name)
        print("Timing:", self.timing)
batch1 = Batch("Python Evening Batch", "6:00 PM - 8:00 PM")
batch1.display()