from robot.api.deco import keyword
#import subprocess
import PyPDF2 as p2


#ROBOT_AUTO_KEYWORDS = False

# x = pdfRead.getPage(1)
# print(x.extractText())
# print(pdfRead.getIsEncrypted())
# print(pdfRead.getDocumentInfo())
# print(pdfRead.getNumPages())

#print(pdfReader.numPages)
# pageObj = pdfReader.getPage(0)
@keyword
def read_pdf(FilePFD):
    pdfFileObj  = open(FilePFD,"rb")
    pdfReader   = p2.PdfFileReader(pdfFileObj)
    
    #x = pdfRead.getDocumentInfo()
    pageObj = pdfReader.getPage(0)
    texty = pageObj.extractText()
    
    return texty
    # i = 0
    # while i < pdfRead.getNumPages():
    #     pageinfo = pdfRead.getPage(i)
    #     print(pageinfo.extractText())
    #     i = i + 1
    # return  FilePFD 
    
#read_pdf("A Sample PDF.pdf")