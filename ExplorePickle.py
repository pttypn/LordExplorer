import pickle
dbtype = {'Barrington': 'ner',
         'Bristol': 'ner',
         'Burrillville': 'ner',
         'CentralFalls': 'ner',
         'Charlestown': 'vis',
          #'Coventry':'ner',
         'Cranston': 'vis',
         'Cumberland': 'vis',
         'EastGreen': 'ner',
         'EastProv': 'ner',
         'Exeter': 'vis',
         'Foster': 'vis',
         'Glocester': 'vis',
         #'Hopkinton': 'vis',
          'Jamestown':'ner',
         'Johnston': 'vis',
         'Lincoln': 'vis',
         'LittleCompton': 'vis',
         'Middletown': 'vis',
          'Narragansett':'ner',
         'NewShore': 'vis',
         'Newport': 'ner',
         'NorthKing': 'vis',
         'NorthProv': 'ner',
         'NorthSmith': 'ner',
         'Pawtucket': 'vis',
         'Portsmouth': 'vis',
         'Providence': 'ner',
         'Richmond': 'vis',
          'Smithfield':'vis',
         'Scituate': 'ner',
         #'SouthKing': 'vis',
         'Tiverton': 'ner',
         'Warren': 'ner',
         'Warwick': 'vis',
         'WestGreen': 'ner',
         'WestWar': 'ner',
         'Westerly': 'vis',
         'Woon': 'vis'}

citynamedict = {'Barrington': 'Barrington',
         'CentralFalls': 'Central Falls',
         'EastGreen': 'East Greenwich',
         'EastProv': 'East Providence',
         'LittleCompton': 'Little Compton',
         'NewShore': 'New Shoreham',
         'NorthKing': 'North Kingstown',
         'NorthProv': 'North Providence',
         'NorthSmith': 'North Smithfield',
         'SouthKing': 'South Kingstown',
         'WestGreen': 'West Greenwich',
         'WestWar': 'West Warwick',
         'Woon': 'Woonsocket'}

#strings and lamda functions for seperating out different types of owners

state_search_string = 'state of ri|state of r |ri state of|state of rh|i-95 re|'+\
    'rhode island department|education depart|rhode island dept|dem parks|ri public tr|'+\
    'ri tnpk|rhode island state of|r i public building|r i dept of|state colleges board|'+\
    'water resources board|university of rhode|r i publi|ri public'

fed_search = 'northern narragansett indian|united states of america|'+\
    'united states postal|us government pro|usa trust narra ind|narragansett indian tri'

muni_search_string = 'city of|cty of|town of|water dep|bristol cnty|e providence sew|providence public buildings|providence water|'+\
    'conservation|conservancy|housing author|'+\
    'providence public |land purchased by city|n kingstown school|woonsocket housing|'+\
    'water authority|portsmouth high sch|pawtucket public bui|scituate school dep|'+\
    'cariho regional high|bristol high scho|tiverton land tru|cumberland land trust'

insti = 'narragansett elec|rhode island airport|r i airport|brown university|cemetery'+\
    '|ri resource recovery corp|ri hospital|prudence conservancy|'+\
    'providence college|newport restoration|johnson & wales|'+\
    'ri school of design|penn central transportation co|'+\
    'southside community land trust|r i airport corp|'+\
    'university of rhode island|private owner|'+\
    'audubon soc|prov & worc|ri airport|providence community heal|rhode island hospital|'+\
    'miriam hospital|unknown|st georges school|providence place gr|convention cent|'+\
    'swan point ceme|newport hospital|preservation society of|ocean state power|'+\
    'r i commerce corp|roger williams univer|bryant uni|salve regina coll|butler hospital|'+\
    'rhode island economic dev|new england institute of|gordon school|women and infants|'+\
    'prospect charterc|moses brown school|ri convention center auth|tiverton power inc|'+\
    'water resources|land trust|nature conservancy'




stateandinsti = state_search_string+'|'+muni_search_string+'|'+fed_search+'|'+insti
government = state_search_string+'|'+muni_search_string+'|'+fed_search
with open('pickles/repdict.pkl','rb') as f:
    replacedict = pickle.load(f)
StateOwners = lambda df: df.loc[df['Owner'].str.contains(government)]
NonStateOwners = lambda df: df.loc[~df['Owner'].str.contains(government)]

OwnerTypes = {'State':StateOwners,'NonState':NonStateOwners}
#StateOwners = lambda df: df.loc[df['Owner'].str.contains(stateandinsti)]
#NonStateOwners = lambda df: df.loc[~df.index.get_level_values('Owner').str.contains(stateandinsti)]
#GovernmentAndInstitutional = pd.Series(db.tally['Owner'].str.contains(StateAndInstitutionalOwners))

revreplacedict = {v: k for k, v in replacedict.items()}