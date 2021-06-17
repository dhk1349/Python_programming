"""
TODO
validation set들이 보통 high resolution이고 pixel ratio도 제각각이다.
validation loader에서는 이를 위해 padding으로 정사각형을 만들고 이루에 resize를 한다.

"""
import os
from glob import glob
import numpy as np
import random
from sklearn.utils import shuffle
from PIL import Image

import torch
import torch.utils.data as data
from torchvision import transforms, datasets


class Augmented_train(data.Dataset):
  def __init__(self, root, transform):
    self.root = root
    self.transform = transform
    self.infer_transform = transforms.Compose([transforms.Resize(300, 300), transforms.CenterCrop([224, 224])])
    self.load_dataset()

  def load_dataset(self):
    self.p = glob(os.path.join(self.root, "p", "*.jpg"))
    self.p_label = np.zeros([len(self.p)])

    self.r = glob(os.path.join(self.root, "r", "*.jpg"))
    self.r_label = np.zeros([len(self.r)])
    self.r_label.fill(1)

    self.s = glob(os.path.join(self.root, "s", "*.jpg"))
    self.s_label = np.zeros([len(self.s)])
    self.s_label.fill(2)

    self.p.extend(self.r)
    self.p.extend(self.s)
    self.labels = np.append(np.append(self.p_label, self.r_label), self.s_label)
    # self.labels.astype('uint32')
    self.files, self.labels = shuffle(self.p, self.labels)

  def __len__(self):
    return len(self.files)

  def __getitem__(self, index):
    file = Image.open(self.files[index])
    label = self.labels[index]
    # label = torch.from_numpy(np.array(label), dtype=torch.long)

    file = self.transform(file)  #tensor format
    bigger = max(file.size()[1], file.size()[2])
    # print(f"Before: {file.size()}")
    file = transforms.Pad([(bigger-file.size()[2])//2, (bigger-file.size()[1])//2, (bigger-file.size()[2])//2, (bigger-file.size()[1])//2])(file)

    # print(f"Later: {file.size()}")

    file = self.infer_transform(file)

    return file, label

class Inference_dataset(data.Dataset):
  def __init__(self, root, transform):
    self.root = root
    self.transform = transform
    self.infer_transform = transforms.Compose([transforms.Resize([300, 300]), transforms.CenterCrop(224)])
    self.load_dataset()

  def load_dataset(self):
    self.p = glob(os.path.join(self.root, "p", "*.jpg"))
    self.p_label = np.zeros([len(self.p)])

    self.r = glob(os.path.join(self.root, "r", "*.jpg"))
    self.r_label = np.zeros([len(self.r)])
    self.r_label.fill(1)

    self.s = glob(os.path.join(self.root, "s", "*.jpg"))
    self.s_label = np.zeros([len(self.s)])
    self.s_label.fill(2)

    self.p.extend(self.r)
    self.p.extend(self.s)
    self.labels = np.append(np.append(self.p_label, self.r_label), self.s_label)
    # self.labels.astype('uint32')
    self.files, self.labels = shuffle(self.p, self.labels)

  def __len__(self):
    return len(self.files)

  def __getitem__(self, index):
    file = Image.open(self.files[index])
    label = self.labels[index]
    # label = torch.from_numpy(np.array(label), dtype=torch.long)

    file = self.transform(file)  #tensor format
    bigger = max(file.size()[1], file.size()[2])
    # print(f"Before: {file.size()}")
    # file = transforms.Pad([(bigger-file.size()[2])//2, (bigger-file.size()[1])//2, (bigger-file.size()[2])//2, (bigger-file.size()[1])//2])(file)
    file = transforms.CenterCrop(bigger)(file)
    # print(f"Later: {file.size()}")

    file = self.infer_transform(file)

    return file, label