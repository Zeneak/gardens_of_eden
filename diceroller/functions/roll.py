import random
#Dice rolling backbone of Gardens of Erden

def roll(active_attribute, active_skill, bonus, target_attribute, target_skill):
    attribute = random.randint(0,int(active_attribute))
    skill= random.randint(0, int(active_skill))
    bonus = int(bonus)
    target_att = random.randint(0,int(target_attribute))
    target_ski = random.randint(0,int(target_skill))
    check_total = attribute + skill + bonus
    target_total = target_att + target_ski
    sux_overflow = check_total - target_total

    if (sux_overflow >= 5)or(sux_overflow <= -5):
        print("Critical", end=" ")
    if (sux_overflow >= 0):
        print("Success!")

    else:
        print("Failure!")
    print('{} + {} + {} = {} total vs {} DC with {} overflow'.format(attribute, skill, bonus, check_total, target_total, sux_overflow))

