# write your code here!
import json, requests

dic = {}
def dollars(currency, rate):
    dollar = currency * rate
    return dollar
def rubles(currency, rate=2.98):
    ruble = currency * rate
    return ruble
def pesos(currency, rate=0.82):
    peso = currency * rate
    return peso
def lempiras(currency, rate=0.17):
    lempira = currency * rate
    return lempira
def australian_dollars(currency, rate=1.9622):
    a_dollar = currency * rate
    return a_dollar
def morrocan_dirhams(currency, rate=0.208):
    dirham = currency * rate
    return dirham
def print_currency():
    coin = int(input('Please, enter the number of conicoins you have: '))
    rate = float(input('Please, enter the exchange rate: '))
    total = dollars(coin, rate)
    print(f'The total amount of dollars: {total}')

def check_rates():
    num = float(input())
    print('I will get {} RUB from the sale of {} conicoins.'.format(round(rubles(num), 2), num))
    print('I will get {} ARS from the sale of {} conicoins.'.format(round(pesos(num), 2), num))
    print('I will get {} HNL from the sale of {} conicoins.'.format(round(lempiras(num), 2), num))
    print('I will get {} AUD from the sale of {} conicoins.'.format(round(australian_dollars(num),2), num))
    print('I will get {} MAD from the sale of {} conicoins.'.format(round(morrocan_dirhams(num),2), num))

def curr(cur, sec):
    global dic
    response = requests.get(f"http://www.floatrates.com/daily/{cur}.json")
    r = response.json()
    to_str = json.dumps(r)
    to_dict = json.loads(to_str)

    for i in to_dict:
        if i == sec.lower():
            dic[i] = to_dict[i]

def calculate_rate(num,sec):
    sec = sec.lower()
    temp = dic[sec]
    rate = temp['rate']
    calculate = rate * num
    code = temp['code']
    print(f'You received {calculate} {code}')

def float_rates():
    read_input = input()
    stop = True
    while stop:

        if read_input == '':
            break
        sec = input()
        if sec == '':
            break
        num = int(input())
        print("Checking the cache...")
        if sec.lower() == 'usd' or sec.lower() == 'eur':
            curr(read_input, sec)

        if sec.lower() in dic:
            print('Oh! It is in the cache!')
            calculate_rate(num, sec)
        else:
            print('Sorry, but it is not in the cache!')
            curr(read_input, sec)
            calculate_rate(num, sec.lower())


float_rates()