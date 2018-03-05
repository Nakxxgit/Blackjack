def get_score(player_deck):
    score_sum=0

    for i in player_deck:
        try:
            score_sum+=int(i[1])

        except:
            if i[1] in ['K', 'Q', 'J']:
                score_sum+=10
            if i[1]=='Ace':
                if (score_sum+11)<=21:
                    score_sum+=11
                else:
                    score_sum+=1
    return score_sum