list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?",
    "상품의 가격에 대해 어떻게 생각하시나요?",
    "상품의 디자인에 대해 어떻게 생각하시나요?",
    "상품에 대한 전반적인 만족도는 어떠신가요?"
]


list_answer =  ["좋음", "중간", "좋아지길"]

for num_first in [0,1,2,3]:
    str_question_number = num_first + 1
    str_question = list_question[num_first]
    print("{}. {}".format(str_question_number,str_question))
    
    for num_second in [0,1,2]:
        str_answer_number = num_second + 1
        str_answer = list_answer[num_second]
        print("{}. {}".format(str_answer_number, str_answer), end = " ")
        
        pass
  
    if num_first < 3:
        print("\n-----------------------------------------\n")
        pass
   
    pass
print("\n")


    
