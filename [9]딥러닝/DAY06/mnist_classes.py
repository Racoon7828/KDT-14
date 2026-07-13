# =============================================================
# MNIST 이미지 손글씨 숫자 분류 관련 사용자 클래스
# -> 모델 클래스    : MNISTDNNN< MNISTCNN
# -> 데이터셋 클래스 : MNISTDataset
# =============================================================
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset

class MnistDnn(nn.Module):
    def __init__(self):
        super().__init__()
        self.hd_layer1 = nn.Linear(784, 350)
        self.hd_layer2 = nn.Linear(350, 174)
        self.hd_layer3 = nn.Linear(174, 84)
        self.out_layer = nn.Linear(84, 10)

    def forward(self, data):
        out = F.relu(self.hd_layer1(data))
        out = F.relu(self.hd_layer2(out))
        out = F.relu(self.hd_layer3(out))
        return self.out_layer(out)

class MnistCnn(nn.Module):
    def __init__(self):
        super().__init__()
        # 특징 추출부
        # 입력 - 흑백 이미지 : 채널 1개
        # 출력 - 커널(5x5) 32개 -> 특징맵 32개
        # 패딩 - 사용안함 valid 또는 0
        self.conv1 = nn.Conv2d(1,32,5)
        self.pool1 = nn.MaxPool2d(2,2)
        self.conv2 = nn.Conv2d(32,64,5)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.flatten = nn.Flatten()

        # 학습부
        self.hd_layer1 = nn.Linear(64 * 4 * 4, 20)
        self.out_layer = nn.Linear(20, 10)

    def forward(self, data):
        # => 특징추출부 : data 입력층 -> conv1 -> relu -> pool1
        out = F.relu(self.conv1(data))
        out = self.pool1(out)
        out = F.relu(self.conv2(out))
        out = self.pool2(out)

        # => 4D 특징맵 --> 2D 특징맵 (BS, 특징값)
        out = self.flatten(out)

        # 학습부
        out = F.relu(self.hd_layer1(out))
        return self.out_layer(out)

class MnistDataset(Dataset):
    def __init__(self, feature, target, ndim=1):
        super().__init__()
        self.feature = feature.values # DF -> ndarray
        self.target = target.values # DF = ndarry
        self.length = len(feature)
        self.ndim = ndim

    # 샘플 수 반환 메서드
    def __len__(self):
        return self.length

    # 인덱스에 해당하는 피쳐와 타겟 텐서 반환 메서드
    def __getitem__(self, index):
        if self.ndim==1:
            feature = torch.tensor(self.feature[index], dtype=torch.float32)/255.
        else :
            feature = torch.tensor(self.data[index], dtype=torch.float32).reshape(-1,28,28)/255.
        target = torch.tensor(self.target[index], dtype=torch.long)
        return feature, target

# if __name__ =='__main__':
#     from torchinfo import layer_info

