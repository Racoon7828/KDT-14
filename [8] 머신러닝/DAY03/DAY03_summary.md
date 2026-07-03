# DAY03 교차검증 & 하이퍼파라미터 튜닝 요약

> **우선순위** : ⭐⭐⭐ 필수 | ⭐⭐ 중요 | ⭐ 참고(개념만)

---

## ⭐⭐⭐ 교차검증 (Cross Validation)

train 데이터를 여러 번 나눠서 검증 → 모델 성능을 더 신뢰성 있게 측정

```python
from sklearn.model_selection import cross_val_score, cross_validate, StratifiedKFold

k_model = KNeighborsClassifier()

# cross_val_score : 검증 점수만 반환
val_scores = cross_val_score(k_model, x_train, y_train, cv=5)
print(f'평균: {val_scores.mean():.4f}')

# cross_validate : 학습/검증 점수 모두 반환
all_scores = cross_validate(k_model, x_train, y_train, return_train_score=True)
scoreDF = pd.DataFrame(all_scores)
scoreDF['GAP'] = abs(scoreDF['train_score'] - scoreDF['test_score'])
```

> GAP이 작을수록 과적합 없이 안정적인 모델

---

## ⭐⭐⭐ StratifiedKFold

클래스 비율을 유지하면서 K개 폴드로 분할 (불균형 데이터에 특히 중요)

```python
skFold = StratifiedKFold(n_splits=5, shuffle=True, random_state=10)
```

| 파라미터 | 설명 | 중요도 |
|---|---|---|
| `n_splits` | 폴드 수 (보통 5) | ⭐⭐⭐ |
| `shuffle=True` | 분할 전 데이터 섞기 | ⭐⭐⭐ |
| `random_state` | 재현성 시드 | ⭐⭐⭐ |

---

## ⭐⭐ K값 탐색 & 시각화

```python
totalDict = {'K': [], 'train_score': [], 'test_score': []}

for k in range(1, 50, 2):
    k_model = KNeighborsClassifier(n_neighbors=k)
    res = cross_validate(k_model, x_train, y_train, return_train_score=True)
    totalDict['K'].append(k)
    totalDict['train_score'].append(res['train_score'].mean())
    totalDict['test_score'].append(res['test_score'].mean())

totalDF = pd.DataFrame(totalDict)
totalDF['Abs_Gap'] = abs(totalDF['train_score'] - totalDF['test_score'])

# 최적 K: test_score 높고, GAP 작은 것
sortDF = totalDF.sort_values(by=['test_score', 'Abs_Gap'], ascending=[False, True])
best_k     = sortDF.iloc[0]['K']
best_score = sortDF.iloc[0]['test_score']

# 시각화
plt.plot(totalDF['K'], totalDF['train_score'], label='TRAIN')
plt.plot(totalDF['K'], totalDF['test_score'],  label='TEST')
plt.vlines(best_k, totalDF['train_score'].min(), totalDF['train_score'].max(),
           colors='red', linestyles='dotted')
plt.text(best_k, best_score + 0.02, f' Best K = {int(best_k)}', c='red')
plt.legend(); plt.grid(); plt.show()
```

---

## ⭐⭐⭐ GridSearchCV (전수 탐색)

지정한 모든 파라미터 조합을 탐색 → 최적 조합 반환

```python
from sklearn.model_selection import GridSearchCV

param_dict = {
    'n_neighbors': range(1, 51, 2),
    'p': [1, 2],
    'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute']
}

gs_model = GridSearchCV(
    KNeighborsClassifier(),
    param_grid=param_dict,
    cv=skFold,
    return_train_score=True,
    n_jobs=-1               # 병렬 처리
)
gs_model.fit(x_train, y_train)

print(gs_model.best_params_)   # 최적 파라미터
print(gs_model.best_score_)    # 최고 교차검증 점수
gs_best = gs_model.best_estimator_  # 최적 모델 인스턴스

cv_resultDF = pd.DataFrame(gs_model.cv_results_)  # 전체 결과
```

---

## ⭐⭐ RandomizedSearchCV (랜덤 탐색)

전체 조합 중 n_iter개만 랜덤 샘플링 → GridSearchCV보다 빠름

```python
from sklearn.model_selection import RandomizedSearchCV

rs_model = RandomizedSearchCV(
    KNeighborsClassifier(),
    param_distributions=param_dict,
    n_iter=50,              # 전체 중 50개만 탐색
    cv=skFold,
    random_state=10,
    return_train_score=True,
    n_jobs=-1
)
rs_model.fit(x_train, y_train)

rs_best = rs_model.best_estimator_
```

> 전체 조합 수 = n_iter면 GridSearchCV와 동일 → n_iter는 전체보다 작게

---

## ⭐⭐⭐ 학습 후 예측 & 평가

```python
# 테스트 데이터로 예측
y_pred = gs_best.predict(x_test)

# 정답/오답 집계
correct   = (y_pred == y_test).sum()
incorrect = len(y_test) - correct
print(f'정답: {correct}개, 오답: {incorrect}개')

# 정확도
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred))
```

---

## GridSearchCV vs RandomizedSearchCV 비교

| | GridSearchCV | RandomizedSearchCV | 중요도 |
|---|---|---|---|
| 탐색 방식 | 전수 탐색 | 랜덤 샘플링 | ⭐⭐⭐ |
| 속도 | 느림 | 빠름 | ⭐⭐⭐ |
| 최적값 보장 | O | X (확률적) | ⭐⭐ |
| 언제 쓰나 | 조합 수 적을 때 | 조합 수 많을 때 | ⭐⭐⭐ |

---

## 전체 흐름

```
데이터 로드 & 전처리
    ↓
train / test 분리 (stratify=target)
    ↓
StratifiedKFold 설정
    ↓
GridSearchCV or RandomizedSearchCV
    → 파라미터 조합별 교차검증
    → best_params_, best_estimator_ 추출
    ↓
best_estimator_.predict(x_test) → 평가
```
