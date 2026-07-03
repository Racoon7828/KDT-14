# DAY01 머신러닝 이미지 분류 기초 요약

> **우선순위** : ⭐⭐⭐ 필수 | ⭐⭐ 중요 | ⭐ 참고(개념만)

---

## 전체 흐름

```
이미지 수집 (크롤링)
    ↓
ROI 추출 (관심 영역만 잘라내기)
    ↓
전처리 (resize → grayscale → flatten → 정규화)
    ↓
DataFrame으로 저장 (픽셀값 + 레이블)
    ↓
train/test 분리
    ↓
모델 학습 (KNN / SVC)
    ↓
평가 & 예측
```

---

## ⭐ 이미지 크롤링 (icrawler)

실무에서는 직접 데이터셋 구축 시 쓰지만, 보통 공개 데이터셋 사용

```python
from icrawler.builtin import BingImageCrawler

crawler = BingImageCrawler(storage={'root_dir': './apple'})
crawler.crawl(keyword='사과', max_num=50)
```

---

## ⭐ ROI 추출 (cv2)

이미지에서 관심 영역(배경 제거)만 잘라내기

```python
import cv2

img = cv2.imread('apple.jpg')
x, y, w, h = cv2.selectROI('SELECT', img)   # 마우스로 영역 선택
roi = img[y:y+h, x:x+w]
cv2.imwrite('roi.jpg', roi)
```

---

## ⭐⭐⭐ 이미지 전처리 (resize + grayscale + flatten)

```python
import cv2
import numpy as np

img = cv2.imread('apple.jpg', cv2.IMREAD_GRAYSCALE)  # 흑백으로 로드

# 크기 통일 (모든 이미지 동일 크기여야 학습 가능)
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)  # 50% 축소
img = cv2.resize(img, (100, 100))               # 100x100으로 통일

# 1D 벡터로 변환 (100x100 → 10000개 픽셀값)
flatten = img.flatten()
```

---

## ⭐⭐⭐ 정규화 (픽셀값 0~1 변환)

```python
x = x / 255.0   # 0~255 → 0.0~1.0
```

> 정규화 안 하면 픽셀값(0~255)이 너무 커서 거리 계산이 왜곡됨

---

## ⭐⭐⭐ 픽셀 데이터 → DataFrame 저장

```python
data_list = []
for target, label in zip(DATA_DIRS, DATA_LABEL):
    for filename in os.listdir(target):
        img = cv2.imread(f'{target}/{filename}', cv2.IMREAD_GRAYSCALE)
        flatten = img.flatten()
        row = flatten.tolist() + [label]  # 픽셀값 + 레이블
        data_list.append(row)

columns = [f'pixel{i}' for i in range(100*100)] + ['label']
df = pd.DataFrame(data_list, columns=columns)
df.to_csv('fruit_data.csv', index=False)
```

---

## ⭐⭐⭐ 학습 전체 코드

```python
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# 피처 / 타겟 분리
x = df.iloc[:, :-1].values / 255.0  # 정규화
y = df['label'].values

# train/test 분리
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)

# 모델 학습
kModel   = KNeighborsClassifier()
svcModel = SVC(kernel='linear')

kModel.fit(X_train, y_train)
svcModel.fit(X_train, y_train)

# 평가
print(kModel.score(X_train, y_train))   # train 점수
print(kModel.score(X_test, y_test))     # test 점수

# 예측
y_pred = kModel.predict(X_test)
```

---

## ⭐⭐⭐ 새 이미지 예측 (실전 활용)

```python
def convert_data(filepath):
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
    img = cv2.resize(img, (100,100))
    return img / 255.0   # 정규화

new_data = [convert_data(f).flatten() for f in ['apple.jpg', 'banana.jpg']]
y_pred = svcModel.predict(new_data)
```

> 예측 시 학습 때와 **동일한 전처리** 적용 필수

---

## 핵심 포인트

| 항목 | 내용 | 중요도 |
|---|---|---|
| 이미지 크기 통일 | 모든 이미지 동일 크기여야 학습 가능 | ⭐⭐⭐ |
| flatten | 2D 이미지 → 1D 벡터 (모델 입력 형태) | ⭐⭐⭐ |
| 정규화 | 0~255 → 0~1 (KNN 거리 계산 왜곡 방지) | ⭐⭐⭐ |
| stratify | 클래스 비율 유지하며 분리 | ⭐⭐⭐ |
| 예측 시 동일 전처리 | 학습과 동일한 resize, 정규화 적용 | ⭐⭐⭐ |
