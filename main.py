from barcode.writer import ImageWriter
import barcode
from PIL import Image, ImageDraw, ImageFont


ean = barcode.get_barcode_class('ean13')
ean2 = ean(input('Введите номер штрихкода:'), writer=ImageWriter())
ean2.save('Штрих-код_00')

img = Image.new('RGB', (685, 354), 'white')
img.save('test1.jpg')

im1 = Image.open('test1.jpg')
im2 = Image.open('Штрих-код_00.png')

im2 = im2.resize(size=(600, 200))
im1.paste(im2, (60, 15))
im1.save('fon_pillow_paste.jpg', quality=95)

im1.close()
im2.close()

img = Image.open('fon_pillow_paste.jpg')
font = ImageFont.truetype("arial.ttf", size=36)
idraw = ImageDraw.Draw(img)
idraw.text((180, 210), 'Бирюлина А.С.', 'black', font=font)
idraw.text((180, 250), input('Введите наименование товара:'), 'black', font=font)
idraw.text((180, 290), ('Арткул: ' + input('Введите артикул:')), 'black', font=font)
img.save('001.jpg')
img = Image.open('001.jpg')
img.show()
