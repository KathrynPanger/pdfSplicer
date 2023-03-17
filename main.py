from splicer import Splicer
zipDict = {"pdfs/bluebonnet_agreement.pdf": [1,2,3,4], "pdfs/lastPage.pdf": [1]}
splicer = Splicer(zipDict, "signed_agreement.pdf")
splicer.makePdf()
