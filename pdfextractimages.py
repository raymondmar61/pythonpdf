#No Producer information or Producer field is blank
import fitz #from PyMuPDF module
import PIL.Image #from pillow module
import io
pdffilename = r"pdffile 2020 01 Jan.pdf"
pdffilewithimages = fitz.open(pdffilename)
counterimagefilename = 1
for pdffilepagenumber in range(len(pdffilewithimages)):
    pdfpage = pdffilewithimages[pdffilepagenumber]
    images = pdfpage.get_images()
    for eachimages in images:
        baseimage = pdffilewithimages.extract_image(eachimages[0])
        # print(baseimage) #print {'ext': 'jpeg', 'smask': 0, 'width': 658, 'height': 355, 'colorspace': 3, 'bpc': 8, 'xres': 96, 'yres': 96, 'cs-name': 'DeviceRGB', 'image': b'\xff\xd8\xff\xee\x00\x0eAdobe\x00d\x80\x00\x00\x00\x01\xff\xdb\x00\x84\x00\x0c\x08\x08\x08\t\x08\x0c\t\t\x0c\x11\x0b\n\x0b\x11\x15\x0f\x0c\x0c\x0f\x15\x18\x13\x13\x15\x13\x13\x18\x17\x12\x14\x14\x14\x14\x12\x17\x17\x1b\x1c\x1e\x1c\x1b\x17$$\'\'$$53335;;;;;;;;;;\x01\r\x0b\x0b\r\x0e\r\x10\x0e\x0e\x10\x14\x0e\x0f\x0e\x14\x14\x10\x11\x11\x10\x14\x1d\x14\x14\x15\x14\x14\x1d%\x1a\x17\x17\x17\x17\x1a% #\x1e\x1e\x1e# ((%%((22022;;;;;;;;;;\xff\xc0\ . . . \x00\x00\x00\x00IEND\xaeB`\x82'}
        imageitselfisbytes = baseimage["image"]
        extractimageextension = baseimage["ext"] #RM:  It's the ext in the baseimage dictionary for which it's not displaying as a dictionary.
        saveactualimage = PIL.Image.open(io.BytesIO(imageitselfisbytes))
        imageextension = baseimage["ext"] #RM:  It's the ext in the baseimage dictionary
        saveactualimage.save(open(f"{pdffilename[:-4]}{counterimagefilename}.{extractimageextension}", "wb")) #image saved as imagename1.jpeg.  RM:  extracted part of the pic.  Not the entire pic.  Scroll up the baseimage there is another extension png.  Interesting.  There are two images saved imagename1.jpeg and imagename2.png.  imagename2.png is the other part of the pic.
        counterimagefilename += 1

#Producer is Distiller
from pypdf import PdfReader
pdffilename = r"pdffile 2008 04 Apr.pdf"
readpdffileobject = PdfReader(pdffilename)
# print(readpdffileobject) #print <pypdf._reader.PdfReader object at 0x7fc3f54ef0d0>
numberofpages = len(readpdffileobject.pages)
print(numberofpages) #print 120
pageonepdffile = readpdffileobject.pages[0] #page 1 is index 0.  RM:  It seems page 1 or index 0 is the entire .pdf file as 120 images.  Index 0 is all 120 pages of 120 images.
#For loop to extract images for all pages in pdf file
#print(pageonepdffile.images) #print [Image_0=/I1, Image_1=/I10, Image_2=/I100, . . . Image_118=/I96, Image_119=/I97, Image_120=/I98, Image_121=/I99]
for eachimage in pageonepdffile.images:
    #print(eachimage.name) #print I1.jpg\n I10.jpg\n I100.jpg\n I101.jpg . . . I97.jpg\n I98.jpg\n I99.jpg
    # print(eachimage.data) #print the bytes for eachimage image
    imagefilename = pdffilename[:-4] + eachimage.name[1:]
    print(imagefilename) #print pdffile 2008 04 Apr1.jpg\n pdffile 2008 04 Apr10.jpg\n pdffile 2008 04 Apr100.jpg\n pdffile 2008 04 Apr101.jpg
    with open(imagefilename, "wb") as fobject:
        fobject.write(eachimage.data)

#Producer is iTextSharp or Acrobat
from pypdf import PdfReader
pdffilename = r"pdffile 2020 02 Feb.pdf"
readpdffileobject = PdfReader(pdffilename)
# print(readpdffileobject) #print <pypdf._reader.PdfReader object at 0x7fc3f54ef0d0>
numberofpages = len(readpdffileobject.pages)
print(numberofpages) #print 119
pageonepdffile = readpdffileobject.pages[0]
# print(pageonepdffile.images) #print [Image_0=['/Xf2', '/Im1']]
# print(type(pageonepdffile.images)) #print <class 'pypdf._page._VirtualListImages'>
#For loop to extract images for all pages in pdf file
for eachpage in range(0, numberofpages):
    print(eachpage) #print 0
    # print(readpdffileobject.pages[eachpage]) #print {'/Contents': IndirectObject(4, 0, 139791050424528), '/MediaBox': [0, 0, 1669, 2200], '/Parent': IndirectObject(5, 0, 139791050424528), '/Resources': {'/XObject': {'/Xf1': IndirectObject(2, 0, 139791050424528)}}, '/Type': '/Page'}
    print(readpdffileobject.pages[eachpage].images) #print [Image_0=['/Xf1', '/Im1']]
    # # print(readpdffileobject.pages[eachpage].images.name) #print AttributeError: '_VirtualListImages' object has no attribute 'name'
    for eachimage in readpdffileobject.pages[eachpage].images:
        print(eachimage) #print ImageFile(name=Im1.jpg, data: 360.2 kB)
        print(type(eachimage)) #print <class 'pypdf._utils.ImageFile'>
        print(eachimage.name) #print Im1.jpg
        imagefilename = f"{pdffilename[:-4]}{eachpage+1}{eachimage.name[-4:]}"
        print(imagefilename) #print pdffile 2020 02 Feb1.jpg
        with open(imagefilename, "wb") as fobject:
            fobject.write(eachimage.data)

#Producer is Distiller
from pypdf import PdfReader
readpdffileobject = PdfReader("pdffile 2008 04 Apr.pdf") #Correct extract images
numberofpages = len(readpdffileobject.pages)
print(numberofpages) #print 1
pageonepdffile = readpdffileobject.pages[0]
#For loop to extract images for all pages in pdf file
for eachimage in pageonepdffile.images:
    with open(eachimage.name, "wb") as fobject:
        fobject.write(eachimage.data) #return Im1.jpg and Im2.png

#Get pdf file names in a directory or folder
import os
folderpath = r"/home/mar/python/pdffiles"
fileslist = []
def listfilenames(directory):
    filenames = os.listdir(directory)
    for eachfilenames in filenames:
        if eachfilenames[-4:] == ".pdf":
            fileslist.append(eachfilenames)
        print("Folder Path: " + os.path.abspath(os.path.join(directory, eachfilenames)), sep="\n") #print Folder Path: /home/mar/python/pdffiles/pdffile 2020 02 Feb.pdf


listfilenames(folderpath)
print(fileslist)
print(len(fileslist))

#Extract the different producers
from pypdf import PdfReader
producerlist = []
fileslist = ["pdffile 2015 10 Oct.pdf", "pdffile 2016 05 May.pdf", "pdffile 2016 06 Jun Anniversary.pdf"]
for eachfilelist in fileslist:
    print(eachfilelist) #print pdffile 2015 10 Oct.pdf
    readpdffileobject = PdfReader(eachfilelist)
    infopdffile = readpdffileobject.metadata
    try:
        print(infopdffile["/Producer"]) #print Adobe Acrobat 11.0.10 Image Conversion Plug-in
        producerlist.append(infopdffile["/Producer"] + ":  " + eachfilelist)
    except:
        print("No Producer")
        producerlist.append("No Producer" + ": " + eachfilelist)
    '''
    pdffile 2015 10 Oct.pdf
    Adobe Acrobat 11.0.10 Image Conversion Plug-in
    pdffile 2016 05 May.pdf
    Adobe Acrobat 11.0.10 Image Conversion Plug-in
    pdffile 2016 06 Jun Anniversary.pdf
    A-PDF Watermark 2.9.0 
    '''
producerlist.sort(reverse=False)
for x in producerlist:
    print(x)
    '''
    A-PDF Watermark 2.9.0 :  pdffile 2016 06 Jun Anniversary.pdf
    Adobe Acrobat 11.0.10 Image Conversion Plug-in:  pdffile 2015 10 Oct.pdf
    Adobe Acrobat 11.0.10 Image Conversion Plug-in:  pdffile 2016 05 May.pdf
    '''