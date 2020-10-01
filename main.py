def spliter(num, people):
    overall = round(num / people)
    newone = overall * people
    exact = round(num / people, 2)
    print(f"{exact} bucks per head")
    if num < newone:
        final = newone - num
        print(f"{final} bucks goes as tip, if everybody pays {overall}")
    elif num > newone:
        final = num - newone
        print(f"{final} bucks extra someone has to pay,if everybody pays {overall}")


if __name__ == '__main__':
    amount = int(input("Enter the Number to split: "))
    divisor = int(input("Split between: "))
    spliter(amount, divisor)