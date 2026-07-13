## ==================================================================
## 딥러닝 - 회귀 학습 관련 함수들
## -> 학습 함수             : training_regression()
## -> 검증 및 테스트 함수    : evaluating_regression()
## -> 예측 함수             : predict_regression()
## ==================================================================
## 학습관련 모듈들
import torch
import numpy as np

## 성능지표 관련 모듈
from sklearn.metrics import mean_squared_error, r2_score


## -------------------------------------------------------
## -> 함수 기능 : 학습용 데이터셋으로 순전파/역전파 진행 함수
## -> 함수 이름 : training_regression 
## -> 매개 변수 : model          : 모델 인스턴스 
## ->            dataloader     : 데이터로더 인스턴스
## ->            loss_fn        : 손실함수 인스턴스
## ->            optimizer      : 최적화 인스턴스
## ->            device         : 모델 저장 위치 
## -> 함수 결과 : 에포크 단위의 LOSS, MSE, RMSE, R2 반환 
## -------------------------------------------------------
def training_regression(model, dataloader, loss_fn, optimizer, device):
    ## 에포크 단위 손실, 예측, 정답  저장
    loss_list, pred_list, target_list = [], [], []

    ## 학습 모드
    model.train()

    ## 배치 단위 학습
    for feature, target in dataloader:
        ## feature, target을 모델과 같은 장치로 이동
        feature, target = feature.to(device), target.to(device)

        ## 순전파
        out = model(feature)

        ## target shape 맞추기
        if out.shape != target.shape:  
            target = target.reshape(out.shape)

        ## 손실 계산
        loss = loss_fn(out, target)

        ## 기존 기울기 초기화
        optimizer.zero_grad()

        ## 역전파
        loss.backward()

        ## 가중치, 절편 업데이트
        optimizer.step()

        ## 배치 손실 누적
        ## loss.item()은 배치 평균 손실 
        ## 배치 크기를 곱해서 전체 손실 합산
        loss_list.append(loss.item() * feature.shape[0])

        ## 배치 단위 예측, 정답 저장  
        ## Scikit-learn의 성능지표 계산을 위해 CPU로 이동 후 numpy 변환
        pred_list.append(out.cpu().detach().numpy())
        target_list.append(target.cpu().detach().numpy())

    ## 평균 Loss
    avg_loss  = sum(loss_list) / len(loss_list)

    ## 전체 배치 결과 합치기
    pred_np   = np.concatenate(pred_list, axis=0)
    target_np = np.concatenate(target_list, axis=0)

    ## 성능지표 계산
    mse  = mean_squared_error(target_np, pred_np)
    rmse = np.sqrt(mse)
    r2   = r2_score(target_np, pred_np)

    return avg_loss, mse, rmse, r2
    

## -------------------------------------------------------
## -> 함수 기능 : 검증용 데이터셋으로 순전파 진행 함수
## -> 함수 이름 : evaluating_regression 
## -> 매개 변수 : model          : 모델 인스턴스 
## ->            dataloader    : 데이터로더 인스턴스
## ->            loss_fn        : 손실함수 인스턴스
## ->            device         : 모델 저장 위치 
## -> 함수 결과 : 에포크 단위의 Loss, RMSE, MAE, R2 반환 
## -------------------------------------------------------
def evaluating_regression(model, dataloader, loss_fn, device):

    ## 에포크 단위 손실 저장
    loss_list, pred_list, target_list = [], [], []

    ## 검증 모드
    model.eval()

    ## 검증 진행
    with torch.no_grad():
        ## 배치 크기로 데이터와 타겟 추출
        for feature, target in dataloader:
            ## 모델과 동일 위치 
            feature, target = feature.to(device),  target.to(device)

            ## 예측
            out = model(feature)

            ## shape 맞추기
            if out.shape != target.shape:
                target = target.reshape(out.shape)

            ## 손실 계산
            loss = loss_fn(out, target)

            ## 배치 손실 누적
            ## loss.item()은 배치 평균 손실 
            ## 배치 크기를 곱해서 전체 손실 합산
            loss_list.append(loss.item() * feature.shape[0])

            # 성능지표 계산을 위해 CPU로 이동 후 numpy 변환
            pred_list.append(out.cpu().detach().numpy())
            target_list.append(target.cpu().detach().numpy())

    ## 평균 Loss
    avg_loss      = sum(loss_list) / len(loss_list)

    ## 전체 배치 결과 합치기
    pred_np   = np.concatenate(pred_list, axis=0)
    target_np = np.concatenate(target_list, axis=0)

    ## 성능지표 계산
    mse  = mean_squared_error(target_np, pred_np)
    rmse = np.sqrt(mse)
    r2   = r2_score(target_np, pred_np)

    return avg_loss, mse, rmse, r2

## -> 예측 함수 -------------------------------------------------------
## -> 함수 기능 : 값을 예측 후 반환 함수
## -> 함수 이름 : predict_regression 
## -> 매개 변수 : single_feature : 스케일링 완료된 피쳐 Tensor. shape = [1, feature개수]
## ->            model          : 학습완료된 모델 인스턴스 
## ->            t_scaler       : 타겟 스케일러
## ->            device         : 모델 저장 위치 
## -> 함수 결과 : 단일 입력 텐서(1개의 샘플)에 대한 값 예측 반환
## -> ----------------------------------------------------------------
def predict_regression(single_feature, model, t_scaler, device):

    ## 평가 모드로 전환
    model.eval()  

    ## 예측 진행
    with torch.no_grad():
        ## 모델과 동일한 위치 설정
        single_feature = single_feature.to(device)   

        ## 모델에서 예측
        pre_tn = model(single_feature)                  

        # Tensor -> numpy 2D 배열 변환
        pred_np = pre_tn.cpu().numpy()

        # 원래 무게 단위로 복원
        pred_weight = t_scaler.inverse_transform(pred_np)

    return pred_weight
