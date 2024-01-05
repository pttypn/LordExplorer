import re
import pandas as pd
import csv
from bs4 import BeautifulSoup
import numpy as np

class SoupParser:
    """
        Workhorse object. The method getvalue() is used to retrieve an attribute value from 
        the input string. Always returns a string, even if nothing is found
        
        str name = name of attribute
        str regular_expression = containing two parts (enclosed by parents)
                    first part is to find the attribute, second part is the attribute
                    itself eg '(Map/Lot)(.*)'
        datatype = 'str' or 'int' or 'real'
        delete_string used to clean value string before returning

        
        """
    def __init__(self,name,AttributeDictionary,delete_string = None):
        self.dbtype = name
        AttributeDictionary = {attname : re.compile(AttributeDictionary[attname]) for attname in AttributeDictionary}
        self.AttributeDictionary = AttributeDictionary
        defaultdelete = ',|\$|:'
        if isinstance(delete_string,str):
            self.delete_pattern = re.compile(delete_string+'|'+defaultdelete)
        else:
            self.delete_pattern = re.compile(defaultdelete)

    def getvalue(self,page, attribute):
        """
        returns value of the attribute found in string
        """
        regexob = self.AttributeDictionary[attribute]
        match = regexob.search(page)
        lastmatch = lambda Match: Match[Match.lastindex]

        if isinstance(match,re.Match):
            try:
                return self.delete_pattern.sub('',lastmatch(match)).strip()
            except:
                return ''
        else:
            return ''
            
    def MakeSoup(self,filepath):
        with open(filepath,encoding = "utf-8")as file:
            soupy = BeautifulSoup(file,'lxml')
            return soupy

    def MakeDF(self, pathtemplate,numberoffiles):
        combinedfiles = ''
        pagevectors = []
        pagenumbers = []
        for i in range(numberoffiles):
            filepath = pathtemplate.format(i)
            with open(filepath,encoding = "utf-8")as file:
                soupy = BeautifulSoup(file,'lxml')
                #print(len(soupy.html.body.find_all('page')))
            for page in soupy.html.body.find_all('page'):
                pagenumbers.append((page.attrs['num'],page.attrs['time']))
                pagevec = []
                for attribute in self.AttributeDictionary:
                    pagevalue = self.getvalue(page.getText(),attribute)  
                    pagevec.append(pagevalue)
                pagevectors.append(tuple(pagevec))
#        print(len(soupy.html.body.find_all('page')))
#        print(len(pagevectors))
#        headers = [*[attname for attname in self.AttributeDictionary],'PageNum']
        headers = [attname for attname in self.AttributeDictionary]
        DF1 = pd.DataFrame({'PageNo':[numby[0] for numby in pagenumbers],
                           'Time':[numby[1] for numby in pagenumbers]})
        DF = pd.DataFrame(pagevectors,columns = headers)
        return pd.concat([DF,DF1],axis = 1)
        
NerRegexDic = {'Accountnum': '(Account)(\\d+)',
             'Location': '(Location and Owner\n\nLocation)(.*)',
             'Description': '(\n\nState Code\\d*\\s*-\\s*)(.*)',
             'Assessment': '(Parcel Total\\$)(.*)',
             'AreaSF': '(\n\nLand Area)(.*)SF',
             'AreaAC': '(\n\nLand Area)(.*)AC',
             'Zoning': '(\n\nZoning)(.*)',
             'Style': '(\n\nDesign:*)(.*)',
             'Owner': '(\n\nOwner)(.*)',
             'Owner2': '(\n\nOwner2)(.*)',
             'Owner3': '(\n\nOwner3)(.*)',
             'OwnerAdd': '(\n\nAddress)(.*)',
             'OwnerAdd2':'(\n\nAddress2)(.*)',
             'OwnerAdd3': '(\n\nAddress3)(.*)',
             'Account': '(User Account)(.*)',
             'YearBuilt': '(\n\nYear Built\\D*)(\\d+)',
             'Bedrooms': '(?i)(\n\nBedr[a-z]*:*\\s*)(\\d+)',
             'Bathrooms': '(?i)(\n\n(\\w*\\s)?(Bath|bth)[a-z]*:*\\s*)(\\d+)',
             'StateCode': '(State Code)(\\d+)',
             'Neighborhood': '(\n\nNeighborhood)(.*)',
             'Cards': '(\n\nCard1/)(\\d)',
             'LivingArea(SF)': '(\n\nAbove Grade Living Area)(.*)',
              'LastSale':'(ReferenceInstrument\n\n)(\d{2}/\d{2}/\d{4})'}
VisRegexDic = {'Location': '(Location\n\n)(.*)',
             'Owner': '(Owner\n\n)(.*)',
             'Owner2': '(\n\nCo-Owner)(.*)',
             'Owner3': '(\n\nCo-Co-Owner)(.*)',
             'OwnerAdd': '(\n\nAddress)(.*)',
             'OwnerAdd2': '(\n\nAddress)(.*)',
             'OwnerAdd3': '(\n\nAddress)(.*)',
             'StateCode': '(\n\nUse Code)(.*)',
             'Description': '(\n\nDescription|\n\nModel)(.+)',
             'Style': '(\n\nDescription|\n\nStyle)(.+)',
             'AreaSF': '(Size \\(Sqr Feet\\))(.*)',
             'AreaAC': '(Size \\(Acres\\))(.*)',
             'Assessment': '(Assessment\n\n\\$)(.*)',
             'Acount': '(Acct#\n\n)(.*)',
             'Zoning': '(Zoning#\n\n)(.*)',
             'Buildings': '(Building Count\n\n)(.*)',
             'Bedrooms': '(?i)((\\w*\\s)?Bedr[a-z]*:*\\s*)(\\d+)',
             'Bathrooms': '(?i)((\\w*\\s)?(Bath|Bth)[a-z]*:*\\s*)(\\d+)',
             'PageNum': '(PID\n\n)(\\d+)',
             'YearBuilt': '(Year Built\\D*|Year Built[a-z]*\n\\D*)(\\d+)',
              'LastSale':'(\nSale Date)(\d{2}/\d{2}/\d{4})'}





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
class AddressParser:
    """Object used to parse the 'Location' of each parcel
    addnumberandstreet method take a dataframe, addressvector, and cityname as arguments
    returns a dataframe with streetnumber, street, city and state columns"""
    def __init__(self):
        self.format_pattern = re.compile(r'-|\'| {2,}|\d+|/|\s*Unit.*')
        self.streetnumber_pattern = re.compile(r'\d+\s|\d+\w\s')
        self.streetname_pattern = re.compile(r'\w+.*')
        
    def streetnumber(self, Address_string):
        number = self.streetnumber_pattern.search(Address_string)
        if  isinstance(number,re.Match):
            return number[0].strip()
        else:
            return ''
        
    def streetname(self, address_string):
        streetname = self.streetnumber_pattern.subn('',address_string)[0]
        if isinstance(streetname,str):
            streetname =  self.format_pattern.subn('',streetname)[0]
        else:
            streetname = address_string
        return streetname
    
    def addnumberandstreet(self,df,addressvector):
        street = [self.streetname(address).lower().strip() for address in df[addressvector]]
        number = [self.streetnumber(address).strip() for address in df[addressvector]]
        #state = ["RI" for address in addressvector]

        return df.assign(Number = number,Street = street)
        
AP = AddressParser()

cities = dbtype.keys()
NERparser = SoupParser('ner',NerRegexDic)
VisParser = SoupParser('vis',VisRegexDic)
ParserDic = {'ner': NERparser,
            'vis':VisParser}