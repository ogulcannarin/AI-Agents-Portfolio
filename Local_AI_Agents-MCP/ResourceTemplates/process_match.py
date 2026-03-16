def process_match(match_resource):
    if match_resource is None:
        print("Maç bulunamadı!")
        return
    
    home = match_resource["home_team"]
    away = match_resource["away_team"]
    score = f"{match_resource['home_goals']} - {match_resource['away_goals']}"
    
    print(f"Hafta {match_resource['week']} | Maç {match_resource['match_id']}: {home} vs {away} → Skor: {score}")