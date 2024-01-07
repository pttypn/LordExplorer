import datetime as dt
import numpy as np
import pandas as pd
import panel as pn
import pickle
import ExplorePickle as EP
pn.extension('tabulator')

from bokeh.models.widgets.tables import DateFormatter
bokeh_formatters = {
    'LastSale': DateFormatter(format= "%d %b %Y"),
}


pickledir = 'pickles/{0}'
df = pd.read_pickle(pickledir.format('2023-12-22.pkl'))
grandTotal = pd.read_pickle(pickledir.format('GrandTotals23-12-22.pkl'))
cityTotal = pd.read_pickle(pickledir.format('CityTotals23-12-22.pkl'))
OwnerNamePresetDir = pickledir.format('OwnerNamePresets23-12-22.pkl')
geodictionarypath = pickledir.format("geodict23-12-22.pkl")

showcolumns = ['Location','City','Description','Style','Bedrooms','Owner','Owner2','Owner3',
               'OwnerAdd','OwnerAdd2','OwnerAdd3']#,'Assessment','LastSale']
tablewidths = {'Location':150,'Description':100,'Style':100,'Bedrooms':70,'Owner':150,'Owner2':100,'Owner3':100,
               'OwnerAdd':150,'OwnerAdd2':100,'OwnerAdd3':100,'Assessment':100,'LastSale':100}
df = df[showcolumns]

#MAIN TAB
#
#
#
def searchowners(df,searchstring,searchallowners = True):
    #Search by Owners
    #returns dataframe
    if searchallownerscheck.value == True:
        ownercolumns = ['Owner','Owner2','Owner3']
    else: 
        ownercolumns = ['Owner']
    searchresult = []
    for column in ownercolumns:
        searchresult.append(df.loc[df[column].str.contains('(?i){0}'.format(searchstring))])
    searchresult = pd.concat(searchresult).drop_duplicates()
    return searchresult
def exactownersearch(df,ownerlist):
    return df.loc[ownerlist]
 #   ownercolumns = ['Owner','Owner2','Owner3']
 #   searchresult = []
    #for ind in ownerlist:
    #    searchresult.append
#    for name in ownerlist:
#        for column in ownercolumns:
#            searchresult.append(df.loc[df[column].str.fullmatch(name)])
#    return pd.concat(searchresult)
    
def searchcities(df,searchlist):
    searchresult = []
    for searchterm in searchlist:
        if searchterm == 'all':
            return df
        searchresult.append(df.loc[df.City.str.fullmatch(searchterm)])
    return pd.concat(searchresult)
def searchproplocation(df,searchstring):
    if len(searchstring)>2:
        return df.loc[df.Location.str.contains(searchstring,case=False)]
    else:
        return df
def searchowneradd(df,searchstring):
    if len(searchstring)>2:
        return df.loc[df.OwnerAdd.str.contains(searchstring,case=False)]
    else:
        return df
#def searchownertype(df, searchstring):
#    if searchstring == 'all':
#        return 
#    else:
#        FindType = EP.OwnerTypes[searchstring]
#        searchresult = FindType(df)
#        return searchresult
        
def updateDF(event):
    print('hey')
    updatedDF = df
    #ownercolumns = ['Owner','Owner2','Owner3']
    if presetselect.value != '':
        #preset section
        with open(OwnerNamePresetDir, 'rb') as f:
            OwnerIndices = pickle.load(f)
        OwnerIndices = OwnerIndices[presetselect.value] #Should be a list
        updatedDF = df.loc[OwnerIndices]
        #updatedDharryharryF = searchowners(updatedDF,searchterm)
        df_widget.value = updatedDF#.reset_index(drop = False)
        df_widget
        ownersearch.value = EP.replacedict[presetselect.value]
        return
    cityvalues = citycheckboxes1.value + citycheckboxes2.value #which cities to search
    if cityvalues[0] == 'all':
        citycheckboxes1.value = ['all']
        citycheckboxes2.value = []
    else:
        updatedDF = searchcities(updatedDF,cityvalues)
   # if ownertypeselect.value != 'all':
   #     updatedDF = searchownertype(updatedDF,ownertypeselect.value)
    updatedDF = searchowners(updatedDF,ownersearch.value)
    updatedDF = searchproplocation(updatedDF,locationsearch.value)
    updatedDF = searchowneradd(updatedDF,owneraddresssearch.value)
    df_widget.value = updatedDF
    updatedDF.to_csv('tempprop.csv')
    return
    
def resetDF(event):
    df_widget.value = df
    citycheckboxes1.value = ['all']
    citycheckboxes2.value = []
    presetselect.value = ''
    owneraddresssearch.value = ''
    ownersearch.value = ''
    locationsearch.value = ''
    #ownertypeselect.value = ['all']

df_widget = pn.widgets.Tabulator(df,frozen_columns=['Location'],show_index=False,width = 1000,
                                 formatters=bokeh_formatters,widths = tablewidths,page_size = 20)


updatebutton = pn.widgets.Button(name='Update')
resetbutton = pn.widgets.Button(name='Reset')
#downloadbutton = pn.widgets.Button(name='Download')
propcsvname = pn.widgets.TextInput(value = 'properties.csv',name = 'Filename')

downloadbutton = pn.widgets.FileDownload('tempprop.csv', filename=propcsvname.value,auto=False)

ownersearch = pn.widgets.TextInput(value = '',name = 'Search by Owner')
searchallownerscheck = pn.widgets.Checkbox(value = True,name = "search all owner columns")

citycheckboxes1 = pn.widgets.CheckBoxGroup(
    value=['all'], options=['all',*[key for key in EP.dbtype.keys()][:17]])
citycheckboxes2 = pn.widgets.CheckBoxGroup(
    value=['all'], options=[key for key in EP.dbtype.keys()][17:])
citycheckboxes = [citycheckboxes1,citycheckboxes2]
cityselect = pn.Accordion(pn.Row(*citycheckboxes, name = 'filter by city'),name = 'cities')

ownertypeselect = pn.widgets.Select(name='Filter by owner type',
                    value='all', options=['all','State','NonState'])
presetselect = pn.widgets.Select(name = 'Presets',value = '',options = ['',*[key for key in EP.replacedict]])

#extra in accordion row ownertypeselect
accordionrow = pn.Row(cityselect,presetselect)

locationsearch = pn.widgets.TextInput(value = '',name = 'Search by Property Location')
owneraddresssearch = pn.widgets.TextInput(value = '',name = 'Search by Owner Address')
debug = pn.widgets.TextInput(value = '',name = 'debug')

#dfparams = (citycheckboxes1.value,citycheckboxes2.value,
#           ownersearch,locationsearch,owneraddresssearch)
    
updatebutton.on_click(updateDF)
resetbutton.on_click(resetDF)

propertytab = pn.Column(accordionrow,
              pn.Row(pn.Column(ownersearch,searchallownerscheck),
                     locationsearch,owneraddresssearch),
              pn.Row(updatebutton, resetbutton,propcsvname,downloadbutton),
              df_widget,
             debug, name = 'Properties')
#
#
#Ownergroup Tab
#Groups the properties in the properties tab by owner
#
def updatesummarytab(event):
    sum_df.value = groupOwners(df_widget.value)
    sum_df.value.to_csv('tempcsv.csv')
    return
    
def groupOwners(inputdf):
    """Takes owner values of the main dataframe,
    and searches in the summary dataframe for those owners"""
    ownerlist = inputdf['Owner'].unique()
    if showtotalscheck.value == True:  
        if grandtotalcheck.value == True:
            return  grandTotal.loc[ownerlist].groupby('City').sum()
        else:
            return grandTotal.loc[ownerlist]
        return grandTotal.loc[ownerlist]
    else: #show city totals
        if grandtotalcheck.value == True:
            return  grandTotal.loc[ownerlist].groupby('City').sum()
        else:
            return cityTotal.loc[ownerlist]

sum_df = pn.widgets.Tabulator(pd.DataFrame(),width = 1000,
                                 formatters=bokeh_formatters,page_size = 20)

summarizebutton = pn.widgets.Button(name = "Update")
showtotalscheck = pn.widgets.Checkbox(value = False,name = 'Show totals')
grandtotalcheck = pn.widgets.Checkbox(value = False,name = 'Grand Total')

    
#fileydown = pn.widgets.FileDownload(file='summarybyowner.csv', filename='summarybyowner.csv')
byownercsvname = pn.widgets.TextInput(value = 'GroupByOwner.csv',name = 'Filename')
downbutton = pn.widgets.FileDownload('tempcsv.csv', filename=byownercsvname.value,auto=True)

downloadcol = pn.Column(byownercsvname,downbutton)
sumsearchcol = pn.Column(summarizebutton,showtotalscheck,grandtotalcheck)
sumtabtopRow = pn.Row(sumsearchcol, downloadcol)

summarizebutton.on_click(updatesummarytab)

summarytab = pn.Column(sumtabtopRow,sum_df,name = 'Group by owner')

#
#
#
#
##MAP TAB
###
import folium
import geopandas
from shapely.geometry import Point

def loadpoints(event):
    maxpoints = maxpointslider.value
    wdf = df_widget.value #working dataframe

    #truncate if there's more points than the max
    if len(wdf) > maxpoints:
        wdf = wdf[:maxpoints]

    #This section makes a geodataframe to be used with folium
    #Load geodictionary pickle, which has formatted locations as keys
    #and coordinates in wgs 84 for values
    with open(geodictionarypath, 'rb') as f:
        geodictionary = pickle.load(f)
    #This lambda formats a row into a key for the geodictionary
    getlocations = lambda df:df['Location']+', '+df['City'].replace(EP.citynamedict) +', RI, '
    #keys used to find coordinates for each row
    locationkeys = getlocations(wdf) #gets indices for points
    coords = locationkeys.apply(getcoords, geodict = geodictionary)
    wdf['Coords'] = coords.apply(Point)
    wdf = wdf.loc[wdf["Coords"]!=(Point(np.nan,np.nan))]

    wdf = geopandas.GeoDataFrame(wdf,geometry = "Coords",crs = "EPSG:4326")
    
    #Make new map with folium
    n = folium.Map(location=[41.82, -71.4], zoom_start=11,tiles="Cartodb Positron")
    #add points to map by iterating through the working dataframe
    for _, r in wdf.iterrows():
        georow = geopandas.GeoSeries(r["Coords"])
        geo_j = georow.to_json()
        geo_j = folium.GeoJson(data=geo_j,
                    marker=folium.CircleMarker(
                        radius=4,
                        fill_color="red",
                        fill_opacity=0.4,
                        color="black",
                        weight=1,drop=True
                    ), 
                    drop=True,style_function=lambda x: {"fillColor": "orange"})
        folium.Popup(r["Location"]).add_to(geo_j)
        geo_j.add_to(n)
    #add newmap to folium pane
    folium_pane.object = n
    #save the html
    folium_pane.object.save('map.html')

    
def getcoords(searchaddy, geodict):
    """Takes a  and returns coordinate points"""
    try:
        return geodict[searchaddy]
    except:
        print(searchaddy)
        return (np.nan,np.nan)    
        
maxpointslider = pn.widgets.DiscreteSlider(name = "Max number of points",options = [i*100 for i in range(1,10)],value = 300)

loadptsbutton = pn.widgets.Button(name = 'Update Map')
loadptsbutton.on_click(loadpoints)
downmapbutton =pn.widgets.FileDownload('map.html', filename='map.html',auto=True)
mapbuttonrow = pn.Row(loadptsbutton,downmapbutton,maxpointslider)

#make the map
m = folium.Map(location=[41.82, -71.4], zoom_start=11,tiles="Cartodb Positron")
folium_pane = pn.pane.plot.Folium(m,sizing_mode='stretch_both')


maptab = pn.Column(mapbuttonrow,folium_pane, name = 'Map')

#
#
#
tabby = pn.Tabs(propertytab,summarytab,maptab).servable()
