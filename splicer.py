
# This class takes in a dictionary of file names and the pages from each file you would like to splice together
class splicer():
    def __init__(self, filesToPages:dict[str:list[int]]):
        self.filesToPages = filesToPages
