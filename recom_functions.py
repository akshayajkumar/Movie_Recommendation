from sklearn.metrics.pairwise import cosine_similarity

def recommend_movie(film,movie_dictionary,n=5):
    if film  in movie_dictionary:
        film_vector = movie_dictionary[film]
        dummy_dict = {}
        for m, v in movie_dictionary.items():
            if  m!= film:
                cosine = cosine_similarity([film_vector],[v])[0][0]
                dummy_dict[m] = cosine
        lst=sorted(dummy_dict.items(), key=lambda x: x[1], reverse=True)[:n]
        return [i[0] for i in lst]
    else:
        return "no movie found"
    
def get_high_quality_image(url, width=600, height=900):
    if "UX" in url:
        url = url.replace("UX67", f"UX{width}")
    if "UY" in url:
        url = url.replace("UY98", f"UY{900}")  
    
    if "CR" in url:
        url = url.replace("CR0,0,67,98", f"CR0,0,{width},{height}")
        url = url.replace("CR2,0,67,98", f"CR2,0,{900},{1200}")
    
    return url