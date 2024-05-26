from fuzzywuzzy import process
import signal

from classes.Menu import Menu
from classes.TTS import TTS
from classes.User import User
from classes.Orders import Orders

minConfidence = 60

tts = TTS()
menu = Menu()
user = User()
orders = Orders()


################################################################################
########### Application logic ##################################################
################################################################################


def view_menu():
    pass

def new_order():
    pass

def view_history():
    pass


# Acts as the entry point to the system proper
# Will repeately prompt the user to select an option until they leave
def main_menu():
    while True:
        tts.say('''
                Would you like to:
                - View the menu,
                - Place a new order,
                - View order history, or
                - Exit
                '''
        )

        choice = input('')
        while not choice:
            tts.say('''Please enter a valid choice.''')
            choice = input('')


        # Do fuzzy string search here

        match choice:
            case 'menu':
                view_menu()
            case 'order':
                new_order()
            case 'history':
                view_history()
            case 'exit':
                leave()
            case _:
                tts.say('''
                        I could not understand that, please try again.
                        '''
                    )


################################################################################
###########  Initial setup  ####################################################
################################################################################

# Elegantly exit application
def leave():
    tts.say('''
            Thank you for using Kai-bot. We hope to see you again soon!
            '''
    )

    tts.remove()
    exit()


# Catches CTRL-C
def signal_handler(sig, frame):
    leave()


# Ask for users name, don't accept empty string
def get_name() -> str:
    tts.say(
        '''
        What\'s your name?
        '''
    )

    name = input('')
    while not name:
        tts.say('''Please enter a valid name.''')
        name = input('')
    
    return name


def main():
    tts.say(
        '''
        Hello, my name is Kai-Bot, an online food ordering system.
        If you wish to leave at any time, please press control-C.
        '''
    )

    # Get and store user's name
    name = get_name()
    user.set_name(name)

    # Greet user w/ input name
    tts.say(user.get_greeting())

    # Navigate to main logic loop
    main_menu()

    leave()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()







# def confirmOrder(name, storedorders, currentOrder):
#     tts.say('Your order has been processed, thank you for ordering from Kai-Bot')
#     storedorders[name][currentOrderNum] = currentOrder
#     with open('orders.txt', 'w') as f:
#         json.dump(storedorders, f)





# def ordering(name, storedorders, previousOrder=None):
#     currentOrder = previousOrder if previousOrder is not None else {}

#     while True:
#         tts.say('The courses available are:')
#         for thing in menu.keys():
#             tts.say(' - ' + thing.capitalize())
#         tts.say('Which course would you like to order from?')
#         searchCourse = input('')
#         if not searchCourse:
#             if len(currentOrder.keys()) < 3:
#                 tts.say('Your current order is:')
#                 dishes = currentOrder
#                 for dish in dishes:
#                     price = dishes[dish]
#                     tts.say(f"{dish.capitalize():25}     ${price:5.2f}")
#                 tts.say('You need at least 3 items for delivery, please select more')
#                 selectedConfidence = 0
#                 while selectedConfidence < 80:
#                     tts.say('Would you like to:')
#                     tts.say('- Order more items')
#                     tts.say('- Exit')
#                     choice = input('')
#                     if not choice:
#                         return
#                     (selectedChoice, selectedConfidence) = process.extractOne(
#                         choice, ['order more', 'exit'])

#                     if selectedConfidence >= 60:
#                         if selectedChoice == 'exit':
#                             return
#                         elif selectedChoice == 'order more':
#                             return ordering(name, storedorders, currentOrder)
#             else:
#                 tts.say('Your current order is:')
#                 dishes = currentOrder
#                 for dish in dishes:
#                     price = dishes[dish]
#                     tts.say(f"{dish.capitalize():25}    ${price:5.2f}")
#                 tts.say('You have more than 3 items, which is enough for delivery')
#                 tts.say('Would you like to:')
#                 tts.say('- Order more items')
#                 tts.say('- Confirm your order')
#                 tts.say('- Exit')
#                 confirm = input('')
#                 if not confirm:
#                     return
#                 else:
#                     (selectedChoice, selectedConfidence) = process.extractOne(
#                         confirm, ['order more items', 'confirm order', 'exit'])

#                     if selectedChoice == 'order more items':
#                         return ordering(name, storedorders, currentOrder)

#                     elif selectedChoice == 'confirm order':
#                         confirmOrder(name, storedorders, currentOrder)
#                         return

#                     elif selectedChoice == 'exit':
#                         return
#         else:
#             (courseName, confidence) = process.extractOne(
#                 searchCourse, menu.keys())

#             if confidence > minConfidence:
#                 dishes = menu[courseName]
#                 tts.say(f'The {courseName} dishes are:')
#                 for dish in dishes:
#                     price = float(dishes[dish])
#                     tts.say(f'  {dish}   ${price: .2f}')

#             tts.say('Which dish would you like to order?')
#             dish = input(f'').lower().strip()
#             if not dish:
#                 return
#             (dishName, confidence) = process.extractOne(
#                 dish, menu[courseName].keys())
#             price = menu[courseName][dishName]
#             currentOrder[dishName] = price
#             tts.say(f'Ok, {dishName} has been added to the order')


# def menuThing():
#     while True:
#         tts.say(f'The courses available are: ')
#         for thing in menu.keys():
#             tts.say(' - ' + thing.capitalize())
#         tts.say('Which menu would you like to view?')
#         searchCourse = input('')

#         if not searchCourse:
#             return
#         (menuCourse, confidence) = process.extractOne(searchCourse, courses)

#         if confidence > 60:
#             print(('=== ' + menuCourse.capitalize() + ' === ').center(25))
#             dishes = menu[menuCourse]
#             for dish in dishes:
#                 price = dishes[dish]
#                 print(f"{dish.capitalize():25}    ${price:5.2f}")

#             print('')
#             return




# # if name in storedorders.keys():
# #     tts.say(f'Welcome back, {nama}')
# #     currentOrderNum = len(storedorders[name].keys()) + 1
# # else:
# #     storedorders[name] = {}
# #     tts.say(f'Hello {nama}, I hope your doing well')
# #     currentOrderNum = 1



# (firstChoice, minuconfidence) = process.extractOne(
#     hel, ['menu', 'order food', 'previous order', 'exit'])

# if firstChoice == 'menu':
#     menuThing()

# elif firstChoice == 'order food':
#     ordering(name, storedorders)

# elif firstChoice == 'previous order':
#     if currentOrderNum > 1:
#         print(('=== Previous Orders === ').center(25))
#         for order in storedorders[name]:
#             dishes = storedorders[name][order]
#             print(f'Order number {order}'.center(25))
#             for dish in dishes:
#                 price = dishes[dish]
#                 print(f" {dish.capitalize():20}    ${price:5.2f}")
#             print()
#     else:
#         tts.say('You do not have any previous orders')

# elif firstChoice == 'exit':
#     tts.say('Bye now, have a nice day')
#     exit()