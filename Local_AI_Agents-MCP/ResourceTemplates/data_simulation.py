import random

matches = []

for week in range(1, 39):
    for match_id in range(1, 11):
        match = {
            "week": week,
            "match_id": match_id,
            "home_team": f"Team_{random.randint(1,20)}",
            "away_team": f"Team_{random.randint(1,20)}",
            "home_goals": random.randint(0,5),
            "away_goals": random.randint(0,5)
        }
        matches.append(match)