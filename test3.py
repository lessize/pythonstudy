# 3)
# 매개변수로 두 개의 리스트를 받아, 두 개의 리스트에 저장된 모든 데이터의 평균을 리턴하는 함수를 작성하시오.

li1 = [1, 2, 3]
li2 = [4, 5, 6]

def avg(a, b) :
  list = a + b
  sum = 0
  for ele in list :
    sum += ele
  return sum / len(list)

print(avg(li1, li2))