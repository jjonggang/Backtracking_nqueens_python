# Backtracking NQueen problem

def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True



def DFS(N, current_row, current_candidate, final_result):
    if current_row == N: # 배치가 끝남
        print(current_candidate)
        final_result.append(current_candidate[:]) # 얕은 복사
        return

    for candidate_col in range(N): # N개의 열 중 되는 것을 하나하나 체크해 나간다.
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row+1, current_candidate, final_result) # 재귀적 호출
            current_candidate.pop() # 백트래킹


def solve_n_queens(N):
    final_result = [] # 배치도 저장
    DFS(N, 0, [], final_result)
    return final_result

solve_n_queens(4)