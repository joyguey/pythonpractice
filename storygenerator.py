#introductions
print ("Hello... there!")
print ("What should I call you?")
name = input()
print ("Hello "+ name +", I want to create a story but I need your help.")
print ("Would you like to help me?")

answer = None
while answer not in ("yes", "no"):
    answer = input("Enter yes or no to continue")
    if answer == "yes":
        pass
    elif answer == "no":
        print ("Fine. Goodbye."),
    else:
        print("Type yes or no, dumdum")

#madlib stories
arcade = '''When I go to the arcade with my <plural noun-1> there are lots of games to play. I spend lots of time there with my friends. In the game X-Men you can be different <plural noun>. The point of the game is to <verb> every robot. You also need to save people. Then you can go to the next level. In the game Star Wars you are Luke Skywalker and you try to destroy every <noun>. In a car racing/motorcycle racing game you need to beat every computerized vehicle that you are <-ing verb> against. There are a whole lot of other cool games. When you play some games you win <plural noun> for certain scores. Once you're done you can cash in your tickets to get a big <noun>. You can save your <plural noun> for another time. When I went to this arcade I didn't believe how much fun it would be. '''
import re
import time

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

#continued prompt location selection
while True:
    place = input("Where would you like to visit after the pandemic is over? You can type 'arcade', 'zoo', 'park', or 'Disneyworld'")
    if place == "arcade":
        madlibs(arcade)
    elif place == "zoo":
        madlib(zoo)
    else: 
        print ("Sorry " +name+ " you can only pick either arcade or zoo. I'm too tired to code the rest.")
        continue 



