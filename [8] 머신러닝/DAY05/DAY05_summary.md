# DAY05 머신러닝 전처리 & 성능평가 요약

> **우선순위** : ⭐⭐⭐ 필수 | ⭐⭐ 중요 | ⭐ 참고(개념만)

---

## ⭐⭐⭐ ex01 | 결측치 처리 (Imputer)

결측치(`NaN`)를 통계값 또는 알고리즘으로 채우는 방법

| 클래스 | 방식 | 특징 | 중요도 |
|---|---|---|---|
| `SimpleImputer` | 평균·중앙값·최빈값·상수 | 가장 단순, 빠름 | ⭐⭐⭐ |
| `KNNImputer` | KNN 알고리즘으로 가까운 K개 이웃값 평균 | 데이터 패턴 반영 | ⭐⭐ |
| `IterativeImputer` | 다른 컬럼을 예측 변수로 반복 추정 | 가장 정교, 느림 | ⭐ |

```python
from sklearn.impute import SimpleImputer, KNNImputer, IterativeImputer

simImputer = SimpleImputer()           # 기본값: 평균
simImputer.fit(X)
simImputer.transform(X)

kImputer = KNNImputer(n_neighbors=2)
kImputer.fit_transform(X)
```

> `fit()` → 통계값 계산  
> `transform()` → 결측치 채움  
> **train 데이터로 fit(), test 데이터는 transform()만**

---

## ⭐⭐ ex02 | 불균형 데이터 처리 (Imbalanced Data)

클래스 간 샘플 수 차이가 클 때 모델이 다수 클래스에 편향되는 문제 해결

| 방법 | 설명 | 장단점 | 중요도 |
|---|---|---|---|
| **UpSampling** | 소수 클래스 복원 샘플링으로 늘림 | 과적합 위험 | ⭐ |
| **DownSampling** | 다수 클래스 비복원 샘플링으로 줄임 | 정보 손실 | ⭐ |
| **SMOTE** | 소수 클래스 합성 데이터 생성 | 새로운 데이터 생성, 가장 권장 | ⭐⭐⭐ |
| **class_weight** | 모델 파라미터로 소수 클래스에 가중치 부여 | 데이터 변경 없이 적용 | ⭐⭐⭐ |

```python
from sklearn.utils import resample
from imblearn.over_sampling import SMOTE

# UpSampling
minorUpDF = resample(minorDF, replace=True, n_samples=len(majorDF), random_state=10)

# DownSampling
majorDownDF = resample(majorDF, replace=False, n_samples=len(minorDF), random_state=10)

# SMOTE (train 데이터에만 적용!)
smote = SMOTE()
X_train_up, y_train_up = smote.fit_resample(X_train, y_train)

# class_weight
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(class_weight='balanced')
```

> **핵심 원칙**: 샘플링은 train 데이터에만 → test는 그대로 유지

---

## ⭐⭐⭐ ex03 | ColumnTransformer (다중 전처리 통합)

컬럼 유형별로 다른 전처리를 한 번에 적용

| 컬럼 유형 | 전처리 방법 | 중요도 |
|---|---|---|
| 수치형 (age, visit_count, avg_price) | `StandardScaler` | ⭐⭐⭐ |
| 순서형 문자 (grade) | `OrdinalEncoder` | ⭐⭐⭐ |
| 명목형 문자 (city, gender) | `OneHotEncoder` | ⭐⭐⭐ |

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, OneHotEncoder

preprocessing = ColumnTransformer(transformers=[
    ('ordEncoder', OrdinalEncoder(),          sord_cols),  # 순서형
    ('ohEncoder',  OneHotEncoder(),           str_cols),   # 명목형
    ('stdScaler',  StandardScaler(),          num_cols),   # 수치형
])

preprocessing.fit(X_train, y_train)
X_train_trans = preprocessing.transform(X_train)
X_test_trans  = preprocessing.transform(X_test)   # fit은 train으로만
```

> **주의**: 변환 후 컬럼 순서가 바뀌므로 `output_indices_`로 확인

---

## ⭐⭐⭐ ex04 | Pipeline (파이프라인)

전처리 + 학습을 하나의 흐름으로 연결 → 코드 간결화, 데이터 누수 방지

```python
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, cross_validate

# Pipeline 구성: 전처리 → 모델
pipe = Pipeline(steps=[
    ('preprocessing', preprocessing),
    ('kModel', KNeighborsClassifier())
])

# 학습 & 평가
pipe.fit(X_train, y_train)
pipe.score(X_test, y_test)

# 교차검증
scores = cross_validate(pipe, X_train, y_train, cv=skf, scoring='accuracy')

# 하이퍼파라미터 튜닝 (파라미터명: 모델이름__파라미터명)
params = {
    'kModel__n_neighbors': [3, 5, 7],
    'kModel__weights': ['uniform', 'distance']
}
gsSearch = GridSearchCV(pipe, param_grid=params, cv=skf)
gsSearch.fit(X_train, y_train)
```

### 모델 저장 & 불러오기
```python
import joblib

joblib.dump(bestModel, 'model.pkl')   # 저장
model = joblib.load('model.pkl')      # 불러오기
y_pred = model.predict(new_data)      # 재학습 없이 바로 예측
```

---

## ⭐⭐⭐ ex05 | 분류 성능 지표 (Metrics)

### 주요 지표

| 지표 | 설명 | 공식 | 중요도 |
|---|---|---|---|
| **Accuracy** | 전체 중 맞게 예측한 비율 | (TP+TN) / 전체 | ⭐⭐⭐ |
| **Precision** | 양성 예측 중 실제 양성 비율 | TP / (TP+FP) | ⭐⭐⭐ |
| **Recall** | 실제 양성 중 양성으로 예측한 비율 | TP / (TP+FN) | ⭐⭐⭐ |
| **F1-score** | Precision과 Recall의 조화평균 | 2 × P×R / (P+R) | ⭐⭐⭐ |
| **Confusion Matrix** | 예측/실제 교차표 | - | ⭐⭐⭐ |
| **classification_report** | 클래스별 지표 한 번에 출력 | - | ⭐⭐⭐ |

> 불균형 데이터 → Accuracy만 보면 안 됨, **Precision/Recall/F1 함께 확인**

### average 옵션 (다중 분류)
- `macro`: 클래스별 점수 단순 평균 (클래스 불균형 무시)
- `weighted`: 클래스 샘플 수 비례 가중 평균

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix, classification_report

accuracy  = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')
recall    = recall_score(y_test, y_pred, average='macro')
f1        = f1_score(y_test, y_pred, average='macro')
```

### Confusion Matrix (혼동행렬)
```python
import seaborn as sns

cm = confusion_matrix(y_test, y_pred)
cmDF = pd.DataFrame(cm, index=target_names, columns=target_names)

sns.heatmap(cmDF, annot=True, fmt='d', cmap='Blues')
```
- 행: 실제 클래스 / 열: 예측 클래스
- 대각선: 맞게 예측 / 비대각선: 틀리게 예측

### Classification Report
```python
print(classification_report(y_test, y_pred, target_names=target_names))
```
클래스별 Precision, Recall, F1-score, Support를 한 번에 출력

---

## 전체 흐름 요약

```
데이터 로드
    ↓
결측치 처리 (Imputer)
    ↓
불균형 처리 (SMOTE / class_weight)
    ↓
전처리 (ColumnTransformer: 스케일링 + 인코딩)
    ↓
Pipeline 구성 (전처리 + 모델)
    ↓
GridSearchCV / cross_validate (튜닝 + 교차검증)
    ↓
성능 평가 (Accuracy, Precision, Recall, F1, Confusion Matrix)
    ↓
모델 저장 (joblib)
```
