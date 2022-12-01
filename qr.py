#https://www.instagram.com/python_developer_07/


import os 
import qrcode 

img = qrcode.make("https://www.instagram.com/python_developer_07/")

img.save("qr07.png" , "PNG")
os.system("open qr07.png")