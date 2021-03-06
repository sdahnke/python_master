import csv
import json
import time

import espn_scraper as espn


def ppjson(data):
    print(json.dumps(data, indent=2, sort_keys=True))


with open('D:\\play_by_play.csv', 'w', newline='') as header:
    head_table = csv.writer(header, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
    head_table.writerow(
        ['League', 'Type', 'Year', 'Date', 'Home_Loc', 'Home_Team', 'Home_abbr', 'Home_Score', 'Away_Loc', 'Away_Team',
         'Away_abbr', 'Away_Score'])

leagues = ['nfl', 'ncf']
print(leagues)
for league in leagues:
    teams = espn.get_teams(league)
    print(league, len(teams))
    i = 2008
    while i <= 2017:
        print(i)
        scoreboard_urls = espn.get_all_scoreboard_urls(league, i)
        for scoreboard_url in scoreboard_urls:
            data = espn.get_url(scoreboard_url, cached_path="cached_json")
            # time.sleep(1)
            try:
                for event in data['content']['sbData']['events']:
                    game_type = event['season']['type']
                    game_year = event['season']['year']
                    game_date = event['competitions'][0]['date']
                    home_location = event['competitions'][0]['competitors'][0]['team']['location']
                    home_name = event['competitions'][0]['competitors'][0]['team']['name']
                    home_abbr = event['competitions'][0]['competitors'][0]['team']['abbreviation']
                    home_score = event['competitions'][0]['competitors'][0]['score']
                    away_location = event['competitions'][0]['competitors'][1]['team']['location']
                    away_name = event['competitions'][0]['competitors'][1]['team']['name']
                    away_abbr = event['competitions'][0]['competitors'][1]['team']['abbreviation']
                    away_score = event['competitions'][0]['competitors'][1]['score']
                    with open('D:\\play_by_play.csv', 'a', newline='') as csvfile:
                        writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
                        writer.writerow(
                            [league, game_type, game_year, game_date, home_location, home_name, home_abbr, home_score,
                             away_location, away_name, away_abbr, away_score])
                        # print(league, game_type, game_year, game_date, home_location, home_name, home_abbr, home_score,away_location, away_name, away_abbr, away_score)
            except:
                print("Error")
        time.sleep(5)
        i = i + 1
