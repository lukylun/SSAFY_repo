import json

# 90년대 개봉작 중 많은 수입을 올린 순위
def my_date(m):
    rev_90 = {}
    for i in movie_list:
        rev_json = open('data/movies/{}.json'.format(i['id']), encoding='utf-8')
        rev_list = json.load(rev_json)
        if rev_list['release_date'][2] == '9':
            rev_90[rev_list['title']] = rev_list['revenue']

    
    return sorted(rev_90, reverse=True, key=lambda x:rev_90[x]) # 영화제목만 출력
    sorted(rev_90.items(), reverse=True, key = lambda x:x[1]) # 영화제목, 수입 출력

# 배급한 영화가 많은 순으로 배급사 정렬
def rank_cmpn(m):
    prod_com = []
    for i in movie_list:
        com_json = open('data/movies/{}.json'.format(i['id']), encoding='utf-8')
        com_list = json.load(com_json)
        for com in com_list['production_companies']:
            prod_com.append(com['name'])

    prod_dict = {i:0 for i in set(prod_com)}
    
    for prod in prod_com:
        prod_dict[prod] += 1

    return sorted(prod_dict, reverse = True, key = lambda x:prod_dict[x]) 
    # return sorted(prod_dict.items(), reverse = True, key = lambda x:x[1]) 

if __name__ == '__main__':
    movie_open = open('data/movies.json', encoding='utf-8')
    movie_list = json.load(movie_open)

    print('배급사 순위:', rank_cmpn(movie_list))
    print('90년대 영화 수입 순위:', my_date(movie_list))
    