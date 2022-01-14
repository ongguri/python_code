import numpy as np
import matplotlib.image as im
import matplotlib.pyplot as plt
import math
import cv2
import os
import pdb

def imgRead(dir1,flen):
    total = []
    for i in dir1:
        os.chdir(i + '\\')
        file = os.listdir()
        flen.append(len(file))

        imgDB = np.zeros((len(file), 200, 200))
        total.append(imgDB)

        arg = np.zeros((200, 200))

        for j in range(len(file)):
        
            xmin, xmax, ymin, ymax = 0, 0, 0, 0
            pointx = []
            pointy = []

            img = cv2.imread(file[j],0)
            
            img = cv2.medianBlur(img, 9)

            ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)            

            phand = img.sum(axis = 1)  # 각 행마다 덧샘을 진행 = phand -> 200 개
            wmax = np.where(phand == np.max(phand))  # phand에서 최대값을 찾음 -> 255값이 가장 많은 행
            p = int(len(wmax[0]) / 2)  # 최대값을 갖는 행들 중 중앙에 있는 행의 번호를 찾기 위해 개수/2를 진행

            hcut = img[wmax[0][p] : wmax[0][p]+1 , : ]  # img 데이터에서 255가 가장 많은 행의 리스트를 hcut에 넣음
            count = np.where(hcut[0] == 255)[0]  # 255값의 위치들을 찾음
            half_count1 = len(np.where(hcut[0] == 255)[0]) // 2
            # 찾은 255값 개수에 절반값을 구함 -> hcut에 더해주어 손목위치를 찾기 위함
            
            hand_mid = (count[0] + count[-1]) // 2
##            img[wmax[0][p]][hand_mid] = 0  # 손에 중앙점을 찍어줌
            
            count2 = np.where(img[199, : ] == 255)[0]
            hand_bot = (count2[0] + count2[-1]) // 2
##            img[199][hand_bot] = 0  # 손목의 중앙점을 찍어줌

##            point = np.arange(0,200,1)
##            a,b = np.meshgrid(point,point)
##            co = np.where(img[b,a] == 255)
##            eco = np.cov(co)
##
##            c,d = np.linalg.eig(eco)
##
##            myradians = math.atan2(d[:,1][0],d[:,1][1])
##            mydegrees = math.degrees(myradians)
##
##            matrix = cv2.getRotationMatrix2D((100,100), mydegrees, 1)
##            img = cv2.warpAffine(img, matrix, (200,200))

            myradians = abs(math.atan2(wmax[0][p] - 199, hand_mid - hand_bot))
            mydegrees = math.degrees(myradians)  # 아크탄젠트 값 구하기

            matrix = cv2.getRotationMatrix2D((100, 100), 90 - mydegrees, 1)
            img = cv2.warpAffine(img, matrix, (200, 200))  # 이미지 로테이션
            
##            cv2.line(img, (0, wmax[0][p]), (200, wmax[0][p]), (255, 0, 0), 1)
##            cv2.line(img, (hand_bot, 199), (hand_mid, wmax[0][p]), (0, 0, 0), 1)
           
            img_trim = img[ : wmax[0][p] + half_count1, : ]
            # img를 첫 행 ~ 255 값을 가장 많이 갖고있는 행 + 원의 반지름 길이로 자름
            
            contours, a = cv2.findContours(img_trim, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)            

            for n in range(len(contours)):
                for m in range(len(contours[n])):
                    pointx.append(contours[n][m][0][0])  # 윤곽선 좌표값에서 x값만 뽑는 과정
                    xmin = min(pointx)  # 뽑힌 x값들중 최소값
                    xmax = max(pointx)

            for n in range(len(contours)):
                for m in range(len(contours[n])):
                    pointy.append(contours[n][m][0][1])  # 윤곽선 좌표값에서 y값만 뽑는 과정
                    ymin = np.min(pointy)
                    ymax = np.max(pointy)
                    
            x = xmin
            y = ymin
            w = xmax - xmin
            h = ymax - ymin
            
            reimg_trim = img_trim[y:y+h, x:x+w]
            img = cv2.resize(reimg_trim, (200, 200))

            arg += img
            
            all_img[200*(int(i) - 1) : 200*int(i), 200*j : 200 * (j+1)] = img
            imgDB[j, :, :] = img
            
##        cv2.imwrite("c:\\handtest\\" + str(i) + ".jpg", img)
            
        os.chdir("c:\\handDB\\")
        argimg = arg/(j+1)
        all_argimg[ : 200, 200*(int(i) - 1) : 200*int(i)] = argimg

    print('imgRead Finished!!')
    
    
    return total


def tmplMake(total):
    tmpl = np.zeros((200, 2000))

##    for ii in range(10):
##        tmpl[:, ii * 200:(ii+1)*200] = total[ii][0]

    tmpl = all_argimg

    print('tmplMake Finished!!')
    
    return tmpl


def tmplMatch(total, tmpl):

    result = np.ones((10, 50)) * -1

    for ii in range(len(flen)):
        temp = []
        for jj in range(flen[ii]):
            
            X = total[ii][jj]
            X1 = np.tile(X, (1, 10))
            
            error = np.sum(np.abs(tmpl - X1), axis = 0)
            error2 = [error[0:200].sum(),error[200:400].sum(),error[400:600].sum(),
            error[600:800].sum(),error[800:1000].sum(),error[1000:1200].sum(),
            error[1200:1400].sum(),error[1400:1600].sum(),error[1600:1800].sum(),
            error[1800:2000].sum()]

            temp = np.argmin(error2)
            result[ii, jj] = temp

    print('tmplMatch Finished!!')

    return result


def cMatMake(flen, result):

    cMat = np.zeros((10, 10))
    bound = np.arange(-0.5, 9.6, 1)
    
    for ii in range(10):
        hist, ddd = np.histogram(result[ii,:],bound)
        cMat[ii,:] = hist

    print('cMatMake Finished!!')
    
    return cMat



def cMatSimMake(cMat):

    cMatSim = np.zeros((4, 10))
    label = np.tile(np.arange(0, 10).reshape(10, 1), (1, 50))

    for ii in range(10):
        cMatSim[0, ii] = ((label == result) & (label == ii)).sum() # TP
        cMatSim[1, ii] = ((ii != result) & (label != ii)&(result != -1)).sum() # TN
        cMatSim[2, ii] = ((ii == result) & (label != ii)).sum() # FP
        cMatSim[3, ii] = ((ii != result) & (label == ii)&(result != -1)).sum() # FN

    print('cMatSimMake Finished!!')
    
    return cMatSim


def scoreMake(flen, cMatSim):

    score = [[0 for jj in range(len(flen))] for ii in range(4)]

    for s in range(len(flen)):

        accuracy = (cMatSim[0][s] + cMatSim[1][s]) / \
                   (cMatSim[0][s] + cMatSim[1][s] + cMatSim[2][s] + cMatSim[3][s])

        precision = cMatSim[0][s] / (cMatSim[0][s] + cMatSim[2][s])

        recall = cMatSim[0][s] / (cMatSim[0][s] + cMatSim[3][s])

        F1 = 2 * (precision * recall) / (precision + recall)
        
        score[0][s] = accuracy
        score[1][s] = precision
        score[2][s] = recall
        score[3][s] = F1
        

    print('scoreMake Finished!!')
    
    return score

if __name__ == "__main__":
    flen = []
    all_img = np.zeros((200*10, 200*46))
    all_argimg = np.zeros((200, 2000))
    os.chdir("c:\\handDB\\")
    dir1 = os.listdir()
    dir1.append(dir1[1])
    dir1.remove(dir1[1])  # 클래스 순서를 정돈
    print(dir1)

    total = imgRead(dir1,flen)
    tmpl = tmplMake(total)
    result = tmplMatch(total, tmpl)
    cMat = cMatMake(flen,result)
    cMatSim = cMatSimMake(cMat)
    score = scoreMake(flen, cMatSim)
    
    print("=====confusion matrix=====\n")
    print(cMat)
    print("\n=======score========\n")
    print("accuracy: ",np.array(score[0]))
    print("\nprecision: ",np.array(score[1]))
    print("\nrecall: ",np.array(score[2]))
    print("\nF1: ",np.array(score[3]))
    print("\n")
    print("각 score 평균: ",np.array(score).mean(1))
    print("\n")

    sum = 0
    
    for m in range(10):
        mean = cMat[m][m] / flen[m]
        sum += mean
        print("Class" + str(m+1) + " 평균 = ", mean)
    print("전체 평균 = ", sum/10)

##plt.imshow(all_argimg)
##plt.show()

##    plt.imshow(all_img)
##    plt.show()
