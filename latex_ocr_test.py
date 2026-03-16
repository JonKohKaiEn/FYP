from pix2text import Pix2Text

p2t = Pix2Text()

# process PDF file
doc = p2t.recognize_pdf("24S1-IE2107-LA-Tutorial.pdf")
doc.to_markdown("linalg.md")
