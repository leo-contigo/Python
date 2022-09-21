# 유튜브 [나도코딩] - 파이썬 코딩 무료 강의 (기본편)

# while
customer = '아이언맨'
index = 5
# index가 1보다 같거나 클떄
while index >=1:
    print("{0} 고객님, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    # index가 하나씩 줄어듬
    index -=1
    # 만약 index =0 일경우
    if index == 0:
        print("주문하신 음료는 폐기되었습니다.")
print('=========================')
print()
# for
# print('대기번호 : 1')
# print('대기번호 : 2')
# print('대기번호 : 3')
for waiting_no in [1, 2, 3, 4, 5] :
    print('대기번호 : {0}'.format(waiting_no))
print()
# 순차적으로 커질때 1
for waiting_no in range(5) : # 대기번호 0번부터
    print('대기번호 : {}'.format(waiting_no))
print()
# 순차적으로 커질때 2
for waiting_no in range(1, 6) : # 대기번호 1번부터 ~ 5번까지
    print('대기번호 : {}'.format(waiting_no))
print('=========================')
print()
# 한줄 for문
# 출석번호 1 2 3 4 → 101 102 103 104로
student = [1,2,3,4,5]
print(student)
# i에 100을 더하는데 그 i는 student 안에 있는 i들
student = [i+100 for i in student]
print(student)
print('=========================')
print()
# 학생의 이름을 길이로 변환
student = ['Iron man','Thor','i am groot']
print(student)
student = [len(i) for i in student]
print(student)
print('=========================')
print()
# 학생이름을 대문자로
student = ['Iron man','Thor','i am groot']
print(student)
student = [i.upper() for i in student]
print(student)
print('=========================')
print()
# 퀴즈

