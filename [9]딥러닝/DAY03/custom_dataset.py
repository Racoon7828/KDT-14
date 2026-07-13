from torch.utils.data import Dataset, TensorDataset
import pandas as pd, numpy as np, torch
import torch.nn as nn
import torch.nn.functional as F

# -----------------------------------------------
# 학습관련 클래스들 선언
# - 모델 클래스
# - 데이터셋 클래스
# -----------------------------------------------
# 데이터 : iris.csv
# 피 쳐 : 꽃받침 길이, 너비, 꽃잎 길이
# 타 겟 : 꽃잎 너비
# -----------------------------------------------
# 클래스 이름 : IrisDataset
# 부모 클래스 : Dataset
# 클래스 속성 : feature, target
# 클래스 기능 : 필수 오버라이딩 메서드
#              df __init__()
#              df __len__()
#              df __getitem__()
# -----------------------------------------------
class IrisDataset(Dataset):
    def __init__(self, feature, target):
        super().__init__()
        self.feature = feature.values # DF -> ndarray
        self.target = target.values # DF = ndarry
        self.cols = feature.columns # 컬럼이름 
        self.rows = feature.shape[0] # 샘플 수
    
    # 샘플 수 반환 메서드
    def __len__(self):
        return self.rows

    # 인덱스에 해당하는 피쳐와 타겟 텐서 반환 메서드
    def __getitem__(self, index):
        feature = torch.FloatTensor(self.feature[index])
        target = torch.FloatTensor(self.target[index])
        return feature, target

# -----------------------------------------------
# 데이터 : iris.csv
# 피 쳐 : 꽃받침 길이, 너비, 꽃잎 길이, 너비
# 타 겟 : 품종
# -----------------------------------------------
# 클래스 이름 : IrisClassifier
# 부모 클래스 : nn.Module
# 클래스 속성 : -
# 클래스 기능 : 필수 오버라이딩 메서드
#              df __init__()
#              df forward()
# 클래스 구성 : 층 | 입력 | 출력 | 활성화함수
#          입력층 | 4개 | 4개 | X : 그대로 은닉층 전달
#          은닉층 | 4개 | 퍼셉결과 3개 | ReLU
#          은닉층 | 3개 | 퍼셉결과 4개 | ReLU
#          출력층 | 4개 | 퍼셉결과 3개 | X : 희귀/분류, 손실함수 변경
# 분류 종류: 다중분류 -> softmax() -> 손실함수 내부처리
# -----------------------------------------------
class IrisClassifier(nn.Module):
    # 모델 층 구성 및 초기화 메서드
    def __init__(self):
        super().__init__()
        self.hd1_layer = nn.Linear(4,3)
        self.hd2_layer = nn.Linear(3,4)
        self.out_layer = nn.Linear(4,3)
    def forward(self, data):
        out = F.relu(self.hd1_layer(data))
        out = F.relu(self.hd2_layer(out))
        return self.out_layer(out)

# -----------------------------------------------
# 데이터 : mnist_train.csv, mnist_test.csv
# 피 쳐 : 픽셀 784개 (28x28)
# 타 겟 : 숫자 0~9 (10개 클래스)
# -----------------------------------------------
class MnistClassifier(nn.Module):
    def __init__(self, in_=784, out_=10):
        super().__init__()
        self.hd1_layer = nn.Linear(in_, 128)
        self.hd2_layer = nn.Linear(128, 64)
        self.out_layer = nn.Linear(64, out_)
    def forward(self, data):
        out = F.relu(self.hd1_layer(data))
        out = F.relu(self.hd2_layer(out))
        return self.out_layer(out)
