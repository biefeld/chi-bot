from fuzzywuzzy import process
import en_core_web_sm
# import win32com.client as wincl
import json

from gtts import gTTS
import playsound
import os

# speak = wincl.Dispatch("SAPI.SpVoice")
minConfidence = 60
tts = gTTS('a')



def retrieveOrders():
    try:
        with open('orders.txt', 'r') as f:
            orders = json.load(f)
    except FileNotFoundError:
        orders = {}
    return orders


storedorders = retrieveOrders()


def confirmOrder(name, storedorders, currentOrder):
    say('Your order has been processed, thank you for ordering from Chi-Bot')
    storedorders[name][currentOrderNum] = currentOrder
    with open('orders.txt', 'w') as f:
        json.dump(storedorders, f)


def say(text):
    tts.text = text
    tts.save('text.mp3')
    playsound.playsound('text.mp3')
    os.remove('text.mp3')


def ordering(name, storedorders, previousOrder=None):
    currentOrder = previousOrder if previousOrder is not None else {}

    while True:
        say('The courses available are:')
        for thing in menu.keys():
            say(' - ' + thing.capitalize())
        say('Which course would you like to order from?')
        searchCourse = input('')
        if not searchCourse:
            if len(currentOrder.keys()) < 3:
                say('Your current order is:')
                dishes = currentOrder
                for dish in dishes:
                    price = dishes[dish]
                    say(f"{dish.capitalize():25}     ${price:5.2f}")
                say('You need at least 3 items for delivery, please select more')
                selectedConfidence = 0
                while selectedConfidence < 80:
                    say('Would you like to:')
                    say('- Order more items')
                    say('- Exit')
                    choice = input('')
                    if not choice:
                        return
                    (selectedChoice, selectedConfidence) = process.extractOne(
                        choice, ['order more', 'exit'])

                    if selectedConfidence >= 60:
                        if selectedChoice == 'exit':
                            return
                        elif selectedChoice == 'order more':
                            return ordering(name, storedorders, currentOrder)
            else:
                say('Your current order is:')
                dishes = currentOrder
                for dish in dishes:
                    price = dishes[dish]
                    say(f"{dish.capitalize():25}    ${price:5.2f}")
                say('You have more than 3 items, which is enough for delivery')
                say('Would you like to:')
                say('- Order more items')
                say('- Confirm your order')
                say('- Exit')
                confirm = input('')
                if not confirm:
                    return
                else:
                    (selectedChoice, selectedConfidence) = process.extractOne(
                        confirm, ['order more items', 'confirm order', 'exit'])

                    if selectedChoice == 'order more items':
                        return ordering(name, storedorders, currentOrder)

                    elif selectedChoice == 'confirm order':
                        confirmOrder(name, storedorders, currentOrder)
                        return

                    elif selectedChoice == 'exit':
                        return
        else:
            (courseName, confidence) = process.extractOne(
                searchCourse, menu.keys())

            if confidence > minConfidence:
                dishes = menu[courseName]
                say(f'The {courseName} dishes are:')
                for dish in dishes:
                    price = float(dishes[dish])
                    say(f'  {dish}   ${price: .2f}')

            say('Which dish would you like to order?')
            dish = input(f'').lower().strip()
            if not dish:
                return
            (dishName, confidence) = process.extractOne(
                dish, menu[courseName].keys())
            price = menu[courseName][dishName]
            currentOrder[dishName] = price
            say(f'Ok, {dishName} has been added to the order')


def dec():
    say('Would you like to:')
    say('- See the menu')
    say('- Order food')
    say('- See previous orders')
    say('- Exit')


def menuThing():
    while True:
        say(f'The courses available are: ')
        for thing in menu.keys():
            say(' - ' + thing.capitalize())
        say('Which menu would you like to view?')
        searchCourse = input('')

        if not searchCourse:
            return
        (menuCourse, confidence) = process.extractOne(searchCourse, courses)

        if confidence > 60:
            print(('=== ' + menuCourse.capitalize() + ' === ').center(25))
            dishes = menu[menuCourse]
            for dish in dishes:
                price = dishes[dish]
                print(f"{dish.capitalize():25}    ${price:5.2f}")

            print('')
            return


menu = {
    'starter': {
        'spring rolls': 4.00,
        'dumplings': 5.50,
        'pork buns': 7.50
    },

    'main': {
        'peking duck': 24.00,
        'sweet n sour pork': 19.00
    },

    'dessert': {
        'red bean buns': 10.00,
        'egg tart': 9.50
    }
}

courses = list(menu.keys())


say('Hello, my name is Chi-Bot, an online food ordering system.')

nlp = en_core_web_sm.load()
say("What's your name?")
name = input('')
# doc = nlp(name + ' and')
# print(doc)
# XA = [(X.text, X.label_) for X in doc.ents]
# (name, type) = XA[0]


nama = name.capitalize()


if name in storedorders.keys():
    say(f'Welcome back, {nama}')
    currentOrderNum = len(storedorders[name].keys()) + 1
else:
    storedorders[name] = {}
    say(f'Hello {nama}, I hope your doing well')
    currentOrderNum = 1
say('If you wish to stop a request at any time, please enter nothing')

minuconfidence = 50

while True:
    dec()

    hel = input('')

    if not hel:
        exit()

    else:
        (firstChoice, minuconfidence) = process.extractOne(
            hel, ['menu', 'order food', 'previous order', 'exit'])

        if firstChoice == 'menu':
            menuThing()

        elif firstChoice == 'order food':
            ordering(name, storedorders)

        elif firstChoice == 'previous order':
            if currentOrderNum > 1:
                print(('=== Previous Orders === ').center(25))
                for order in storedorders[name]:
                    dishes = storedorders[name][order]
                    print(f'Order number {order}'.center(25))
                    for dish in dishes:
                        price = dishes[dish]
                        print(f" {dish.capitalize():20}    ${price:5.2f}")
                    print()
            else:
                say('You do not have any previous orders')

        elif firstChoice == 'exit':
            say('Bye now, have a nice day')
            exit()
