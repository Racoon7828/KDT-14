# =============================================================
# MNIST 이미지 손글씨 숫자 분류 관련 사용자 클래스
# -> 모델 클래스
# -> 데이터셋 클래스
# =============================================================
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset

class MnistClassifier(nn.Module):
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
    
class MnistDataset(Dataset):
    def __init__(self, feature, target):
        super().__init__()
        self.feature = feature.values # DF -> ndarray
        self.target = target.values # DF = ndarry
        self.length = len(feature)

    # 샘플 수 반환 메서드
    def __len__(self):
        return self.length

    # 인덱스에 해당하는 피쳐와 타겟 텐서 반환 메서드
    def __getitem__(self, index):
        feature = torch.FloatTensor(self.feature[index])
        target = torch.tensor(self.target[index], dtype=torch.long)
        return feature, target


