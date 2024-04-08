# 1)
# 키보드로 두 수를 입력받아 두 수 사이의 모든 정수의 합을 출력하시오.
# 단 입력받은 두 수는 합에 포함하지 않는다.
num1 = int(input('숫자 1 : '))
num2 = int(input('숫자 2 : '))
sum = 0
for ele in range(num1 + 1, num2) :
  sum += ele

print(sum)

