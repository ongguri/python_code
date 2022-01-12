import random


'''
board = []
choiceH = []
choiceC =[]
li = []
change_board = []

find_num = 0
num = 0

end_game = ''


# 0) 일차리스트를 이차원 리스트로 만들어주는 함수

def change_li():

    global board
    global change_board
    global li

    for i in board:
        li.append(i)
        if len(li) == 3:
            change_board.append(li)
            li = []
    board = change_board
    change_board = []
    return change_board
    
    

# 1) 보드설정

def new_board():

    global board
    global li

    for i in range(1,10):
        li.append(i)

        if len(li) == 3:
            board.append(li)
            li = []
        

# 5) 디스플레이

def display():

    global board

    for i in board:
        print(i)
    print()



# 2) 사용자 번호입력



def user_choice():

    global choiceH
    global choiceC
    global board
    global num
    global find_num
    
    while True:
        
        num = int(input("번호 선택: "))

        if num in choiceH:
            print("이미 선택된 번호입니다.")
        elif num in choiceC:
            print("이미 선택된 번호입니다.")
        else:
            choiceH.append(num)
            board = sum(board,[])  # 이차원 리스트를 일차원 리스트로 만들기
            find_num = board.index(num)  # 입력숫자 인덱스 위치 찾기
            board[find_num] = 'O'
            change_li()
            break

# 3) 컴퓨터 번호입력

def com_choice():
    
    global num
    global choiceC
    global choiceH
    global board
    global find_num
    
    while True:
        num = random.randint(1,9)
        
        if num not in choiceC:
            if num not in choiceH:
                choiceC.append(num)
                board = sum(board,[])
                find_num = board.index(num)
                board[find_num] = 'X'
                change_li()
                break


# 4) 승패여부

def result_game():

    global board
    global choiceH
    global choiceC
    global end_game

    board = sum(board,[])

    if board[0] == board[1] == board[2]:
        end_game = True
        if board[0] == 'O':
            print()
            print("승리")
        else:
            print()
            print("패배")
    elif board[3] == board[4] == board[5]:
        end_game = True
        if board[3] == 'O':
            print()
            print("승리")
        else:
            print()
            print("패배")
    elif board[6] == board[7] == board[8]:
        end_game = True
        if board[6] == 'O':
            print()
            print("승리")
        else:
            print()
            print("패배")
    elif board[0] == board[3] == board[6]:
        end_game = True
        if board[0] == 'O':
            print()
            print("승리")
        else:
            print()
            print("패배")
    elif board[1] == board[4] == board[7]:
        end_game = True
        if board[1] == 'O':
            print()
            print("승리")
        else:
            print()
            print("패배")
    elif board[2] == board[5] == board[8]:
        end_game = True
        if board[2] == 'O':
            print()
            print("승리")
        else:
            print()
            print("패배")
    elif board[0] == board[4] == board[8]:
        end_game = True
        if board[0] == 'O':
            print()
            print("승리")
        else:
            print()
            print("패배")
    elif board[2] == board[4] == board[6]:
        end_game = True
        if board[2] == 'O':
            print()
            print("승리")
        else:
            print()
            print("패배")

    elif len(choiceH) == 5:
        end_game = True
        print('무승부')

    change_li()

    return end_game
        


# board 상태 출력 
new_board()
display()

while True:
    user_choice()
    result_game()
    if end_game:
        print()
        display()
        break
    com_choice()
    display()
    result_game()

    if end_game:
        break
print("게임이 종료되었습니다.")
'''



# 0) 일차리스트를 이차원 리스트로 만들어주는 함수

def change_li(li):

    new = []
    change = []

    for i in li:
        new.append(i)
        if len(new) == 3:
            change.append(new)
            new = []
    return change

    

# 1) 보드설정

def new_board(bo):

    li = []
    
    for i in range(1,10):
        li.append(i)

        if len(li) == 3:
            bo.append(li)
            li = []
    return bo



# 5) 디스플레이

def display(dis):

    for i in board:
        print(i)
    print()



# 2) 사용자 번호입력



def user_choice(bo):

    num = 0
    find_num = 0
    bo = sum(bo,[])
    
    while True:
        
        num = int(input("번호 선택: "))

        if num not in bo:
            print("이미 선택된 번호입니다.")
        
        else:
            find_num = bo.index(num)  # 입력숫자 인덱스 위치 찾기
            bo[find_num] = 'O'
            b = change_li(bo)
            break

    return b



# 3) 컴퓨터 번호입력

def com_choice(bo):
    
    num = 0
    find_num = 0
    bo = sum(bo,[])
    
    while True:
        num = random.randint(1,9)
        
        if num in bo:
            find_num = bo.index(num)
            bo[find_num] = 'X'
            b = change_li(bo)
            break
            
    return b



# 4) 승패여부

def result_game(bo,co):

    end_game = ''

    bo = sum(bo,[])

    if bo[0] == bo[1] == bo[2]:
        end_game = True
        if bo[0] == 'O':
            print()
            print("승리")
        else:
            print()
            print("패배")
    elif bo[3] == bo[4] == bo[5]:
        end_game = True
        if bo[3] == 'O':
            print()
            print("승리")
        else:
            print()
            print("패배")
    elif bo[6] == bo[7] == bo[8]:
        end_game = True
        if bo[6] == 'O':
            print()
            print("승리")
        else:
            print()
            print("패배")
    elif bo[0] == bo[3] == bo[6]:
        end_game = True
        if bo[0] == 'O':
            print()
            print("승리")
        else:
            print()
            print("패배")
    elif bo[1] == bo[4] == bo[7]:
        end_game = True
        if bo[1] == 'O':
            print()
            print("승리")
        else:
            print()
            print("패배")
    elif bo[2] == bo[5] == bo[8]:
        end_game = True
        if bo[2] == 'O':
            print()
            print("승리")
        else:
            print()
            print("패배")
    elif bo[0] == bo[4] == bo[8]:
        end_game = True
        if bo[0] == 'O':
            print()
            print("승리")
        else:
            print()
            print("패배")
    elif bo[2] == bo[4] == bo[6]:
        end_game = True
        if bo[2] == 'O':
            print()
            print("승리")
        else:
            print()
            print("패배")

    elif co == 5:
        end_game = True
        print('무승부')

    b = change_li(bo)

    return b, end_game
    

            


board = []
count = 0

board = new_board([])

display(board)

while True:
    board = user_choice(board)
    count += 1
    board, end_g = result_game(board,count)
    if end_g:
        print()
        display(board)
        print()
        print('게임이 종료되었습니다.')
        break
    board = com_choice(board)
    display(board)
    board, end_g = result_game(board,count)
    if end_g:
        print()
        display(board)
        print()
        
        print('게임이 종료되었습니다.')
        break
    
    



