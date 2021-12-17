import mwclient
import json
site = mwclient.Site('lol.fandom.com', path='/')

teamName = 'intz'
response = site.api('cargoquery',
                    limit='max',
                    tables="Players",
                    fields="ID,Name,Country,Age,Role",
                    where=f"Team like '{teamName}'"
                    )

jsonDict = json.dumps(response, indent=2)
print(jsonDict)