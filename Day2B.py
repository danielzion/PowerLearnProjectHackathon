career_opts = ["Engineer",
                "Artist",
                "Sports person", 
                "Doctor "]

career_question = {'1': "Do you love STEM course like Physics, Mathematics and other Science Subjects?",
                    '2': "Are you passionate about Entertainment and Arts?",
                    '3': "Do you have a thing for sporting activities", 
                    '4': "Are you hospitable and love caring for the sick"}

career_advice = ["Since you live STEM courses, you are advised to become an Engineer", "Because of your passion for Entertainment and Arts, becoming an Artist would be a great career path", 
                    "Since you have a thing for sports, becoming a Sports person would be achievable if you put in more efforts to develop yourself", 
                    "Due to your love for the sick and your affection, becoming a Doctor would be a good career to choose"]


def response():
    print("If your answer is YES")
    for i in career_question:
        print(f"Press {i} -- {career_question[i]}")
    career_input = input("Enter your Response\n")

    if career_input == "1":
        print(f"{career_advice[0]}")
    elif career_input == "2":
        print(f"{career_advice[1]}")
    elif career_input == "3":
        print(f"{career_advice[2]}")
    elif career_input == "4":
        print(f"{career_advice[3]}")
    else:
        print("Invalid Response")
        response()

response()