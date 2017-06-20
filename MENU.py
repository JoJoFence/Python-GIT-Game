import os
#this is the list of games in the folder
games = ["mapgen","game"]

while True:
    command = input("What do you want to do: ")
    if command == "run":
        for game in games:
            print(game)
        choose = input("Which game to run: ")
        if choose in games:
            #runs the file as long as they are in the same folder
            os.startfile(choose+".py")
    elif command == "load":
        choose = input("What is the file name of the game?")
        choose = choose.replace(".py","")
        games.append(choose)
        print(games)
    else:
        print("The Commands Are:")
        print("run (Takes in the file name of the game without the .py)")
        print("load (Takes in the file name of any python file ")

