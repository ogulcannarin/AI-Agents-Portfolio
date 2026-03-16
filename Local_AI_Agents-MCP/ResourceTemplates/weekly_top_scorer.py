from data_simulation import matches

def weekly_top_scorer(week):
    weekly_matches = [m for m in matches if m["week"] == week]
    team_goals = {}

    for match in weekly_matches:
        # Ev sahibi
        team_goals[match["home_team"]] = team_goals.get(match["home_team"], 0) + match["home_goals"]
        # Deplasman
        team_goals[match["away_team"]] = team_goals.get(match["away_team"], 0) + match["away_goals"]

    # En çok gol atan
    top_team = max(team_goals, key=team_goals.get)
    top_goals = team_goals[top_team]

    return top_team, top_goals