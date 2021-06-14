### Task1: Traning the baseline model

----

#### [사용한 가상환경]

spds066 (conda virtual env)



#### [바뀐 부분]

dataloader

기존의 dataloader 대신 torch의 ImageFolder 클래스를 통해 불러왔음

그리고 torch의 transform에서 Grayscale, Resize를 사용하여 모델의 input의 크기를 맞추어줌. 

(Resize의 역할이 큰 것으로 보임)



#### [Argument]

epoch 15, batch size 40



#### [Result]

새로운 dataset인 tensorflow의 rps dataset으로 훈련을 진행

위와 같은 설정으로 모델을 훈련한 경우 대체적으로 90% 이상의 validation acc를 보임.

간혹 training이 아예 되지 않는 경우도 있는데 이 경우는 bad local minima에 빠진 것으로 보임.



#### [training result]

(torch) dhk1349@dhk1349:~/Desktop/1-1/rps/Baseline$ python3 main.py --epoch 15 --batchsize=40
Current device: cuda:1
.......model updated (epoch =  1 )
epoch: 0001 / 0015 | train loss: 1.10682 | train accuracy: 0.3262 | validation loss: 1.09835 | validation accuracy: 0.3333
.......model updated (epoch =  2 )
epoch: 0002 / 0015 | train loss: 0.93965 | train accuracy: 0.4794 | validation loss: 0.64971 | validation accuracy: 0.6075
.......model updated (epoch =  3 )
epoch: 0003 / 0015 | train loss: 0.34452 | train accuracy: 0.8194 | validation loss: 0.39044 | validation accuracy: 0.8925
.......model updated (epoch =  4 )
epoch: 0004 / 0015 | train loss: 0.05293 | train accuracy: 0.9798 | validation loss: 0.34781 | validation accuracy: 0.9194
epoch: 0005 / 0015 | train loss: 0.00150 | train accuracy: 1.0000 | validation loss: 0.42961 | validation accuracy: 0.9005
epoch: 0006 / 0015 | train loss: 0.00087 | train accuracy: 1.0000 | validation loss: 0.58173 | validation accuracy: 0.9032
epoch: 0007 / 0015 | train loss: 0.00013 | train accuracy: 1.0000 | validation loss: 0.60964 | validation accuracy: 0.8817
epoch: 0008 / 0015 | train loss: 0.00017 | train accuracy: 1.0000 | validation loss: 0.59037 | validation accuracy: 0.8978
epoch: 0009 / 0015 | train loss: 0.00010 | train accuracy: 1.0000 | validation loss: 0.63977 | validation accuracy: 0.8978
epoch: 0010 / 0015 | train loss: 0.00005 | train accuracy: 1.0000 | validation loss: 0.63772 | validation accuracy: 0.8978
epoch: 0011 / 0015 | train loss: 0.00006 | train accuracy: 1.0000 | validation loss: 0.79789 | validation accuracy: 0.8763
epoch: 0012 / 0015 | train loss: 0.00010 | train accuracy: 1.0000 | validation loss: 0.73282 | validation accuracy: 0.8790
epoch: 0013 / 0015 | train loss: 0.00003 | train accuracy: 1.0000 | validation loss: 0.75891 | validation accuracy: 0.8602
epoch: 0014 / 0015 | train loss: 0.00003 | train accuracy: 1.0000 | validation loss: 0.76209 | validation accuracy: 0.8790
epoch: 0015 / 0015 | train loss: 0.00003 | train accuracy: 1.0000 | validation loss: 0.72508 | validation accuracy: 0.8898
Model with the best validation accuracy is saved.
Best epoch:  3
Best validation accuracy:  0.91935486
Done.