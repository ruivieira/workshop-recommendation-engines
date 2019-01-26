import csv
from scipy import sparse
import numpy as np

def load_data(path):
    max_movie = 0
    max_user = 0
    data = []
    pairs = []
    with open(path, 'rt') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader, None)
        for row in reader:
            movie_id = int(row[0])
            user_id = int(row[1])
            rating = float(row[2])
            max_movie = max(movie_id, max_movie)
            max_user = max(user_id, max_user)
            data.append((movie_id, user_id, rating,))
            pairs.append((movie_id, user_id, ))
    
    ratings = sparse.lil_matrix((max_movie, max_user))
    for d in data:
        ratings[d[0]-1, d[1]-1] = d[2]

    return (ratings, np.array(pairs))