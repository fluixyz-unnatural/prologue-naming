import random
import time

jinmei_kanji = []
with open('jinmei_kanji.csv','r') as f:
    jinmei_kanji = f.read().split('\n')[:-1]

seis = []
with open('sei_uniq.csv','r') as f:
    seis = f.read().split('\n')[:-1]

def random_pick (arr):
    i = random.randint(0,len(arr)-1)
    return arr[i]

def generate():
    name_len = random.randint(1,2)
    name = ""
    for i in range(name_len):
        name += random_pick(jinmei_kanji)
    sei = random_pick(seis)
    return (sei+' '+ name)

def main():
    while True:
        print(generate())
        time.sleep(0.1)

if __name__ == '__main__':
    main()