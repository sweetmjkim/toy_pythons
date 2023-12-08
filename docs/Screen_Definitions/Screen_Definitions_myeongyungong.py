# 통계 내기
# 점수 계산 / 학점 출력 
# 변수 : 답항지 문항 [], 정답 [], 점수 합계 [], 점수에 따른 학점 출력 []

# 정해진 숫자를 점수로 치환해서 대입해서 합계를 낸다.

# 문제 정답

score = [10,15,10,5]
list_answer = []

correct = input("번호를 입력하세요 : ")
list_correct = [2,1,1,2]

index = [0,0,0,0]

for number in list_correct:
    for my_score in score:
        result = int(my_score)
        print("{}".format(result))






# 학점 출력
# sum = 점수합계
# my_grade = 학점 출력


def main():
    # print("응답한 내용 : {}".format(list_static))
    print("당신 응답 합계 : {}".format())
    print("학점은 : {}".format())