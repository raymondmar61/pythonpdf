import pikepdf

file = "56_power_query_tutorials.pdf"
pdffile = pikepdf.Pdf.open(file)
urls = []
for page in pdffile.pages:
    for annots in page.get("/Annots"):
        uri = annots.get("/A").get("/URI")
        if uri is not None:
            print("URL found:", uri)
            urls.append(uri)
urls = list(set(urls)) #RM:  program printed duplicates or .pdf file duplicate links.  Convert to set and convert back to list.
urlscount = len(urls)
print("Total URLs extracted:", urlscount) #print Total URLs extracted: 59
print(urls)
'''
[pikepdf.String("https://www.myonlinetraininghub.com/secret-power-query-function-list"), pikepdf.String("https://www.myonlinetraininghub.com/connecting-to-an-oauth-api-like-paypal-with-power-query"), pikepdf.String("https://www.myonlinetraininghub.com/table-statistics-from-table-profile-in-power-query"), pikepdf.String("https://www.myonlinetraininghub.com/vlookup-in-power-query-using-list-functions"), . . . 
'''
print("\n")

filewrite = open("powerquerytutorialslinks.txt", "w")
for extracturlfromurlslist in range(0, urlscount):
    print(urls[extracturlfromurlslist])
    # print(type(urls[extracturlfromurlslist])) #print <class 'pikepdf.objects.Object'>
    '''
    https://www.myonlinetraininghub.com/secret-power-query-function-list
    https://www.myonlinetraininghub.com/connecting-to-an-oauth-api-like-paypal-with-power-query
    https://www.myonlinetraininghub.com/table-statistics-from-table-profile-in-power-query
    https://www.myonlinetraininghub.com/vlookup-in-power-query-using-list-functions
    ...
    '''
    filewrite.write(str(urls[extracturlfromurlslist]) + "\n")
filewrite.close()

with open("powerquerytutorialslinks.txt", "r") as readtextfile:
    for webpageurl in readtextfile.readlines():
        print(webpageurl)
