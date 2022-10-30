import qrcode
 
# Data to encode
data = input('Enter the Data: ')
version=int(input('Enter the version (complexity)[1 - 15]: '))  #maxvalue  15
box_size=int(input('Enter the Box size [1 - 10] : '))  # max value 10
 
qr = qrcode.QRCode(version ,box_size,border = 5)
 
# Adding data to the instance 'qr'
qr.add_data(data)
 
img = qr.make_image(fill_color = 'black',back_color = 'white')
 
f=input("name it as: ")     #image name
 
img.save(f'{f}.png')
 
print('qr code generated and saved in the gallery')