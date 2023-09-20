#import PyPDF2 #RM:  module version type pip show PyPDF2

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
