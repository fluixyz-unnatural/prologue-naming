from bs4 import BeautifulSoup

def parse(filename):
    with open(filename,'r') as f:
        soup = BeautifulSoup(f.read(),'html.parser')
        for row in soup.find_all('tr')[1:]:
            items = row.find_all('td')
            sei = items[4].text.replace(items[5].text,'')
            print(sei)

def main():
    parse('0.html')
    parse('1.html')
    parse('2.html')

if __name__ == '__main__':
    main()