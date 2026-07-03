# DAY02 이미지 데이터 증강 (Data Augmentation) 요약

> **우선순위** : ⭐⭐⭐ 필수 | ⭐⭐ 중요 | ⭐ 참고(개념만)

---

## ⭐⭐⭐ 데이터 증강이란?

원본 이미지에 변형을 가해 학습 데이터 양을 늘리는 기법

- **언제 쓰나**: 학습 데이터가 적을 때 → 과적합 방지, 일반화 성능 향상
- **실전**: `albumentations`, `imgaug` 라이브러리도 많이 사용

---

## ⭐⭐ 기하학적 변환

| 함수 | 설명 | 중요도 |
|---|---|---|
| `cv2.flip(img, mode)` | 좌우/상하 반전 | ⭐⭐⭐ |
| `cv2.getRotationMatrix2D` + `warpAffine` | 회전 변환 | ⭐⭐ |
| `cv2.warpAffine` (이동행렬) | 이동(translate) | ⭐⭐ |
| 슬라이싱 + `cv2.resize` | 랜덤 크롭 | ⭐⭐ |

```python
import cv2
import numpy as np

# (1) 좌우/상하 반전
def flip_image(img, mode=1):
    return cv2.flip(img, mode)
    # mode: 1=좌우, 0=상하, -1=좌우+상하

# (2) 회전
def rotate_image(img, angle):
    h, w = img.shape[:2]
    M = cv2.getRotationMatrix2D((w//2, h//2), angle, 1.0)
    return cv2.warpAffine(img, M, (w, h))

# (3) 이동
def translate_image(img, tx, ty):
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    return cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

# (4) 랜덤 크롭
def random_crop(img, scale=0.8):
    h, w = img.shape[:2]
    new_h, new_w = int(h * scale), int(w * scale)
    y = np.random.randint(0, h - new_h)
    x = np.random.randint(0, w - new_w)
    return cv2.resize(img[y:y+new_h, x:x+new_w], (w, h))
```

---

## ⭐⭐ 픽셀값 변환

| 함수 | 설명 | 중요도 |
|---|---|---|
| `cv2.convertScaleAbs(img, alpha, beta)` | 밝기/대비 조절 | ⭐⭐ |
| `np.random.normal` + clip | 가우시안 노이즈 추가 | ⭐ |
| `cv2.GaussianBlur(img, (k,k), 0)` | 블러 처리 | ⭐ |

```python
# (1) 밝기/대비 조절
def adjust_brightness_contrast(img, brightness=0, contrast=1.0):
    return cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)
    # 결과 = 원본 * alpha + beta

# (2) 가우시안 노이즈
def add_gaussian_noise(img, sigma=20):
    noise = np.random.normal(0, sigma, img.shape).astype(np.int16)
    return np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)

# (3) 블러
def gaussian_blur(img, ksize=5):
    return cv2.GaussianBlur(img, (ksize, ksize), 0)
```

---

## ⭐⭐⭐ 증강 파이프라인 (원본 1장 → N장)

```python
def augment_image(img):
    result = img.copy()

    if np.random.rand() < 0.5:
        result = flip_image(result, 1)                          # 50% 확률 좌우반전

    angle = np.random.uniform(-20, 20)
    result = rotate_image(result, angle)                        # -20~20도 랜덤 회전

    result = adjust_brightness_contrast(result,
                brightness=np.random.randint(-30, 30),
                contrast=np.random.uniform(0.8, 1.2))          # 밝기/대비 랜덤 조절
    return result

# 원본 1장 → 8장 생성
augmented = [augment_image(imgNP) for _ in range(8)]
```

---

## ⭐⭐⭐ 폴더 단위 일괄 증강 (실전 활용)

```python
def augment_folder(src_dir, dst_dir, n_aug=5, exts=('.jpg','.jpeg','.png')):
    os.makedirs(dst_dir, exist_ok=True)
    for fname in os.listdir(src_dir):
        if not fname.lower().endswith(exts): continue
        img = cv2.imread(os.path.join(src_dir, fname))
        for i in range(n_aug):
            aug = augment_image(img)
            save_name = f'aug_{i}_{fname}'
            cv2.imwrite(os.path.join(dst_dir, save_name), aug)

# 사용 예시
augment_folder('../Data/Images/apple',  '../Data/AB_AUG/apple',  n_aug=4)
augment_folder('../Data/Images/banana', '../Data/AB_AUG/banana', n_aug=4)
```

---

## 핵심 포인트

| 항목 | 내용 | 중요도 |
|---|---|---|
| 증강 목적 | 데이터 부족 시 과적합 방지 | ⭐⭐⭐ |
| 적용 시점 | **train 데이터에만** 적용, test는 원본 그대로 | ⭐⭐⭐ |
| 파이프라인 | 여러 변환을 무작위 조합해서 다양성 확보 | ⭐⭐⭐ |
| 실전 라이브러리 | `albumentations` (더 빠르고 다양한 기법) | ⭐ |
