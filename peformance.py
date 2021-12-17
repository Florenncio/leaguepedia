import mwclient
import json
site = mwclient.Site('lol.fandom.com', path='/')

teamName = 'intz'

ScoreboardTeams = site.api('cargoquery',
                    limit='max',
                    tables="ScoreboardTeams",
                    fields="Team, Side, Number, IsWinner, Score, Picks, Bans, GameId, StatsPage",
                    where=f"Team like '{teamName}'",
                    )
jsonDict = json.dumps(ScoreboardTeams, indent=2)
print(jsonDict)