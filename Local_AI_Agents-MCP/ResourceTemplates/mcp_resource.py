from data_simulation import matches

def mcp_resource(uri_template, week, match_id):
    uri = uri_template.format(week=week, match_id=match_id)
    for match in matches:
        if match["week"] == week and match["match_id"] == match_id:
            return match
    return None