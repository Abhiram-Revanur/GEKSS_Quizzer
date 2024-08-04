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
else:
    a = int(a)
    print("""Cool!
      Here we go!
      """)
print("""The rules are pretty simple.
      A question will be printed on your screen where you have to type 1, for the first option, 2 for the second and so.
      """)
s = input("""What do you want to do today?
          1. General Knowledge
          2. Science
          3. Space
          """)
s = int(s)
t = 0
m = 3
while t < 3:
     t += 1
     if s == 1 or s == 2 or s== 3:
          print("Sorry, this is invalid.")
     else:
            s = int(s)
            if s == 1:
                    print("You seem to be interested in the General Knowledge Section.")
                    print("It consists of 2 sub-sections - Cricket and Current Affairs.")

                    print("Section - 1: Sports")
                    q1 = input(print("""Q.1 The most trending thing in India is Cricket, and the recently concluded T20 World Cup.
                                    This is the second time India won the T20 World cup. When was the first time?
                                    1. 2007
                                    2. 2011
                                    3. 1983
                                    4. 2017                        
                                    """))
                    q2 = input(print("""Q.2 A few days ago, in the newspapers, there was this news of an England great bowler playing his last test against WI.
                                    He is also the only to get 700+ test wickets, grabbing this title last match.
                                    Who is this bowler?
                                    1. Jimmie Anderson
                                    2. James Anderson
                                    3. Stuart Broad
                                    4. Ben Stokes                        
                                    """))
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

