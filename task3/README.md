## SPDS Final Project Instruction

2021-23144 한동훈



#### [환경설정]

```shell
$ conda create -n spds066 python=3.8

$ conda activate spds066
$ pip3 install -r requirements.txt
```

* Python version은 3.8을 사용하며, task1, 3을 실행하기 위해 필요한 라이브러리는 requirements.txt에 명시하였다. 



#### [Task1]

##### [Training & Validation Script]

```sh
$ cd task1
$ sbatch run.sh
```

* Test set accuracy는 대략적으로 90% 정도가 나온다. 

* Model parameter를 param.data로 저장하였다. 


##### [File Description]

>main.py: argument parser 및 main 함수
>
>train.py: 기본 모델 정의 및 모델 훈련 코드



#### [Task3]

##### [Training Script]

```shell
$ cd task3
$ sbatch run.sh
```



##### [Test Script]

```shell
$ cd task3
$ sbatch run_eval.sh

or

$ srun evaluate.py <testset path> <result file path>
```

* Validation accuracy는 대략 50-57%가 나오며 55% Validation accuracy가 나온 파라미터를 param.data로 저장하였습니다.



##### [File Descroption]

> dataset.py: Custum data loader를 정의
>
> evaluate.py: Test dataset prediction code
>
> main.py: argument parsing  및 main function 정의. 실행함수임
>
> Mobilenet.py: Mobile network의 pytorch implementation code
>
> train.py: Model training code

* Mobilenet small을 사용
* Validation data는 정사각형으로 padding 하고 gaussian blur등을 사용한 후 300x300(training set sample 크기)으로 Resize.
* 모든 input은 224로 crop하여 모델 input으로 사용



##### [Details]

* 처음에 rps training set + torch transforms augmentation 으로 model training을 한 후에
* 중간부터 rps training set에 Places2 dataset을 배경으로 섞은 뒤 torch transform augmentation을 하여 training
* Place2를 배경으로 섞는 코드는 dataset.py 내의 augmented_train class 내에 정의 되어있음