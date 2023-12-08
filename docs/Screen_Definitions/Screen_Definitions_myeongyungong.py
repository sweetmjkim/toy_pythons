# 통계 내기
# 점수 계산 / 학점 출력 
# 변수 : 답항지 문항 [], 정답 [], 점수 합계 [], 점수에 따른 학점 출력 []

# 정해진 숫자를 점수로 치환해서 대입해서 합계를 낸다.

# 문제 정답

def result_cal(user_answer) :
    pass
    correct_answer = [2,1,1,2]
    score_list=[10,15,10,5]
    score=[]
    for i in range(len(user_answer)):
       if user_answer[i] == correct_answer[i] :
            score.append(int(score_list[i]))
            user_sum = sum(score)
    if user_sum >=30 :
        user_score = "A"
    elif user_sum >=20 :
        user_score = "B"
    else:
        user_score = "C"
    print ("--------결과---------")
    print("응답한 내용 : 1번 {}, 2번 {}, 3번 {}, 4번 {}".format(user_answer[0], user_answer[1],user_answer[2], user_answer[3]))
    print("당신 응답 합계 : {}점".format(user_sum))
    print("학점은 {}입니다.".format(user_score))
 

result_cal(question())