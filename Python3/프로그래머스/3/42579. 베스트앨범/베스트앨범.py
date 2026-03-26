def solution(genres, plays):
    answer = []
    music = []
    for i in range(len(genres)):
        music.append([genres[i],plays[i],i])
    music.sort(key=lambda x: (-x[1],x[2]))
    
    
    genres_dic = {}
    for i in range(len(genres)):
        if genres[i] in genres_dic.keys():
            genres_dic[genres[i]] += plays[i]
        else:
            genres_dic[genres[i]] = plays[i]
    genres_dic = sorted(genres_dic.items(), key=lambda x:-x[1])
    
    for g in genres_dic:
        target_genre = g[0]
        genre_cnt = 0
        for i in range(len(music)):
            if music[i][0] == target_genre:
                answer.append(music[i][2])
                genre_cnt += 1
                if genre_cnt == 2:
                    break
    return answer