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
for question in [0, 1, 2, 3] :
    str_question = list_question[question]
    print("{}".format(question+1), end = " ")
    print("{}".format(str_question))

    for answer in [0, 1, 2] :
        final_answer = list_answer[answer]
        print("{}.{}".format(answer+1, final_answer), end = " ")
    print("")
    print("--------------------------------------------------------")
    pass
print("End progrem!")
