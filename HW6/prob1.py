#import the nescessary libs
import numpy as np
import torch

# Loading the Fashion-MNIST dataset
from torchvision import datasets, transforms

import time
import matplotlib.pyplot as plt

outs=[]
start = time.time()
# Get GPU Device
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

print(device)

# Define a transform to normalize the data
transform = transforms.Compose([transforms.ToTensor(),
                                    transforms.Normalize((0.5,), (0.5,))
                                                                   ])
# Download and load the training data
trainset = datasets.FashionMNIST('MNIST_data/', download = True, train = True, transform = transform)
testset = datasets.FashionMNIST('MNIST_data/', download = True, train = False, transform = transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size = 64, shuffle = True, num_workers=4)
testloader = torch.utils.data.DataLoader(testset, batch_size = 64, shuffle = True, num_workers=4)

# Examine a sample
dataiter = iter(trainloader)
images, labels = dataiter.next()

# Define the network architecture
from torch import nn, optim
import torch.nn.functional as F

model = nn.Sequential(nn.Linear(784, 128),
                      nn.ReLU(),
                      nn.Linear(128, 10),
                      nn.LogSoftmax(dim = 1)
                     )

model.to(device)

# Define the loss
criterion = nn.CrossEntropyLoss()

# Define the optimizer
optimizer = optim.Adam(model.parameters(), lr = 0.001)
# optimizer = optim.SGD(model.parameters(), lr = 0.001)

# Define the epochs
epochs = 5

train_losses, test_losses = [], []
t_start=time.time()
for e in range(epochs):
  running_loss = 0
  for images, labels in trainloader:
    # Flatten Fashion-MNIST images into a 784 long vector
    images = images.to(device)
    labels = labels.to(device)
    images = images.view(images.shape[0], -1)
    
    # Training pass
    optimizer.zero_grad()
    
    output = model.forward(images)
    loss = criterion(output, labels)
    loss.backward()
    optimizer.step()
    
    running_loss += loss.item()
  else:
    test_loss = 0
    accuracy = 0
    
    # Turn off gradients for validation, saves memory and computation
    with torch.no_grad():
      # Set the model to evaluation mode
      model.eval()
      
      # Validation pass
      for images, labels in testloader:
        images = images.to(device)
        labels = labels.to(device)
        images = images.view(images.shape[0], -1)
        ps = model(images)
        test_loss += criterion(ps, labels)
        top_p, top_class = ps.topk(1, dim = 1)
        equals = top_class == labels.view(*top_class.shape)
        accuracy += torch.mean(equals.type(torch.FloatTensor))

    # getting grads
    grads = np.array([x.grad for x in model.parameters()])
    sqr_grads = torch.square(grads[1])
    sum_grads = torch.sum(sqr_grads)
    print(sum_grads)
    outs.append(sum_grads)

    model.train()

    print("Epoch: {}/{}..".format(e+1, epochs),
          "Training loss: {:.3f}..".format(running_loss/len(trainloader)),
          "Test loss: {:.3f}..".format(test_loss/len(testloader)),
          "Test Accuracy: {:.3f}".format(accuracy/len(testloader)))
t_end=time.time()
end = time.time()
print(f"Total time: {end-start}\nTraining time: {t_end-t_start}")
plt.plot(outs)
plt.show()
