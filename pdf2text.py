import PyPDF2 as pdf
file=open('sample.pdf','rb')
pdf_reader=pdf.PdfFileReader(file)
n=pdf_reader.getNumPages()
for i in range(n):
  pages1=pdf_reader.getPage(i)
  print(pages1.extractText())