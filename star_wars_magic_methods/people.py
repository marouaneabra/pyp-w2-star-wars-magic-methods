class People(object):
    def __init__(self, name, dark_side=False,light_side=True):
        self.name=name
        self.dark_side=dark_side
        self.light_side=light_side
        
    def __str__(self):
        return self.name
        
    def obiwan(self):
        returnStr=("Help me "+self.name+", you're my only hope.")
        return returnStr
