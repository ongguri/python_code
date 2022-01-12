from tkinter import * # tkinter 의 모든 정의를 임포트한다.
from tkinter import messagebox  # tkinter 에서 메세지박스를 사용
import random  # 렌덤함수 호출

user_num = []  # 유저가 선택한 번호를 받기위한 빈 리스트
com_num =[] # 컴퓨터가 선택한 번호를 받을 빈 리스트

class gameplay:  # gameplay 라는 틱텍토 승패여부 클래스

    def win_lose(self, user, com):  # 승패여부를 따지는 함수

        __Msg = ''  # 결과를 담을 __Msg 변수
        
        if (1 in user) and (2 in user) and (3 in user):  # 만약 유저가 선택한 번호중 1,2,3 이 포함되어있다면
            __Msg = messagebox.showinfo("게임 종료", "유저 승리")  # 메세지박스로 '유저승리'창을 띄운다.
            self.window.destroy()  # 메인루프를 종료하고 전체위젯 삭제
        elif (4 in user) and (5 in user) and (6 in user):  # 만약 유저가 선택한 번호중 4,5,6 이 포함되어있다면
            __Msg = messagebox.showinfo("게임 종료", "유저 승리")  # 메세지박스로 '유저 승리'창을 띄운다.
            self.window.destroy()  # 메인루프를 종료하고 전체위젯 삭제
        elif (7 in user) and (8 in user) and (9 in user):  # 만약 유저가 선택한 번호중 7,8,9 가 포함되어있다면
            __Msg = messagebox.showinfo("게임 종료", "유저 승리")  # 메세지박스로 '유저 승리'창을 띄운다.
            self.window.destroy()  # 메인루프를 종료하고 전체위젯 삭제
        elif (1 in user) and (4 in user) and (7 in user):  # 만약 유저가 선택한 번호중 1,4,7 이 포함되어있다면
            __Msg = messagebox.showinfo("게임 종료", "유저 승리")  # 메세지박스로 '유저 승리'창을 띄운다.
            self.window.destroy()  # 메인루프를 종료하고 전체위젯 삭제
        elif (2 in user) and (5 in user) and (8 in user):  # 만약 유저가 선택한 번호중 2,5,8 이 포함되어있다면
            __Msg = messagebox.showinfo("게임 종료", "유저 승리")  # 메세지박스로 '유저 승리'창을 띄운다.
            self.window.destroy()  # 메인루프를 종료하고 전체위젯 삭제
        elif (3 in user) and (6 in user) and (9 in user):# 만약 유저가 선택한 번호중 3, 6, 9 가 포함되어있다면
            __Msg = messagebox.showinfo("게임 종료", "유저 승리")  # 메세지박스로 '유저 승리'창을 띄운다.
            self.window.destroy()  # 메인루프를 종료하고 전체위젯 삭제
        elif (1 in user) and (5 in user) and (9 in user):# 만약 유저가 선택한 번호중 1,5,9 가 포함되어있다면
            __Msg = messagebox.showinfo("게임 종료", "유저 승리")  # 메세지박스로 '유저 승리'창을 띄운다.
            self.window.destroy()  # 메인루프를 종료하고 전체위젯 삭제
        elif (3 in user) and (5 in user) and (7 in user):# 만약 유저가 선택한 번호중 3,5,7 이 포함되어있다면
            __Msg = messagebox.showinfo("게임 종료", "유저 승리")  # 메세지박스로 '유저 승리'창을 띄운다.
            self.window.destroy()  # 메인루프를 종료하고 전체위젯 삭제
            
        elif len(user) == 5:  # 만약 유저가 선택한 번호가 총 5개라면
            __Msg = messagebox.showinfo("게임 종료", "무승부")  # 메세지박스로 '무승부'창을 띄운다.
            self.window.destroy()  # 메인루프를 종료하고 전체위젯 삭제
            
        if (1 in com) and (2 in com) and (3 in com):  # 만약 컴퓨터가 선택한 번호중 1,2,3 이 포함되어있다면
            __Msg = messagebox.showinfo("게임 종료", "유저 패배")  # 메세지박스로 '유저 패배'창을 띄운다.
            self.window.destroy()  # 메인루프를 종료하고 전체위젯 삭제
        elif (4 in com) and (5 in com) and (6 in com):  # 만약 컴퓨터가 선택한 번호중 4,5,6 이 포함되어있다면
            __Msg = messagebox.showinfo("게임 종료", "유저 패배")  # 메세지박스로 '유저 패배'창을 띄운다.
            self.window.destroy()  # 메인루프를 종료하고 전체위젯 삭제
        elif (7 in com) and (8 in com) and (9 in com):# 만약 컴퓨터가 선택한 번호중 7,8,9 가 포함되어있다면
            __Msg = messagebox.showinfo("게임 종료", "유저 패배")  # 메세지박스로 '유저 패배'창을 띄운다.
            self.window.destroy()  # 메인루프를 종료하고 전체위젯 삭제
        elif (1 in com) and (4 in com) and (7 in com):# 만약 컴퓨터가 선택한 번호중 1,4,7 이 포함되어있다면
            __Msg = messagebox.showinfo("게임 종료", "유저 패배")  # 메세지박스로 '유저 패배'창을 띄운다.
            self.window.destroy()  # 메인루프를 종료하고 전체위젯 삭제
        elif (2 in com) and (5 in com) and (8 in com):# 만약 컴퓨터가 선택한 번호중 2,5,8 이 포함되어있다면
            __Msg = messagebox.showinfo("게임 종료", "유저 패배")  # 메세지박스로 '유저 패배'창을 띄운다.
            self.window.destroy()  # 메인루프를 종료하고 전체위젯 삭제
        elif (3 in com) and (6 in com) and (9 in com):# 만약 컴퓨터가 선택한 번호중 3,6,9 이 포함되어있다면
            __Msg = messagebox.showinfo("게임 종료", "유저 패배")  # 메세지박스로 '유저 패배'창을 띄운다.
            self.window.destroy()  # 메인루프를 종료하고 전체위젯 삭제
        elif (1 in com) and (5 in com) and (9 in com):# 만약 컴퓨터가 선택한 번호중 1,5,9 가 포함되어있다면
            __Msg = messagebox.showinfo("게임 종료", "유저 패배")  # 메세지박스로 '유저 패배'창을 띄운다.
            self.window.destroy()  # 메인루프를 종료하고 전체위젯 삭제
        elif (3 in com) and (5 in com) and (7 in com):# 만약 컴퓨터가 선택한 번호중 3,5,7 이 포함되어있다면
            __Msg = messagebox.showinfo("게임 종료", "유저 패배")  # 메세지박스로 '유저 패배'창을 띄운다.
            self.window.destroy()  # 메인루프를 종료하고 전체위젯 삭제
            
        if __Msg == 'ok':  # 만약 __Msg가 'ok' 라면
            return True  # True 를 반환
        else: # 'ok'가 아니라면
            return False  # False 를 반환
            

class numChoice(gameplay):  # 번호를 선택하는 클래스를 선언한다.
    global user_num  # 전역변수 user_num 을 선언한다.
    global com_num  # 전역변수 com_num 을 선언한다.
    __Uchoice_num = []  # private 로 쓸 유저의 선택번호를 받을 맴버변수 선언
    __Cchoice_num = []  # private 로 쓸 컴퓨터의 선택번호를 받을 맴버변수 선언
    def com_choice(self):  # 컴퓨터가 번호를 선택하는 함수
        
        while True:  # break 전까지 무한반복
            self.num = random.randint(1,9)  # num 변수에 1~9까지 랜덤정수를 저장한다.
            if (self.num not in self.__Uchoice_num) and (self.num not in self.__Cchoice_num):  # num에 저장된 정수가 유저나 컴퓨터가 선택하지 않은 정수라면
                if self.num == 1:  # num이 1이라면
                    self.canvas.create_line(0, 0, 341, 266)  # 캔버스에 좌표(0,0) 부터 (341, 266)까지 직선을 그린다.
                    self.canvas.create_line(341, 0, 0, 266)  # 캔버스에 좌표(341,0) 부터 (0,266)까지 직선을 그린다.
                    self.__Cchoice_num.append(1)  # Cchoice_num 에 1를 추가한다.
                elif self.num == 2:  # num이 2 라면
                    self.canvas.create_line(341, 0, 682, 266)  # 캔버스에 좌표(341,0) 부터 (682,266)까지 직선을 그린다.
                    self.canvas.create_line(682, 0, 341, 266)  # 캔버스에 좌표(682,0) 부터 (341, 266)까지 직선을 그린다.
                    self.__Cchoice_num.append(2)  # Cchoice_num 에 2를 추가한다.
                elif self.num == 3:  # num이 3이라면
                    self.canvas.create_line(682, 0, 1023, 266)  # 캔버스에 좌표(682,0) 부터 (1023, 266)까지 직선을 그린다.
                    self.canvas.create_line(1023, 0, 682, 266)  # 캔버스에 좌표(1023,0) 부터 (682, 266)까지 직선을 그린다.
                    self.__Cchoice_num.append(3)  # Cchoice_num 에 3를 추가한다.
                elif self.num == 4:  # num이 4 라면
                    self.canvas.create_line(0, 266, 341, 532)  # 캔버스에 좌표(0,266) 부터 (341, 532)까지 직선을 그린다.
                    self.canvas.create_line(341, 266, 0, 532)  # 캔버스에 좌표(341,266) 부터 (0, 532)까지 직선을 그린다.
                    self.__Cchoice_num.append(4)  # Cchoice_num 에 4를 추가한다.
                elif self.num == 5:  # num이 5라면
                    self.canvas.create_line(341, 266, 682, 532)  # 캔버스에 좌표(341,266) 부터 (682,532)까지 직선을 그린다.
                    self.canvas.create_line(682, 266, 341, 532)  # 캔버스에 좌표(682,266) 부터 (341, 532)까지 직선을 그린다.
                    self.__Cchoice_num.append(5)  # Cchoice_num 에 5를 추가한다.
                elif self.num == 6:  # num이 6이라면
                    self.canvas.create_line(682, 266, 1023, 532)  # 캔버스에 좌표(682,266) 부터 (1023,532)까지 직선을 그린다.
                    self.canvas.create_line(1023, 266, 682, 532)  # 캔버스에 좌표(1023,266) 부터 (682,532)까지 직선을 그린다.
                    self.__Cchoice_num.append(6)  # Cchoice_num 에 6를 추가한다.
                elif self.num == 7:  # num이 7이라면
                    self.canvas.create_line(0, 532, 341, 798)  # 캔버스에 좌표(0,532) 부터 (341, 798)까지 직선을 그린다.
                    self.canvas.create_line(341, 532, 0, 798)  # 캔버스에 좌표(341,532) 부터 (0, 798)까지 직선을 그린다.
                    self.__Cchoice_num.append(7)  # Cchoice_num 에 7를 추가한다.
                elif self.num == 8:  # num이 8이라면
                    self.canvas.create_line(341, 532, 682, 798)  # 캔버스에 좌표(341,532) 부터 (682,798)까지 직선을 그린다.
                    self.canvas.create_line(682, 532, 341, 798)  # 캔버스에 좌표(682,532) 부터 (341, 798)까지 직선을 그린다.
                    self.__Cchoice_num.append(8)  # Cchoice_num 에 8를 추가한다.
                elif self.num == 9:  # num이 9라면
                    self.canvas.create_line(682, 532, 1023, 798)  # 캔버스에 좌표(682,532) 부터 (1023,798)까지 직선을 그린다.
                    self.canvas.create_line(1023, 532, 682, 798)  # 캔버스에 좌표(1023,532) 부터 (682, 266)까지 직선을 그린다.
                    self.__Cchoice_num.append(9)  # Cchoice_num 에 9를 추가한다.
                break  # 무한반복문을 빠져나온다.
            else:  # 만약 num이 유저나 컴퓨터가 이미 선택한번호라면
                continue  # 다시 위로 올라가 번호를 선택하게 한다.
    
    def user_choice(self, event):  # 유저나 번호를 선택하는 함수
        
        while True:  # break 전까지 무한반복
            if (event.x < 341) and (event.y < 266):  # 만약 클릭한 좌표가 (x < 341, y < 266) 범위라면
                if (1 not in self.__Uchoice_num) and (1 not in self.__Cchoice_num):  # 만약 1이, 유저나 컴퓨터가 전에 선택하지 않았다면
                    self.__Uchoice_num.append(1)  # Uchoice_num 변수에 1 추가
                    self.canvas.create_oval(0,0,341,266)  # 캔버스에 좌표(0,0), (341, 266)으로 만들어진 사각형안에 원을 그린다.
                    break  # 무한반복문을 빠져나온다.
                else:  # 만약 1이 이미 선택된 번호라면
                    messagebox.showwarning("경고","이미 선택된 번호입니다.")  # 선택된 번호를 알리는 메세지박스를 띄운다.
                    return  # 유저선택함수를 빠져나와 다시 유저가 선택할수있는 기회를 부여
                    
            elif (341 < event.x < 682) and (event.y < 266):  # 만약 클릭한 좌표가 (341 < x < 682, y < 266) 범위라면
                if (2 not in self.__Uchoice_num) and (2 not in self.__Cchoice_num):  # 만약 2가, 유저나 컴퓨터가 전에 선택하지 않았다면
                    self.__Uchoice_num.append(2)  # Uchoice_num 변수에 2 추가
                    self.canvas.create_oval(341, 0, 682, 266)  # 캔버스에 좌표(341,0), (682, 266)으로 만들어진 사각형안에 원을 그린다.
                    break  # 무한반복문을 빠져나온다.
                else:  # 만약 2가 이미 선택된 번호라면
                    messagebox.showwarning("경고","이미 선택된 번호입니다.")  # 선택된 번호를 알리는 메세지박스를 띄운다.
                    return  # 유저선택함수를 빠져나와 다시 유저가 선택할수있는 기회를 부여
                    
            elif (682 < event.x < 1023) and (event.y < 266):  # 만약 클릭한 좌표가 (682 < x < 1023, y < 266) 범위라면
                if (3 not in self.__Uchoice_num) and (3 not in self.__Cchoice_num):  # 만약 3이, 유저나 컴퓨터가 전에 선택하지 않았다면
                    self.__Uchoice_num.append(3)  # Uchoice_num 변수에 3 추가
                    self.canvas.create_oval(682, 0, 1023, 266)  # 캔버스에 좌표(682,0), (1023, 266)으로 만들어진 사각형안에 원을 그린다.
                    break  # 무한반복문을 빠져나온다.
                else:  # 만약 3이 이미 선택된 번호라면
                    messagebox.showwarning("경고","이미 선택된 번호입니다.")  # 선택된 번호를 알리는 메세지박스를 띄운다.
                    return  # 유저선택함수를 빠져나와 다시 유저가 선택할수있는 기회를 부여

            elif (event.x < 341) and (266 < event.y < 532):  # 만약 클릭한 좌표가 (x < 341, 266 < y < 532) 범위라면
                if (4 not in self.__Uchoice_num) and (4 not in self.__Cchoice_num):  # 만약 4가, 유저나 컴퓨터가 전에 선택하지 않았다면
                    self.__Uchoice_num.append(4)  # Uchoice_num 변수에 4 추가
                    self.canvas.create_oval(0, 266, 341, 532)  # 캔버스에 좌표(0, 266), (341, 532)으로 만들어진 사각형안에 원을 그린다.
                    break  # 무한반복문을 빠져나온다.
                else:  # 만약 4가 이미 선택된 번호라면
                    messagebox.showwarning("경고","이미 선택된 번호입니다.")  # 선택된 번호를 알리는 메세지박스를 띄운다.
                    return  # 유저선택함수를 빠져나와 다시 유저가 선택할수있는 기회를 부여
                    
            elif (341 < event.x < 682) and (266 < event.y < 532):  # 만약 클릭한 좌표가 (341 < x < 682, 266 < y < 532) 범위라면
                if (5 not in self.__Uchoice_num) and (5 not in self.__Cchoice_num):  # 만약 5가, 유저나 컴퓨터가 전에 선택하지 않았다면
                    self.__Uchoice_num.append(5)  # Uchoice_num 변수에 5 추가
                    self.canvas.create_oval(341, 266, 682, 532)  # 캔버스에 좌표(341, 266), (682, 532)으로 만들어진 사각형안에 원을 그린다.
                    break  # 무한반복문을 빠져나온다.
                else:  # 만약 5가 이미 선택된 번호라면
                    messagebox.showwarning("경고","이미 선택된 번호입니다.")  # 선택된 번호를 알리는 메세지박스를 띄운다.
                    return  # 유저선택함수를 빠져나와 다시 유저가 선택할수있는 기회를 부여
                    
            elif (682 < event.x < 1023) and (266 < event.y < 532):  # 만약 클릭한 좌표가 (682 < x < 1023, 266 < y < 532) 범위라면
                if (6 not in self.__Uchoice_num) and (6 not in self.__Cchoice_num):  # 만약 6이, 유저나 컴퓨터가 전에 선택하지 않았다면
                    self.__Uchoice_num.append(6)  # Uchoice_num 변수에 6 추가
                    self.canvas.create_oval(682, 266, 1023, 532)  # 캔버스에 좌표(682,266), (1023,532)으로 만들어진 사각형안에 원을 그린다.
                    break  # 무한반복문을 빠져나온다.
                else:  # 만약 6이 이미 선택된 번호라면
                    messagebox.showwarning("경고","이미 선택된 번호입니다.")  # 선택된 번호를 알리는 메세지박스를 띄운다.
                    return  # 유저선택함수를 빠져나와 다시 유저가 선택할수있는 기회를 부여

            elif (event.x < 341) and (532 < event.y < 798):  # 만약 클릭한 좌표가 (x < 341, 532 < y < 798) 범위라면
                if (7 not in self.__Uchoice_num) and (7 not in self.__Cchoice_num):  # 만약 7이, 유저나 컴퓨터가 전에 선택하지 않았다면
                    self.__Uchoice_num.append(7)  # Uchoice_num 변수에 7 추가
                    self.canvas.create_oval(0, 532, 341, 798)  # 캔버스에 좌표(0,532), (341, 798)으로 만들어진 사각형안에 원을 그린다.
                    break  # 무한반복문을 빠져나온다.
                else:  # 만약 7이 이미 선택된 번호라면
                    messagebox.showwarning("경고","이미 선택된 번호입니다.")  # 선택된 번호를 알리는 메세지박스를 띄운다.
                    return  # 유저선택함수를 빠져나와 다시 유저가 선택할수있는 기회를 부여
                    
            elif (341 < event.x < 682) and (532 < event.y < 798):  # 만약 클릭한 좌표가 (341 < x < 682, 532 < y < 798) 범위라면
                if (8 not in self.__Uchoice_num) and (8 not in self.__Cchoice_num):  # 만약 8이, 유저나 컴퓨터가 전에 선택하지 않았다면
                    self.__Uchoice_num.append(8)  # Uchoice_num 변수에 8 추가
                    self.canvas.create_oval(341, 532, 682, 798)  # 캔버스에 좌표(341, 532), (682, 798)으로 만들어진 사각형안에 원을 그린다.
                    break  # 무한반복문을 빠져나온다.
                else:  # 만약 8이 이미 선택된 번호라면
                    messagebox.showwarning("경고","이미 선택된 번호입니다.")  # 선택된 번호를 알리는 메세지박스를 띄운다.
                    return  # 유저선택함수를 빠져나와 다시 유저가 선택할수있는 기회를 부여
                    
            elif (682 < event.x < 1023) and (532 < event.y < 798):  # 만약 클릭한 좌표가 (682 < x < 1023, 532 < y < 798) 범위라면
                if (9 not in self.__Uchoice_num) and (9 not in self.__Cchoice_num):  # 만약 9가, 유저나 컴퓨터가 전에 선택하지 않았다면
                    self.__Uchoice_num.append(9)  # Uchoice_num 변수에 9 추가
                    self.canvas.create_oval(682, 532, 1023, 798)  # 캔버스에 좌표(682,532), (1023, 798)으로 만들어진 사각형안에 원을 그린다.
                    break  # 무한반복문을 빠져나온다.
                else:  # 만약 9가 이미 선택된 번호라면
                    messagebox.showwarning("경고","이미 선택된 번호입니다.")  # 선택된 번호를 알리는 메세지박스를 띄운다.
                    return  # 유저선택함수를 빠져나와 다시 유저가 선택할수있는 기회를 부여

        while True:  # 무한반복문을 실행

            user_num = self.__Uchoice_num  # user_num 변수에 Uchoice_num변수 저장
            com_num = self.__Cchoice_num  # com_num 변수에 Cchoice_num 변수 저장
            if self.win_lose(user_num, com_num):  # 만약 승패여부 함수의 반환값이 True라면
                break  # 무한반복문을 빠져나온다
            else:  # 만약 승패여부 함수의 반환값이 False 라면
                self.com_choice()  # com_choice 함수를 실행한다.
                if self.win_lose(user_num,com_num):  # 만약 승패여부 함수의 반환값이 True 라면
                    break  # 무한반복문을 빠져나온다
            break  # 무한반복을 빠져나온다.



class board(numChoice):  # board 판을 생성하기위한 클래스

    def __init__(self):  # 생성자 선언
        self.window = Tk()  # 창을 생성한다.
        self.window.title("tic tac toe")  # 윈도우창에 제목표시
        self.window.geometry('1024x800')  # 윈도우창 초기 크기 설정
        self.window.resizable(width = True, height = True)  # 가로세로 크기 변경을 가능하게 함

        self.canvas = Canvas(self.window, width = 1024, height= 800, bg = 'white')  # 캔버스 창을 1023 x 800 크기로 배경은 하얗게 만듬
        self.canvas.pack(expand = 1)  # 캔버스를 가득 채우게끔 배치함

        self.row_line = 800 // 3  # 행을 3등분하기위해 800을 3으로 나눔
        self.column_line = 1024 // 3  # 열을 3등분 하기위해 1024를 3으로 나눔
        
        for i in range(0, 800, self.row_line):  # i는 0부터 800 까지, 800//3 만큼 증가
            self.canvas.create_line(0, i, 1024, i)  # 캔버스에 좌표 (0,i) 부터 (1024,i) 까지 라인을 그린다.
            
        for j in range(0, 1024, self.column_line):  # j는 0부터 1024까지, 1024//3 만큼 증가
            self.canvas.create_line(j, 0, j, 800)  # 캔버스에 좌표 (j,0) 부터 (j, 800) 까지 라인을 그린다.

        self.canvas.bind('<Button-1>', self.user_choice)  #  왼쪽마우스버튼을 누르면 user_choice 함수가 연결되게 바인딩 한다.

        self.window.mainloop()  # 이벤트 루프를 생성한다.

board()  # GUI 를 생성한다.
