#libraries
import re
import time

#introductions
print ("Hello... there!")
print ("What should I call you?")
name = input()
print ("Hello "+ name +", I want to create a story but I need your help.")
print ("Would you like to help me?")

def yes_no_evaluator(answer):
    while answer not in ("yes", "no"):
        if answer == "yes":
            pass
        elif answer == "no":
            print ("Fine. Goodbye."),
        else:
            print("Type yes or no, dumdum")
raw_answer = input("Enter yes or no to continue")
answer = raw_answer.lower().replace(" ","")
yes_no_evaluator(answer)

#madlib stories
arcade = '''When I go to the arcade with my <plural noun-1> there are lots of games to play. I spend lots of time there with my friends. In the game X-Men you can be different <plural noun>. The point of the game is to <verb> every robot. You also need to save people. Then you can go to the next level. In the game Star Wars you are Luke Skywalker and you try to destroy every <noun>. In a car racing/motorcycle racing game you need to beat every computerized vehicle that you are <-ing verb> against. There are a whole lot of other cool games. When you play some games you win <plural noun> for certain scores. Once you're done you can cash in your tickets to get a big <noun>. You can save your <plural noun> for another time. When I went to this arcade I didn't believe how much fun it would be. '''

#this solution I found online but uses the re library
def madlibs(arcade):
    fields = sorted(set( re.findall('<[^>]+>', arcade) ))
    values = input('\nInput a comma-separated list of words to replace the following items'
                   '\n  %s: ' % ','.join(fields)).split(',')
    story = arcade
    for f,v in zip(fields, values):
        story = story.replace(f, v)
    time.sleep(3)
    print('\nHere is the story: \n\n' + story)

#hardcode method
zoo = "Today I went to the zoo. I saw a(n) (adjective) (animal) jumping up and down in its tree. He (verb, past tense) (adverb) through the large tunnel that led to its (adjective1) (noun). I got some peanuts and passed them through the cage to a gigantic gray (animal2) towering above my head. Feeding that animal made me hungry. I went to get (number) scoop(s) of ice cream. It filled my stomach. Afterwards I had to (verb) (adverb1) to catch our bus."
def madlib(zoo):
    adj = str(input("Enter an adjective:"))
    animal = str(input("Enter an animal:"))
    verbpt = str(input("Enter a verb in past-tense:"))
    adverb = str(input ("Enter an adverb:"))
    adj1 = str(input("Enter another adjective:"))
    noun = str(input("Enter another noun:"))
    animal2 = str(input("Enter another animal:"))
    num = str(input ("Enter a number:"))
    verb = str(input ("Enter a verb:"))
    adverb1 = str(input("Enter another adverb:"))

    zoo = zoo.replace ("(adjective)", adj)
    zoo = zoo.replace ("(animal)", animal)
    zoo = zoo.replace ("(verb, past tense)", verbpt)
    zoo = zoo.replace ("(adverb)", adverb)
    zoo = zoo.replace ("(adjective1)", adj1)
    zoo = zoo.replace ("(noun)", noun)
    zoo = zoo.replace ("(animal2)", animal2)
    zoo = zoo.replace ("(number)", num)
    zoo = zoo.replace ("(verb)", verb)
    zoo = zoo.replace ("(adverb1)", adverb1)
    time.sleep (3)
    print("Here is the story: "+ zoo)

#hardcode version 2
disney = "Last month, I went to Disney World with (friend's name). We traveled for (hours) hours by (vehicle). Finally, we arrived and it was very (adjective). There were (adjective1) people (-ing verb) everywhere. There were also people dressed up in (animal) costumes. I wish it had been more (adjective2), but we (past tense verb) anyway. We also went on a ride called Magic (noun). (friend's name) nearly fell off the ride! Later, we went to the hotel and (past tense verb1). Next year, I want to go to (place), where we can (verb)."
def mdlb(disney):
    fn = str(input("Enter a friend's name:"))
    hr = str(input("Enter a number:"))
    vehicle = str(input("Enter a type of vehicle:"))
    adj = str(input ("Enter an adjective:"))
    adj1 = str(input("Enter another adjective:"))
    ing = str(input("Enter a verb ending in -ing:"))
    animal = str(input("Enter an animal:"))
    adj2 = str(input ("Enter another adjective:"))
    pstverb = str(input ("Enter a past tense verb:"))
    noun = str(input("Enter a noun:"))
    pstverb1 = str(input ("Enter another past tense verb:"))
    place = str(input("Enter a place:"))
    verb = str(input("Enter a verb:"))

    keywords = ["(friend's name)","(hours)","(vehicle)","(adjective)","(adjective1)","(-ing verb)","(animal)","(adjective2)","(past tense verb)","(noun)","(past tense verb1)","(place)","(verb)"]
    replacements = [fn,hr,vehicle,adj,adj1,ing,animal,adj2,pstverb,noun,pstverb1,place,verb]
    for key,repl in zip(keywords,replacements):
        disney = disney.replace(key, repl)
    time.sleep(3)
    print("Here is the story:"+disney)

#hardcode version 2 continued
park = "Today, my fabulous camp group went to a an amusement park. It was a fun park with lots of cool (plural noun) and enjoyable play structures. When we got there, my kind counselor shouted loudly, 'Everybody off the (noun).' We all pushed out in a terrible hurry. My counselor handed out yellow tickets, and we scurried in. I was so excited! I couldn't figure out what exciting thing to do first. I saw a scary roller coaster I really liked so, I (adverb) ran over to get in the long line that had about (number) people in it. When I finally got on the roller coaster I was (past tense verb). In fact I was so nervous my two knees were knocking together. This was the (-est adjective) ride I had ever been on! In about two minutes I heard the crank and grinding of the gears. That’s when the ride began! When I got to the bottom, I was a little (past tense verb1) but I was proud of myself. The rest of the day went (adverb1). It was a(n) (adjective1) day at the fun park. "
def mdlib(park):
    pn = str(input("Enter a plural noun:"))
    noun = str(input("Enter a noun:"))
    adverb = str(input("Enter an adverb:"))
    num = str(input ("Enter a number:"))
    pstverb = str(input ("Enter a past tense verb:"))
    adj = str(input("Enter an adjective ending in -est:"))
    pstverb1 = str(input("Enter another past tense verb:"))
    adverb1 = str(input("Enter another adverb:"))
    adj1 = str(input ("Enter another adjective:"))

    keywords = ["(plural noun)","(noun)","(adverb)","(number)","(past tense verb)","(-est adjective)","(past tense verb1)","(adverb1)","(adjective1)"]
    replacements = [pn,noun,adverb,num,pstverb,adj,pstverb1,adverb1,adj1]
    for key,repl in zip(keywords,replacements):
        park = park.replace(key, repl)
    time.sleep(3)
    print("Here is the story:"+park)

#continued prompt location selection
while True:
    place = input("Where would you like to visit after the pandemic is over? You can type 'arcade', 'zoo', 'park', or 'disney' or 'q' to quit")
    if place == "arcade":
        madlibs(arcade)
    elif place == "zoo":
        madlib(zoo)
    elif place == "disney":
        mdlb(disney)
    elif place == "park":
        mdlib(park)
    elif place == "q":
        break
    else: 
        print ("Sorry " +name+ " you can only pick the options listed. I'm too tired to generate more.")
        continue 



