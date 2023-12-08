# 문제 풀고, 점수 따른 학점 출력
# 파일 이름과 업무분장 협의해 결정
# 업무 분장 : 문제 풀고 / 점수 따른 학점 출력
# 특정 시점에 통합 : 각자 만든 코드 합함.

# # 문제 만들기 _ juuuuuu
# 아래는 4개의 Python 관련 문제와 각 문항의 난이도에 따른 점수화
# 1. 문제: Python에서 변수를 선언하는 방법은? (점수: 10점)
#    1) var name, 2) name = value, 3) set name, 4) name == value
#    - 정답: 2
# 2. 문제: Python에서 리스트(List)의 특징은 무엇인가요? (점수: 15점)
#    1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다
#    - 정답: 1
# 3. 문제: Python에서 조건문을 작성하는 방법은? (점수: 10점)
#    1) if-else, 2) for-in, 3) while, 4) def
#    - 정답: 1
# 4. 문제: Python에서 함수를 정의하는 방법은? (점수: 5점)
#    1) class, 2) def, 3) import, 4) return
#    - 정답: 2

# —----- 결과 —-------------
# 응답한 내용 : 1번 2, 2번 1, 3번 1, 4번 2
# 당신 응답 합계 : 40점
# 학점은 A 입니다.
# # 

def question():    
    question_list = ["1. 문제: Python에서 변수를 선언하는 방법은? (점수: 10점)",
                    "2. 문제: Python에서 리스트(List)의 특징은 무엇인가요? (점수: 15점)",
                    "3. 문제: Python에서 조건문을 작성하는 방법은? (점수: 10점)",
                    "4. 문제: Python에서 함수를 정의하는 방법은? (점수: 5점)"
                    ]
    answer_list = ["1) var name, 2) name = value, 3) set name, 4) name == value",
                "1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다",
                "1) if-else, 2) for-in, 3) while, 4) def",
                "1) class, 2) def, 3) import, 4) return"
    ]

    user_answer = []
    for a in range(len(question_list)):
        print(question_list[a])
        print(answer_list[a])
        input_answer = int(input("- 정답:"))
        user_answer.append(input_answer)
        pass
    pass
    return user_answer

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
