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

##### [Training & Validation Code]

```sh
$ cd task1
$ sbatch run.sh
```

* Test set accuracy는 대략적으로 90% 이상이 나온다. 

* Model parameter를 param.data로 저장하였다. 



#### [Task3]

##### [Training Code]

```shell
$ cd task3
$ sbatch run.sh
```



##### [Test Script]

```shell
$ cd task3
$ sbatch run_eval.sh

or

$ python3 evaluate.py <testset path> <result file path>
```

* Validation accuracy는 대략 50-57%가 나오며 55% Validation accuracy가 나온 파라미터를 param.data로 저장하였습니다.