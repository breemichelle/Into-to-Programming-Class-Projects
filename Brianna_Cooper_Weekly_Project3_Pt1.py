#display name
print('Brianna Cooper')
#date
print('June 13, 2024')
#class
print('COSC 1336')
#solving for
print('Weekly Project 3 Part 1')



#input player's name, number of at-bats, singles, doubles, triples, and home runs

#import Stats
from Stats import battingAve, sluggingPercentage

def main():
    #get player details
    player_name = input("Enter the player's name: ")

    #get number of at-bats
    at_bats = int(input("Enter the number of at-bats. "))
    #input validation
    if at_bats < 0:
        print("The number of at-bats cannot be negative.")
        input()

    #get the number of singles
    singles = int(input("Enter the number of singles. "))
    #input validation
    if singles < 0:
        print("The number of singles cannot be negative.")
        input()

    #get the number of doubles
    doubles = int(input("Enter the number of doubles. "))
    #input validation
    if doubles < 0:
        print("The number of doubles cannot be negative.")
        input()

    #get the number of triples
    triples = int(input("Enter the number of triples. "))
    #input validation
    if triples < 0:
        print("The number of triples cannot be negative.")
        input()

    #get the number of home runs
    home_runs = int(input("Enter the number of home runs. "))
    #input validation
    if home_runs < 0:
        print("The number of home runs cannot be negative.")
        input()

    #calculate

    total_hits = singles + doubles + triples + home_runs
    batting_average = battingAve(total_hits, at_bats)
    slugging_percentage = sluggingPercentage(singles, doubles, triples, home_runs, at_bats)

    #display

    print('The player name is ', player_name)
    print('The batting average is ', format(batting_average, '.3f'))
    print('The slugging average is ', format(slugging_percentage, '.3f'))

main()
        
    

    
