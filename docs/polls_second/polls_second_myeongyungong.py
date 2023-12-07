# source from ../polls_first/polls_first_myungjunkim.py
# 최종 답
# 1. 상품의 품질에 대해 어떻게 생각하시나요?
# 1. 좋음     2. 중간     3. 좋아지길
# ----------
# 2. 상품의 가격에 대해 어떻게 생각하시나요?    
# 1. 좋음     2. 중간     3. 좋아지길
# ----------
# 3. 상품의 디자인에 대해 어떻게 생각하시나요?    
# 1. 좋음     2. 중간     3. 좋아지길
# ----------
# 4. 상품에 대한 전반적인 만족도는 어떠신가요?    
# 1. 좋음     2. 중간     3. 좋아지길

# 문제
# list_question = [
#     "상품의 품질에 대해 어떻게 생각하시나요?",
#     "상품의 가격에 대해 어떻게 생각하시나요?",
#     "상품의 디자인에 대해 어떻게 생각하시나요?",
#     "상품에 대한 전반적인 만족도는 어떠신가요?"
# ]
# list_answer =  ["좋음", "중간", "좋아지길"]

list_question = ["상품의 품질에 대해 어떻게 생각하시나요?"
                ,"상품의 가격에 대해 어떻게 생각하시나요?"
                ,"상품의 디자인에 대해 어떻게 생각하시나요?"
                ,"상품에 대한 전반적인 만족도는 어떠신가요?"
                ]
list_answer =  ["좋음", "중간", "좋아지길"]
list_answer_number = [0,0,0]

for question in [0, 1, 2, 3] :
    str_question = list_question[question]
    print("{}. {}".format(question+1,str_question))

    for answer in [0, 1, 2] :
        final_answer = list_answer[answer]
        print("{}.{}".format(answer+1, final_answer), end = " ")
        pass
    
    print("")
    # 번호 입력 받기 및 입력한 번호 계산
    number_answer = int(input("당신의 생각은 몇 번 : "))
    index = number_answer - 1
    list_answer_number[index] = list_answer_number[index] + 1
    
    print("--------------------------------------------------------\n")
    pass

# 답항별 갯수 표기
print("답항별 갯수 표시 : {}".format(list_answer_number))

# 답변별 가중치 표기, 어떤 숫자를 더 많이 눌렀나?
print("답변별 가중치(좋음:3, 중간:2, 좋아지길:1)")

# 답항 가중 평균 계산
avg_hight = (list_answer_number[0]*3 + list_answer_number[1]*2 + list_answer_number[2]*1)
avg_low = (list_answer_number[0] + list_answer_number[1] + list_answer_number[2])
avg = avg_hight / avg_low
print("답항 가중 평균 : {}".format(avg))

print("End progrem!")
