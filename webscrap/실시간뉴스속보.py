# %%
# http 요청, 응답 수행
import requests
# html 문서 파싱 (DOM 요소 다루듯 쉽게 접근하는 기능 제공)
from bs4 import BeautifulSoup
# 정규표현식
import re
# pandas
import pandas as pd
# 
import matplotlib.pyplot as plt

# %%
# 폰트설정
plt.rc("font", family='Malgun Gothic')

# 마이너스폰트 설정
plt.rc("axes", unicode_minus=False)

# %%
# http 요청
url = 'https://cc.naver.com/cc?a=new.real&r=&i=&bw=939&px=34&py=183&sx=34&sy=183&m=1&nsc=finance.news&u=https://finance.naver.com/news/news_list.naver?mode=LSS2D&section_id=101&section_id2=258&page=2'
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
params = {}
res = requests.get(url, headers = headers, params = params)
res.status_code

# %%
html = BeautifulSoup(res.text, 'html.parser')
html

# %%
# 실시간 뉴스 속보 목록
news_list = html.select_one('#contentarea_left > ul')
type(news_list)

# %%
articleSubject_list = news_list.select('.articleSubject')
articleSummary_list = news_list.select('.articleSummary')
len(articleSubject_list), len(articleSummary_list)

# %%
# 뉴스 제목 목록 가져오기
news_subjects = [subject.text for subject in articleSubject_list]
# 뉴스 링크 목록 가져오기
news_home_url = 'https://finance.naver.com'
news_link = [f"{news_home_url}{subject.select_one('a')['href']}" for subject in articleSubject_list]
# 뉴스 요약 목록 가져오기
news_summaries = [summary.get_text() for summary in articleSummary_list]
# 뉴스 언론사 목록 가져오기
media_companies = [summary.select_one('.press').text for summary in articleSummary_list]
# 뉴스 작성일 목록 가져오기
news_cdates = [summary.select_one('.wdate').text for summary in articleSummary_list]

# %%
"""
- bs4.element.Tag.text       : 엘리먼트 컨텐츠의 모든 텍스트 가져오기
- bs4.element.Tag.get_text() : 엘리먼트 컨텐츠의 첫번째 노드의 텍스트 가져오기
- bs4.element.Tag.contents   : 엘리먼트 컨텐츠를 html로 가져오기
"""

# %%
# zip() 함수를 사용해서 여러 리스트의 요소를 묶기
zipped_lists = zip(news_subjects, news_link, news_summaries, media_companies, news_cdates)
# zip 객체를 리스트로 변환
result_list = list(zipped_lists)
len(result_list[0])

result_list

# %%
[num for num in range(5)]
list([num for num in range(5)])
tuple(num for num in range(5))

# %%
# \n, \t 제거하기
[ tuple(ele.replace('\n', '').replace('\t', '') for ele in t) for t in result_list ]

# %%
result = [ tuple((re.sub(r'[\t\n]|^\s+|\s+$', '', ele)).strip() for ele in t) for t in result_list ]

# %%
col_names = ['제목', 'URL', '요약', '언론사', '작성일시']
df = pd.DataFrame(result, columns = col_names)
df

# %%
df['언론사'].value_counts().plot.bar()

# %%
df.to_excel('실시간뉴스속보.xlsx', index=False)
df.to_csv('실시간뉴스속보.csv', index=False)

# %%
df = pd.read_excel('실시간뉴스속보.xlsx')
df2 = pd.read_csv('실시간뉴스속보.csv')

# %%
df.shape, df2.shape