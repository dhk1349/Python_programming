import os
import numpy as np
import torch
import torch.nn as nn

from torch.utils.data import DataLoader
from torchvision import transforms, datasets

from copy import copy
from pyramidnet import PyramidNet
from Resnet import *

import warnings

warnings.filterwarnings('ignore')


def train(args):

  num_train = len(os.listdir(os.path.join(args.train_dir, 'paper/'))) + \
          len(os.listdir(os.path.join(args.train_dir,'rock/'))) + \
          len(os.listdir(os.path.join(args.train_dir, 'scissors')))
  
  num_val = len(os.listdir(os.path.join(args.val_dir, 'p/'))) + \
          len(os.listdir(os.path.join(args.val_dir, 'r/'))) + \
          len(os.listdir(os.path.join(args.val_dir, 's/')))

  # transform = transforms.Compose([transforms.Resize((256, 256)), transforms.RandomHorizontalFlip(p=0.5)
  #                                 , transforms.RandomVerticalFlip(p=0.5), transforms.ToTensor()])
  transform = transforms.Compose([transforms.Grayscale(3), transforms.Resize((224, 224)), transforms.RandomHorizontalFlip(), transforms.RandomVerticalFlip(),
                                  transforms.ToTensor(), transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])
  t2 = transforms.Compose([transforms.Grayscale(3), transforms.Resize((224, 224)), transforms.ToTensor(), transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])
  # transform = transforms.Compose([transforms.Grayscale(num_output_channels=1), transforms.Resize((89, 100)), transforms.ColorJitter(), transforms.RandomHorizontalFlip(p=0.5)
  #                                 , transforms.RandomVerticalFlip(p=0.5), transforms.ToTensor()])
  dataset_train = datasets.ImageFolder(root=args.train_dir, transform=transform)
  loader_train = DataLoader(dataset_train, batch_size=args.batchsize,
                            shuffle=True, num_workers=8)
  dataset_val = datasets.ImageFolder(root=args.val_dir, transform=t2)
  loader_val = DataLoader(dataset_val, batch_size=args.batchsize,
                          shuffle=True, num_workers=8)


  # Define Model
  # dataset_protoc = ["cifar10", "cifar100", "imagenet"]
  # alpha = [48, 64, 300]
  # depth = [164, 110, 200]
  # numclass = 3
  # bottleneck = [True, False, True]
  # model = PyramidNet(dataset_protoc[2], 18, 8, numclass, bottleneck[0])

  # Define Model
  model = nn.Sequential(nn.Conv2d(3, 32, 2, padding=1),
                        nn.ReLU(),
                        nn.MaxPool2d(kernel_size=2),
                        nn.Conv2d(32, 64, 2, padding=1),
                        nn.ReLU(),
                        nn.MaxPool2d(kernel_size=2),
                        nn.Conv2d(64, 128, 2, padding=1),
                        nn.ReLU(),
                        nn.MaxPool2d(kernel_size=2),
                        nn.Conv2d(128, 256, 2, padding=1),
                        nn.ReLU(),
                        nn.MaxPool2d(kernel_size=2),
                        nn.Conv2d(256, 256, 2, padding=1),
                        nn.ReLU(),
                        nn.MaxPool2d(kernel_size=2),
                        nn.Conv2d(256, 128, 2, padding=1),
                        nn.ReLU(),
                        nn.MaxPool2d(kernel_size=2),
                        nn.Conv2d(128, 64, 2, padding=0),
                        nn.ReLU(),
                        nn.MaxPool2d(kernel_size=1),
                        torch.nn.Flatten(),

                        nn.Linear(576, 1000, bias = True),
                        nn.Dropout(0.75),
                        nn.Linear(1000, 3, bias = True),
                       )

  soft = nn.Softmax(dim=1)

  # model = ResNet18()


  print('the number of model parameters: {}'.format(sum([p.data.nelement() for p in model.parameters()])))
  device = torch.device('cuda:1' if torch.cuda.is_available() else 'cpu')
  torch.cuda.set_device(device)
  print("Current device:", device)
  
  model.to(device)
  
  # Define the loss
  criterion = nn.CrossEntropyLoss().to(device)
  
  # Define the optimizer
  # optim = torch.optim.SGD(model.parameters(), lr = 0.001)
  optim = torch.optim.Adam(model.parameters(), lr = 0.001)
  #optim = torch.optim.SGD(model.parameters(), lr = 0.001, momentum=0.9)

  best_epoch = 0
  accuracy_save = np.array(0)
  for epoch in range(args.epochs):

    model.train()
    train_loss = []
    correct_train = 0
    correct_val = 0
    correct_batch = 0

    for batch, (data, label) in enumerate(loader_train, 1):
      # label = data['label'].to(device)
      # input = data['input'].to(device)
      label = label.to(device)
      input = data.to(device)

      output = model(input)
      # print(output.size())
      label_pred = soft(output).argmax(1)
  
      optim.zero_grad()
  
      loss = criterion(output, label)
      loss.backward()
  
      optim.step()
  
      correct_train += (label == label_pred).float().sum()

      # print(loss)
      try:
          train_loss += [loss.item()]
      except RuntimeError :
          print(f"{input.size()} raised CUDA illegal access" )
      # train_loss.append(loss.item())

    accuracy_train = correct_train / num_train
  
    correct_val = 0
    accuracy_tmp = np.array(0)
    with torch.no_grad():

      model.eval() 
      val_loss = []
      for batch, (data, label) in enumerate(loader_val, 1):
        label_val = label.to(device)
        input_val = data.to(device)
        # label_val = data['label'].to(device)
        # input_val = data['input'].to(device)

        output_val = model(input_val)
  
        label_val_pred = soft(output_val).argmax(1)
  
        correct_val += (label_val == label_val_pred).float().sum()
  
        loss = criterion(output_val, label_val)
        # val_loss += [loss.item()]
        val_loss.append(loss.item())

      accuracy_val = correct_val / num_val
  
      # Save the best model wrt val accuracy
      accuracy_tmp = accuracy_val.cpu().numpy()
      if accuracy_save < accuracy_tmp:
        best_epoch = epoch
        accuracy_save = accuracy_tmp.copy()
        torch.save(model.state_dict(), 'param.data')
        print(".......model updated (epoch = ", epoch+1, ")")
        
    print("epoch: %04d / %04d | train loss: %.5f | train accuracy: %.4f | validation loss: %.5f | validation accuracy: %.4f" %
          (epoch+1, args.epochs, np.mean(train_loss), accuracy_train, np.mean(val_loss), accuracy_val))

  print("Model with the best validation accuracy is saved.")
  print("Best epoch: ", best_epoch)
  print("Best validation accuracy: ", accuracy_save)
  print("Done.")
    
