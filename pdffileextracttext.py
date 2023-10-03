#Extract Text from PDF with Python [0B5N6Xt5K8Q]
#from PyPDF2 import PdfFileReader #DeprecationError: PdfFileReader is deprecated and was removed in PyPDF2 3.0.0. Use PdfReader instead.  DeprecationError: PdfFileWriter is deprecated and was removed in PyPDF2 3.0.0. Use PdfWriter instead.  RM:  Moreover, the syntax changed.  Syntax errors and corrections returned when running the code and following the video.
from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path
import re
pdffileobject = PdfReader("lorem.pdf")
#Information for each page
importpdffilepageone = pdffileobject.pages[0] #Page one is zero index.  Use indexing zero.
print(importpdffilepageone) #print {'/Type': '/Page', '/Parent': IndirectObject(2, 0, 140471337321664), '/Resources': {'/Font': {'/F1': IndirectObject(5, 0, 140471337321664)}, '/ExtGState': {'/GS7': IndirectObject(7, 0, 140471337321664), '/GS8': IndirectObject(8, 0, 140471337321664)}, '/ProcSet': ['/PDF', '/Text', '/ImageB', '/ImageC', '/ImageI']}, '/MediaBox': [0, 0, 612, 792], '/Contents': IndirectObject(4, 0, 140471337321664), '/Group': {'/Type': '/Group', '/S': '/Transparency', '/CS': '/DeviceRGB'}, '/Tabs': '/S', '/StructParents': 0}.  '/StructParents': 0 is the page number index 0 page 1 the object pdffileobject represents.
extracttext = importpdffilepageone.extract_text()
print(extracttext) #print Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Morbi tristique senectus et netus et malesuada fames ac turpis. Elementum . . . .  RM:  extracttext the page 1 pdf file as text.
#For loop extract text in pdf file
for eachpage in pdffileobject.pages:
    print(eachpage.extract_text())
    '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
    dolore magna aliqua. Morbi tristique senectus et netus et malesuada fames ac turpis. Elementum . . .
    '''
#Write pdf file to a text file
with Path("lorempdftotext.txt").open(mode="w") as outputfileobject:
    outputtext = ""
    for eachpage in pdffileobject.pages:
        outputtext += eachpage.extract_text()
    outputfileobject.write(outputtext)
#Get pages which has Waldo in the page
findwaldopagelist = []
for eachpage in pdffileobject.pages:
    waldopagenumberindex = eachpage["/StructParents"]
    waldopagenumberindextext = eachpage.extract_text()
    if "Waldo" in waldopagenumberindextext:
        findwaldopagelist.append(waldopagenumberindex)
print(findwaldopagelist) #page [2, 7, 10, 12, 15, 17, 20, 25, 26]
pdffilewriterobject = PdfWriter()
for eachpage in findwaldopagelist:
    pdffilewriterobject.add_page(pdffileobject.pages[eachpage])
with Path("loremwaldo.pdf").open(mode="wb") as outputfileobject2:  #wb stands for write binary
    pdffilewriterobject.write(outputfileobject2)
#Extract sentences with Waldo.  Use regular expressions.
waldosentenceslist = []
for eachpage in pdffileobject.pages:
    waldopagenumberindex = eachpage["/StructParents"]
    waldopagenumberindextext = eachpage.extract_text()
    if "Waldo" in waldopagenumberindextext:
        sentencewithwaldo = ["Page number " + str(waldopagenumberindex) + ":  " + sentence.replace("\n", "") for sentence in re.split("\. |\? |\!", waldopagenumberindextext) if "Waldo" in sentence] #re.split splits each sentence in waldopagenumberindextext either period, question mark, or exclamation mark.  Replace \n with nothing.
        print(sentencewithwaldo)
        '''
        ['Page number 2:  Amet porttitor Waldo eget dolor morbi non arcu risus']
        ['Page number 7:  Risus nec feugiat in Waldo fermentum posuere urna nec tincidunt praesent']
        ['Page number 10:  Quisque sagittis purus sit Waldo amet volutpat consequat mauris']
        ...
        '''
        sentencewithwaldostring = ["Page number " + str(waldopagenumberindex) + ":  " + sentence.replace("\n", "") for sentence in re.split("\. |\? |\!", waldopagenumberindextext) if "Waldo" in sentence][0]
        print(sentencewithwaldostring)  #RM:  Quick way convert list to string which is extract the first and only item in list.
        '''
        Page number 2:  Amet porttitor Waldo eget dolor morbi non arcu risus
        Page number 7:  Risus nec feugiat in Waldo fermentum posuere urna nec tincidunt praesent
        Page number 10:  Quisque sagittis purus sit Waldo amet volutpat consequat mauris
        ...
        '''
        waldosentenceslist.append(sentencewithwaldostring)
print(waldosentenceslist) #print ['Page number 2:  Amet porttitor Waldo eget dolor morbi non arcu risus', 'Page number 7:  Risus nec feugiat in Waldo fermentum posuere urna nec tincidunt praesent', 'Page number 10:  Quisque sagittis purus sit Waldo amet volutpat consequat mauris', . . .]
waldosentenceslistastext = "\n".join(waldosentenceslist)
print(waldosentenceslistastext)
'''
Page number 2:  Amet porttitor Waldo eget dolor morbi non arcu risus
Page number 7:  Risus nec feugiat in Waldo fermentum posuere urna nec tincidunt praesent
Page number 10:  Quisque sagittis purus sit Waldo amet volutpat consequat mauris
...
'''
with Path("waldosentences.txt").open(mode="w") as outputfileobject3:
    outputfileobject3.write(waldosentenceslistastext)

#Extract Text from any PDF File in Python 3.10 Tutorial [RULkvM7AdzY]
import PyPDF2 #PyPDF2.errors.DeprecationError: PdfFileReader is deprecated and was removed in PyPDF2 3.0.0. Use PdfReader instead.  DeprecationError: PdfFileWriter is deprecated and was removed in PyPDF2 3.0.0. Use PdfWriter instead.  RM:  Moreover, the syntax changed.  Syntax errors and corrections returned when running the code and following the video.
import re
def extracttextfrompdf(pdffile: str) -> [str]:  #Receive a pdf file type string.  Return a string array.
    with open(pdffile, "rb") as readfileasbytes:
        reader = PyPDF2.PdfReader(readfileasbytes, strict=False)
        extractpdftextlist = []
        for eachpage in reader.pages:
            contentextracttext = eachpage.extract_text()
            extractpdftextlist.append(contentextracttext)
        return extractpdftextlist


pdftext = extracttextfrompdf("lorem.pdf")
for eachpdftext in pdftext:
    #print(eachpdftext) #print Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Morbi tristique senectus et netus et malesuada fames ac turpis. Elementum pulvinar etiam non quam lacus suspendisse. Vel pretium lectus quam id. Gravida rutrum quisque non tellus. Risus viverra adipiscing at in tellus integer. Porta lorem mollis aliquam ut porttitor. Nam at lectus . . . .
    pass
counter = 0
for eachpdftext in pdftext:
    wordsonlynopunctuationlist = re.split(r"\s+|[,;?!.-]\s*", eachpdftext.lower())
    #print(wordsonlynopunctuation) #print ['lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'sed', 'do', 'eiusmod', 'tempor', 'incididunt', 'ut', 'labore', 'et', 'dolore', 'magna', 'aliqua', 'morbi', 'tristique', 'senectus', 'et', 'netus', 'et', 'malesuada', 'fames', 'ac', 'turpis', 'elementum', 'pulvinar', 'etiam', 'non', 'quam', 'lacus', 'suspendisse', 'vel', 'pretium', 'lectus', 'quam', 'id', 'gravida', 'rutrum', 'quisque', 'non', 'tellus', 'risus', 'viverra', 'adipiscing', 'at', 'in', 'tellus', 'integer', 'porta', 'lorem', 'mollis', 'aliquam', 'ut', 'porttitor', 'nam', 'at', 'lectus', 'urna', 'duis', 'massa', 'ultricies', 'mi', 'quis', 'hendrerit', 'dolor', 'magna', 'eget', 'est', 'erat', 'nam', 'at', 'lectus', 'urna', 'duis', 'convallis', 'convallis', 'tellus', 'at', 'tellus', 'at', 'urna', 'condimentum', 'mattis', 'pellentesque', 'id', 'malesuada', 'bibendum', 'arcu', 'vitae', 'elementum', 'curabitur', 'vitae', 'nunc', 'sed', 'bibendum', 'est', 'ultricies', 'integer', 'quis', 'auctor', 'sed', 'viverra', 'ipsum', 'nunc', 'aliquet', 'bibendum', 'enim', 'facilisis', 'gravida', 'eu', 'turpis', 'egestas', 'pretium', 'aenean', 'pharetra', 'magna', 'ac', 'placerat' . . ., '']'
    if "lorem" in wordsonlynopunctuationlist:
        counter += 1
print("Word found:", counter) #print Word found: 27

#Extract PDF Content with Python [w2r2Bg42UPY]
# import pdfminer
# print(pdfminer.__version__) #print 20221105
from pdfminer.high_level import extract_pages, extract_text
import re

pdffilename = "neuralninesamplepdf.pdf"
for pagelayout in extract_pages(pdffilename):
    for eachelement in pagelayout:
        print(eachelement)
        '''
        <LTTextBoxHorizontal(0) 36.000,742.755,162.539,753.735 'NeuralNine Sample PDF File \n'>
        <LTTextBoxHorizontal(1) 36.000,713.775,264.607,724.755 'This is an ordinary PDF File with some informa(cid:415)on. \n'>
        <LTTextBoxHorizontal(2) 36.000,684.796,264.406,695.776 'Here are ﬁve names:  Mike, Sara, Bob, John, Emma \n'>
        <LTTextBoxHorizontal(3) 36.000,655.816,273.083,666.796 'Here are six numbers:  100, 200, 4310, 233, 544, 122 \n'>
        <LTTextBoxHorizontal(4) 36.000,626.837,155.558,637.817 'Here is a table full of data: \n'>
        <LTTextBoxHorizontal(5) 41.640,527.715,74.287,608.357 'Name \nMike \nOlivia \nBob \nSophia \nSimon \n'>
        <LTTextBoxHorizontal(6) 221.415,527.715,240.884,608.357 'Age \n28 \n38 \n68 \n24 \n25 \n'>
        <LTTextBoxHorizontal(7) 401.217,527.715,459.951,608.357 'Job \nProgrammer \nAccountant \nAccountant \nLawyer \nProgrammer \n'>
        <LTRect 36.000,610.620,36.480,611.100>
        ...
        <LTRect 575.520,527.040,576.000,527.520>
        <LTFigure(Im1) 35.760,342.240,351.600,512.640 matrix=[315.84,0.00,0.00,170.40, (35.76,342.24)]>
        <LTFigure(Im2) 35.760,171.840,351.600,342.240 matrix=[315.84,0.00,0.00,170.40, (35.76,171.84)]>
        <LTTextLineHorizontal 36.000,728.235,38.477,739.215 ' \n'>
        <LTTextLineHorizontal 36.000,699.256,38.477,710.236 ' \n'>
        <LTTextLineHorizontal 36.000,670.276,38.477,681.256 ' \n'>
        <LTTextLineHorizontal 36.000,641.297,38.477,652.277 ' \n'>
        <LTTextLineHorizontal 36.000,612.317,38.477,623.297 ' \n'>
        <LTTextLineHorizontal 36.000,513.795,38.477,524.775 ' \n'>
        <LTTextLineHorizontal 351.300,169.215,353.777,180.195 ' \n'>
        '''
textfrompdffile = extract_text(pdffilename)
print(textfrompdffile)
'''
NeuralNine Sample PDF File 

This is an ordinary PDF File with some informa(cid:415)on. 

Here are ﬁve names:  Mike, Sara, Bob, John, Emma 

Here are six numbers:  100, 200, 4310, 233, 544, 122 

Here is a table full of data: 

Name 
Mike 
Olivia 
Bob 
Sophia 
Simon 

Age 
28 
38 
68 
24 
25 

Job 
Programmer 
Accountant 
Accountant 
Lawyer 
Programmer 
...
'''
textfrompdffile = extract_text(pdffilename)
patterntoextracttext = re.compile(r"[a-zA-Z]+,{1}\s{1}") #Begins with lower case character or upper case character as many as possible, next a comma immediately one space, next a space immediately one space
matchespatterntext = patterntoextracttext.findall(textfrompdffile)
print(matchespatterntext) #print ['Mike, ', 'Sara, ', 'Bob, ', 'John, ']
listcomprehensionslicelist = [names[:-2] for names in matchespatterntext]
print(listcomprehensionslicelist) #print ['Mike', 'Sara', 'Bob', 'John']
import fitz #from PyMuPDF module
import PIL.Image #from pillow module
import io
pdffilewithimages = fitz.open(pdffilename)
counterimagefilename = 1
for pdffilepagenumber in range(len(pdffilewithimages)):
    pdfpage = pdffilewithimages[pdffilepagenumber]
    images = pdfpage.get_images()
    for eachimages in images:
        baseimage = pdffilewithimages.extract_image(eachimages[0])
        print(baseimage) #print {'ext': 'jpeg', 'smask': 0, 'width': 658, 'height': 355, 'colorspace': 3, 'bpc': 8, 'xres': 96, 'yres': 96, 'cs-name': 'DeviceRGB', 'image': b'\xff\xd8\xff\xee\x00\x0eAdobe\x00d\x80\x00\x00\x00\x01\xff\xdb\x00\x84\x00\x0c\x08\x08\x08\t\x08\x0c\t\t\x0c\x11\x0b\n\x0b\x11\x15\x0f\x0c\x0c\x0f\x15\x18\x13\x13\x15\x13\x13\x18\x17\x12\x14\x14\x14\x14\x12\x17\x17\x1b\x1c\x1e\x1c\x1b\x17$$\'\'$$53335;;;;;;;;;;\x01\r\x0b\x0b\r\x0e\r\x10\x0e\x0e\x10\x14\x0e\x0f\x0e\x14\x14\x10\x11\x11\x10\x14\x1d\x14\x14\x15\x14\x14\x1d%\x1a\x17\x17\x17\x17\x1a% #\x1e\x1e\x1e# ((%%((22022;;;;;;;;;;\xff\xc0\ . . . \x00\x00\x00\x00IEND\xaeB`\x82'}
        imageitselfisbytes = baseimage["image"]
        saveactualimage = PIL.Image.open(io.BytesIO(imageitselfisbytes))
        imageextension = baseimage["ext"] #RM:  It's the ext in the baseimage dictionary
        saveactualimage.save(open(f"imagename{counterimagefilename}.{imageextension}", "wb")) #image saved as imagename1.jpeg.  RM:  extracted part of the pic.  Not the entire pic.  Scroll up the baseimage there is another extension png.  Interesting.  There are two images saved imagename1.jpeg and imagename2.png.  imagename2.png is the other part of the pic.
        counterimagefilename += 1
import tabula #frpm tabula-py
pdffilewithtables = tabula.read_pdf(pdffilename, pages="all") #pages=*page number* for specific page number
print(pdffilewithtables)
'''
Sep 19, 2023 11:26:49 PM org.apache.pdfbox.pdmodel.font.PDType0Font toUnicode
WARNING: No Unicode mapping for CID+415 (415) in font IHGHHN+Calibri
[     Name  Age         Job
0    Mike   28  Programmer
1  Olivia   38  Accountant
2     Bob   68  Accountant
3  Sophia   24      Lawyer
4   Simon   25  Programmer]
'''
print(type(pdffilewithtables)) #print <class 'list'>
print(pdffilewithtables[0]) #RM:  instructor says can save as a panda's data frame.
'''
     Name  Age         Job
0    Mike   28  Programmer
1  Olivia   38  Accountant
2     Bob   68  Accountant
3  Sophia   24      Lawyer
4   Simon   25  Programmer
'''
print(type(pdffilewithtables[0])) #print <class 'pandas.core.frame.DataFrame'>
print(pdffilewithtables[0][pdffilewithtables[0].Age > 30])
'''
     Name  Age         Job
1  Olivia   38  Accountant
2     Bob   68  Accountant
'''

#PyPDF2 Crash Course - Working with PDFs in Python [2023] [OdIHUdQ1-eQ]
import PyPDF2 as pdf
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
# print(pdf.__version__) #print 3.0.1.  RM:  YouTuber using 3.0.1.
# print(dir(pdf)) #print ['DocumentInformation', 'PageObject', 'PageRange', 'PaperSize', 'PasswordType', 'PdfFileMerger', 'PdfFileReader', 'PdfFileWriter', 'PdfMerger', 'PdfReader', 'PdfWriter', 'Transformation', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '__warningregistry__', '_cmap', '_codecs', '_encryption', '_merger', '_page', '_protocols', '_reader', '_security', '_utils', '_version', '_writer', 'constants', 'errors', 'filters', 'generic', 'pagerange', 'papersizes', 'parse_filename_page_ranges', 'types', 'warnings', 'xmp'].  These are the methods.
#Summary:  PyPDF2 opens the pdf file.  Working with the pdf file PdfReader reads the pdf file, PdfWriter writes the pdf file split file extract file, and PdfMerger merges the pdf file join file.
fileopenpdf = open("NativityExample.pdf", "rb")
readerreadpdf = PdfReader(fileopenpdf)
infopdffile = readerreadpdf.metadata
print(infopdffile) #print {'/Title': 'Nativity_Example', '/Producer': 'Skia/PDF m110 Google Docs Renderer'}
print(infopdffile.title) #print 'Nativity_Example.  RM:  the title is different than the file name NativityExample.pdf.
print(readerreadpdf.pages) #print <PyPDF2._page._VirtualList object at 0x7fde65f10ac0>
print(len(readerreadpdf.pages)) #print 3.  Number of pages.
extractfirstpage = readerreadpdf.pages[0].extract_text()
print(extractfirstpage) #print The nativity of Jesus, nativity of Christ, birth of Jesus or birth of Christ is described in the biblical gospels of Luke and Matthew . The two accounts agree that Jesus was born in Bethlehem in . . .
def extracttextfrompdf(pdffile):
    with open(pdffile, "rb") as fobject:
        readerreadpdf = PdfReader(pdffile)
        resultslist = []
        for i in range(0, len(readerreadpdf.pages)):
            selectedpageextracttext = readerreadpdf.pages[i].extract_text()
            print(selectedpageextracttext)
            resultslist.append(selectedpageextracttext)
        return " ".join(resultslist) #convert list to a single document


extracttextfrompdf("NativityExample.pdf") #return The nativity of Jesus, nativity of Christ, birth of Jesus or birth of Christ is described in the biblical gospels of Luke and Matthew . The two accounts agree that Jesus was born in Bethlehem in . . .
#Split pdf file into separate pages.
import os
def splitpdffile(pdffile):
    with open(pdffile, "rb") as fobject:
        readerreadpdf = PdfReader(pdffile)
        #Exact each page
        for pagenumber in range(0, len(readerreadpdf.pages)):
            selectedpageextracttext = readerreadpdf.pages[pagenumber]
            writerwritepdf = PdfWriter()
            writerwritepdf.add_page(selectedpageextracttext)
            filename = os.path.splitext(pdffile)[0]
            outputfilename = f"{filename}{pagenumber+1}.pdf"
            #Save the extract to compile to a new pdf file
            with open(outputfilename, "wb") as outputobject:
                writerwritepdf.write(outputobject)
            print("Created a pdf file:{}".format(outputfilename))


splitpdffile("NativityExample.pdf") #return Created a pdf file:NativityExample0.pdf\n Created a pdf file:NativityExample1.pdf\n Created a pdf file:NativityExample2.pdf
#Extract page range
def extractselectedpages(pdffile, startpage: int, endpage: int):
    with open(pdffile, "rb") as fobject:
        readerreadpdf = PdfReader(pdffile)
        writerwritepdf = PdfWriter()
        for pagenumber in range(startpage - 1, endpage):
            selectedpageextracttext = readerreadpdf.pages[pagenumber]
            writerwritepdf.add_page(selectedpageextracttext)
            filename = os.path.splitext(pdffile)[0]
            outputfilename = f"{filename}page{startpage}to{endpage}.pdf"
        with open(outputfilename, "wb") as outputobject:
            writerwritepdf.write(outputobject)
        print("Extracted {} file to {}".format(pdffile, outputfilename))


extractselectedpages("NativityExample.pdf", 1, 2) #return Extracted NativityExample.pdf file to NativityExamplepage1to2.pdf
#Extract last page or extract a page
def extractonepage(pdffile, pagenumber):
    with open(pdffile, "rb") as fobject:
        readerreadpdf = PdfReader(pdffile)
        writerwritepdf = PdfWriter()
        selectedpageextracttext = readerreadpdf.pages[pagenumber - 1]
        writerwritepdf.add_page(selectedpageextracttext)
        filename = os.path.splitext(pdffile)[0]
        outputfilename = f"{filename}page{pagenumber}.pdf"
        with open(outputfilename, "wb") as outputobject:
            writerwritepdf.write(outputobject)
        print("Extracted {} file page {}".format(outputfilename, pagenumber))


extractlastpage = len(readerreadpdf.pages)
extractonepage("NativityExample.pdf", extractlastpage) #return Extracted NativityExamplepage3.pdf file page 3
extractanyonepage = 2
extractonepage("NativityExample.pdf", extractanyonepage) #return Extracted NativityExamplepage2.pdf file page 2
#Merge pdf from a folder of pdf files
def fetchpdffilesinfolder(folderpath):
    targetpdffiles = []
    for path, subdirectory, filenames in os.walk(folderpath): #Need subdirectory in for loop to prevent ValueError: too many values to unpack (expected 2)
        for eachfilenames in filenames:
            if eachfilenames.endswith(".pdf"):
                targetpdffiles.append(os.path.join(path, eachfilenames))
    return targetpdffiles


print(fetchpdffilesinfolder("/home/mar/python")) #print ['/home/mar/python/NativityExamplepage3.pdf', '/home/mar/python/NativityExamplepage1to2.pdf', '/home/mar/python/fixsteamuserratingcharts.pdf', '/home/mar/python/NativityExample0.pdf', '/home/mar/python/NativityExample.pdf', '/home/mar/python/NativityExamplepage0to2.pdf', '/home/mar/python/loremwaldo.pdf', '/home/mar/python/NativityExample3.pdf', '/home/mar/python/neuralninesamplepdf.pdf', '/home/mar/python/56_power_query_tutorials.pdf', '/home/mar/python/NativityExample2.pdf', '/home/mar/python/NativityExample1.pdf', '/home/mar/python/NativityExamplepage2.pdf', '/home/mar/python/lorem.pdf']
def mergepdffilesfromlist(pdffileslist, outputpdffilename="default.pdf"):
    merger = PdfMerger()
    with open(outputpdffilename, "wb") as fobject:
        for eachpdffileslist in pdffileslist:
            merger.append(eachpdffileslist)
        merger.write(fobject)


#Merge pdf from a list of pdf files in a folder
pdflistfromfolder = fetchpdffilesinfolder("/home/mar/python")
mergepdffilesfromlist(pdflistfromfolder)
def mergepdffilesfromlistfiledirectory(filedirectory, pdffileslist, outputpdffilename="default.pdf"):
    merger = PdfMerger()
    with open(outputpdffilename, "wb") as fobject:
        for eachpdffileslist in pdffileslist:
            print(filedirectory + eachpdffileslist)
            merger.append(eachpdffileslist)
        merger.write(fobject)


filedirectory = "/home/mar/python"
pdflist = ["loremwaldo.pdf", "NativityExample.pdf"]
mergepdffilesfromlistfiledirectory(filedirectory, pdflist)
#Rotate pdf rotate page.  Rotation angle must be a multiple of 90.
def rotatepdffile(pdffile, pagenumber: int, rotation: int=90):
    pagenumber -= pagenumber
    with open(pdffile, "rb") as fobject:
        reader = PdfReader(fobject)
        writer = PdfWriter()
        writer.add_page(reader.pages[pagenumber])
        writer.pages[pagenumber].rotate(rotation)
        filename = os.path.splitext(pdffile)[0]
        outputfilename = f"{filename}rotated{rotation}degrees.pdf"
        with open(outputfilename, "wb") as outputobject:
            writer.write(outputobject)
        print("Rotated {} file to {}".format(pdffile, outputfilename))


rotatepdffile("loremwaldo.pdf", 1)

#Extract text, links, images, tables from Pdf with Python ｜ PyMuPDF, PyPdf, PdfPlumber tutorial [G0PApj7YPBo]
from pypdf import PdfReader
readpdffileobject = PdfReader("neuralninesamplepdf.pdf")
numberofpages = len(readpdffileobject.pages)
print(numberofpages) #print 1
pageonepdffile = readpdffileobject.pages[0] #page 1 is index 0
print(pageonepdffile.extract_text())
'''
NeuralNine Sample PDF File 
 
This is an ordinary PDF File with some informaƟon. 
 
Here are ﬁve names:  Mike, Sara, Bob, John, Emma 
 
Here are six numbe rs:  100, 200, 4310, 233, 544, 122 
 
Here is a table full of data: 
 
Name Age Job 
Mike 28 Programmer 
Olivia 38 Accountant 
Bob 68 Accountant 
Sophia 24 Lawyer 
Simon 25 Programmer 
'''
#For loop to extract text for all pages in pdf file
for eachpage in range(0, numberofpages):
    pdffilepagenumber = readpdffileobject.pages[eachpage]
    print(pdffilepagenumber.extract_text())
#For loop to extract images for all pages in pdf file
for eachimage in pageonepdffile.images:
    with open(eachimage.name, "wb") as fobject:
        fobject.write(eachimage.data) #return Im1.jpg and Im2.png
#Extract tables
import pdfplumber
with pdfplumber.open("neuralninesamplepdf.pdf") as fobject:
    for eachtable in fobject.pages:
        print(eachtable.extract_tables()) #print [[['Name', 'Age', 'Job'], ['Mike', '28', 'Programmer'], ['Olivia', '38', 'Accountant'], ['Bob', '68', 'Accountant'], ['Sophia', '24', 'Lawyer'], ['Simon', '25', 'Programmer']]]
#Convert pdf to image
import fitz #fitz module comes from pymupdf
documentpdfobject = fitz.open("pythoninfiniteloopalistlinks.pdf")
print(documentpdfobject.page_count) #print 2
print(documentpdfobject.metadata) #print {'format': 'PDF 1.6', 'title': '', 'author': '', 'subject': '', 'keywords': '', 'creator': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36', 'producer': 'Skia/PDF m97', 'creationDate': 'D:20220127022807Z', 'modDate': "D:20231002223603-07'00'", 'trapped': '', 'encryption': None}
pageonepdffile = documentpdfobject.load_page(0) #page 1 is index 0
print(pageonepdffile.get_text())
'''
1/26/22, 6:28 PM
python infinite loop a list - Google Search
https://www.google.com/search?q=python+infinite+loop+a+list&oq=python+infinite+loop+a+list&aqs=chrome..69i57j0i22i30l3.9167j1j7&sourceid=chro…
1/3
About 13,500,000 results (0.62 seconds) 
How can I in�nitely loop an iterator in Python, via a generator ...
May 2, 2019 — You can iterate over a list, appending an item to it: somelist = [item1, item2,
...
'''
convertpdftoimage = pageonepdffile.get_pixmap()
convertpdftoimage.save(f"page{pageonepdffile.number+1}.jpg") #return page1.jpg
#Extract links
getalllinks = pageonepdffile.get_links()
print(getalllinks) #print [{'kind': 2, 'xref': 26, 'from': Rect(86.0, 175.5, 363.9999694824219, 191.0), 'uri': 'https://stackoverflow.com/questions/12944882/how-can-i-infinitely-loop-an-iterator-in-python-via-a-generator-or-other', 'id': ''}, {'kind': 2, . . . }]
print(len(getalllinks)) #print 18
print(type(getalllinks)) #print <class 'list'>
for eachgetalllinks in range(0, len(getalllinks)):
    print(getalllinks[eachgetalllinks]) #print {'kind': 2, 'xref': 26, 'from': Rect(86.0, 175.5, 363.9999694824219, 191.0), 'uri': 'https://stackoverflow.com/questions/12944882/how-can-i-infinitely-loop-an-iterator-in-python-via-a-generator-or-other', 'id': ''}
    print(type(getalllinks[eachgetalllinks])) #print <class 'dict'>
    #Use get() method to get the value for uri
    print(str(getalllinks[eachgetalllinks].get("uri"))) #print https://stackoverflow.com/questions/12944882/how-can-i-infinitely-loop-an-iterator-in-python-via-a-generator-or-other

#Extracting data from PDF files using Python [y_ORF4FpZYo]
import PyPDF2
import re
filenamepdf = "MS_2019.pdf"
#documentpdfobject = PyPDF2.PdfFileReader(filenamepdf) ##PyPDF2.errors.DeprecationError: PdfFileReader is deprecated and was removed in PyPDF2 3.0.0. Use PdfReader instead.
documentpdfobject = PyPDF2.PdfReader(filenamepdf)
print(type(documentpdfobject)) #print <class 'PyPDF2._reader.PdfReader'>
numberofpages = len(documentpdfobject.pages)
print(numberofpages) #print 65
searchterm = "independent"
listpages = [] #Tuple key for listpages (all occurrences, page number)
for pagenumber in range(0, numberofpages):
    currentpage = documentpdfobject.pages[pagenumber]
    textincurrentpage = currentpage.extract_text()
    if re.findall(searchterm, textincurrentpage):
        #print(re.findall(searchterm, textincurrentpage)) #print ['independent']\n ['independent']\n ['independent', 'independent']\n ['independent']
        countpages = len(re.findall(searchterm, textincurrentpage))
        listpages.append((countpages, pagenumber + 1))
print(listpages) #print [(1, 1), (1, 3), (2, 30), (1, 31)].  One independent in page 1, one in page 3, two in page 30, and one in page 31.  Page 1 is index 0.
totalpagescontainingsearchterm = len(listpages)
print(totalpagescontainingsearchterm) #print 4
totalwordcountsearchterm = [eachtuple[0] for eachtuple in listpages]
print(totalwordcountsearchterm) #print [1, 1, 2, 1]
print(sum(totalwordcountsearchterm)) #print 5
print(f"The word {searchterm} was found {sum(totalwordcountsearchterm)} times on {totalpagescontainingsearchterm} pages.") #print The word independent was found 5 times on 4 pages.

def createfunction(filenamepdf: str, searchterm: str):
    documentpdfobject = PyPDF2.PdfReader(filenamepdf)
    numberofpages = len(documentpdfobject.pages)
    #print(numberofpages) #print 65
    listpages = [] #Tuple key for listpages (all occurrences, page number)
    for pagenumber in range(0, numberofpages):
        currentpage = documentpdfobject.pages[pagenumber]
        textincurrentpage = currentpage.extract_text()
        if re.findall(searchterm, textincurrentpage):
            countpages = len(re.findall(searchterm, textincurrentpage))
            listpages.append((countpages, pagenumber + 1))
    #print(listpages) #print [(1, 1), (1, 3), (2, 30), (1, 31)].  One independent in page 1, one in page 3, two in page 30, and one in page 31.  Page 1 is index 0.
    totalpagescontainingsearchterm = len(listpages)
    #print(totalpagescontainingsearchterm) #print 4
    totalwordcountsearchterm = sum([eachtuple[0] for eachtuple in listpages])
    #print(totalwordcountsearchterm) #print [1, 1, 2, 1]
    return (totalwordcountsearchterm, totalpagescontainingsearchterm)


filenamepdf = "MS_2019.pdf"
searchterm = "independent"
printresult = createfunction(filenamepdf, searchterm)
print(printresult) #print (5, 4)
print(f"The word {searchterm} was found {printresult[0]} times on {printresult[1]} pages.") #print The word independent was found 5 times on 4 pages.
