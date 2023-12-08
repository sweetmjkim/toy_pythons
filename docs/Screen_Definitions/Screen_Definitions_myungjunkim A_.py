# 문제 풀고, 점수 따른 학점 출력
# 파일 이름과 업무분장 협의해 결정
# 업무 분장 : 문제 풀고 / 점수 따른 학점 출력
# 특정 시점에 통합 : 각자 만든 코드 합함.

list_problems = ["1. 문제: Python에서 변수를 선언하는 방법은? (점수: 10점)"
            ,"1) var name, 2) name = value, 3) set name, 4) name == value"
            ,"2. 문제: Python에서 리스트(List)의 특징은 무엇인가요? (점수: 15점)"
            ,"1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다"
            ,"3. 문제: Python에서 조건문을 작성하는 방법은? (점수: 10점)"
            ,"1) if-else, 2) for-in, 3) while, 4) def"
            ,"4. 문제: Python에서 함수를 정의하는 방법은? (점수: 5점)"
            ,"1) class, 2) def, 3) import, 4) return"
              ]
list_anwser = [0, 1, 2, 3]
# tmp_anwser = [1, 2, 3, 4]
for num_count in [0, 2, 4, 6] :
    str_question = list_problems[num_count]
    print("{}".format(str_question))
    str_anwser = list_problems[num_count+1]
    print("{}".format(str_anwser))

    # str_question_result = input("당신의 답변(순서 맞게 번호로 입력) : ")
    # num_question_result = int(str_question_result) # 문자를 숫자로 변환
    num_question_result = 1 # 문자를 숫자로 변환
    index = num_question_result - 1 # index 위치값 적용
    
    # list_anwser[index]  = list_anwser[index] + 1 

    print("------------------------------------------")
    pass
print("선호 답항 : {}" .format(list_anwser))
print("End Program!")

