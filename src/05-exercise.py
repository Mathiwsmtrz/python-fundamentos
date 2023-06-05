badge_january = int(input("what is your budget for january? "))
badge_february = int(input("what is your budget for february? "))
badge_march = int(input("what is your budget for march? "))

total = (badge_january + badge_february + badge_march)
average = int(total / 3)

print(f'your total is {total}')
print(f'your avergae budget is {average}')