#!/usr/local/bin/python3

import io
import math
import sys
from PIL import Image

def JPEGSaveWithTargetSize(im, filename, target):
   """Save the image as JPEG with the given name at best quality that makes less than "target" bytes"""
   # Min and Max quality
   Qmin, Qmax = 25, 96
   # Highest acceptable quality found
   Qacc = -1
   while Qmin <= Qmax:
      m = math.floor((Qmin + Qmax) / 2)

      # Encode into memory and get size
      buffer = io.BytesIO()
      im.save(buffer, format="JPEG", quality=m)
      s = buffer.getbuffer().nbytes

      if s <= target:
         Qacc = m
         Qmin = m + 1
      elif s > target:
         Qmax = m - 1

   # Write to disk at the defined quality
   if Qacc > -1:
      im.save(filename, format="JPEG", quality=Qacc)
      im.show()
   else:
      print("ERROR: No acceptble quality factor found", file=sys.stderr)

################################################################################
# main
################################################################################

# Load sample image
from PIL import Image
import requests
from io import BytesIO

url="https://raw.githubusercontent.com/lumanyu/ai_app/main/data/recipe/braised_pork.png"
response = requests.get(url)
im = Image.open(BytesIO(response.content)) #原始图片来自网络
rgb_im = im.convert('RGB')
#im = Image.open('/Users/mark/sample/images/lena.png')  #原始图片来自本地磁盘

# Input Image Limitation
storage=100000  #目标图片存储空间
max_width=100   #目标图片宽度
min_width=100
max_height=100  #目标图片高度
min_width=100

new_width=max_width
new_height=max_height
if rgb_im.width/rgb_im.height>new_width/new_height:
    new_height=int(new_height*rgb_im.height/rgb_im.width)
else:
    new_width=(new_width*rgb_im.width/rgb_im.height)

resized_im = rgb_im.resize((new_width, new_height), Image.Resampling.LANCZOS)


# Save at best quality under 100,000 bytes
JPEGSaveWithTargetSize(resized_im, "result.jpg", storage)
