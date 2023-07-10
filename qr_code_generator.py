# install all the libs
# create a func to collect a text and convert it to a qrcode
# save the qrcode in a folder
# create a func to read the qrcode and show the text
# create a func to delete the qrcode
import qrcode


def generate_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save("my_qr.png")


url = input("Enter the url: ")
generate_qrcode(url)
