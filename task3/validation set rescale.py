import os
import numpy as np
import torch
import torch.nn as nn
import PIL
from PIL import Image
import random
from glob import glob
from torch.utils.data import DataLoader
from torchvision import transforms, datasets


files = glob("/home/dhk1349/Desktop/1-1/rps/validation/p/*.jpg")
# files = glob("/home/dhk1349/Desktop/1-1/rps/rps/augmented_rps/p/*.png")
random.shuffle(files)
t2 = transforms.Compose([transforms.Resize((224, 224)), transforms.GaussianBlur(3), transforms.ColorJitter(brightness=(0.2, 2), contrast=(0.3, 2), saturation=(0.2, 2), hue=(-0.3, 0.3)), transforms.RandomHorizontalFlip(),
                                  transforms.RandomVerticalFlip(), transforms.Grayscale(3)])

for idx, f in enumerate(files):
    img = Image.open(f)
    img = t2(img)
    img.show()
    if idx ==5:
        break
