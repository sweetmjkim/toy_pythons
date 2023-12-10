# 통계 내기
# 점수 계산 / 학점 출력 
# 변수 : 답항지 문항 [], 정답 [], 점수 합계 [], 점수에 따른 학점 출력 []

# 정해진 숫자를 점수로 치환해서 대입해서 합계를 낸다.

# 문제 정답

# 정해진 답에 대한 점수 합계
answer = [2,1,1,2]          # 정해진 정답 변수 -> 이후에 입력받을수 있게 변환
user_answer = [0,0,0,0]     # 입력 받을 정답 변수 
list_score = [10,15,10,5]   # 정답에 따른 점수 변수
score = 0                   # 합산 변수

for i in user_answer:
    user_answer[i] = list_score[i]
    score += user_answer[i]

    if score >= 30:
        user_grade = 'A'
    elif score >= 20:
        user_grade = 'B'
    else :
        user_grade = 'C'

print("응답결과 : 1번 : {} 2번 : {}, 3번 : {}, 4번 : {}".format(answer[0],answer[1],answer[2],answer[3]))
print("합산 점수 : {}".format(score))
print("등급 : {}".format(user_grade))
    

# 입력한 값으로 점수 합계(진행중)

user_answer = [0,0,0,0]     # 입력 받을 정답 변수 
list_score = [10,15,10,5]   # 정답에 따른 점수 변수
score = 0                   # 합산 변수

for i in range(len(user_answer)):
    input_answer = int(input("정답 입력 : ")) # 정답 입력받을 변수
    user_answer[i] = input_answer

    if input_answer == 2:
        score += list_score[i]
    elif input_answer == 1:
        score += list_score[i]

    if score >= 30:
        user_grade = 'A'
    elif score >= 20:
        user_grade = 'B'
    else :
        user_grade = 'C'

print("응답결과 : 1번 : {} 2번 : {}, 3번 : {}, 4번 : {}".format(user_answer[0],user_answer[1],user_answer[2],user_answer[3]))
print("합산 점수 : {}".format(score))
print("등급 : {}".format(user_grade))
        
