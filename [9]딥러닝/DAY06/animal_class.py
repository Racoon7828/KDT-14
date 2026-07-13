# =============================================================
# 동물 이미지 이진분류 관련 사용자 클래스
# -> 모델 클래스    : AnimalDnn, AnimalDnnReg, AnimalCnn, AnimalCnnReg
# -> 데이터셋 클래스 : AnimalDataset
# =============================================================
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset

# DNN 기본 모델
class AnimalDnn(nn.Module):
    def __init__(self):
        super().__init__()
        self.hd_layer1 = nn.Linear(4096, 512)
        self.hd_layer2 = nn.Linear(512, 128)
        self.out_layer = nn.Linear(128, 2)

    def forward(self, data):
        out = F.relu(self.hd_layer1(data))
        out = F.relu(self.hd_layer2(out))
        return self.out_layer(out)

# DNN + Dropout + BatchNorm
class AnimalDnnReg(nn.Module):
    def __init__(self):
        super().__init__()
        self.hd_layer1 = nn.Linear(4096, 512)
        self.bn1       = nn.BatchNorm1d(512)
        self.dropout1  = nn.Dropout(0.5)

        self.hd_layer2 = nn.Linear(512, 128)
        self.bn2       = nn.BatchNorm1d(128)
        self.dropout2  = nn.Dropout(0.3)

        self.out_layer = nn.Linear(128, 2)

    def forward(self, data):
        out = F.relu(self.bn1(self.hd_layer1(data)))
        out = self.dropout1(out)
        out = F.relu(self.bn2(self.hd_layer2(out)))
        out = self.dropout2(out)
        return self.out_layer(out)

# CNN 기본 모델
class AnimalCnn(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 16, 3, padding=1)
        self.pool1 = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.conv3 = nn.Conv2d(32, 64, 3, padding=1)
        self.pool3 = nn.MaxPool2d(2, 2)
        self.flatten = nn.Flatten()

        self.hd_layer = nn.Linear(64 * 8 * 8, 128)
        self.out_layer = nn.Linear(128, 2)

    def forward(self, data):
        out = self.pool1(F.relu(self.conv1(data)))
        out = self.pool2(F.relu(self.conv2(out)))
        out = self.pool3(F.relu(self.conv3(out)))
        out = self.flatten(out)
        out = F.relu(self.hd_layer(out))
        return self.out_layer(out)

# CNN + Dropout + BatchNorm
class AnimalCnnReg(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 16, 3, padding=1)
        self.bn1   = nn.BatchNorm2d(16)
        self.pool1 = nn.MaxPool2d(2, 2)

        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
        self.bn2   = nn.BatchNorm2d(32)
        self.pool2 = nn.MaxPool2d(2, 2)

        self.conv3 = nn.Conv2d(32, 64, 3, padding=1)
        self.bn3   = nn.BatchNorm2d(64)
        self.pool3 = nn.MaxPool2d(2, 2)

        self.flatten = nn.Flatten()
        self.dropout1 = nn.Dropout(0.5)
        self.hd_layer = nn.Linear(64 * 8 * 8, 128)
        self.dropout2 = nn.Dropout(0.3)
        self.out_layer = nn.Linear(128, 2)

    def forward(self, data):
        out = self.pool1(F.relu(self.bn1(self.conv1(data))))
        out = self.pool2(F.relu(self.bn2(self.conv2(out))))
        out = self.pool3(F.relu(self.bn3(self.conv3(out))))
        out = self.flatten(out)
        out = self.dropout1(out)
        out = F.relu(self.hd_layer(out))
        out = self.dropout2(out)
        return self.out_layer(out)

# 데이터셋 : ndim=1 DNN용 1D, ndim=2 CNN용 (1,64,64)
class AnimalDataset(Dataset):
    def __init__(self, feature, target, ndim=1):
        super().__init__()
        self.feature = feature.values if hasattr(feature, 'values') else feature
        self.target = target.values if hasattr(target, 'values') else target
        self.length = len(self.feature)
        self.ndim = ndim

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if self.ndim == 1:
            feature = torch.tensor(self.feature[index], dtype=torch.float32) / 255.
        else:
            feature = torch.tensor(self.feature[index], dtype=torch.float32).reshape(1, 64, 64) / 255.
        target = torch.tensor(self.target[index], dtype=torch.long)
        return feature, target
