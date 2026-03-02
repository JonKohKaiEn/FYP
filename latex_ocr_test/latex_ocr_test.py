from pix2text import Pix2Text


model = Pix2Text()

question = model.recognize("question_img.png")
print(question)
