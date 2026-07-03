# 머신러닝 핵심 흐름 & 문법 정리

> **전처리는 공통 → 모델/평가지표만 바뀜**

---

## 전체 흐름

```
데이터 로드
    ↓
EDA (탐색적 분석)
    ↓
결측치 처리 (Imputer)
    ↓
인코딩 (문자 → 숫자)
    ↓
피처 / 타겟 분리
    ↓
train / test 분리
    ↓
스케일링
    ↓
모델 선택 & 학습
    ↓
교차검증 + 튜닝 (GridSearchCV)
    ↓
평가
    ↓
모델 저장 (joblib)
```

---

## [1] 데이터 로드 & EDA

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt, koreanize_matplotlib
import seaborn as sns

df = pd.read_csv('data.csv')
```

| 함수 | 기능 |
|---|---|
| `df.shape` | 전체 행/열 수 반환 → 데이터 크기 파악 |
| `df.info()` | 컬럼명, 데이터 타입, 결측치 수 한눈에 확인 |
| `df.describe()` | 수치형 컬럼의 최소/최대/평균/표준편차 등 통계 요약 |
| `df.describe(include='all')` | 문자형 컬럼까지 포함해서 전체 통계 출력 |
| `df.isnull().sum()` | 컬럼별 결측치(NaN) 개수 반환 |
| `df['col'].value_counts()` | 해당 컬럼의 값별 빈도수 반환 (클래스 균형 확인용) |
| `df['col'].value_counts(normalize=True)` | 빈도수를 비율(0~1)로 반환 |

---

## [2] 결측치 처리

> NaN 값을 적절한 값으로 채워 모델이 학습할 수 있게 만드는 과정

```python
from sklearn.impute import SimpleImputer, KNNImputer
```

| 함수/클래스 | 기능 |
|---|---|
| `df['col'].fillna(값)` | 해당 컬럼의 NaN을 지정한 값으로 채움 |
| `SimpleImputer(strategy='mean')` | 평균/중앙값/최빈값/상수 중 하나로 NaN 채움 |
| `KNNImputer(n_neighbors=5)` | 가장 비슷한 K개 행의 값 평균으로 NaN 채움 |
| `.fit(x_train)` | train 데이터로 통계값(평균 등) 계산 |
| `.transform(x)` | 계산된 통계값으로 실제 NaN을 채움 |
| `.fit_transform(x)` | fit + transform 한 번에 실행 |

```python
# 방법 1 : 직접 채우기
df['col'] = df['col'].fillna(df['col'].mean())    # 평균
df['col'] = df['col'].fillna(df['col'].median())  # 중앙값
df['col'] = df['col'].fillna('N')                 # 문자형

# 방법 2 : SimpleImputer
imputer = SimpleImputer(strategy='mean')
imputer.fit(x_train)
x_train = imputer.transform(x_train)
x_test  = imputer.transform(x_test)   # test는 transform만!

# 방법 3 : KNNImputer
imputer = KNNImputer(n_neighbors=5)
x_train = imputer.fit_transform(x_train)
```

---

## [3] 인코딩 (문자 → 숫자)

> 머신러닝 모델은 문자열을 처리 못 함 → 전부 숫자로 변환 필요

```python
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, OneHotEncoder
```

| 클래스 | 대상 | 기능 |
|---|---|---|
| `LabelEncoder` | 타겟(정답) 컬럼 | 문자를 0, 1, 2... 정수로 순차 변환 (1D 입력) |
| `OrdinalEncoder` | 순서 있는 피처 | 순서를 보존해서 정수로 변환 (2D 입력) |
| `OneHotEncoder` | 순서 없는 피처 | 각 값을 별도 컬럼(0/1)으로 분리 (더미 변수) |
| `.fit(data)` | 어떤 값들이 있는지 목록 파악 |
| `.transform(data)` | 파악한 목록 기준으로 실제 변환 |
| `.inverse_transform(data)` | 숫자 → 원래 문자로 복원 (LabelEncoder) |

```python
# 타겟 컬럼 → LabelEncoder (1D)
le = LabelEncoder()
y_encoded = le.fit_transform(y)
le.inverse_transform(y_encoded)   # 숫자 → 원래 문자로 복원

# 순서 있는 피처 → OrdinalEncoder (2D)
oe = OrdinalEncoder()
x_train[['grade']] = oe.fit_transform(x_train[['grade']])

# 순서 없는 피처 → OneHotEncoder (2D)
ohe = OneHotEncoder(sparse_output=False)
ohe.fit_transform(x_train[['city']])
```

---

## [4] 피처 / 타겟 분리

> 모델에게 "이걸로 학습해" (피처) vs "이게 정답이야" (타겟) 구분

```python
feature = df[df.columns[1:]]   # 피처 (첫 번째 컬럼 제외)
target  = df[df.columns[0]]    # 타겟 (첫 번째 컬럼)

# 또는 컬럼명으로 직접 지정
feature = df.drop('Species', axis=1)   # Species 제외한 나머지
target  = df['Species']                # Species만
```

---

## [5] train / test 분리

> 모델을 학습시킬 데이터와 성능을 검증할 데이터를 분리

```python
from sklearn.model_selection import train_test_split
```

| 파라미터 | 기능 |
|---|---|
| `test_size=0.2` | 전체 데이터의 20%를 test로 사용 |
| `random_state=42` | 매번 같은 방식으로 분리 (재현성) |
| `stratify=target` | 클래스 비율을 유지하며 분리 (불균형 데이터 필수) |

```python
# 순서 주의: x_train, x_test, y_train, y_test
x_train, x_test, y_train, y_test = train_test_split(
    feature, target,
    test_size=0.2,
    random_state=42,
    stratify=target
)
```

---

## [6] 스케일링

> KNN처럼 거리 기반 모델은 값 크기 차이에 민감 → 범위 통일 필요

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
```

| 클래스 | 기능 |
|---|---|
| `StandardScaler` | 평균 0, 표준편차 1로 변환 (가장 일반적) |
| `MinMaxScaler` | 최솟값 0, 최댓값 1 사이로 변환 |
| `RobustScaler` | 중앙값 기준 변환 → 이상치 영향 적음 |
| `.fit(x_train)` | train 데이터로 평균/최대최소 등 계산 |
| `.transform(x)` | 계산된 기준으로 실제 변환 |
| `.fit_transform(x)` | fit + transform 한 번에 |

```python
scaler = StandardScaler()

scaler.fit(x_train)                        # train으로만 fit
x_train = scaler.transform(x_train)
x_test  = scaler.transform(x_test)        # test는 transform만!
```

> **핵심**: test에 fit 하면 → test 정보가 학습에 새어들어가는 **데이터 누수(leakage)** 발생

---

## [7] 다중 전처리 통합 (ColumnTransformer)

> 수치형/순서형/명목형 컬럼에 각각 다른 전처리를 한 번에 적용

```python
from sklearn.compose import ColumnTransformer
```

| 함수 | 기능 |
|---|---|
| `ColumnTransformer(transformers=[...])` | 각 컬럼 유형별 전처리기를 묶어서 한 번에 실행 |
| `transformers` | `(이름, 전처리기, 컬럼목록)` 튜플 리스트로 지정 |

```python
num_cols  = ['age', 'price']
sord_cols = ['grade']
str_cols  = ['city', 'gender']

preprocessing = ColumnTransformer(transformers=[
    ('ord', OrdinalEncoder(),  sord_cols),
    ('ohe', OneHotEncoder(),   str_cols),
    ('std', StandardScaler(),  num_cols),
])
```

---

## [8] Pipeline

> 전처리 → 모델 학습을 하나의 흐름으로 묶어 코드 간결화 + 데이터 누수 방지

```python
from sklearn.pipeline import Pipeline
```

| 함수/속성 | 기능 |
|---|---|
| `Pipeline(steps=[...])` | `(이름, 객체)` 순서대로 자동 실행되는 파이프라인 생성 |
| `.fit(x, y)` | 모든 단계를 순서대로 학습 |
| `.predict(x)` | 전처리 → 예측 자동 실행 |
| `.score(x, y)` | 전처리 → 예측 → 점수 계산 자동 실행 |
| `.named_steps['이름']` | 특정 단계의 객체 꺼내기 (ex. 트리 구조 시각화) |
| `단계이름__파라미터명` | GridSearchCV 파라미터 지정 형식 (더블 언더스코어) |

```python
pipe = Pipeline(steps=[
    ('scaler', StandardScaler()),
    ('model',  KNeighborsClassifier())
])

pipe.fit(x_train, y_train)
pipe.predict(x_test)
pipe.score(x_test, y_test)

# GridSearchCV 파라미터명: 단계이름__파라미터명
params = {'model__n_neighbors': [3, 5, 7]}
```

---

## [9] 교차검증 + 튜닝

> 데이터를 여러 번 나눠서 검증 → 더 신뢰성 있는 성능 측정 + 최적 파라미터 탐색

```python
from sklearn.model_selection import StratifiedKFold, KFold
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
```

| 클래스/속성 | 기능 |
|---|---|
| `StratifiedKFold` | 클래스 비율 유지하며 K개 폴드로 분할 (분류용) |
| `KFold` | 단순히 K개 폴드로 분할 (회귀용) |
| `GridSearchCV` | 지정한 모든 파라미터 조합을 전수 탐색 |
| `RandomizedSearchCV` | 전체 조합 중 n_iter개만 랜덤 샘플링 (빠름) |
| `n_splits` | 폴드 수 (보통 5) |
| `n_jobs=-1` | CPU 코어 전부 사용해서 병렬 처리 |
| `return_train_score=True` | train 점수도 같이 저장 (과적합 확인용) |
| `.best_params_` | 최적 파라미터 딕셔너리 반환 |
| `.best_score_` | 최고 교차검증 점수 반환 |
| `.best_estimator_` | 최적 파라미터로 학습된 모델 인스턴스 반환 |
| `.cv_results_` | 모든 조합의 상세 결과 딕셔너리 반환 |

```python
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

gs = GridSearchCV(pipe, param_grid=params, cv=skf,
                  return_train_score=True, n_jobs=-1)
gs.fit(x_train, y_train)

gs.best_params_
gs.best_score_
best_model = gs.best_estimator_

# 전체 결과 DataFrame으로 확인
cv_df = pd.DataFrame(gs.cv_results_)
```

---

## [10] 모델 종류

### 분류 (Classification) — 카테고리 예측

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
```

| 모델 | 기능 | 특징 |
|---|---|---|
| `KNeighborsClassifier` | 가장 가까운 K개 이웃의 다수결로 분류 | 단순, 느림, 스케일링 필수 |
| `SVC` | 클래스 경계선(초평면)을 최대 마진으로 분리 | 고차원에 강함, 느림 |
| `DecisionTreeClassifier` | 조건 분기(if/else)로 트리 구조 생성해 분류 | 해석 쉬움, 과적합 위험 |
| `RandomForestClassifier` | 여러 DecisionTree의 다수결 → 앙상블 | 안정적, 실무에서 많이 씀 |

```python
KNeighborsClassifier(n_neighbors=5, weights='uniform', p=2)
SVC(C=1.0, kernel='rbf', class_weight='balanced')
DecisionTreeClassifier(max_depth=5, min_samples_leaf=2, criterion='gini')
RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
```

### 회귀 (Regression) — 수치 예측

```python
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
```

| 모델 | 기능 | 특징 |
|---|---|---|
| `LinearRegression` | 피처와 타겟의 선형 관계를 수식으로 표현 | 가장 단순한 회귀 |
| `Ridge` | LinearRegression + L2 규제 (계수 크기 제한) | 과적합 방지 |
| `Lasso` | LinearRegression + L1 규제 (불필요 피처 계수 0으로) | 피처 선택 효과 |
| `KNeighborsRegressor` | K개 이웃 값의 평균으로 예측 | KNN의 회귀 버전 |
| `DecisionTreeRegressor` | 트리 구조로 수치 예측 | DecisionTree의 회귀 버전 |
| `RandomForestRegressor` | 여러 트리의 평균으로 예측 | 안정적, 실무에서 많이 씀 |

```python
LinearRegression()
Ridge(alpha=1.0)     # alpha 클수록 규제 강함
Lasso(alpha=1.0)
KNeighborsRegressor(n_neighbors=5)
DecisionTreeRegressor(max_depth=5)
RandomForestRegressor(n_estimators=100, random_state=42)
```

---

## [11] 평가 지표

### 분류 평가

```python
from sklearn.metrics import (accuracy_score, precision_score,
                              recall_score, f1_score,
                              confusion_matrix, classification_report)
```

| 함수 | 기능 |
|---|---|
| `accuracy_score` | 전체 예측 중 맞은 비율 (정확도) |
| `precision_score` | 양성으로 예측한 것 중 실제 양성 비율 (오탐 관련) |
| `recall_score` | 실제 양성 중 양성으로 예측한 비율 (미탐 관련) |
| `f1_score` | precision과 recall의 조화평균 (둘 다 고려) |
| `confusion_matrix` | 실제 vs 예측 교차표 (어디서 틀렸는지 확인) |
| `classification_report` | 클래스별 precision/recall/f1 한 번에 출력 |
| `zero_division=0` | 예측 샘플 없는 클래스 경고 제거 |
| `average='macro'` | 클래스별 점수 단순 평균 |
| `average='weighted'` | 샘플 수 비례 가중 평균 |

```python
print(classification_report(y_test, y_pred, zero_division=0))

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(pd.DataFrame(cm), annot=True, fmt='d', cmap='Blues')
```

### 회귀 평가

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
```

| 함수 | 기능 |
|---|---|
| `mean_squared_error` | 예측 오차를 제곱해서 평균 → 큰 오차에 민감 |
| `mean_absolute_error` | 예측 오차 절대값 평균 → 이상치에 덜 민감 |
| `r2_score` | 모델이 데이터 분산을 얼마나 설명하는지 (1이 최고) |

```python
mse  = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5        # 루트 MSE → 원래 단위와 동일해서 해석 쉬움
mae  = mean_absolute_error(y_test, y_pred)
r2   = r2_score(y_test, y_pred)

print(f'RMSE : {rmse:.4f}')
print(f'MAE  : {mae:.4f}')
print(f'R²   : {r2:.4f}')
```

---

## [12] 모델 저장 & 불러오기

```python
import joblib, os
```

| 함수 | 기능 |
|---|---|
| `joblib.dump(model, path)` | 학습된 모델을 파일(.pkl)로 저장 |
| `joblib.load(path)` | 저장된 모델 파일을 불러옴 |
| `os.makedirs(path, exist_ok=True)` | 폴더가 없으면 생성 (있어도 에러 안 남) |

```python
os.makedirs('../Models', exist_ok=True)
joblib.dump(best_model, '../Models/model.pkl')

model = joblib.load('../Models/model.pkl')
model.predict(new_data)   # 재학습 없이 바로 예측
```

---

## [13] 새 데이터 예측

```python
# DataFrame 형태로 만들어서 넣어야 함 (학습 때와 컬럼명 동일해야)
new_data = pd.DataFrame([[300, 30, 35, 12, 4.5]],
                        columns=['Weight','Length','Diagonal','Height','Width'])

pred = best_model.predict(new_data)

# 분류 → LabelEncoder로 원래 문자 복원
print(le.inverse_transform(pred)[0])

# 회귀 → 숫자 그대로 출력
print(f'예측값 : {pred[0]:.2f}')
```

---

## 분류 vs 회귀 한눈에 비교

| 항목 | 분류 | 회귀 |
|---|---|---|
| 출력 | 카테고리 (도미/빙어) | 숫자 (무게 1200g) |
| 모델 이름 | `Classifier` | `Regressor` |
| 교차검증 | `StratifiedKFold` | `KFold` |
| GridSearchCV scoring | 기본값 (accuracy) | `'neg_root_mean_squared_error'` |
| 평가지표 | Accuracy, F1 | RMSE, R² |
| 전처리/Pipeline/GridSearchCV | **동일** | **동일** |

---

## [14] DecisionTree 전용 (DAY07)

### 트리 구조 시각화

```python
from sklearn.tree import plot_tree

dt = best_model.named_steps['dtModel']   # Pipeline에서 DecisionTree 단계 꺼내기

plt.figure(figsize=(24, 10))
plot_tree(dt,
          feature_names=feature.columns.tolist(),   # 피처명
          class_names=le.classes_,                  # 클래스명 (분류만)
          filled=True,                              # 노드 색 채우기
          rounded=True,                             # 둥근 모서리
          fontsize=9)
plt.show()
```

### 피처 중요도 (Feature Importance)

> 어떤 피처가 분류/예측에 가장 많이 영향을 줬는지 확인

```python
importance = pd.Series(dt.feature_importances_,
                       index=feature.columns).sort_values(ascending=False)

sns.barplot(x=importance.values, y=importance.index)
plt.title('피처 중요도')
plt.show()
```

| 속성/함수 | 기능 |
|---|---|
| `.feature_importances_` | 각 피처의 중요도 배열 반환 (합계 = 1.0) |
| `named_steps['단계이름']` | Pipeline 내부 단계 객체 꺼내기 |

### 결정 경계 시각화 (Decision Boundary)

> 2개 피처 선택 → 전체 영역을 격자로 예측 → 색으로 경계 표시

```python
x2 = df[['Length', 'Height']].values
y2 = le.transform(df['Species'])

dt_2d = DecisionTreeClassifier(max_depth=5, random_state=42)
dt_2d.fit(x2, y2)

# 격자 생성 → 전체 영역 예측
x_min, x_max = x2[:, 0].min()-1, x2[:, 0].max()+1
y_min, y_max = x2[:, 1].min()-1, x2[:, 1].max()+1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.2),
                     np.arange(y_min, y_max, 0.2))
Z = dt_2d.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.4, cmap='Set3')      # 배경 색칠
plt.scatter(x2[:, 0], x2[:, 1], c=y2, cmap='Set1', edgecolors='k')
plt.show()
```

### DecisionTree 주요 파라미터

| 파라미터 | 기능 | 기본값 |
|---|---|---|
| `max_depth` | 트리 최대 깊이 (None=무제한 → 과적합 위험) | None |
| `min_samples_leaf` | 리프 노드 최소 샘플 수 (클수록 단순한 트리) | 1 |
| `criterion` | 분할 기준 (`'gini'` / `'entropy'` — 분류) | `'gini'` |
| `criterion` | 분할 기준 (`'squared_error'` / `'absolute_error'` — 회귀) | `'squared_error'` |

---

## [15] DAY08 추가 문법

### 특수 결측치 처리 (`?` 같은 경우)

> CSV에 NaN 대신 `?` 같은 문자로 결측치를 표현하는 경우

```python
# '?' 개수 확인
(df['stalk-root'] == '?').sum()

# 최빈값으로 대체
df['stalk-root'] = df['stalk-root'].replace('?', df['stalk-root'].mode()[0])
# mode()[0] : 최빈값 1개 반환 (mode()는 Series를 반환하므로 [0]으로 꺼냄)
```

### OrdinalEncoder — 미학습 값 처리

> test 데이터에 train에서 못 본 값이 들어와도 에러 없이 처리

```python
OrdinalEncoder(
    handle_unknown='use_encoded_value',   # 모르는 값 → 에러 대신 지정값으로
    unknown_value=-1                      # 모르는 값을 -1로 인코딩
)
```

### 식별자 컬럼 제거

> OrderID, UserID 같은 컬럼은 학습에 의미 없으므로 제거

```python
feature = df.drop(['OrderID', 'target'], axis=1)   # 여러 컬럼 동시 제거
```

### 상관계수로 피처 영향도 확인

```python
# 타겟과 각 피처의 상관계수 (1에 가까울수록 강한 양의 상관관계)
df.corr()['Delivery_Time_min'].sort_values(ascending=False)
```

### 회귀 GridSearchCV scoring

```python
# 회귀에서 RMSE 기준으로 최적화
gs = GridSearchCV(pipe, param_grid=params, cv=kf,
                  scoring='neg_root_mean_squared_error')   # 음수 RMSE

# best_score_는 음수로 반환 → 앞에 - 붙여서 양수로
print(f'최고 CV RMSE : {-gs.best_score_:.4f}')
```

> `neg_`가 붙은 이유 : sklearn은 점수가 클수록 좋은 방향으로 통일 → RMSE는 작을수록 좋으니 음수로 저장

### 실제 vs 예측 산점도 (회귀 시각화)

```python
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()], 'r--')   # 완벽한 예측선 (y=x)
plt.xlabel('실제값')
plt.ylabel('예측값')
plt.show()
# 점들이 빨간 대각선에 가까울수록 예측이 정확
```
