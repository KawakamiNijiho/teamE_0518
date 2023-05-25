import sys
args = sys.argv
url = args[1]
name = args[2]

import os
# os.pat.joinを利用して相対パスを生成
path = os.path.join("..","files",name)

import qrcode
img = qrcode.make(url)

img.save(path)