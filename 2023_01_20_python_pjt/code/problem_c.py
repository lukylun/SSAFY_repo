import json
from pprint import pprint
import problem_b

def movie_info(movies, genres):
    movie_list = []

    for movie in movies:
        movie_list.append(problem_b.movie_info(movie, genres))

    return movie_list
    
    # info_lst = ['id','title','poster_path','vote_average','overview','genre_ids']
    # final_lst = []
    # for movie in movies_list:
    #     info_dict = {}
    #     for i,b in movie.items():
    #         if i in info_lst:
    #             info_dict[i] = b
                

    #     cnt = 0
    #     for j in info_dict['genre_ids']:    
    #         for i in genres_list:
    #             if i['id'] == j:
    #                 info_dict['genre_ids'][cnt] = i['name']
    #                 cnt += 1
    #     final_lst.append(info_dict)
    # return final_lst
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
