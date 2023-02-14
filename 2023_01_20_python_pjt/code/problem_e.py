import json


def dec_movies(movies):
    answer = []
    for i in movies_list:
        rev_json = open('data/movies/{}.json'.format(i['id']), encoding='utf-8')
        rev_list = json.load(rev_json)
        if rev_list['release_date'][5:7] == '12':
            answer.append(rev_list['title'])
    return answer
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
