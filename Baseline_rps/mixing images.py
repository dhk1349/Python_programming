import numpy as np
import os
import random
from PIL import Image
from glob import glob
from tqdm import tqdm

# img1 = np.asarray(Image.open("/home/dhk1349/Desktop/1-1/rps/rps/rps/scissors/scissors01-017.png"))
# img2 = np.asarray(Image.open("/home/dhk1349/Desktop/1-1/rps/rps/sample.jpg"))
#
# img3 = np.asarray(Image.open("/home/dhk1349/Desktop/1-1/rps/validation/p/spds-rps_p_0.jpg"))
# print(img1.shape, img2.shape, img3.shape)
#
# # files = glob("/home/dhk1349/Desktop/1-1/rps/validation/p/*.jpg")
# # for i in files:
# #     img = np.asarray(Image.open(i))
# #     print(img.shape)
#
# files = glob("/home/dhk1349/Desktop/1-1/rps/rps/rps/paper/*.png")
# back = np.zeros((300, 300, 3), dtype=np.uint8)
# content = np.asarray(Image.open("/home/dhk1349/Desktop/1-1/rps/rps/sample.jpg"))
# back[22:256+22, 22:256+22, :] = content
# # print(back.shape)
# # pil_image = Image.fromarray(back)
# # pil_image.show()
# # white pixel is (255, 255, 255)
# for idx, i in enumerate(files):
#     """
#     이런식으로 하면 손의 edge는 남고 색은 날아간다.
#     """
#     img = np.array(Image.open(i))
#     img = img[:, :, :3]
#     print(img[:, :, 0])
#     for i in range(img.shape[0]):
#         for j in range(img.shape[1]):
#             if np.sum(img[i, j, :]) > 225*3:
#                 img[i, j, :] = back[i, j, :]
#     # img = (img + back)//2
#     print(img.shape)
#     pil_image = Image.fromarray(img)
#     pil_image.show()
#     if idx == 11:
#         break



"""
Mixing background with places large validation set
"""
train_dir = "../rps/rps/"
background_dir = "/media/dhk1349/disk1/datasets/val_large_places512/"
save_dir = "../rps/augmented_rps/"
sub_dir = ["rock", "scissors"]


for sd in sub_dir:
    train_files = glob(os.path.join(train_dir, sd,  "*.png"))
    bg_file = glob(os.path.join(background_dir, "*.jpg"))
    random.shuffle(bg_file)

    for idx, f in tqdm(enumerate(train_files)):
        img = np.array(Image.open(f))
        img = img[:, :, :3]
        bg = np.array(Image.open(bg_file[idx])) #512 pixels
        bg = bg[:300, :300, :] # crop to 300 pixels

        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if np.sum(img[i, j, :]) > 225*3:
                    img[i, j, :] = bg[i, j, :]

        pil_image = Image.fromarray(img)
        pil_image.save(os.path.join(save_dir, sd, f.split("/")[-1]))