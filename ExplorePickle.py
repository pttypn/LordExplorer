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


replacedict = {'stonelink and greenfin':'.*(ri property wire llc (50%) & alpha holdings llc (50%)|bluefin properties llc|greenfin properties llc|bluefin providence one llc|ri property wire llc|bluefin providence two llc|progressive housing llc|circle holdings llc|hannah & chloe llc|ccm holdings llc|alpha holdings llc & ri property wire|edgewood property holdings i llc|590 charles street llc|bluestate housing llc|greenfin holdings llc|green properties llc|ri property wire|bluefin).*',
               'rhode island state of':'.*(' + state_search_string + ').*',
               
              'ri airport corp':'.*(ri airport corp|rhode island airport co).*',
               
              'narragansett electric':'.*(narragansett elec).*',
                'elmwood realty':'.*(elmwood realty llc|spring street realty llc|butler jeffrey|elmwood realty north llc|elmwood realty llc (rr)|pawtuxet village properties).*',

               'united states of america':'united states of america|'+\
            'united states postal|us government pro',
              
              'housing authorities combined':'.*(housing aut|housing athorit).*',
               
              'city of providence': '.*(city of prov|providence city of|prov bldg san|providence publi).*',
               
              'pioneer investments':'.*(pioneer in).*',
                'walter bronhard':'.*(85 congdon street llc|walter l bronhard|150 lloyd llc|71 keene holding llc|71 barnes holding llc|waterman holding llc|brook holding llc|euclid holding llc|113 keene holding llc).*',
               
              'walter king':'.*(walter king|king walter).*',
               
              '02908 holdco':'.*(02908|214 williams|250 williams|34-36 eaton|44 arnold'+
                            '|55 radcl|235 oakl|104 sheld|liege lots|109-115 pine|48 liege'+
                            '115 hux|93 pemb).*',
               
              'peter marinucci et al':'.*(marinucci peter|peter marinucci|lillian marinucci|pocasset proper).*',
               
              'audubon society of ri':'.*audubon so.*',
               'nature conservancy the':'.*(nature conservancy).*',
              'gaia winchester':'gaia winchester','johnson bros':
              '.*(johnson brothers|johsnon bro|jt co-invest i).*',
                  'omni' : '.*(omni maple|trio partners owner|omni dev|jordan caffey townhomes|portland street development co|joseph caffey aparments llc|cornplanter row limited partnership|omni friendship limited partnership|omni washington l.p.|phoenix apartments lp|omni development corp.|omni phoenix renaissance|h d c limited partnership|omni development corporation|omni turning point llc|trio partners owner llc.).*',
                'providence growth':'.*(providence growth).*',
                  'osko elie':'.*(osko elie).*',
                  '151 tremont combined': '.*(ikauniks pamela|11 willow street 1996 realty t|north elmwood revitalization|parkis historic properties llc|bellevue development associates lp|westfield commons lp|elmwood neighborhood revitalization lp i|elmwood neighborhood revitalization part|community works rhode island|elmwood neighborhood revitalization ltd|peoples redevelopment corp|broad street revitalization|elmwood development company|adelaide avenue limited partnership|elmwood revitalization limited partnersh|stephens hall development associates lp|hope renewed realty corp non-profit corp|olney village lp|olneyville redux limited partnership|olneyville housing corp|amherst gardens lp|riverside gateway lp|riverside gateway limited partnership).*',
                  'ferland':'.*(anne associates|farmington/ dyer apartments llc|farmington /dyer apartments llc|fc central properties llc|250/3226 apartments llc|3350 pawtucket avenue llc|parkway apartments lp &|kent heights apartments llc|rumford apartments lp &|maple housing group|arthur street apartments llc|ferland corporation|evergreen street apartments llc|lonsdale apartments l p|ferland corp|fermar associates|geneva apartments l p|meadow view group|sessions/taft apartments llc|hagan apartments lp|cranberry apartments llc|fourteen forty-five warwick ave apart ll|diamond hill apartments llc|northern ri apartments llc|plaza village group|walnut hill apartments lp).*',
                  'swap inc combined':'.*(apf limited partnership|the composition owner llc|swap inc|revitalize southside lp|southside gateways limited|southside gateways/broad street llc|friendship pine associates limited partn|tp10 llc|potters avenue area revitalization lp|tp 10 llc|201 thurbers inc|maplewood lp).*',
                  'lanmar corp':'.*(lanmar corp).*',
                  'salamone francesco':'.*(salamone francesco|salamone frank|carol botelho-salamone|salamone carol a botelho|salamone carol botelho-|salamone carol botelho|francesco salamone|salamone francisco|salamone frank (rr)|botelho-salamone carol|salamone franceso|botelho-salamone carol a).*',
                  '719 front st combined lawyermaybe': '.*(clocktower associates lp|greenridge associates lp|woonsocket neighborhood development|woonsocket neighborhood development corp|wndc|marshfield associates lp|reclaiming the vision ii lp|reclaiming thr vision ii lp|reclaming the vision ii lp|reclaiming the visiin ii lp).*',
                  '44 washington st combined rihousing':'.*(fallon david r & kathleen i|cumberland place lp|ri housing & mtg finance corp|rhode island housing and mortgage finance corp|ri housing & mortgage finance corp|ri housing & mortgage finance corp.|canonchet hills limited partne|rhode island housing & mortgage finance|rihmfc|ri housing mortgage finance corp|northern plaza associates|subsidized properties iii lp|neighborhood preservation apts lp|neighborhood preservation apar|rhode island housing development corp|rhode island housing and mtg fin corp|ri housing and mortgage finance corp|healyn properties llc|indian run village rih llc|rhode island housing|matthew xxv associates lp|rhode island housing & mtg fin corp|school house place lp|ri housing|kenney edward d jr|new babson associates).*',
                  'greenwich bay trevor wiggins combined':'.*(greenwich bay homes llc|wiggins edward j et ux|boston street apartments llc|greenwich bay holdings ii llc|greenwich bay holdings v llc|penwood inc &|greenwich bay holdings iv llc|cwb associates|stone ridge apartments llc|wiggins edward j & helen a|blais henry j iii & b & w associates|wiggins holdings inc|blais henry j iii & patricia c &|greenwich bayholdings ii llc|greenwich bay holdings llc|wiggins edward j|seneca place apartments llc|c w associates|venturecap investment group ii inc|greenwich bay development|edward j wiggins|venturcap investment group ii inc|gbr properties llc|fifty west apartments llc|walker street apartments llc|greenwich bay holdings v llc.|greenwich bay holdings llc.|greenwich bay holdings iii llc|greenwich bay homes llc.|greenwich bay holdings ii llc.).*',
                  'picerne real estate group':'.*(picerne david r walker ridge|david r picerne|949 park avenue llc|picerne commercial pool llc|friendly community|picerne investment corp|pontiac associates|woodridge investment corporation|kelly & picerne inc|ri realty trust llc|957 reservoir llc|blackamore investments llc|jrc realty corp|garden village apartments llc|western hills apartments llc|meshanticut house appartments llc|captain and bush apartments llc|wfd associates l p|walden woods associates|the oaks at orchard valley homeowners as|lippitt land investments phase ii llc|commerce park west|friedman trust et als|potowomut realty co|crescent park manor associates &|crescent park manor associates|kelly & picerne inc.|wfd associates lp|wampanoag associates &|captain and bush apartments llc &|simmonsville assoc iii|simmonsville associates|middletown associates|windover farm homeowners association|775 boston neck road llc|picerne ronald r.s.|picerne jeanne p|picerne jeanne m.|warren ave assoc|friendly community limited partnership|romeo s picerne|old north land investments llc|w f d associates lp|picerne commercial pool|brookside apartments|cowesett hills aparments llc|picerne commerical pool llc|meadowbrook corp|pilgrim land developers inc|picerne ronald r s trust|greenwich village associates|fairfax village apartments llc|warwick associates|twenty two ninety warwick avenue llc|j & r associates|bayside associates|richmond center ltd partnership|bayside bc apartments llc|bayside a apartments llc|shady oaks apartments llc|second ave assoc limited).*',
                  'john gullison': '.*(gullison r john|mri 10 woolsey partnership|mri 14 woolsey partnership|mri 16 woolsey partnership|gullison john r|mri 4 ludlow partnership|mri 3 ludlow partnership|mri 5 ludlow partnership|mri 4 bristol partnership|mri 9 woolsey road partnership|mri 15 woolsey partnership|mri 2 ludlow partnership|mri 2 bristol partnership|mri 2 buck partnership|nri 14 rosa partnership|nri 18 rosa partnership|nri 325 broadway partnership|nri 6 ledyard partnership|nri 2-4 ledyard partnership|nri peckham ave partnership|nri 9 bedlow partnership|nri 516 broadway partnership|nri 1 peckham partnership|nri 3 homer partnership|nri 33 newport partnership|nri 75/73 gibbs partnership|zimble bonnie f life estate|zimble bonnie life estate|nri 51 kingston partnership|nri 22 pond partnership|nri 7 gould partnership|nri 5 gould partnership|nri 16 burnside partnership|nri 14 lincoln partnership|nri 10 lincoln partnership|nri 11 lincoln partnership|nri 207 broadway partnership|nri 34 mt vernon partnership|nri 12 goodwin st partnership|nri 104-108 girard partnership|pri 2870 e main partnership).*',
                  'Armory Properties':'.*(dupre robert e|maple creek llc|abodhi properties llc|334 broadway llc|rcg armory 331 broadway llc|seven hundred fity-five lofts llc|armory revival company|rcg 767 bongartz llc|rcg cobblestone llc|rcg glassworks llc|westminster crossing llc|rcg armory pearl llc|west fountains lofts llc|west fountain lofts llc|rcg armory central llc|rcg armory firehouse llc|rcg armory 45 central|elementary llc|kips properties llc|sustainable llc|166 valley street llc|west river partners llc|ocean state land company llc|rcg armory park view llc|1570-1582 westminster llc|mark van noppen|riverfront capital llc|riverfront apartments llc|60 federal llc|donigian park llc).*',
                  '600 cass combined - maybe j boucher':'.*(boucher real estate partners lp|boucher 1275 llc|repm inc|north village partners|ubs realty inc|lantern house partners|bc partners llc|rankin path realty llc|boucher john j|dcb realty llc|boucher properties llc|bernon real estate partners lp|elite realty inc).*',
                  '931 jefferson combined':'.*(9 betsy drive llc|cross street realty llc|silverfish properties lc|351 budlong rd llc|rockville mill hopkinton llc|pemberton place housing|vista llc|handford g winona & kalander jonathan v|blackstone valley place realty llc|v n housing corp|freedom housing corporation|west house corporation the|silverfish properties llc|elmhurst house|1637 mineral spring avenue llc|keats gardens inc|belmont commons inc|spurwink supported living inc|church community housing|kenyon development llc|brooketone properties llc|b&m properties llc|k & s llc|gosselin christopher a|jlb realty llc|nine thirty one realty llc|jefferson boulevard realty llc|college park realty llc|germani stephen s|st anns apartments l p).*',
                  #'56 pine street':'.*(413 roosevelt mill llc|dnc pawtucket holding llc|mejia guimecindo &|garone robert|hartford holdings llc|east greenwich acquisitions|route 6 auto auction llc|bastos carlos h. jr.|dnc holdings llc|hartford solar realty llc|hartford soalr realty llc|hartford realty holdings llc|washington highway llc|bbww properties llc|newport avenue realty llc|branch holdings llc|229 waterman realty llc|c m b inc|bbso realty llc|corman properties llc|rhode island legal services inc|ministerio dos negocios|56 pine street llc|hanley building condominium association|dnc acquisitions llc|thomas chester|skyline realty llc|dnm hodings llc).*',
                  #'coforge': '.*(ri equity group llc|burrillville health ctr assoc|pine street realty delaware x llc|pine street realty delaware v llc|pine street realty delaware vllc|pine street realty delaware llc|pine street realty delaware ii|pine street realty delaware xi llc|pine street realty delaware ix llc|pine street realty llc|pine street realty delaware vi llc|pine street realty dexter llc|pine street realty delaware iii llc|tbp cranston llc|pine street realty delaware iv llc|clark street llc|highland hills apartments llc|scott cynthia|brookwood properties subsidiary llc|pine street realty delaware iv|pine street delaware vii llc|pine street realty deleware x llc|pine street delaware x llc|pine street realty deleware 1x llc|pine street realty viii llc|pine street realty delaware viii llc|westfield development & associates lp|pine street realty delaware ix llc.|pine street realty delaware vii llc.|pine street realty delaware vi llc.|pine street realty delaware viii llc.).*',
                   'pine street': '.*(pine street realty delaware x llc|pine street realty delaware v llc|pine street realty delaware vllc|pine street realty delaware llc|pine street realty delaware ii|pine street realty delaware xi llc|pine street realty delaware ix llc|pine street realty llc|pine street realty delaware vi llc|pine street realty dexter llc|pine street realty delaware iii llc|pine street realty delaware iv llc|pine street realty delaware iv|pine street delaware vii llc|pine street realty deleware x llc|pine street delaware x llc|pine street realty deleware 1x llc|pine street realty viii llc|pine street realty delaware viii llc|pine street realty delaware ix llc.|pine street realty delaware vii llc.|pine street realty delaware vi llc.|pine street realty delaware viii llc.).*',
                  'dnc acquisitions et al':'.*(dnc acqui|dnc hol|dnc paw).*',
                  '861 a broad st combined':'.*(allegria court inc|dean street studios lp|lp historic west end ii|west end preservation apartments l p|lexington avenue development associates|ontario apartments partnership|norimentas inc|roland m boucher apts).*',
                  'marsocci': '.*(marsocci properties llc|marsocci michael|marsocci prop llc|marsocci venturesllc|marsocci ventures llc|michael j marsocci jr|michale j marsocci jr).*',
                  '566 smith - maybe colaluca': '.*(latch realty llc|359 river llc|uptum investments llc|upturn investments llc|admiral properties llc|rise realty llc|colaluca property llc|citadel properties llc|up & coming llc|joseph colaluca|providence property group llc|victory partners llc|john colaluca).*',
                  #'davidson bogel combined': '.*(ri equity group llc|burrillville health ctr assoc|pine street realty delaware vllc|pine street realty delaware llc|tbp cranston llc|clark street llc|highland hills apartments llc|scott cynthia|brookwood properties subsidiary llc|pine street realty delaware vi llc|pine street realty delaware v llc|westfield development & associates lp|pine street realty delaware vi llc.).*',
                  'the greene company': '.*(greene co|greene company the|greene co inc|greene co the).*',
                  'anthony gemma': '.*(7th heaven realty llc|cloud 9 realty|vip realty llc|patriot homes and land development llc|oasis realty lp|simple realty llc|royal realty llc|tlc realty llc|easy realty llc|simple realty llc.|cloud 9 realty llc|dream realty llc|tlc realty llc.|simple realty. llc.).*',
                  'provrentals - 334 carpenter combined':'.*(8 hewitt street llc|34 knight street llc|federal hill partners llc|468 west fountain llc|1290 westminster llc|530 broadway llc|lamb janis lee|lemoi michael).*',
                  'damico-burchfield':'.*(20 jones llc|albert david holdings llc|federal hill capital llc|federal hill investment trust llc|damico robert a|damico robert a ii|renee realty llc|twenty twelve fund llc|destiny partners llc|shamrock partners llc|relentless realty llc|dv8 realty llc|m & m prop development llc|loans for investment properties llc (rr)|loans for investment properties llc).*',
                  '11 south angell combined':'.*(stahl richard j|wildacre norwood llc|resnevic realty llc|weiner works llc|total investments llc|nmx ventures llc|wayland sq llc|tts llc|5 traverse st llc|adi avraham|79 ives st llc|103 point st llc|conrad condominium association|49 westfield llc|153 irving ave llc|michael a marchionte trustee|joseph wein|130 cypress st llc|735 hope st llc|com98 llc|daniel k kwan|96 salmon st llc|jenckes hill development llc).*',
                  'jason schectman':'.*(suburban realty group llc|long term rentals llc|jason a shectman|jason a shechtman|jason shechtman|off broadway properties llc|pratt realty llc|shechtman stephen j).*',
                  'lor-sher combined':'.*(lor-sher apartments llc|compagnone mary|waterman chenango llc|lor sher apartments llc|mary compagnone|salvatore compagnone jr).*',
                  'gerard brennan':'.*(home villas properties llc|gerard k brennan).*',
                  '444 elwood ny combined':'.*(rd pilesgrove llc|albert family lmt part|rdi llc).*',
                  'elj inc': '.*(e.l.j. inc|elj inc.|elj inc|e.l.j. inc.|francis bros realty inc|e l j inc).*',
                  '270 bellevue combined': '.*(eden haven llc|james kerrie|castner michael a|houghton david w & linda s levine|wheeler john m & laura e|haverkorn ronald & tatiana j wermuth|pizzaruso james &|smith david m|673 bellevue llc|empire ocean management llc|lennoxlove investments llc|ziemba elizabeth|conway paul g &|hower zachary & jennifer|981 realty llc|equity trust company custodian|seawell kim soo j|the winthrop trust|hower zachary & jennifer t/e|hower zachary & hower jennifer t/e|hower zachary|zj properties llc|chandler jonathan).*',
                  'kyltiff':'.*(kytiff investments & consulting llc|kyltiff investments & consulting llc).*',
                  '224 dexter combined':'.*(weh sankofa l.p.|west elmwood housing development corp|hope renewed realty corporation).*',
                  'smith hill visions': '.*(shv ii limited partnership|smith hill visions limited partnership).*',
                  'coastline - maybe chafees': '.*(gabellieri verna bertolini|three brook llc|wee hoose farm llc|james pond realty company llc|second scobco llc|excel realty co llc|metcalf realty llc|metcalf pauline & jesse p & mauran esthe|1250 llc|bell pike llc|willson steven b & masser william truste|pearsons robert c|curran alton j & coast line tr trustees|elm parsonage llc|south chestnut realty llc|south richmond realty llc|point chestnut llc|hospital-elm realty llc|point-parsonage holdings llc|three brook l l c).*',
                  '528 smithfield probablylawyercombined':'.*(applegate realty co|national development group inc|national devel group inc &|ellis mohammed s|rjc np llc|1030 chalkstone investments llc|rjc austin llc).*',
                  'attleboro po box': '.*(xue deng ping d et al li hong linda chen|cheng linda lihong &|cheng lihong & xue dengping|linda lihong cheng|linda li hong cheng|deng ping duncan xue|deng ping o xue|ping deng xue|deng ping xue|deng ping d xue|duncan deng ping xue).*'
                 }

stateandinsti = state_search_string+'|'+muni_search_string+'|'+fed_search+'|'+insti
government = state_search_string+'|'+muni_search_string+'|'+fed_search


StateOwners = lambda df: df.loc[df['Owner'].str.contains(government)]
NonStateOwners = lambda df: df.loc[~df['Owner'].str.contains(government)]

OwnerTypes = {'State':StateOwners,'NonState':NonStateOwners}
#StateOwners = lambda df: df.loc[df['Owner'].str.contains(stateandinsti)]
#NonStateOwners = lambda df: df.loc[~df.index.get_level_values('Owner').str.contains(stateandinsti)]
#GovernmentAndInstitutional = pd.Series(db.tally['Owner'].str.contains(StateAndInstitutionalOwners))

revreplacedict = {v: k for k, v in replacedict.items()}