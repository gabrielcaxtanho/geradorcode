
import qrcode
from PIL import Image

# URL que será aberta ao escanear o código QR
url = "https://gabrielcaxtanho.github.io/caodivulga/"

# Criar um objeto QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Adicionar dados ao objeto QRCode (URL)
qr.add_data(url) 
qr.make(fit=True)

# Criar uma imagem do código QR usando a biblioteca PIL
img_qr = qr.make_image(fill_color="black", back_color="white")

# Salvar a imagem do código QR
img_qr.save("qrcodepagina.png")

# Exibir a imagem do código QR (opcional)
img_qr.show()

