import os

pay = []
ordered = []
total_Day = 0

class ConsoleColor:
    # Color
    BLACK = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    GRAY = '\033[97m'

    # Style
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # BackgroundColor
    BgBLACK = '\033[40m'
    BgRED = '\033[41m'
    BgGREEN = '\033[42m'
    BgORANGE = '\033[43m'
    BgBLUE = '\033[44m'
    BgPURPLE = '\033[45m'
    BgCYAN = '\033[46m'
    BgGRAY = '\033[47m'

    # End
    END = '\033[0m'


def finito(n,t):
    os.system('clear')
    print(f'{ConsoleColor.BgBLUE + ConsoleColor.YELLOW + lop + ConsoleColor.END}')
    print('Ordered:')
    for k in ordered:
        print(f'*{k}')
    print('_' * 20)
    bal = sum(pay)
    print(f'Total to pay: {bal}')
    while True:
        ispaid=input('\nPaid? Y/N').lower()
        if ispaid in 'yn':
            if ispaid == 'y':
                t += bal
                pay.clear()
                ordered.clear()
                return t

def topping(n):
    if n == 's':
        pizz_price = 15
        size_pi = 'Small Pizza:$15'
        pepperoni_price = 2
    elif n == 'm':
        pizz_price = 20
        size_pi = 'Medium Pizza:$20'
        pepperoni_price = 3
    else:
        pizz_price = 25
        size_pi = 'large Pizza:$25'
        pepperoni_price = 4
        str_pep = str(pepperoni_price)
    this_sum = []
    tops = []
    tops.append(size_pi)
    this_sum.append(pizz_price)
    while True:
        os.system('clear')
        print(f'{ConsoleColor.BgBLUE + ConsoleColor.YELLOW + lop + ConsoleColor.END}')
        print(f'{ConsoleColor.CYAN + ConsoleColor.BOLD + "Your Toppings:" + ConsoleColor.END}{tops}\n'
              f'{ConsoleColor.CYAN + ConsoleColor.BOLD + "This order:" + ConsoleColor.END} ${sum(this_sum)}')
        print(
            f'{ConsoleColor.UNDERLINE + ConsoleColor.BgRED + ConsoleColor.BOLD + "*Pepperoni - $" + str(pepperoni_price) + ConsoleColor.END} \n'
            f'{ConsoleColor.BOLD + ConsoleColor.UNDERLINE + ConsoleColor.BgORANGE + "*Cheese - $1 " + ConsoleColor.END} ')
        toppings = input(f'Enter:\n{ConsoleColor.BOLD + ConsoleColor.RED + "P" + ConsoleColor.END} - to add Pepperoni\n'
                         f'{ConsoleColor.BOLD + ConsoleColor.RED + "C" + ConsoleColor.END} - to add Cheese\n'
                         f'{ConsoleColor.BOLD + ConsoleColor.RED + "d" + ConsoleColor.END} - to delete order\n'
                         f'{ConsoleColor.BOLD + ConsoleColor.RED + "Q" + ConsoleColor.END} to finish Pizza\n>>').lower()
        if toppings in 'pcdq':
            if toppings == 'p':
                this_sum.append(pepperoni_price)
                tops.append(f'Pepperoni:{pepperoni_price}')
            elif toppings == 'c':

                this_sum.append(1)
                tops.append('Cheese:$1')
            elif toppings == 'd':
                this_sum.clear()
                tops.clear()
            else:
                pay.extend(this_sum)
                ordered.extend(tops)
                break

lop = ''' _____ _                 ____          _              _____           _                 
 |  __ (_)               / __ \        | |            / ____|         | |                
 | |__) | __________ _  | |  | |_ __ __| | ___ _ __  | (___  _   _ ___| |_ ___ _ __ ___  
 |  ___/ |_  /_  / _` | | |  | | '__/ _` |/ _ \ '__|  \___ \| | | / __| __/ _ \ '_ ` _ \ 
 | |   | |/ / / / (_| | | |__| | | | (_| |  __/ |     ____) | |_| \__ \ ||  __/ | | | | |
 |_|   |_/___/___\__,_|  \____/|_|  \__,_|\___|_|    |_____/ \__, |___/\__\___|_| |_| |_|
                                                              __/ |                      
                                                             |___/                       '''


print('Welcome to Pizza House')

print('Choose Your Pizza\nS. Small pizza $15.\nM. Medium Pizza: $20.\nL.Large Pizza $25\nQ - quit')

while True:
    os.system('clear')
    print(f'{ConsoleColor.BgBLUE + ConsoleColor.YELLOW + lop + ConsoleColor.END}')
    print(f'{ConsoleColor.RED + "Orders" + ConsoleColor.END}: {ordered}')
    print(f'{ConsoleColor.RED + "Total to Pay:" + ConsoleColor.END} ${sum(pay)}')
    print(f'{ConsoleColor.RED + "Total today:" + ConsoleColor.END} ${total_Day}')
    print("-" * 30)
    pizza_choice = input(f'Choose the size\n Enter:  {ConsoleColor.RED + "S" + ConsoleColor.END} - Small Pizza.'
                         f' {ConsoleColor.RED + "M" + ConsoleColor.END} = Medium Pizza. {ConsoleColor.RED + "L" + ConsoleColor.END}'
                         f' - Large Pizza {ConsoleColor.RED + "Q" + ConsoleColor.END} - Finish order & Pay\n>>').lower()
    if pizza_choice in 'smlq':
        if pizza_choice in 'sml':
            topping(pizza_choice)
        else:
            total_Day = finito(pay,total_Day)
            # finito(total_Day)

