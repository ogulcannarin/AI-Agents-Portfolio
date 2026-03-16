from mcp_resource import mcp_resource
from process_match import process_match
from weekly_top_scorer import weekly_top_scorer

uri_template = "football://match/{week}/{match_id}"

for week in range(1, 39):
    print(f"\n=== Hafta {week} ===")
    for match_id in range(1, 11):
        resource = mcp_resource(uri_template, week, match_id)
        process_match(resource)
    
    top_team, top_goals = weekly_top_scorer(week)
    print(f"Haftanın En Çok Gol Atan Takımı: {top_team} ({top_goals} gol)\n")