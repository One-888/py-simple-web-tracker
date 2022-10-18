import webbrowser
import keyboard
import time


def show_page(url, time_seconds):
    webbrowser.open(url)
    time.sleep(time_seconds)
    keyboard.press_and_release('ctrl+w')


url_list = [r'https://www.kayak.com/flights/BKK-PIT/2022-10-27?sort=bestflight_a',
            r'https://www.skyscanner.net/transport/flights/BKKT/PIT/221027?adultsv2=1&cabinclass=economy&childrenv2=&currency=USD&rtn=0'
            r'https://www.orbitz.com/Flights-Search?flight-type=on&mode=search&trip=oneway&leg1=from:BKK,to:Pittsburgh+(PIT+-+Pittsburgh+Intl.),departure:10/27/2022TANYT&options=cabinclass:economy&passengers=children:0,adults:1,seniors:0,infantinlap:Y&fromDate=10/27/2022&d1=2022-10-27',
            r'https://www.united.com/en/us/fsr/choose-flights?f=BKK&t=PIT&d=2022-10-26&tt=1&sc=7&px=1&taxng=1&newHP=True&clm=7&st=bestmatches&tqp=R&fareWheel=False',
            r'https://www.kayak.com/flights/BKK-PIT/2022-10-27?sort=bestflight_a&fs=airlines=~AA',
            r'https://www.kayak.com/flights/BKK-PIT/2022-10-27?sort=bestflight_a&fs=airlines=~DL',
            r'https://www.kayak.com/flights/BKK-PIT/2022-10-27?sort=bestflight_a&fs=airlines=~UA',
            r'https://www.kayak.com/flights/BKK-PIT/2022-10-27?sort=bestflight_a&fs=airlines=~KE']


print('Start in 15 seconds...')
time.sleep(15)
reload_seconds = 30

for i in range(10):
    for url in url_list:
        show_page(url, reload_seconds)
