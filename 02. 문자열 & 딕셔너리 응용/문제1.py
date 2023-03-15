# 주민등록번호 유효성을 체크해 보자

# 각 자리에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5 를 곱한다.( 단, 마지막 자리는 빼놓음 )
# 각 자리의 숫자를 모두 더한다.
# 11로 나눈 나머지 값을 구한다.
# 11에서 결과값을 뺀다( 단, 마지막 결과가 두자리인 경우 다시 10으로 나눈 나머지 값을 구한다. ).
# 결과가 주민등록번호 마지막 자리와 일치하면 유효한 주민등록번호이다.

nums = input().replace('-', "") # 주민등록번호를 입력받아 하이픈을 제거
mulNums = '234567892345' # 곱할 가중치들을 문자열로 저장

if(len(nums) != 13): # 주민등록번호가 13자리가 아니라면
    print("주민등록번호를 다시 확인해 주세요.")


sum = 0 # 각 자릿 수의 숫자를 더할 변수

for i in range(12): # 0부터 11까지
    sum += int(nums[i]) * int(mulNums[i]) # 각 자릿 수에 가중치를 곱한다

sum = (11 - sum % 11) % 10 
# 11을 sum을 11로 나눈 나머지로 빼고, 10을 나눈다.


if(sum == int(nums[-1])): # 결과값이 nums의 마지막 인덱스의 요소와 같다면
        print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")