print("""Welcome to GEKSS Quizzer!
      Your Quizzing pal for General Knowledge, Space and Sciences!
    """)

n = input("What is your name? ")

def introage():
    xage = input(f"""This is a universal site with no age limits or such stuff, but {n},
      it would help us in our info if you could state your age.
      """)
    return xage

a = introage()

while not a.isdigit():
    print("Sorry, your age is not in integers")
    a = introage()

a = int(a)
print("""Cool!
      Here we go!
      """)
print("""The rules are pretty simple.
      A question will be printed on your screen where you have to type 1, for the first option, 2 for the second and so.
      """)

t = 0
m = 3
while t < m:
    s = input("""What do you want to do today?
          1. General Knowledge
          2. Science
          3. Space
          """)
    
    if not s.isdigit():
        print("Sorry, that's not a valid number.")
        t += 1
        continue

    s = int(s)
    if s in [1, 2, 3]:
        if s == 1:
            print("You seem to be interested in the General Knowledge Section.")
            print("It consists of 2 sub-sections - Cricket and Current Affairs.")

            print("Section - 1: Cricket")
            q1 = input("""Q.1 The most trending thing in India is Cricket, and the recently concluded T20 World Cup.
                        This is the second time India won the T20 World cup. When was the first time?
                        1. 2007
                        2. 2011
                        3. 1983
                        4. 2017                        
                        """)
            q2 = input("""Q.2 A few days ago, in the newspapers, there was this news of an England great bowler playing his last test against WI.
                        He is also the only to get 700+ test wickets, grabbing this title last match.
                        Who is this bowler?
                        1. Jimmie Anderson
                        2. James Anderson
                        3. Stuart Broad
                        4. Ben Stokes                        
                        """)
        

            q3 = input(print("""Q.3 Back in December 2022, a currently star-cricketer suffered an accident.
                            The accident was so severe, he had suffered a 90 degree turn in his leg and was rumoured not to be able to play cricket again.
                            But he made his recovery, back to India's world cup team.
                            Who is this player?
                            1. K Lokesh Rahul
                            2. Rishabh Rajendra Pant
                            3. Shreyas Iyer
                            4. Mahendra Singh Dhoni
                            """))
            q4 = input(print("""Q.4 A spinner is a batsman's delight. But not every spinner.
                            There are a couple of spinners who have made stuff scary for batsmen with their wits.
                            One of them is an Australian who played the 1993-94 Ashes test and bowled the ball of the century with a forty-five degree turn.
                            Who was this great?
                            1. Ravichandran Ashwin
                            2. Adam Zampa
                            3. Mark Waugh
                            4. Shane Warne
                            """))
            q5 = input(print("""Q.5 Which IPL team's ex captain said that he would not drop out of the race until he levelled 
                            fellow Rohit Sharma preceeding 2022?
                            1. Shreyas Iyer
                            2. Virat Kohli
                            3. Pat Cummins
                            4. Mahendra Singh Dhoni
                            """))
            print(f"""Congratulations {n}. 
                You have completed the first Section of your General Knowledge quiz.
                """)
            print("Here are your results!")
            q1 = int(q1)
            if q1 == 1:
                print("Your first answer was right!")
            elif q1 != 1:
                print(f"""Your first asnwer was wrong.
                    The correct answer was option 1 - 2007
                    """)
            q2 = int(q2)
            if q2 == 2:
                print(f"""Your second answer was right""")
            elif q2 != 2:
                print(""" Your second answer was wrong.
                    The right answer was option 2 - James Anderson""")
            q3 = int(q3)
            if q3 == 2:
                print("Rishabh Rajendra Pant was the right answer!")
            elif q3 != 2:
                print("""Your Third answer was wrong!
                    The right asnwer was option 2 - Rishabh Rajendra Pant
                    """)
            q4 = int(4)
            if q4 == 4:
                print("""Shane Warne is the right answer""")
            elif q4 != 4:
                print("""Your fourth answer was wrong.
                    The right asnwer was option 4 - Shane Warne
                    """)
            q5 = int(q5)
            if q5 == 4:
                print("""Way to go!
                    You got your last answer right!
                    """)
            elif q5 != 4:
                print("""I am sorry, but the last answer was wrong.
                    The right answer was Mahendra Singh Dhoni, after gaining
                    his fourth IPL trophy.""")
            print("Section - 2 : Current Affairs")
            c1 = input(f"""Q1. Recently, there was a politcian in USA who was shot in his right ear.
                        Who was he, and where was he shot?
                        1. Joe Biden - Pentagon house.
                        2. Kamala Harris - Chicago
                        3. Donald Trump - Pennsylvenia
                        4. Rishi Sunak - California

                        """)
            c2 = input(f"""Q.2 Which is one of the metals discovered in the Sutlej that is very rare?
                        1. Titanium
                        2. Tantalum
                        3. Magnesium
                        4. Magnesium
                        """)
            c3 = input(f"""Q.3 The current Olympics is taking place in Paris.
                        When does Inida bid to host the olympics?
                        1. 2036
                        2. 2028
                        3. 2040
                        4. 2032
                        """)
            c4 = input(f"""Q.4 Which recent Prabhas starrer reached international greatness within a month of its release?
                        1. Kalki 2898 AD
                        2. Pushpa : The Rise
                        3. Pushpa : The Rule
                        4. Saaho
                        """)
            c5 = input(f"""Q.5 Who acted as Peter Parker for the first time in 2001?
                        1. Tom Holland
                        2. Andrew Garfield
                        3. Robert Downy Jr.
                        4. Tobey Maguire
                        """)
            print("With this, you have completed the second sub-section as well of the General Knowledge section.")
            print("Here are your results!")
            c1 == int(c1)
            if c1 == 3:
                    print("Your first answer was right!")
            elif c1 != 3:
                    print(f"""Your first answer was wrong.
                        The right answer was option 3 - Donal Trump at Pennsylvenia
                        """)
            c2 == int(c2)
            if c2 == 2:
                    print("Your second answer - Tantalum - was right.")
            elif c2 != 2:
                    print(f"""The second answer was wrong.
                        The right answer was option 2 - Tantalum
                        """)
            c3 == int(c3)
            if c3 == 2:
                    print(f"""Your third answer was right.""")
            elif c3 != 2:
                    print(f"""The third answer was wrong.
                        The right answer was option 2 - again.
                        """)
            c4 == int(c4)
            if c4 == 1:
                    print(f"""Kalki 2898 AD is the right answer!""")
            elif c4 != 1:
                    print(f"""I am sorry, but the fourth answer was wrong.
                        The right answer was option 1 - Kalki 2898 AD.
                        """)
            c5 == int(c5)
            if c5 == 4:
                    print(f"""The last answer - Tobey Maguire - was correct as he made an appearance in the movie 'Spider-Man'.""")
            elif c5 != 4:
                    print(f"""The last asnwer was wrong.
                        The right asnwer was Tobey Maguire as he made an apperance in 'Spider-Man'""")
                    
            print (f"""Congratulations {n},
                    You have completed the General Knowledge section.
                    Now that you are done, we have a small request for you from our side - 
                    Do share this site with as many people as possible.
                    """)
            print(f"""Thank you and see you soon, {n} hopefully.""")
            break

        if s == 2:
             print("You have opted for Science.")
             s1 = input(f"""Q.1 The first question comes of Physics, one of the most basic and ground level topics of the subject.
                        Newton discovered Gravity by seeing an appple falll on him. But we also say Newton's laws of Motion.
                        How many laws of Motion has he scripted?
                        1. 3
                        2. 5
                        3. 7
                        4. 6                        
                        """)
             s2 = input(f"""Q.2 As much as our knowledge, there are 118 elements that make the periodic table up.
                        But there have been studies of a 119th element. It is not permanantly fixed or known, but name its temporary name.
                        1. Uranium
                        2. Ununennium
                        3. Nihonium
                        4. Moskovi
                        """)
             s3 = input(f"""Even this is related to chemistry and the periodic table.
                        The constant research of the elemants and chemicals to make the periodic table is conducted by a group.
                        Name the group..
                        1. IPAC
                        2. IUPA
                        3. PAC
                        4. IUPAC                        
                        """)







        else:
            print("Sorry, this is invalid.")
            t += 1
        if t == m:
            print("You have exceeded the maximum number of attempts.")
