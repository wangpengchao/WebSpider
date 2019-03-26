import requests
import re
import json


def getOnePage(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',

    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    return None


def parseOnePage(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
        re.S
    )
    items = re.findall(pattern, html)

    # print(items, sep='\n')

    for item in items:
        yield{
            'index': item[0],
            'image': item[1],
            'titile': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5].strip() + item[6].strip()
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        print(type(json.dump(content)))
        f.write(json.dump(content, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    url = 'https://maoyan.com/board/4'
    html = getOnePage(url)
    for item in parseOnePage(html):
        write_to_file(item)
        # print(item)


