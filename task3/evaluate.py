''' YOU CAN MODIFY EVERYTHING BELOW '''

import sys
import numpy as np

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import transforms, datasets

from copy import copy
from dataset import *
from Mobilenet import *
import warnings


def main(test_dir, result):
  num_test = len(os.listdir(test_dir))
  # num_test = 64

  ''' YOU SHOULD SUBMIT param.data FOR THE INFERENCE WITH TEST DATA'''
  model_ckpt = './param.data'

  t2 = transforms.Compose(
      [transforms.GaussianBlur(3), transforms.ColorJitter(brightness=(0.2, 2), contrast=(0.3, 2), saturation=(0.2, 2),
                                                          hue=(-0.3, 0.3)), transforms.ToTensor(),
       transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])

  dataset_test = test_dataset(root=test_dir, transform=t2)
  loader_test = DataLoader(dataset_test, batch_size=num_test,
                          shuffle=True, num_workers=8)

  # Define Model
  model = mobilenetv3_small()
  soft = nn.Softmax(dim=1)

  device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
  print("Current device:", device)

  if model_ckpt:
    state_dict = torch.load(model_ckpt)
    state_dict = {m.replace('module.', '') : i for m, i in state_dict.items()}
    model.load_state_dict(state_dict)

  correct_test = 0
  model.eval()
  with torch.no_grad():
    model = model.cuda()

    pred=[]
    fname=[]
    ans = {0 : "Paper", 1 : "Rock", 2 : "Scissors"}
    for batch, (data, filename) in enumerate(loader_test, 1):

      input_test = data.to(device)
      fname_test = filename
      # fname.append(filename)
      output_test = model(input_test)

      label_test_pred = soft(output_test).argmax(1)
      # print(label_test_pred)
      # pred.append(int(label_test_pred))
  ''' WRITE THE TEST SET PREDICTION RESULT. FOLLOW THE INSTRUCTION BELOW. '''
  # Print one prediction result in a line.
  # One prediction result should have the format as {filename, label_prediction}.
  # 'label_prediction' should ONLY contain 0 or 1 or 2 (NOT 0.0 or 1.0E-15).
  # 0: Paper, 1: Rock, 2: Scissors
  # See an example file provided in the eTL. Format is VERY IMPORTANT.

  label_test_pred = label_test_pred.cpu().numpy().tolist()

  f = open(result, "w")
  for i in range(len(fname_test)):
    f.write(fname_test[i] + ",")
    f.write(str(label_test_pred[i]) + "\n")
  f.close()
  print("Done.")

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

