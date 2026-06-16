import matplotlib.pyplot as plt
import matplotlib.cm as cm
import koreanize_matplotlib
import cv2

# 매개변수 : nrow - 행 개수
#           ncol - 컬럼 개수
#           titles - 그래프별 제목 리스트
#           datas - 이미지 데이터 리스트
#           cmap - 그래프별 컬러맵

def printPlots(nrow, ncol, titles, datas, cmap=None):

    # 그래프 마다 컬러맵 설정값 
    cmaps = [None] * (nrow*ncol) if cmap==None else cmap * (nrow*ncol) if len(cmap)==1 else cmap

    # 그래프 그리기
    f_w, f_y = 3 * ncol , 3 * nrow 
    _, axes = plt.subplots(nrow, ncol , sharey = True, figsize=(f_w, f_y))

    # 그래프 객체를 1D차원으로 변환
    axes = [axes] if (nrow * ncol) == 1 else axes.flatten() if nrow != 1 else axes

    # 그래프 객체 채우기
    for ax, title, data, cmap in zip(axes, titles, datas, cmaps):
        ax.set_title(title)
        ax.imshow(data, cmap)
        ax.axis('off')   

    plt.tight_layout()
    plt.show()

def printPlotImage(nrow, ncol, titles, plots, images, cmap=None):
    # 그래프 마다 컬러맵 설정값 
    cmaps = [None] * (nrow*ncol) if cmap==None else cmap * (nrow*ncol) if len(cmap)==1 else cmap
    # 그래프 그리기
    f_w, f_y = 6 * ncol , 6 * nrow 
    _, axes = plt.subplots(nrow, ncol ,  figsize=(f_w, f_y))
    # _, axes = plt.subplots(nrow, ncol)
    # 그래프 객체를 1D차원으로 변환
    axes = [axes] if (nrow * ncol) == 1 else axes.flatten() if nrow != 1 else axes
    # 그래프와 이미지 식별용 플래그 저장
    datas = images + plots
    flags = ['i' for _ in range(len(images))] + ['p' for _ in range(len(plots))]
    # 그래프 객체 채우기
    for ax, title, data, flag, cur_cmap in zip(axes, titles, datas, flags, cmaps):
        ax.set_title(title)
        if flag == 'p': ax.plot(data)
        else: ax.imshow(data, cmap=cur_cmap)
    plt.tight_layout()
    plt.show()

## ------------------------------------------------------
## 함수이름 : printDistance
## 함수기능 : 이미지의 거리값 출력 함수 
## 매개변수 : imgNP    - 이미지 배열 데이터
##           disNP   - 거리값 저장 배열 데이터
##           title   - 그래프 제목
## 함수결과 : 직접 출력으로 없음 None
## ------------------------------------------------------
def printDistance(images, dist, title, cmap_=None):
    plt.figure(figsize=(5, 5))
    plt.imshow(images, cmap=cmap_ if cmap_ else "gray", vmin=0, vmax=255)
    for y in range(dist.shape[0]):
        for x in range(dist.shape[1]):
            plt.text(x, y, str(dist[y, x]), ha="center", va="center", fontsize=8)
    plt.title(f"{title}")
    plt.xticks(range(images.shape[1]))
    plt.yticks(range(images.shape[0]))
    plt.grid()
    plt.show()
