# NFL import
from espn_api.football import League

# League data
league_id = 683889
year = 2021
s2 = 'AEBkGcWZaPJjz6qyb4x1aeano%2FBkB3DGnS%2BQxlqtDYWJ%2FkdnubnD%2BkqH%2BqAQQw3WE9aqn7KulmkOGwrKd6QYnNLWNgYoI0DuHPurpWL6Z1sWCE%2B3Cknp%2BjV8TNL389hEXi925y8ofPbLdD2srGVA63qyMx2sLiMb59TPD9s%2BNd%2FwfpiiArAUieHYxEYyGO54%2BGd6EDwKKyF9FKDhWi1R9Xxry3UDIl1rCGCxtbNByuyq5clsPadfwjgODbZk3KUpIJvANM3ZtnxOoOfjX3%2B%2Bt%2B6yqJSO4DTBpumEplSZU1Q5NQ%3D%3D'
swid = '{4C06E684-74DA-46C8-A8C7-83B56D58F2B7}'


# League import
league = League(league_id = league_id, year = year, espn_s2 = s2, swid = swid, debug = False)

print(league.top_scored_week())