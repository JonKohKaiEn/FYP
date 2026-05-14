from pix2text import Pix2Text

p2t = Pix2Text()

# process PDF file
doc = p2t.recognize_pdf("question sources/linear_algebra.pdf")
doc.to_markdown("linalg.md")
