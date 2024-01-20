# 변수
a = 10
print("a의 출력은 = ", a)

# 자료형
# 숫자 ( 정수 )
a = 100

# 문자
b = 'hello world'

# 문자열
c = "hello world"

# 불린
d = True

# 리스트
e = [1, 2, 3, 4, 5]

# 딕셔너리
f = {'data1': 'traveler', 'data2': 'blog'}

# 자판기 만들기

menu = {'1': 1000, '2': 1200, '3': 800}
print("메뉴판\n", menu)
input1 = input("메뉴를 입력하세요 : ")
money = input("돈을 넣을 금액을 입력 : ")
money = int(money)

if input1 in menu:
  if (money >= menu[input1]):
    print("메뉴의 금액은 " + str(menu[input1]) + "입니다.")
    print("거스름돈 ", money - menu[input1], "원을 받아가세요.")
  else:
    print("메뉴를 주문할 돈이 부족합니다")
    print("부족한 금액 = ", menu[input1] - money)
else:
  print("메뉴를 잘못 입력하셨습니다.")
