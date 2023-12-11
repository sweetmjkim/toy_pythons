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