
# This is where we start our general Knowledge questions
def cricket(player_name):
    print(f"Welcome to the Cricket Section, {player_name}.")    

    # Here is the list of questions, options and the right answer
    # If you want to add more questions, then follow the same format as the below questions

    questions = [
        {
            "question": "Q1. When did India first win the T20 World Cup?",
            "options": ["2007", "2011", "1983", "2017"],
            "correct_answer": 1,
        },
        {
            "question": "Q2. Which England bowler recently retired after taking 700+ test wickets?",
            "options": [
                "Jimmie Anderson",
                "James Anderson",
                "Stuart Broad",
                "Ben Stokes",
            ],
            "correct_answer": 2,
        },
        {
            "question": "Q3. Which cricketer made a remarkable recovery after a severe accident in December 2022?",
            "options": [
                "K Lokesh Rahul",
                "Rishabh Rajendra Pant",
                "Shreyas Iyer",
                "Mahendra Singh Dhoni",
            ],
            "correct_answer": 2,
        },
        {
            "question": "Q4. Who bowled the 'ball of the century' in the 1993-94 Ashes test?",
            "options": [
                "Ravichandran Ashwin",
                "Adam Zampa",
                "Mark Waugh",
                "Shane Warne",
            ],
            "correct_answer": 4,
        },
        {
            "question": "Q5. Which IPL team's ex-captain said he wouldn't drop out of the race until he leveled with Rohit Sharma preceding 2022?",
            "options": [
                "Shreyas Iyer",
                "Virat Kohli",
                "Pat Cummins",
                "Mahendra Singh Dhoni",
            ],
            "correct_answer": 4,
        },
        {
            "question": "Q6. Which is the most celebrated national cricket league?",
            "options": [
                "Indian Premier League (IPL)",
                "Pakistan Premier League (PPL)",
                "County Cricket",
                "None of the above",
            ],
            "correct_answer": 1,
        },
        {
            "question": "Q7. Which is the team that has won the most number of ODI World cups",
            "options": [
                "India",
                "Australia",
                "West Indies",
                "England",
            ],
            "correct_answer": 2,
        },
        {
            "question": "Q8. Who became the first Indian to take a U-Turn from retirement to play for an overseas league?",
            "options": [
                "Dinesh Karthik",
                "Mahendra SIngh Dhoni",
                "Sachin Tendulkar",
                "Gautam Gambhir",
            ],
            "correct_answer": 1,
        },
        {
            "question": "Q9. If the ball is turned by a pacer in the moment of release to move the ball after pitching, what is it called?",
            "options": [
                "Swing",
                "Turn",
                "Stock",
                "Cutter",
            ],
            "correct_answer": 4,
        }
        {
            "question": "Q10. What is the position known behind the bowler to his left side in the deep for a right-hand batter?",
            "options": [
                "Long-On",
                "Deep Midwicket",
                "Third-Man",
                "Long-Off",
            ]
            "correct_answer": 4,
        }
    ]

    # This is where we keep track of the score
    score = 0
    # Here we are "enumerating", meaning we are giving a number to each element in the list, starting from 1 instead of 0
    # By doing so, we get to map the respective question and the number
    for i, q in enumerate(questions, 1):
        print(f"\n{q['question']}") # Prints the questions
        # Print all the answer options
        for j, option in enumerate(q["options"], 1):
            print(f"{j}. {option}")


        # Here in this while true loop, we make sure that the value that the user gives is valid
        while True:
            try:
                answer = int(input("Your answer (1-4): "))
                if 1 <= answer <= 4:    # If the answer is valid, then continue to the next part
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")

        # If the answer is the right answer, then increase the score
        if answer == q["correct_answer"]:
            print("Correct!")
            score += 1
        else:
            print(
                f"Incorrect. The correct answer was: {q['options'][q['correct_answer']-1]}"
            )

    print(
        f"\nCongratulations {player_name}! You have completed the Cricket quiz."
    )
    # Here we print the final score of the player
    print(f"Your score: {score}/{len(questions)}")
    print(f"Good work, {player_name}. At least you made the attempt of attempting.")
    print("We hope to see you soon!")
    print("Good Bye!")


def Science(player_name):
    print(f"Welcome to the Science Section, {player_name}.")    

    questions = [
        {
            "question": "Q1. How many laws of motion were scripted by Newton?",
            "options": ["3", "4", "5", "13"],
            "correct_answer": 1,
        },
        {
            "question": "Q2. What is the abbrevation of the group that researches the elements?",
            "options": [
                "IPAC",
                "IUPA",
                "IPAUC",
                "IUPAC",
            ],
            "correct_answer": 4,
        },
        {
            "question": "Q3. How many official elements are present in the periodic table?",
            "options": [
                "117",
                "118",
                "119",
                "158",
            ],
            "correct_answer": 2,
        },
        {
            "question": "Q4. Around how many taste buds does an average human have?",
            "options": [
                "25,000",
                "2,50,000",
                "2,500",
                "None of the above",
            ],
            "correct_answer": 1,
        },
        {
            "question": "Q5. Which is the substance within a bone that makes new cells constantly?",
            "options": [
                "Bone Substance",
                "Bone Juice",
                "Bone Mallow",
                "Bone Marrow",
            ],
            "correct_answer": 4,
        },
        {
            "question": "Q6. Did you know that if you swallowed a blade, it would melt within your stomach? Name the acid that aids this.",
            "options": [
                "Hydrochloric Acid",
                "Baking Soda",
                "Bile Juice",
                "None of the above",
            ],
            "correct_answer": 1,
        },
        {
            "question": "Q7. What is liquid that can trap a laser?",
            "options": [
                "Orange Juice",
                "Bile Juice",
                "Blood",
                "Water",
            ],
            "correct_answer": 4,
        },
        {
            "questions": "Q8. What is the hugest provider of oxygen in the world?",
            "options": [
                "Rainforests",
                "Oceans",
                "Grass",
                "Factories",
            ]
            "correct_answer": 2,
        },
        {
            "question": "Q9. With the help of what do aquatic animals navigate around to their homes?",
            "options": [
                "Gravitational Force",
                "Magnetic Force",
                "Magnetic Field of Earth",
                "None of the above",
            ],
            "correct_answer": 3,
        },
        {
            "question": "Q10. How much can a cloud weigh?",
            "options": [
                "A few pounds",
                "A million pounds",
                "A few hundred pounds",
                "A few thousand pounds",
            ],
            "correct_answer": 2,
        },
    ]

    score = 0
    
    for i, q in enumerate(questions, 1):
        print(f"\n{q['question']}") 
        for j, option in enumerate(q["options"], 1):
            print(f"{j}. {option}")


        while True:
            try:
                answer = int(input("Your answer (1-4): "))
                if 1 <= answer <= 4:   
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")

        if answer == q["correct_answer"]:
            print("Correct!")
            score += 1
        else:
            print(
                f"Incorrect. The correct answer was: {q['options'][q['correct_answer']-1]}"
            )

    print(
        f"\nCongratulations {player_name}! You have completed the Science quiz."
    )
    print(f"Your score: {score}/{len(questions)}")
    print(f"Good work, {player_name}. At least you made the attempt of attempting.")
    print("We hope to see you soon!")
    print("Good Bye!")

def Space(player_name):
    print(f"Welcome to the Space Section, {player_name}.")    

    questions = [
        {
            "question": "Q1. In which year was Pluto stopped to be considered a normal planet?",
            "options": ["2006", "2007", "2009", "2004"],
            "correct_answer": 3,
        },
        {
            "question": "Q2. Which is the closest galaxy to the Milkyway?",
            "options": [
                "Andromeda",
                "Andrimica",
                "Creamyway",
                "None of the Above",
            ],
              "correct_answer": 1,
        },
        {
            "question": "Q3. How are the shapes of the orbits of the planets?",
            "options": [
                "Round",
                "Elliptical",
                "Square",
                "Spherical",
            ],
            "correct_answer": 2,
        },
        {
            "question": "Q4. What happened to the first person to say 'The planets revolve around the Earth'?",
            "options": [
                "Welcomed",
                "Burnt",
                "Traumatised",
                "Appreciated",
            ],
            "correct_answer": 2,
        },
        {
            "question": "Q5.  Which was the project launched to our Solar body by India?",
            "options": [
                "Surya L-1",
                "Surya 3",
                "Aditya 11",
                "Aditya L-1",
            ],
            "correct_answer": 4,
        },
        {
            "question": "Q6. The Karman Line is how many kilometers from the earth's surface?",
            "'options": [
                "250",
                "100",
                "50",
                "1000",
            ],
            "correct_answer": 2,
        },
        {
            "question": "Q7. Which of the following have no moons in our solar system?",
            "options": [
                "Mercury",
                "Venus",
                "Both",
                "Neptune",
            ],
            "correct_answer": 3,
        },
        {
            "question": "Q8. What type of star is the sun?",
            "options": [
                "Average",
                "Below average",
                "Small",
                "Big",
            ],
            "correct_answer": 1,
        },
        {
            "questions": "Q9. Sunsets on Mars appear in which colour?",
            "options": [
                "Blue",
                "Orange",
                "Green",
                "None of the above",
            ],
            "correct_answer": 1,
        },
        {
            "question": "Q10. Which planet has the most moons?",
            "options": [
                "Mars",
                "Jupiter",
                "Uranus",
                "None of the above",
            ],
            "correct_answer": 2,
        },
    ]

    score = 0
    
    for i, q in enumerate(questions, 1):
        print(f"\n{q['question']}") 
        for j, option in enumerate(q["options"], 1):
            print(f"{j}. {option}")


        while True:
            try:
                answer = int(input("Your answer (1-4): "))
                if 1 <= answer <= 4:   
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")

        if answer == q["correct_answer"]:
            print("Correct!")
            score += 1
        else:
            print(
                f"Incorrect. The correct answer was: {q['options'][q['correct_answer']-1]}"
            )

    print(
        f"\nCongratulations {player_name}! You have completed the Space quiz."
    )
    print(f"Your score: {score}/{len(questions)}")
    print(f"Good work, {player_name}. At least you made the attempt of attempting.")
    print("We hope to see you soon!")
    print("Good Bye!")


def GK(player_name):
    print(f"Welcome to the General Knowledge Section, {player_name}.")    

    questions = [
        {
            "question": "Q1. Who was the American politician shot in the ear recently?",
            "options": ["Donald Trump", "Kamala Harris", "Joe Biden", "Rishi Sunak"],
            "correct_answer": 1,
        },
        {
            "question": "Q2. Which is one of the rare metals discovered in Sutlej?",
            "options": [
                "Titanium",
                "Manganese",
                "Tantalum",
                "Magnesium",
            ],
              "correct_answer": 3,
        },
        {
            "question": "Q3. When does India bid to hold the Olympics?",
            "options": [
                "2028",
                "2036",
                "2040",
                "2048",
            ],
            "correct_answer": 2,
        },
        {
            "question": "Q4. Which recent Prabhas starrer became a huge international success?",
            "options": [
                "Pushpa : The Rise",
                "Pushpa : The Rule",
                "Saaho",
                "Kalki 2898 AD",
            ],
            "correct_answer": 4,
        },
        {
            "question": "Q5.  Who acted as Peter Parker for the first time in early 2000's?",
            "options": [
                "Tom Holland",
                "Andrew Garfield",
                "Tobey Maguire",
                "None of the Above",
            ],
            "correct_answer": 3,
        },
    ]

    score = 0
    
    for i, q in enumerate(questions, 1):
        print(f"\n{q['question']}") 
        for j, option in enumerate(q["options"], 1):
            print(f"{j}. {option}")


        while True:
            try:
                answer = int(input("Your answer (1-4): "))
                if 1 <= answer <= 4:   
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")

        if answer == q["correct_answer"]:
            print("Correct!")
            score += 1
        else:
            print(
                f"Incorrect. The correct answer was: {q['options'][q['correct_answer']-1]}"
            )

    print(
        f"\nCongratulations {player_name}! You have completed the General Knowledge quiz."
    )
    print(f"Your score: {score}/{len(questions)}")
    print(f"Good work, {player_name}. At least you made the attempt of attempting.")
    print("We hope to see you soon!")
    print("Good Bye!")

def main():
    print("Welcome to C-GEKSS Quizzer!")
    print("Your quizzing pal for Cricket, General Knowledge, Space and Science!")

    player_name = input("Enter your name here participant: ")
    print(f"Hello {player_name}. Welcome to the C-GEKSS Quiz")
    print(
        "The rules are simple: A question will be printed on the screen and you have to answer by typing 1, 2, 3, or 4 for the respective options"
    )

    while True:
        try:
            # Here we are taking the input from the user to see what the user wants to play
            s = int(
                input(
                    "What do you want to be quizzed on today?\n1. Cricket\n2. Science\n3. Space\n4. General Knowledge (1-4): "
                )
            )
            if 1 <= s <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")



    # When you do implement the functions for the Science Quiz and the Space Quiz, fill them here exactly how I have done it
    if s == 1:
        cricket(player_name)
    elif s == 2:
        Science(player_name)
    elif s == 3:
        Space(player_name)
    elif s == 4:
        GK(player_name)
    

if __name__ == "__main__":
    main()

