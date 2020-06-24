"""
    날짜 : 2020/06/24
    이름 : 이성진
    내용 : 예외처리 교재 p222
"""

# try ~ except
if __name__=='__main__':
    r1 = r2 = r3 = r4 = 0
    num1, num2, num3, num4 = 1, 0, 3, 4

    try:
        r1 = num1 + num2
        r2 = num1 - num2
        r3 = num2 * num3
        r4 = num4 / num2

    except:
        print('예외발생!')

    print('r1 :', r1)
    print('r2 :', r2)
    print('r3 :', r3)
    print('r4 :', r4)

# try ~ except ... except
if __name__=='__main__':

    list = [10, 20 ,30]
    try:
        print('리스트 번호 입력 :', end='')
        i = int(input())

        print('해당 숫자는 :', list[i])

    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다.')
    except IndexError:
        print('해당하는 리스트값이 없습니다.')



# try ~ except ... finally
if __name__ == '__main__':

    is_exist = False

    try:
        file = open('./test.txt', 'r')
        is_exist = True
    except:
        print('파일이 존재하지 않습니다.')
    finally:
        if is_exist:
            print('파일을 열었습니다.')
        else:
            print('파일을 추가하세요.')





# try ~ except ... else
if __name__=='__main__':
    pass