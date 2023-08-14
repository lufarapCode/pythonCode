import pyqrcode 
import png 

link = input("Ingresa la url: ")
nombre = input("ingresa el nombre a guardar: ")
qr_code = pyqrcode.create(link)
qr_code.png(f"{nombre}.png", scale =5)
print ("EL código Qr ha sido creado")

# url = pyqrcode.create('6231')
# url.svg('uca-url.svg', scale=4)
# url.eps('uca-url.eps', scale=1)
# print(url.terminal(quiet_zone=1))
# url.show()

# big_code = pyqrcode.create('0987654321', error='L', version=27, mode='binary')
# big_code.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
# big_code.show()