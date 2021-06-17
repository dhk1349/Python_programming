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
  def __init__(self, root, bg_root, transform, device):
    self.root = root
    self.bg_root = bg_root
    self.transform = transform
    self.load_dataset()
    self.device = device

  def load_dataset(self):
    self.p = glob(os.path.join(self.root, "paper", "*.png"))
    self.p_label = np.zeros([len(self.p)])

    self.r = glob(os.path.join(self.root, "rock", "*.png"))
    self.r_label = np.zeros([len(self.r)])
    self.r_label.fill(1)

    self.s = glob(os.path.join(self.root, "scissors", "*.png"))
    self.s_label = np.zeros([len(self.s)])
    self.s_label.fill(2)

    self.p.extend(self.r)
    self.p.extend(self.s)
    self.labels = np.append(np.append(self.p_label, self.r_label), self.s_label)
    # self.labels.astype('uint32')
    self.bg = glob(os.path.join(self.bg_root, "*.jpg"))
    self.files, self.labels = shuffle(self.p, self.labels)
    self.data = torch.zeros(len(self.files), 3, 224, 224)
    # self.data.to(self.device)
    self.bg_data = torch.zeros(len(self.bg), 3, 300, 300)

    for idx in range(len(self.bg)):
      bg = Image.open(self.bg[idx % len(self.bg)])
      bg = transforms.ToTensor()(bg)
      bg = bg[:, :300, :300]
      self.bg_data[idx] = bg

    for idx in range(len(self.files)):
      file = Image.open(self.files[idx])
      file = transforms.ToTensor()(file)
      file = file[:3, :, :]
      bg = self.bg_data[idx%len(self.bg)]

      minus = torch.tensor(-1)
      zero = torch.tensor(0)
      maxnum = torch.tensor(255)

      filter = file[0, :, :] + file[1, :, :] + file[2, :, :]
      filter = torch.where(filter>2.6, filter, minus.float())

      _filter = torch.stack((filter, filter, filter))
      file = torch.where(_filter<0, file, bg)
      file = self.transform(file)

      self.data[idx] = file

  def __len__(self):
    return len(self.files)

  def __getitem__(self, index):
    return self.data[index], self.labels[index]

class Inference_dataset(data.Dataset):
  def __init__(self, root, transform):
    self.root = root
    self.transform = transform
    self.infer_transform = transforms.Compose([transforms.Resize([300, 300]), transforms.CenterCrop(224)])
    self.load_dataset()

  def load_dataset(self):
    print("loading validation set...")
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

    file = self.transform(file)  #tensor format
    bigger = max(file.size()[1], file.size()[2])
    file = transforms.CenterCrop(bigger)(file)

    file = self.infer_transform(file)

    return file, label



class test_dataset(data.Dataset):
  def __init__(self, root, transform):
    self.root = root
    self.transform = transform
    self.infer_transform = transforms.Compose([transforms.Resize([300, 300]), transforms.CenterCrop(224)])
    self.load_dataset()

  def load_dataset(self):
    print("loading test set...")
    self.files = glob(os.path.join(self.root, "*.jpg"))

  def __len__(self):
    return len(self.files)

  def __getitem__(self, index):
    file = Image.open(self.files[index])

    file = self.transform(file)  #tensor format
    bigger = max(file.size()[1], file.size()[2])
    file = transforms.CenterCrop(bigger)(file)

    file = self.infer_transform(file)

    return file, self.files[index]