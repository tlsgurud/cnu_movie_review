# WebCrowling
# -> Daum News 목록 -> 여러건의 기사와 본문 수집

import requests
from bs4 import BeautifulSoup

url = 'https://news.daum.net/breakingnews/digital'
result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')
url_list = doc.select('ul.list_new2 a.link_txt')
print(len(url_list))
for url in url_list:
    print('## NEWS -> {}번###########################################')
    new_url = url('href')
    print('# URL: {}'.format(new_url))
    result = requests.get(new_url)  # url의 전체 코드를 가져옴
    doc = BeautifulSoup(result.text, 'html.parser')
    title = doc.select('h3.tit_view')[0].get_text()
    contents = doc.select('section p')

    contents.pop(-1)  # 기자 정보 삭제
    content = ''  # 본문 총합
    for info in contents:
        content += info.get_text()


    print('# 뉴스 제목: {}'.format(title))
    print('# 뉴스 본문: {}'.format(content))

