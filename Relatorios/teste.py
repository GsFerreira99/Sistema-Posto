from reportlab.pdfgen.canvas import Canvas

def write(myfile, page_number):
    myfile.drawString(200, 600, 'Page number %i script' % page_number)

myfile = Canvas('multi_pages.pdf')
total_pages = 3

for i in range(total_pages):
    write(myfile, i)
    myfile.showPage()

myfile.save()