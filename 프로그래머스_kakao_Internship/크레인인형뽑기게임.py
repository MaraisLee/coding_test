# https://school.programmers.co.kr/learn/courses/30/lessons/64061
#                       board	                                    moves	      ->  result
# [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	[1,5,3,5,1,2,1,4] ->	4

def solution(board, moves):
    answer = 0
    # stack 구조랑 같음, 후입선출 (위에 쌓인게 먼저 나감)
    stack_list = []
    for i in moves:
        # 2차원배열 길이만 큼
        for j in range(len(board)):
            # 인형뽑기에서 해당 열을 쭉 내려가면서 0이 아니면 젤 위에 있다는 말
            if board[j][i-1] != 0:
                stack_list.append(board[j][i-1])
                # 인형 뽑았다면 그자리 비워주기
                board[j][i-1] = 0
                # 2개 이상 쌓여있다면 같은 건지 확인 (2개 같은 게 붙어있으면 터트려줘야함)
                if len(stack_list) > 1:
                    if stack_list[-2] == stack_list[-1]:
                        # 터트린 두개 스택에서 하나씩 빼주기
                        stack_list.pop(-1)
                        stack_list.pop(-1)
                        answer += 2
                # 두번째 for문을 돌면서 젤 위에 있는 인형을 이미 뽑았다면 다음 move로 바로 이동
                break
    return answer
