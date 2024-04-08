# 2)
# 키보드로 세 문자열을 입력받고, 입력받은 세 문자열을 리스트에 저장하시오.
# 그 후 리스트에 저장된 문자열 중 가장 긴 문자열과 가장 짧은 문자열의 글자 수 차이를 출력하시오.
str1 = input('단어 1 : ')
str2 = input('단어 2 : ')
str3 = input('단어 3 : ')

num_list = [len(str1), len(str2), len(str3)]

max_num = num_list[0]
min_num = num_list[0]

for ele in num_list :
  if max_num < ele :
    max_num = ele
  if min_num > ele :
    min_num = ele

print(max_num - min_num)