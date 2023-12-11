# 입력한 값으로 점수 합계(진행중)
class Calculate:
    def __init__(self) : 
        pass

    def cal_score(self):

        user_answer = [0,0,0,0]     # 입력 받을 정답 변수 
        list_score = [10,15,10,5]   # 정답에 따른 점수 변수
        score = 0                   # 합산 변수

        for i in range(len(user_answer)):
            input_answer = int(input("정답 입력 : ")) # 정답 입력받을 변수
            user_answer[i] = input_answer # user_answer에 정답 삽입

            # 정답 입력 번호 시 점수 합산
            if input_answer == 2:
                score += list_score[i]
            elif input_answer == 1:
                score += list_score[i]
        

    def main(self,user_answer,score): # 등급 매기고 출력
        # 등급 매기기
        if score >= 30:
            user_grade = 'A'
        elif score >= 20:
            user_grade = 'B'
        else :
            user_grade = 'C'
        
        print("응답결과 : 1번 : {} 2번 : {}, 3번 : {}, 4번 : {}".format(user_answer[0],user_answer[1],user_answer[2],user_answer[3]))
        print("합산 점수 : {}".format(score))
        print("등급 : {}".format(user_grade))

        
   

calculate = Calculate()
calculate.cal_score()
calculate.main()
