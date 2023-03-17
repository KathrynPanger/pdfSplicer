import PyPDF2
# This class takes in a dictionary of file names and the pages from each file you would like to splice together.
# List them in the order you would like the final pdf to have them in. This may mean adding the same file
# to the list twice with different pages specified, if you want to splice something in the middle, for example
class splicer():
    def __init__(self, filesToPages:dict[str:list[int]], newFileName):
        self.filesToPages = filesToPages
        self.newFileName = newFileName
    def makePdf(self):
        pdfWriter = PyPDF2.PdfFileWriter()
        for fileName, pageNumbers in self.filesToPages.items():
            pdfFileObj = open(f'{fileName}', 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            for page in pageNumbers:
                pageObj = pdfReader.getPage(page)
                pdfWriter.addPage(pageObj)

        newFile = open(newFileName, 'wb')
        pdfWriter.write(newFileName)
        newFile.close()