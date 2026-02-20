# Comment this script
class FileService:
    def __init__(self, fileName):
        self.fileName = fileName
        self.data = None
    
    def readFile(self):
        try:
            fileObject = open(self.fileName, "r")
        except FileNotFoundError:
            return None
        data = fileObject.read()
        fileObject.close()
        self.data = data
        return self.data
    
    def writeFile(self, data):
        fileObject = open(self.fileName, "w")
        fileObject.write(data)
        fileObject.close()
    
    def appendFile(self, data):
        fileObject = open(self.fileName, "a")
        fileObject.write(data)
        fileObject.close()
