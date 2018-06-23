# merge cut watermark encrypt decrypt
# pdf merge source1 source2 destination
# pdf watermark source marksrc destination
# pdf encrypt source password destination
# pdf decrypt source password destination
# pdf cut source start-end destination

# algorithm
# create file objects for source as well as destination files
# create pdfreader objects for source objects
# create a new pdfwriter object
# perform various funtions
# write in the pdfwriter object
# use pdfwriter's write method to write in the file objects
# close all file objects


import PyPDF2, sys

if len(sys.argv) == 5:
    if sys.argv[1] == "merge":
        #pdf merge source1 source2 destination
        source1_path = sys.argv[2]
        source2_path = sys.argv[3]
        dest_path = sys.argv[4]

        # creating file objects
        file_s1 = open(source1_path, "rb")
        file_s2 = open(source2_path, "rb")
        file_d = open(dest_path,"wb")

        # creating pdfreader and pdfwriter objects
        pdf_r1 = PyPDF2.PdfFileReader(file_s1)
        pdf_r2 = PyPDF2.PdfFileReader(file_s2)
        pdf_w = PyPDF2.PdfFileWriter()

        # traversing the pages
        for pagenum in range(pdf_r1.numPages):
            pageObj  = pdf_r1.getPage(pagenum)
            pdf_w.addPage(pageObj)
        for pagenum in range(pdf_r2.numPages):
            pageObj  = pdf_r2.getPage(pagenum)
            pdf_w.addPage(pageObj)

        # file write
        pdf_w.write(file_d)

        # closing the files
        file_s1.close()
        file_s2.close()
        file_d.close()


    elif sys.argv[1] == "watermark":
        #pdf watermark source marksrc destination
        source_path = sys.argv[2]
        water_path = sys.argv[3]
        dest_path = sys.argv[4]

        # creating file objects
        file_s = open(source_path, "rb")
        file_w = open(water_path, "rb")
        file_d = open(dest_path, "wb")

        # creating pdfreader and pdfwriter objects
        pdf_rs = PyPDF2.PdfFileReader(file_s)
        pdf_rw = PyPDF2.PdfFileReader(file_w)
        pdf_w = PyPDF2.PdfFileWriter()

        # initialising watermark page object
        water_page = pdf_rw.getPage(0)

        # traversing the pages
        for pagenum in range(pdf_rs.numPages):
            pageObj = pdf_rs.getPage(pagenum)
            pdf_w.addPage(pageObj.mergePage(water_page))

        # file write
        pdf_w.write(file_d)

        # closing the files
        file_s.close()
        file_w.close()
        file_d.close()


    elif sys.argv[1] == "encrypt":
        #pdf encrypt source password destination
        source_path = sys.argv[2]
        password = sys.argv[3]
        dest_path = sys.argv[4]

        # creating file objects
        file_s = open(source_path, "rb")
        file_d = open(dest_path, "wb")

        # creating pdfreader and pdfwriter objects
        pdf_r = PyPDF2.PdfFileReader(file_s)
        pdf_w = PyPDF2.PdfFileWriter()

        # traversing the pages
        for pagenum in range(pdf_r.numPages):
            pageObj = pdf_r.getPage(pagenum)
            pdf_w.addPage(pageObj)

        # encrypt the writer
        pdf_w.encrypt(password)

        # file write
        pdf_w.write(file_d)

        # closing the files
        file_s.close()
        file_d.close()


    elif sys.argv[1] == "decrypt":
        #pdf decrypt source password destination
        source_path = sys.argv[2]
        water_path = sys.argv[3]
        dest_path = sys.argv[4]

        # creating file objects
        file_s = open(source_path, "rb")
        file_d = open(dest_path, "wb")

        # creating pdfreader and pdfwriter objects
        pdf_r = PyPDF2.PdfFileReader(file_s)
        pdf_w = PyPDF2.PdfFileWriter()

        #encrypt the reader
        pdf_r.decrypt(password)

        # traversing the pages
        for pagenum in range(pdf_r.NumPages):
            pageObj = pdf_r.getPage(pagenum)
            pdf_w.addPage(pageObj)

        # file write
        pdf_w.write(file_d)

        # closing the files
        file_s.close()
        file_d.close()

    elif sys.argv[1] == "cut":
        #pdf cut source start-end destination
        source_path = sys.argv[2]
        start_page, end_page = map(int, sys.argv[3].split("-"))
        start_page, end_page = start_page-1, end_page
        dest_path = sys.argv[4]

        # creating file objects
        file_s = open(source_path, "rb")
        file_d = open(dest_path, "wb")

        # creating pdfreader and pdfwriter objects
        pdf_r = PyPDF2.PdfFileReader(file_s)
        pdf_w = PyPDF2.PdfFileWriter()

        # traversing the pages
        for pagenum in range(start_page, end_page):
            pageObj = pdf_r.getPage(pagenum)
            pdf_w.addPage(pageObj)

        # file write
        pdf_w.write(file_d)

        # closing the files
        file_s.close()
        file_d.close()
