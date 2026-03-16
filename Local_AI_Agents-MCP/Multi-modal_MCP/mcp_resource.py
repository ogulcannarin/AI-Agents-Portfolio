def mcp_resource(uri_template, week, match_id, extras=None):
    uri = uri_template.format(week=week, match_id=match_id)
    return {
        "uri": uri,
        "week": week,
        "match_id": match_id,
        "score": extras.get("score") if extras else None,
        "heatmap": extras.get("heatmap") if extras else None
    }