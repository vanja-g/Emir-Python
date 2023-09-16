def main():
    print("this program determines the distance between to a lightning strike")
    timeelapsed = int(input("how many seconds past after the flash till you heard the sound?:"))
    distancefromthunder = 343*timeelapsed

    print(distancefromthunder)
main()