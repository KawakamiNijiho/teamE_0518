import os,qrcode
from PIL import Image

path = os.path.join("./", "files", "Pengsoo.png")

# 썸네일 만들기
thub_img = Image.open(thub_img_path)
thub_img.thumbnail((60, 60))


# img = Image.open("./files/Pengsoo.png")
# img.show()


im = Image.save(path)

# import qrcode
# from PIL import Image

# # 텍스트 데이터 입력
# data = "This is the text that will be encoded into the QR code"

# # QR 코드 객체 생성
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )

# # 데이터 추가
# qr.add_data(data)
# qr.make(fit=True)

# # 이미지 생성
# img = qr.make_image(fill_color="black", back_color="white")

# # 이미지 저장
# img.save("qrcode.png")
