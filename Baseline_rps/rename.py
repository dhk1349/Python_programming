import os
from glob import glob

path = "/home/dhk1349/Desktop/1-1/rps/mydataset"
subf=["r","p","s"]

for i in subf:
    filelist = glob(os.path.join(path, i, "*.JPG"))
    print(os.path.join(path, i, "*.JPG"))
    print()
    for idx, f in enumerate(filelist):
        os.rename(f, os.path.join(path, i, f"spds066_{i}_{idx}.jpg"))
