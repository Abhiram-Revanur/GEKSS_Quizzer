from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


QUIZZES = {
    "cricket": [
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
        },
        {
            "question": "Q10. What is the position known behind the bowler to his left side in the deep for a right-hand batter?",
            "options": [
                "Long-On",
                "Deep Midwicket",
                "Third-Man",
                "Long-Off",
            ],
            "correct_answer": 4,
        },
        {
            "question": "Q11. After how many years has Sri Lanka beaten India in a bilateral ODI-series?",
            "options": [
                "27",
                "28",
                "29",
                "21",
            ],
            "correct_answer": 1,
        },
        {
            "question": "Q12. What is the full-form of the famous Australian cricket ground SCG?",
            "options": [
                "Scorchers Cricket Ground",
                "Samurai Cricket Ground",
                "Southern Cricket Ground",
                "Sydney Cricket Ground",
            ],
            "correct_answer": 4,
        },
        {
            "question": "Q13. Which ground is known as the home of cricket?",
            "options": [
                "Oval",
                "Lords",
                "Wankhade Stadium",
                "Gods",
            ],
            "correct_answer": 2,
        },
        {
            "question": "Q14. The first cricket match was played 180 years ago between which two countries?",
            "options": [
                "England and Australia",
                "Australia and West Indies",
                "England and South Africa",
                "USA and Canada",
            ],
            "correct_answer": 4,
        },
        {
            "question": "Q15. When were the first laws of cricket published?",
            "options": [
                "2014",
                "1679",
                "1744",
                "1771",
            ],
            "correct_answer": 3,
        },
    ],
    "science": [
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
            "question": "Q7. What is the liquid that can trap a laser?",
            "options": [
                "Orange Juice",
                "Bile Juice",
                "Blood",
                "Water",
            ],
            "correct_answer": 4,
        },
        {
            "question": "Q8. What is the hugest provider of oxygen in the world?",
            "options": [
                "Rainforests",
                "Oceans",
                "Grass",
                "Factories",
            ],
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
        {
            "question": "Q11. Botany is the study of ",
            "options": [
                "Organisms",
                "Motion",
                "Creation",
                "Plants",
            ],
            "correct_answer": 4,
        },
        {
            "question": "Q12. What are the three-dimensions?",
            "options": [
                "Length, breadth, and weight",
                "Length, height and weight",
                "Length, width and breadth",
                "None of the above",
            ],
            "correct_answer": 4,
        },
        {
            "question": "Q13. What is the process of rain in the water cycle known as?",
            "options": [
                "Precipitation",
                "Drizzling",
                "Raining",
                "None of the above",
            ],
            "correct_answer": 1,
        },
        {
            "question": "Q14. Sound waves travel through the help of ",
            "options": [
                "Water",
                "Air",
                "Oceans",
                "None of the above",
            ],
            "correct_answer": 2,
        },
        {
            "question": "Q15. Milk turns to curd due to ",
            "options": [
                "Microbes",
                "Water",
                "Air",
                "Exposure",
            ],
            "correct_answer": 1,
        },
    ],
    "space": [
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
            "question": "Q4. What did people do to Nicolaus Copernicus when he said, 'The sun doesn't revolve around the earth, but the earth revolves around the sun?'",
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
            "options": [
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
            "question": "Q9. Sunsets on Mars appear in which colour?",
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
        {
            "question": "Q11. The speciality of the Chandrayaan-3 mission was that it ",
            "options": [
                "Landed on the other side of the moon",
                "Discovered human skeletons",
                "Crash landed but was still functional",
                "None of the above",
            ],
            "correct_answer": 1,
        },
        {
            "question": "Q12. Nothing can escape a black hole due to the fact that it has a huge ",
            "options": [
                "Space",
                "Gravitational pull",
                "Magnetic pull",
                "Magnetic field",
            ],
            "correct_answer": 2,
        },
        {
            "question": "Q13. What are groups of stars in our sky called?",
            "options": [
                "Satellites",
                "Star Groups",
                "Karman",
                "None of the above",
            ],
            "correct_answer": 4,
        },
        {
            "question": "Q14. What is the top-most layer in our atmosphere known as?",
            "options": [
                "Stratosphere",
                "Exosphere",
                "Outo-sphere",
                "Outersphere",
            ],
            "correct_answer": 2,
        },
        {
            "question": "Q15. Which is the disc shaped ring outside Neptune around 30 Astronomical Units (AU)?",
            "options": [
                "Asteroid Belt",
                "Helio Pause",
                "Kuiper Belt",
                "None of the above",
            ],
            "correct_answer": 3,
        },
    ],
    "gk": [
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
        {
            "question": "Q6. When did the modern olympic games take place for thr first time?",
            "options": [
                "1986",
                "1896",
                "550 BCE",
                "None of the above",
            ],
            "correct_answer": 2,
        },
        {
            "question": "Q7. Lake Turkana, recently seen in the news, is located in which country?",
            "options": [
                "Kenya",
                "Nigeria",
                "Russia",
                "Egypt",
            ],
            "correct_answer": 1,
        },
        {
            "question": "Q8. On Aug 8, which state made its first 'Grain ATM' used to improve food quality?",
            "options": [
                "Karnataka",
                "Rajasthan",
                "West Bengal",
                "Odisha",
            ],
            "correct_answer": 4,
        },
        {
            "question": "Q9. The GBR (Great Barrier Reef) is facing its highest temperatures in around how many years?",
            "options": [
                "400",
                "250",
                "780",
                "None of the above",
            ],
            "correct_answer": 1,
        },
        {
            "question": "Q10. Recently, which state government has approved Logistic Policy 2024 to create five lakhs job opportunities?",
            "options": [
                "Assam",
                "Uttar Pradesh",
                "Karnataka",
                "Maharashtra",
            ],
            "correct_answer": 4,
        },
        {
            "question": "Q11. Where is India conducting the 'Parvat Prahaar' Military Exercise?",
            "options": [
                "Tibet",
                "Nepal",
                "Ladakh",
                "Punjab",
            ],
        "correct_answer": 3,
        },
        {
            "question": "Q12. Among which two countries is the Mahakali River a border according to the 1816 treaty of Sugauli?",
            "options": [
                "India and Bhutan",
                "Bhutan and Nepal",
                "India and Nepal",
                "None of the above",
            ],
            "correct_answer": 3,
        },
        {
            "question": "Q13. Which is the first state to adopt the Disaster Insurance?",
            "options": [
                "Nagaland",
                "Maharashtra",
                "Tamil Nadu",
                "Kerala",
            ],
            "correct_answer": 1,
        },
        {
            "question": "Q14. Which state Chief Minister has been awarded the Lee Kuan Yew Exchange Fellowship?",
            "options": [
                "West Bengal",
                "Bihar",
                "Assam",
                "None of the above",
            ],
            "correct_answer": 3,
        },
        {
            "question": "Q15. Swati Nayak, who was in the news, has won which award?",
            "options": [
                "Norman E. Borlaug award",
                "Booker award",
                "Jnana Peetha award",
                "None of the above",
            ],
            "correct_answer": 1,
        },
    ],
    "Defence" : [
        {
            "question" : "Q1. Where is the first 'Indian Air Force Heritage Museum' located in India?",
            "options" : [
                "Chandigarh",
                "Bangalore",
                "Chennai",
                "None of the above",
            ],
            "correct_answer": 1,
        },
        {
            "question" : "Q2. How many seats are reserved in NDA for Naval Cadets?",
            "options" : [
                "48",
                "72",
                "42",
                "108",
            ],
            "correct_answer": 3,
        },
        {
            "question" : "Q3. Where is the Officers' Training Academy located?",
            "options" : [
                "Pune",
                "Bombay",
                "Bangalore",
                "Chennai",
            ],
            "correct_answer": 4,
        },
        {
            "question" : "Q4. How long is the corse at the Officer's Training Academy?",
            "options" : [
                "5 Weeks",
                "49 Weeks",
                "40 Weeks",
                "None of the above",
            ],
            "correct_answer": 2,
        },
        {
            "question" : "Q5. 'Bharat Drone Shakti Exhibition 2023' was inaugurated in which state?",
            "options" : [
                "Telangana",
                "Uttar Pradesh",
                "Andhra Pradesh",
                "Himachal Pradesh",
            ],
            "correct_answer": 2,
        },
        {
            "question" : "Q6. What is the motto of Indian Army?",
            "options" : [
                "Seva Paramo Dharm",
                "Self before Service",
                "Nation first",
                "None of the above",
            ],
            "correct_answer": 1,
        },
        {
            "question" : "Q7. Who inaugurated the Bharat Drone Shakti exhibition 2023?",
            "options" : [
                "Defence Minister - Rajnath Singh",
                "Finance Minister - Nirmala Sitharaman",
                "Prime Minister - Narendra Modi",
                "President - Draupadi Murmu",
            ],
            "correct_answer": 1,
        },
        {
            "question" : "Q8. Which was the search and rescue mission by India to Syria and Turkey after the earthquake in 2023?",
            "options" : [
                "Operation Earthquake",
                "Operation Vijay",
                "Operation Dost",
                "Operation Rakshak",
            ],
            "correct_answer": 3,
        },
        {
            "question" : "Q9. Which was the first war India fought post independence for itself?",
            "options" : [
                "1947 Indo-Pak War",
                "1946 Indo-Sino War",
                "1962 Indo-Sino War",
                "None of the above",
            ],
            "correct_answer": 1,
        },
        {
            "question" : "Q10. Operation Gibraltar was launched by which country against India?",
            "options" : [
                "China",
                "Pakistan",
                "Saudi Arabia",
                "Japan",
            ],
            "correct_answer" : 2,
        },
        {
            "question" : "Q11. What is the name of the border that India shares with China?",
            "options" : [
                "Line Of Control (LOC)",
                "Line of Actual Control (LAC)",
                "The Great Wall",
                "None of the above",
            ],
            "correct_answer" : 2,
        },
        {
            "question" : "Q12. When was operation Sajag launched?",
            "options" : [
                "24 January 2021",
                "4 October 2021",
                "5 November 2021",
                "None of the above",
            ],
            "correct_answer" : 2,
        },
        {
            "question" : "Q13. Which force launched Operation Meghdoot?",
            "options" : [
                "Indian Air Force",
                "Indian Army",
                "Indian Navy",
                "Para SF Forces of India",
            ],
            "correct_answer" : 1,
        },
        {
            "question" : "Q14. Which was the operation launched by Indian Navy in 1971?",
            "options" : [
                "Operation Trident",
                "Operation Meghdoot",
                "Operation Vijay",
                "None of the above?",
            ],
            "correct_asnwer" : 1,
        },
        {
            "question" : "Q15. Which is the war also known as the 'Bangladesh Liberation War'?",
            "options" : [
                "1965 Indo-Sino war",
                "1962 Indo-Sino war",
                "1971 Indo-Pak war",
                "None of the above",
            ],
            "correct_answer" : 3,
        }
    ],
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz/<category>', methods=['GET', 'POST'])
def quiz(category):
    if category not in QUIZZES:
        return redirect(url_for('index'))
    
    questions = QUIZZES[category]
    score = 0
    incorrect_answers = []
    if request.method == "POST":
        for question in questions:
            answer = request.form.get(f"question_{question['question']}")
            if answer and int(answer) == question['correct_answer']:
                score += 1
            else:
                incorrect_answers.append({
                    'question': question['question'],
                    'user_answer': question['options'][int(answer)-1] if answer else "Not answered",
                    'correct_answer': question['options'][question['correct_answer']-1]
                })
        
        return render_template('results.html', score=score, total=len(questions), category=category, incorrect_answers=incorrect_answers)
    
    return render_template('quiz.html', questions=questions, category=category)

if __name__ == "__main__":
    app.run(debug=True)
