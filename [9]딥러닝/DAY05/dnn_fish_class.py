## ===============================================
## 생선 무게 예측 관련 클래스들 
## -> 모   델 클래스 : WeightRegression
## -> 데이터셋 클래스 : WeightDataset
## ===============================================
## -----------------------------------------------
## 모듈 로딩
## -----------------------------------------------
## 공통
import torch

## 인공신경망 모델 관련
import torch.nn as nn 
import torch.nn.functional as F 

## 데이터셋 관련
from torch.utils.data import Dataset 


## -----------------------------------------------
## 모델 클래스 
## -----------------------------------------------
## 클래스이름 : WeightRegression
## 클래스역할 : 생선 무게 예측
## 모델층구조 :  층       입력        출력      연산여부     활성화함수 
##          입력층    피쳐 4개        4개         X           X      : 전달
##          은닉층      4개          3개     4개 * W + b    ReLU
##          출력층      3개          1개     3개 * W + b    선택
##                                                        학습종류 ->회귀/분류   
##                                                        손실함수
## 부모클래스 : torch.nn.Module
## 필수오버라이딩
##     _ _init_ _()
##     forward( )
## -----------------------------------------------
class WeightRegression(nn.Module):

    ## -------------------------
    ## 모델 층 구성 초기화 메서드
    ## -------------------------
    def __init__(self):
        super().__init__()
        self.hd1_layer = nn.Linear(4, 3)    ## 입력층 -> 은닉층1
        self.out_layer = nn.Linear(3, 1)    ## 은닉층1 -> 출력층

    ## ---------------------------------
    ## 순전파 메서드 : 회귀- 출력층 AF X
    ## ---------------------------------
    def forward(self, data):
        ## 입력층 data -> hd1_layer 은닉층 -> AF
        ## F.relu( data*W +b )   
        ao1 = F.relu(self.hd1_layer(data))    

        ## hd1_layer 은닉층 -> out_layer 출력층
        weightedSum = self.out_layer(ao1)

        return weightedSum


## -----------------------------------------------
## 데이터셋 클래스 
## -----------------------------------------------
## 클래스이름 : WeightDataset
## 클래스역할 : 피쳐와 타겟 데이터 관리/가독성/모듈화
## 부모클래스 : torch.utils.data.Dataset
## 필수오버라이딩
##     _ _init_ _()
##     _ _getitem_ _( )
##     _ _len_ _( )
## -----------------------------------------------
class WeightDataset(Dataset):

    ## --------------------------------
    ## ndarray타입의 피쳐와 타겟 전달 받음
    ## -> 4개 피쳐 스케일링 처리 
    ## --------------------------------
    def __init__(self, featureNP_, targetNP_):
        self.featureNP = featureNP_
        self.targetNP  = targetNP_
        self.length    = targetNP_.shape[0]

    ## --------------------------------
    ## 샘플 데이터 개수 반환 메서드 
    ## --------------------------------
    def __len__(self):
        return self.length 

    ## --------------------------------
    ## 특정 인덱스의 피쳐와 타겟 반환 메서드
    ## -> X, y 모두 1D 반환
    ## -> DataLoader에서 배치크기만큼 호출
    ## --------------------------------
    def __getitem__(self, index):
        # 피쳐 4개 
        X = torch.tensor(self.featureNP[index], dtype = torch.float32)
        # 회귀 모델 출력 shape이 [batch_size, 1]이므로 => 정답 y도 [1] 형태로 맞춤
        y = torch.tensor(self.targetNP[index], dtype=torch.float32).reshape(1)
        return X, y
        