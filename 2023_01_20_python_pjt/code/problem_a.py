import json
from pprint import pprint


def movie_info(movie):
    info_dict = {'id': movie.get('id'),
    'title': movie.get('title'),
    'vote_average': movie.get('vote_average'),
    'overview': movie.get('overview'),
    'genre_ids': movie.get('genre_ids')
    }

    return info_dict
    
    # info_dict = {}
    # info_lst = ['id','title','poster_path','vote_average','overview','genre_ids']
    # for i, b in movie_dict.items():
    #     if i in info_lst:
    #         info_dict[i] = b
    # return info_dict
    # 여기에 코드를 작성합니다.    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
