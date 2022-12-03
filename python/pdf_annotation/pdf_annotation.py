import fitz
doc = fitz.open("example.pdf")
for i in range(doc.pageCount):
	page = doc[i]
	for annot in page.annots():
		print(i, "||", annot.info["content"], "||", annot.colors, "||", annot.type)

# https://stackoverflow.com/questions/72311956/how-to-extract-highlights-and-text-box-contents-from-pdf-in-python/72313329#72313329