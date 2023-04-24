from collections import Counter
def solution(participant, completion):
    player = participant+completion
    player =Counter(player)

    for i, v in player.items():
        if v%2 !=0:
            return i