import webbrowser
import keyboard
import time


def show_page(url, time_seconds):
    split_3_part = time_seconds/3
    webbrowser.open(url)
    time.sleep(split_3_part)
    print('\r**   ', end=' ')
    time.sleep(split_3_part)
    print('\r**** ', end=' ')
    time.sleep(split_3_part)
    print('\r******', end=' ')
    keyboard.press_and_release('ctrl+w')


def clear_page(number_of_pages):
    webbrowser.open(r'www.google.com')
    for i in range(number_of_pages):
        time.sleep(1)
        keyboard.press_and_release('ctrl+w')
    time.sleep(1)


def full_screen():
    webbrowser.open(r'www.google.com')
    keyboard.press_and_release('ctrl+N')
    keyboard.press_and_release('f11')
    keyboard.press_and_release('ctrl+0')


url_list = [r'https://www.kayak.com/flights/BKK-PIT/2022-10-27?sort=bestflight_a',
            r'https://www.skyscanner.net/transport/flights/BKKT/PIT/221027?adultsv2=1&cabinclass=economy&childrenv2=&currency=USD&rtn=0'
            r'https://www.orbitz.com/Flights-Search?flight-type=on&mode=search&trip=oneway&leg1=from:BKK,to:Pittsburgh+(PIT+-+Pittsburgh+Intl.),departure:10/27/2022TANYT&options=cabinclass:economy&passengers=children:0,adults:1,seniors:0,infantinlap:Y&fromDate=10/27/2022&d1=2022-10-27',
            r'https://www.kayak.com/flights/BKK-PIT/2022-10-27?sort=bestflight_a&fs=airlines=~AA',
            r'https://www.kayak.com/flights/BKK-PIT/2022-10-27?sort=bestflight_a&fs=airlines=~DL',
            r'https://www.kayak.com/flights/BKK-PIT/2022-10-27?sort=bestflight_a&fs=airlines=~UA',
            r'https://www.kayak.com/flights/BKK-PIT/2022-10-27?sort=bestflight_a&fs=airlines=~KE']


print('Start in 15 seconds...')
time.sleep(15)
print('Go..')
reload_seconds = 30

# clear_page(1)
full_screen()
for i in range(10):
    for url in url_list:
        show_page(url, reload_seconds)
