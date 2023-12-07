# source from ..polls_first/polls_first_myungjunkim.py


list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?",
    "상품의 가격에 대해 어떻게 생각하시나요?",
    "상품의 디자인에 대해 어떻게 생각하시나요?",
    "상품에 대한 전반적인 만족도는 어떠신가요?"
]

list_answer =  ["좋음", "중간", "좋아지길"]
list_index_answer =  [0 , 0, 0]
for num_first in [0,1,2,3]:
    str_question_number = num_first + 1
    str_question = list_question[num_first]
    print("{}. {}".format(str_question_number,str_question))
    
    for num_second in [0,1,2]:
        str_answer_number = num_second + 1
        str_answer = list_answer[num_second]
        print("{}. {}".format(str_answer_number, str_answer), end = " ")
        pass


    if num_first <= 3:
        print("\n")
        str_question_result = input("당신 생각은 몇번 : ")
        num_question_result = int(str_question_result) # 문자를 숫자로 변환
        index = num_question_result - 1 # index 위치값 적용


        print("-----------------------------------------")
    list_index_answer[index] = list_index_answer[index] + 1
    pass


print("")
print("---------------- 통 계 ----------------")
print("설문자 답항별 갯수 표시 : {} ".format(list_index_answer))
print("\n")

weighted_mean = ((list_index_answer[0] * 3) + (list_index_answer[1] * 2) +(list_index_answer[2] * 1)) / (list_index_answer[0] + list_index_answer[1] + list_index_answer[2])
print(weighted_mean)
