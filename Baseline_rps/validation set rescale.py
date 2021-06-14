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


files = glob("/home/dhk1349/Desktop/1-1/rps/validation/s/*.jpg")
random.shuffle(files)
t2 = transforms.Compose([transforms.Resize((224, 224))])

for idx, f in enumerate(files):
    img = Image.open(f)
    img = t2(img)
    img.show()
    if idx ==10:
        break
