import qrcode

url = "https://the-circle-work.github.io/Printer-Setup/"

img = qrcode.make(url, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=4)
img.save("qr-code.png")
print("Saved qr-code.png for:", url)
