def solution(keyinput, board):
    # 시작 위치
    x, y = 0, 0
    
    # 이동 범위 제한 (중앙 기준 최대 이동 가능 범위)
    max_x = board[0] // 2
    max_y = board[1] // 2

    # 키 입력 처리
    for key in keyinput:
        if key == "left" and x > -max_x:
            x -= 1
        elif key == "right" and x < max_x:
            x += 1
        elif key == "up" and y < max_y:
            y += 1
        elif key == "down" and y > -max_y:
            y -= 1

    return [x, y]
