# -*- coding: utf-8 -*-
"""
Created on Tue May  4 15:27:41 2021

@author: dhk1349
"""
import os
import argparse
from PIL import Image
from glob import glob


parser = argparse.ArgumentParser()
parser.add_argument('--path', required=True ,type=str, default='./')

args=parser.parse_args()

files = glob(os.path.join(args.path,"*png"))
for f in files:
    print(f"Converting \n\t{f} to \n\t{f[:-3]}pdf")
    image1 = Image.open(f)
    im1 = image1.convert('RGB')
    im1 = im1.transpose(Image.ROTATE_270)
    a4im = im1.resize((565,842))
    """
    a4im = Image.new('RGB',
                 (595, 842),   # A4 at 72dpi
                 (255, 255, 255))  # White
    a4im.paste(im1, im1.getbbox())  # Not centered, top-left corner
    """
    a4im.save(f[:-3]+"pdf", "PDF", quality=100)