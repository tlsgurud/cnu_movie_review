# NaverMovieReviewList.py
# -> Naver 영화(1개 선택) 리뷰 정보 수집(review, score, writer, date)

import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=206657&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1'
result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

review_list = doc.select('div.score_result > ul > li')

for i, one in enumerate(review_list):
    print('## REVIEW -> {} #############################################################'.format(i+1))
    # 평점 정보 수집
    score = one.select('div.star_score > em')[0].get_text()
    # 리뷰 정보 수집
    review = one.select('div.score_reple > p > span')




    print(':: REVIEW: {}'.format((review)))
    print(':: SCORE: {}'.format(score))