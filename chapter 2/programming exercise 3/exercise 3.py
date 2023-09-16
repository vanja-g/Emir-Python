def main():
    print("this program computes the average of 3 exam scores")
    score1, score2, score3= eval(input("enter 3 scores seperated by a comma"))
    average= (score1 + score2 + score3 / 2)
    print("the average of the scores is", average)

main()