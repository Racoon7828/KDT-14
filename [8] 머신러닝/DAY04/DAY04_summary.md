# DAY04 머신러닝 전처리 & KNN 실습 요약

> **우선순위** : ⭐⭐⭐ 필수 | ⭐⭐ 중요 | ⭐ 참고(개념만)

---

## ⭐⭐⭐ scalering | 스케일러 (특성 정규화)

KNN처럼 거리 기반 알고리즘은 특성 값의 크기/범위 차이에 민감 → 스케일링 필수

| 클래스 | 변환 방식 | 특징 | 중요도 |
|---|---|---|---|
| `StandardScaler` | 평균 0, 표준편차 1 | 가장 일반적, 정규분포 가정 | ⭐⭐⭐ |
| `MinMaxScaler` | 0 ~ 1 범위로 변환 | 범위가 고정되어야 할 때 | ⭐⭐⭐ |
| `RobustScaler` | 중앙값·IQR 기준 변환 | 이상치에 강함 | ⭐⭐ |
| `MaxAbsScaler` | 최대 절대값으로 나눔 | -1 ~ 1 범위, 희소 데이터에 적합 | ⭐ |

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, MaxAbsScaler

stdScaler = StandardScaler()
stdScaler.fit(data)               # 평균·분산 계산
scaled = stdScaler.transform(data)  # 변환
```

### train/test 데이터 분리 시 주의사항

```python
stdScaler.fit(x_train)                       # train 데이터로만 fit
scaled_x_train = stdScaler.transform(x_train)
scaled_x_test  = stdScaler.transform(x_test)  # test는 transform만
```

> **핵심**: test 데이터로 fit 하면 데이터 누수(leakage) 발생 → 반드시 train으로만 fit

---

## ⭐⭐⭐ encoding | 인코딩 (범주형 → 수치형 변환)

머신러닝 모델은 문자열을 직접 처리할 수 없으므로 숫자로 변환 필요

| 클래스 | 대상 | 특징 | 중요도 |
|---|---|---|---|
| `LabelEncoder` | 타겟(레이블) 컬럼 | 1D 입력, 정수로 순차 변환 | ⭐⭐⭐ |
| `OrdinalEncoder` | 순서 있는 문자 피처 | 2D 입력, 순서 보존 변환 | ⭐⭐⭐ |
| `OneHotEncoder` | 순서 없는 문자 피처 | 2D 입력, 컬럼 수 증가 (더미 변수) | ⭐⭐⭐ |

```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder

# LabelEncoder - 타겟 컬럼 (1D)
lblEncoder = LabelEncoder()
lblEncoder.fit(data['B_TYPE'])
encoded = lblEncoder.transform(data['B_TYPE'])

# OrdinalEncoder - 순서 있는 피처 (2D, ex: 등급 1<2<3)
odEncoder = OrdinalEncoder()
odEncoder.fit(data[['Grade']])
encoded = odEncoder.transform(data[['Grade']])

# OneHotEncoder - 순서 없는 피처 (2D, ex: 혈액형, 도시)
ohEncoder = OneHotEncoder(sparse_output=False)
ohEncoder.fit(data[['Blood']])
encoded = ohEncoder.transform(data[['Blood']])
```

### 선택 기준

```
문자형 피처
├── 순서 있음 (1등급<2등급<3등급) → OrdinalEncoder
└── 순서 없음 (서울/부산/대구, A/B/O형) → OneHotEncoder

타겟(정답) 컬럼 → LabelEncoder
```

---

## ⭐⭐⭐ bream_smelt_knn | KNN 분류 실습 (fish.csv)

**목표**: Bream(도미) vs Smelt(빙어) 이진 분류

### 데이터 로드 & 전처리

```python
# 필요한 컬럼 + 필요한 행만 로드
fishDF = pd.read_csv(DATA_FILE,
                     usecols=['Species', 'Weight', 'Length', 'Height'],
                     skiprows=range(36, 146))  # Bream(35행) + Smelt(14행)만

# 피처 / 타겟 분리
featureDF = fishDF[fishDF.columns[1:]]  # Weight, Length, Height
targetSR  = fishDF[fishDF.columns[0]]  # Species
```

### 시각화 (산점도로 분류 가능성 확인)

```python
cols = [['Length','Height'], ['Length','Weight'], ['Height','Weight']]
fig, axes = plt.subplots(1, 3, figsize=(16, 4))

for ax, (col1, col2) in zip(axes, cols):
    breamDF = fishDF[fishDF['Species'] == 'Bream']
    smeltDF = fishDF[fishDF['Species'] == 'Smelt']
    ax.scatter(breamDF[col1], breamDF[col2], label='Bream')
    ax.scatter(smeltDF[col1], smeltDF[col2], label='Smelt')
    ax.legend()
```

### GridSearchCV로 최적 K 탐색

```python
params   = {'n_neighbors': range(3, 30, 2)}
scv      = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
gsModel  = GridSearchCV(KNeighborsClassifier(), param_grid=params,
                        cv=scv, return_train_score=True)
gsModel.fit(x_train, y_train)

bestModel = gsModel.best_estimator_
print(gsModel.best_params_, gsModel.best_score_)
```

### ⭐ kneighbors() — 이웃 데이터 확인

```python
# 새 데이터의 K개 이웃 거리·인덱스 반환
distance, indices = bestModel.kneighbors(new_data)

# 이웃 데이터 확인
x_train2 = x_train.reset_index(drop=True)
print(x_train2.iloc[indices[0]])  # 첫 번째 예측 데이터의 이웃들
```

### 예측 결과 비교

```python
y_pre = bestModel.predict(x_test)

compareDF = pd.DataFrame(np.vstack([y_test, y_pre]), index=['정답','예측']).T
compareDF['맞음'] = compareDF['정답'] == compareDF['예측']

correct   = compareDF['맞음'].sum()
incorrect = compareDF.shape[0] - correct
print(f'정답: {correct}개, 오답: {incorrect}개')
```

---

## ⭐⭐ bream_smelt_knn_scale | 스케일링 적용 KNN

스케일링 없이 KNN 수행 → 단위가 큰 Weight(g)가 거리 계산 지배

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)  # train: fit + transform
x_test_scaled  = scaler.transform(x_test)        # test: transform만

gs_model = GridSearchCV(
    KNeighborsClassifier(),
    param_grid={'n_neighbors': range(1, 30, 2)},
    return_train_score=True,
    n_jobs=-1
)
gs_model.fit(x_train_scaled, y_train)
```

### K값 변화에 따른 성능 시각화

```python
res    = pd.DataFrame(gs_model.cv_results_)
sorted = res.sort_values(by=['param_n_neighbors'])

plt.plot(sorted['param_n_neighbors'], sorted['mean_test_score'],  label='Test')
plt.plot(sorted['param_n_neighbors'], sorted['mean_train_score'], label='Train')
plt.xlabel('n_neighbors (K)')
plt.ylabel('Score')
plt.legend()
plt.show()
```

---

## 전체 흐름 요약

```
데이터 로드 (필요 컬럼/행 선택)
    ↓
EDA - 산점도로 분류 가능성 시각화 확인
    ↓
피처 / 타겟 분리
    ↓
train / test 분리 (stratify=target)
    ↓
인코딩 (LabelEncoder / OrdinalEncoder / OneHotEncoder)
    ↓
스케일링 (fit은 train으로만, test는 transform만)
    ↓
GridSearchCV + StratifiedKFold → 최적 K 탐색
    ↓
bestModel.predict(x_test) → 예측 & 비교
    ↓
kneighbors() → 이웃 데이터 시각화
```

### 스케일링 적용 전후 비교

| | 스케일링 없음 | 스케일링 있음 |
|---|---|---|
| 문제 | Weight(g) 단위가 커서 거리 계산 왜곡 | 모든 피처 동등한 기여 |
| 결과 | 성능 낮을 수 있음 | 일반적으로 성능 향상 |
| 권장 | X | O (KNN 필수) |
