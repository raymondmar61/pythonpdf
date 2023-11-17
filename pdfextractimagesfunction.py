from pypdf import PdfReader
from pypdf import PdfWriter

#Get all pdf files
import os
folderpath = r"/home/mar/python/pdffiles"
fileslist = []
def listfilenames(directory):
    filenames = os.listdir(directory)
    for eachfilenames in filenames:
        if eachfilenames[-4:] == ".pdf":
            fileslist.append(eachfilenames)
        # print("Folder Path: " + os.path.abspath(os.path.join(directory, eachfilenames)), sep="\n") #print Folder Path: /home/mar/python/pdffiles/pdffile 2020 02 Feb.pdf


#Get Producer information to determine which function to extract pdf images
producerlist = []
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
        #Edit pdf file metadata insert /Producer metadata by writing all pages in pdf file
        writepdffileobject = PdfWriter()
        #Add all pages in pdf file to the PdfWriter
        for eachpage in readpdffileobject.pages:
            writepdffileobject.add_page(eachpage)
        #Insert new metadata
        writepdffileobject.add_metadata({"/Producer": "No Producer", "/CustomField": "CustomField2"})
        #Save the updated pdf to the same file name
        with open(eachfilelist, "wb") as updatemetadatafileobject:
            writepdffileobject.write(updatemetadatafileobject)

    '''
    pdffile 2020 02 Feb.pdf
    iTextSharp™ 5.5.9 ©2000-2016 iText Group NV (AGPL-version); modified using iTextSharp™ 5.5.9 ©2000-2016 iText Group NV (AGPL-version)
    pdffile 2008 04 Apr.pdf
    Acrobat Distiller 7.0.5 (Windows)
    pdffile 2009 05 May Hardcopy.pdf
    Adobe Acrobat 8.1 Image Conversion Plug-in
    pdffile 2008 06 Jun Hardcopy.pdf
    Adobe Acrobat 8.1 Image Conversion Plug-in
    pdffile 2006 06 Jun Anniversary.pdf
    Acrobat Distiller 7.0.5 (Windows)
    '''
#Sort and print the pdf files
producerlist.sort(reverse=False)
for x in producerlist:
    print(x)

#Different functions for different types of Producers
def distiller(pdffilename):
    readpdffileobject = PdfReader(pdffilename)
    numberofpages = len(readpdffileobject.pages)
    print(numberofpages) #print 120
    pageonepdffile = readpdffileobject.pages[0] #page 1 is index 0.  RM:  It seems page 1 or index 0 is the entire .pdf file as 120 images.  Index 0 is all 120 pages of 120 images.
    for eachimage in pageonepdffile.images:
        imagefilename = pdffilename[:-4] + eachimage.name[1:]
        print(imagefilename) #print pdffile 2008 04 Apr1.jpg\n pdffile 2008 04 Apr10.jpg\n pdffile 2008 04 Apr100.jpg\n pdffile 2008 04 Apr101.jpg
        with open(imagefilename, "wb") as fobject:
            fobject.write(eachimage.data)
def itextsharpacrobat(pdffilename):
    readpdffileobject = PdfReader(pdffilename)
    numberofpages = len(readpdffileobject.pages)
    print(numberofpages) #print 119
    pageonepdffile = readpdffileobject.pages[0]
    for eachpage in range(0, numberofpages):
        for eachimage in readpdffileobject.pages[eachpage].images:
            imagefilename = f"{pdffilename[:-4]}{eachpage+1}{eachimage.name[-4:]}"
            print(imagefilename) #print pdffile 2020 02 Feb1.jpg
            if eachimage.name[-4:] == ".jp2":
                with open(imagefilename, "wb") as fobject:
                    fobject.write(eachimage.data)
            if eachimage.name[-4:] == ".jpg":
                with open(imagefilename, "wb") as fobject:
                    fobject.write(eachimage.data)


for eachfilelist in fileslist:
    readpdffileobject = PdfReader(eachfilelist)
    infopdffile = readpdffileobject.metadata
    choosefunctionextractimage = infopdffile["/Producer"]
    print(eachfilelist + ":" + choosefunctionextractimage)
    if choosefunctionextractimage.find("iTextSharp") >= 0:
        print("iTextSharp itextsharpacrobat()")
        itextsharpacrobat(eachfilelist)
    elif choosefunctionextractimage.find("Adobe Acrobat") >= 0:
        print("Adobe Acrobat itextsharpacrobat()")
        itextsharpacrobat(eachfilelist)
    elif choosefunctionextractimage.find("5.0.2") >= 0:
        print("5.0.2 itextsharpacrobat()")
        itextsharpacrobat(eachfilelist)
    elif choosefunctionextractimage.find("A-PDF") >= 0:
        print("A-PDF itextsharpacrobat()")
        itextsharpacrobat(eachfilelist)
    elif choosefunctionextractimage.find("No Producer") >= 0:
        print("No Producer itextsharpacrobat()")
        itextsharpacrobat(eachfilelist)
    elif choosefunctionextractimage.find("Bullzip PDF Printer") >= 0:
        print("Bullzip PDF Printer itextsharpacrobat()")
        itextsharpacrobat(eachfilelist)
    elif choosefunctionextractimage.find("Distiller") >= 0:
        print("Distiller distiller()")
        distiller(eachfilelist)
    elif choosefunctionextractimage.find("TCPDF") >= 0:
        print("TCPDF distiller()")
        distiller(eachfilelist)
    elif choosefunctionextractimage.find("5.0.7") >= 0:
        print("5.0.7 distiller()")
        distiller(eachfilelist)
    else:
        print("Metadata /Producer missing")
