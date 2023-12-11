# 클래스화 작업
class QuizTest:
    def __init__(self):
        self.question_list = ["1. 문제: Python에서 변수를 선언하는 방법은? (점수: 10점)",
                              "2. 문제: Python에서 리스트(List)의 특징은 무엇인가요? (점수: 15점)",
                              "3. 문제: Python에서 조건문을 작성하는 방법은? (점수: 10점)",
                              "4. 문제: Python에서 함수를 정의하는 방법은? (점수: 5점)"
                             ]
        self.answer_list = ["1) var name, 2) name = value, 3) set name, 4) name == value",
                            "1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다",
                            "1) if-else, 2) for-in, 3) while, 4) def",
                            "1) class, 2) def, 3) import, 4) return"
        ]
        self.correct_answer = [2,1,1,2]
        self.score_list=[10,15,10,5]

    def question(self):
        self.user_answer = []

        for a in range(len(self.question_list)): 
            print(self.question_list[a])
            print(self.answer_list[a])
            input_answer = int(input("- 정답:"))
            self.user_answer.append(input_answer)

        return self.user_answer

    def result_cal(self):
        score=[]
        for i in range(len(self.user_answer)):
            if self.user_answer[i] == self.correct_answer[i] :
                score.append(int(self.score_list[i]))
                user_sum = sum(score)

        if user_sum >=30 :
            user_score = "A"
        elif user_sum >=20 :
            user_score = "B"
        else:
            user_score = "C"
        print ("--------결과---------")
        print("응답한 내용 : 1번 {}, 2번 {}, 3번 {}, 4번 {}".format(self.user_answer[0], self.user_answer[1],self.user_answer[2], self.user_answer[3]))
        print("당신 응답 합계 : {}점".format(user_sum))
        print("학점은 {}입니다.".format(user_score))

# 클래스의 인스턴스 생성
quiz = QuizTest()

# 메소드 호출
quiz.question()
quiz.result_cal()