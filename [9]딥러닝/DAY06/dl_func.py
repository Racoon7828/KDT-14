## ==================================================================
## 딥러닝 학습에 관련된 함수들
## ------------------------------------------------------------------
## -> 학습 함수
## -> 검증 및 테스트 함수
## -> 예측 함수
## ==================================================================
## 모듈 로딩
import torch


## -> 학습 함수 -------------------------------------------------------
## -> 함수 기능 : 학습용 데이터셋으로 순전파/역전파 진행 함수
## -> 함수 이름 : training 
## -> 매개 변수 : MODEL          : 모델 인스턴스 
## ->            DATA_LODAER    : 데이터로더 인스턴스
## ->            LOSS_FN        : 손실함수 인스턴스
## ->            OPTIM          : 최적화 인스턴스
## ->            DATA_NUMS      : 데이터 수
## ->            DEVICE         : 모델 저장 위치 
## -> 함수 결과 : 에포크 단위의 손실, 정확도 반환 
## -> ----------------------------------------------------------------
def training(MODEL, DATA_LODAER, LOSS_FN, OPTIM, DATA_NUMS, DEVICE):
    ## 에포크 단위 손실, 정확도 저장
    loss_total, acc_total = [], []       

    ## 학습 모드 설정
    MODEL.train()      

    ## 배치크기 만큼 데이터 추출해서 학습 진행 
    for feature, target in DATA_LODAER:
        ## 피쳐와 타겟을 모델과 동일 위치 
        feature, target = feature.to(DEVICE), target.to(DEVICE)   

        ## 순전파 진행 : 모델변수명(피쳐)
        out=MODEL(feature)  
        
        ## 손실계산 및 W,b 업데이트
        OPTIM.zero_grad()                          ## 모델 W,b의 grad 속성 초기화
        loss = LOSS_FN(out, target.reshape(-1))    ## 예측-정답의 손실계산
        loss.backward()                            ## W,b의 새로운 값 계산
        OPTIM.step()                               ## W,b의 새로운 값 저장

        ## 정확도 계산
        pre = out.argmax(dim=1)                 ## 행 즉 샘플 단위로 확률이 가장 큰 클래스 추출 (BS,)

        ##- 예측 클래스/품종과 정답 품종 비교 (둘 다 1D (BS,)로 맞춰서 비교)
        acc = (pre == target.reshape(-1))

        ## 배치 단위의 손실값과 정답 동일한 개수 저장 => item() 원소값 추출 단, 원소1개만 존재 해야 함!!
        loss_total.append(loss.item())
        acc_total.append(acc.sum().item())

    ## 1 에포크 단위의 손실과 정답 계산 후 반환
    return sum(loss_total)/len(loss_total) , sum(acc_total)/DATA_NUMS



## -> 검증/테스트 함수 -------------------------------------------------------
## -> 함수 기능 : 모델 학습 진행 중 파라미터 즉, W와 b가 제대로 업데이트 되고
##               있는지 검사하는 용도 함수 
##               학습 중단 여부 결정/ 모델 저장 여부 결정
## -> 함수 이름 : evaluating 
## -> 매개 변수 : MODEL          : 모델 인스턴스 
## ->            DATA_LODAER    : 데이터로더 인스턴스
## ->            LOSS_FN        : 손실함수 인스턴스
## ->            DATA_NUMS      : 데이터 수
## ->            DEVICE         : 모델 저장 위치 
## -> 함수 결과 : 1에포크 대한 검증 실행 (손실, 정확도 반환)
## -> ----------------------------------------------------------------
def evaluating(MODEL, DATA_LODAER, LOSS_FN, DATA_NUMS, DEVICE):
    ## 에포크 단위 손실, 정확도 저장
    loss_total, acc_total = [], []       

    ## 검증/평가 모드 설정
    ## - 모델의 W,b 업데이트 진행 안됨! 역전파 진행 안됨! 
    MODEL.eval()      

    ## 배치크기 만큼 데이터 추출해서 학습 진행 
    ## W,b 파라미터 업데이트 기능 해제
    with torch.no_grad():
        for feature, target in DATA_LODAER:
            ## 모델과 동일한 저장 위치 설정
            feature, target = feature.to(DEVICE), target.to(DEVICE)  

            ## 모델 순전파 : 모델변수명(피쳐)
            out=MODEL(feature)  

            ## 손실계산 진행
            loss = LOSS_FN(out, target.reshape(-1))   ## 예측-정답의 손실계산 

            ## 정확도 계산
            pre = out.argmax(dim=1)                   ## 행 즉 샘플 단위로 확률이 가장 큰 클래스 추출 (BS,)

            ##- 예측 클래스/품종과 정답 품종 비교 (둘 다 1D (BS,)로 맞춰서 비교)
            acc = (pre == target.reshape(-1))

            ## 배치 단위의 손실값과 정답 동일한 개수 저장 => item() 원소값 추출 단, 원소1개만 존재 해야 함!!
            loss_total.append(loss.item())
            acc_total.append(acc.sum().item())

    ## 1 에포크 단위의 손실과 정답 계산 후 반환
    return sum(loss_total)/len(loss_total) , sum(acc_total)/DATA_NUMS


## -> 예측 함수 -------------------------------------------------------
## -> 함수 기능 : 모델 완성 후 사용을 위해 필요한 함수
## -> 함수 이름 : predict 
## -> 매개 변수 : single_feature : (torch.Tensor)  shape = [1, feature_dim] 
## ->            MODEL          : 학습완료된 모델 인스턴스 
## ->            DEVICE         : 모델 저장 위치 
## -> 함수 결과 : 단일 입력 텐서(1개의 샘플)에 대한 품종 이름 예측
## -> ----------------------------------------------------------------
def predict(single_feature, MODEL, DEVICE, label_map=None):
    ## 평가 모드로 전환
    MODEL.eval()  

    ## 예측 진행
    with torch.no_grad():
        ## 모델과 동일한 위치 설정
        single_feature = single_feature.to(DEVICE)   

        ## 모델에서 예측
        out = MODEL(single_feature)                  

        ## 예측값을 사용자 보기 좋게 
        pred_class = out.argmax(dim=1).item()        # 예측 클래스 인덱스 추출
                                                     # item() : 원소 1개 있는 텐서에서 원소 추출 
        return label_map[pred_class] if label_map else pred_class