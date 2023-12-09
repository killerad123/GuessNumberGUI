import random


def hint(guess_ans):
    guess_ans1 = guess_ans

    list = [2, 3, 4, 5, 6, 7, 8, 9]
    divisors = []
    for i in range(1,guess_ans1//2):
         if (guess_ans1 % i == 0):
            divisors.append(i)
    # for nums in list:
    #     if (guess_ans1 % nums == 0):
    #         divisors.append(nums)
    # print(divisors)        
    if(len(divisors)==0):
        print("Its a prime number , Sorry No further hints are available for prime number")
    else:
        indexNumber = random.randint(0,len(divisors)-1)
    # print(f"Hint : Ans is divisible by {random.choice(divisors)}")
        print(f"Hint : Ans is divisible by {divisors[indexNumber]}")


def main():
    print('''
                                Welcome to Just Guess It game !!!!
          ''')
    guess_ans = random.randint(1, 100)
    print(guess_ans)
    print("Press 5 for Hint")
    print("The number will be in between 1 to 100 and there will be 10 chances\n")
    chances_num = []
    # for i in range(1, 11):
    chance=0
    while(True):
        try:
            user_num = int(input("Enter your guess\n"))
        except ValueError:
            print("Invalid Input: Please enter a valid number.")
        else:    
            chances_num.append(user_num)
            chance+=1
            if user_num == guess_ans:
                print(f"Correct guess !!! You won in {chance} chances")
                break
            if (user_num == 5):
                chance-=1
                hint(guess_ans)
                continue
                # to skip the below if else condition bcoz we need to run next input after displaying hint we used continue here

            if chance == 10:
                print(
                    f"Sorry,Chances are finished.Better Luck Next Time and the answer was {guess_ans}")
                print(f"Your numbers was {chances_num}")
            else:
                print("your number is greater than ans" if (
                    user_num > guess_ans) else "your number is less than the ans")
                print(f"Oops!!! Try again . {chance} chances are done ")

    return


main()
