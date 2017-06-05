import pandas as pd
import numpy as np
import math
from scipy.spatial.distance import cosine


def get_user_track_array():
  import numpy as np
  user_count = User.query.count()
  track_count = Track.query.count()

  ar = [[0 for col in xrange(track_count)] for row in xrange(user_count)]

  for user in User.query.all():
    user_votes = Vote.query.filter_by(user_id=user.id).all()
    for vote in user_votes:
      if vote.vote_flag:
        ar[user.id - 1][vote.track_id - 1] = 1

  return np.array(ar)

def getScore(history, similarities):
  denumerator = sum(similarities)
  if denumerator == 0:
    return 0

  return sum(history*similarities)/denumerator


original = get_user_track_array()
original_pd = pd.DataFrame(original)
song_to_song = pd.DataFrame(index=original_pd.columns, columns=original_pd.columns)

for i in xrange(len(song_to_song.columns)):
  for j in xrange(len(song_to_song.columns)):
    similarity = 1-cosine(original_pd.ix[:,i],original_pd.ix[:,j])
    song_to_song.ix[i,j] = similarity
    if math.isnan(similarity):
      song_to_song.ix[i,j] = 0

data_neighbours = pd.DataFrame(index=song_to_song.columns,columns=[range(1,11)])

for i in range(0,len(song_to_song.columns)):
  data_neighbours.ix[i,:10] = song_to_song.ix[0:,i].sort_values(ascending=False)[:10].index

data_sims = pd.DataFrame(index=original_pd.index,columns=original_pd.columns)

for i in range(0,len(data_sims.index)):
  for j in range(0,len(data_sims.columns)):
    user = data_sims.index[i]
    product = data_sims.columns[j]

    if original_pd.ix[i][j] == 1:
      data_sims.ix[i][j] = 0
    else:
      product_top_names = data_neighbours.ix[product][1:10]
      product_top_sims = song_to_song.ix[product].sort_values(ascending=False)[1:10]
      user_purchases = original_pd.ix[user,product_top_names]

      data_sims.ix[i][j] = getScore(user_purchases,product_top_sims)


result_dict = {}

for i in xrange(len(data_sims.index)):
  top_matches = data_sims.ix[i,:].sort_values(ascending=False)[0:10].index.values
  result_dict[i+1] = [x + 1 for x in top_matches]

print result_dict
