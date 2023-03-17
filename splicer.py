import PyPDF2

# This class takes in a dictionary of file names and the pages from each file you would like to splice together.
# List them in the order you would like the final pdf to have them in. This may mean adding the same file
# to the list twice with different pages specified, if you want to splice something in the middle, for example

#NOTE: Use actual page numbers, not page indicies

class Splicer():
    def __init__(self, filesToPages, newFileName):
        self.filesToPages = {}
        for fileName, pageNumbers in filesToPages.items():
            self.filesToPages[fileName] = [item - 1 for item in pageNumbers]
        self.newFileName = newFileName

    def makePdf(self):
        pdfWriter = PyPDF2.PdfWriter()
        for fileName, pageNumbers in self.filesToPages.items():
            pdfFileObj = open(f'{fileName}', 'rb')
            pdfReader = PyPDF2.PdfReader(pdfFileObj)
            for page in pageNumbers:
                pageObj = pdfReader.pages[page]
                pdfWriter.add_page(pageObj)

        newFile = open(self.newFileName, 'wb')
        pdfWriter.write(newFile)
        newFile.close()