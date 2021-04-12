"""
"Liabilities_and_Assets":"24453"
"Foreign_Exchange_Reserves":"24454"
"Cash_Balances_of_SCB":"24455"
"SCB_Business_in_India":"24456"
"Ratio_and_Rates":"24457"
"Money_Stock":"24458"
"Reserve_Money":"24459"
"Liquidity_Operations":"24460"
"Major_Price_Indices":"24461"
"Certificates_of_Deposit":"24462"
"Commercial_Paper":"24463"
"Money_Markets":"24464"
"Treasury_Bills_Outstanding":"24465"
"Market_Borrowings":"24466"
"""

# create seperate function for each of above

import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

def Scraptable(id):
    try:
        s = requests.Session()
        main_url = "https://www.rbi.org.in/Scripts/WSSView.aspx?Id=" + str(id)
        resp = s.get(main_url)
        Html_file = open("tables.html", "w+", encoding="utf-8")
        Html_file.write(resp.text)
        Html_file.close()
        table_MN = pd.read_html('tables.html')
        soup = bs(resp.text, 'html.parser')
        try:
            Publicaton_Date = soup.find_all('td', {'class': 'tableheader'})[1].text.strip().replace("Date :",'').strip()
        except:
            Publicaton_Date = ''

        try:
            DATA_DATE=''
            DATA_DATESpan = soup.find_all('span', {'class': 'head'})
            for item in DATA_DATESpan:
                if 'As on ' in item.text:
                    DATA_DATE=item.text.replace("As on ","").strip()
                    break
        except:
            DATA_DATE = ''

        return table_MN[1].iloc[4:],Publicaton_Date,DATA_DATE
    except:
        return ''


def Liabilities_and_Assets(id):
    tables,PublicatonDate,DATA_DATE=Scraptable(id)
    print("PublicatonDate: "+PublicatonDate)
    print("DATA_DATE: " + DATA_DATE)
    print("Table: " + tables)
    return tables


def Foreign_Exchange_Reserves(id):
    tables,PublicatonDate,DATA_DATE=Scraptable(id)
    print("PublicatonDate: "+PublicatonDate)
    print("DATA_DATE: " + DATA_DATE)
    print("Table: " + tables)
    return tables


def Cash_Balances_of_SCB(id):
    tables,PublicatonDate,DATA_DATE=Scraptable(id)
    print("PublicatonDate: "+PublicatonDate)
    print("DATA_DATE: " + DATA_DATE)
    print("Table: " + tables)
    return tables


def SCB_Business_in_India(id):
    tables,PublicatonDate,DATA_DATE=Scraptable(id)
    print("PublicatonDate: "+PublicatonDate)
    print("DATA_DATE: " + DATA_DATE)
    print("Table: " + tables)
    return tables


def Ratio_and_Rates(id):
    tables,PublicatonDate,DATA_DATE=Scraptable(id)
    print("PublicatonDate: "+PublicatonDate)
    print("DATA_DATE: " + DATA_DATE)
    print("Table: " + tables)
    return tables


def Money_Stock(id):
    tables,PublicatonDate,DATA_DATE=Scraptable(id)
    print("PublicatonDate: "+PublicatonDate)
    print("DATA_DATE: " + DATA_DATE)
    print("Table: " + tables)
    return tables


def Reserve_Money(id):
    tables,PublicatonDate,DATA_DATE=Scraptable(id)
    print("PublicatonDate: "+PublicatonDate)
    print("DATA_DATE: " + DATA_DATE)
    print("Table: " + tables)
    return tables


def Liquidity_Operations(id):
    tables,PublicatonDate,DATA_DATE=Scraptable(id)


def Major_Price_Indices(id):
    tables,PublicatonDate,DATA_DATE=Scraptable(id)
    print("PublicatonDate: "+PublicatonDate)
    print("DATA_DATE: " + DATA_DATE)
    print("Table: " + tables)
    return tables


def Certificates_of_Deposit(id):
    tables,PublicatonDate,DATA_DATE=Scraptable(id)
    print("PublicatonDate: "+PublicatonDate)
    print("DATA_DATE: " + DATA_DATE)
    print("Table: " + tables)
    return tables


def Commercial_Paper(id):
    tables,PublicatonDate,DATA_DATE=Scraptable(id)
    print("PublicatonDate: "+PublicatonDate)
    print("DATA_DATE: " + DATA_DATE)
    print("Table: " + tables)
    return tables


def Money_Markets(id):
    tables,PublicatonDate,DATA_DATE=Scraptable(id)
    print("PublicatonDate: "+PublicatonDate)
    print("DATA_DATE: " + DATA_DATE)
    print("Table: " + tables)
    return tables


def Treasury_Bills_Outstanding(id):
    tables,PublicatonDate,DATA_DATE=Scraptable(id)
    print("PublicatonDate: "+PublicatonDate)
    print("DATA_DATE: " + DATA_DATE)
    print("Table: " + tables)
    return tables


def Market_Borrowings(id):
    tables,PublicatonDate,DATA_DATE=Scraptable(id)
    print("PublicatonDate: "+PublicatonDate)
    print("DATA_DATE: " + DATA_DATE)
    print("Table: " + tables)
    return tables

def get_fridays(dstart, dend):
    days = []
    #dstart = date(2020,1,1)
    #dend = date(2020,12,31)
    # print fridays
    # days = [print(dstart + timedelta(days=x), end="\n") for x in range((dend-dstart).days + 1) if (dstart + timedelta(days=x)).weekday() == 4]

    for x in range((dend-dstart).days + 1):
        if (dstart + timedelta(days=x)).weekday() == 4:
            friday = dstart + timedelta(days=x)
            days.append(friday.strftime('%m/%d/%Y'))
    return days

def get_weekly_suppliment(friday):
    """
    return id of each wss category.
    Args:
        friday ([str]): date as string(only friday), because WSS is
        published on every Friday from RBI.
    Returns:
        [array]: array of params Id from WSS
    """
    # path =r"https://www.rbi.org.in/Scripts/WSSViewDetail.aspx?TYPE=Basic&PARAM1=12/18/2015"
    path =r"https://www.rbi.org.in/Scripts/WSSViewDetail.aspx?TYPE=Basic&PARAM1={}".format(friday)
    res = requests.get(path)
    soup = BeautifulSoup(markup=res.text, features="html.parser")

    wss=[]
    my_dict={}
    for link in soup.table.find_all("a"):
        if 'WSSView' in link.get('href'):
            id = (link.get('href').split('='))[-1]
            # print(link.string,"---", link.get('href'))
            # print(link.string,"---", id)
            wss.append([link.string, id])
            my_dict[link.string]=id
            #print(my_dict)

    return my_dict

def slice_tensor(data, slice_begin, size):
    """
    get timeseries across tensor
    slice tensor fr a given location.

    Args:
        data ([type]): tensor
        slice_begin ([type]): [description]
        size ([type]): [description]

    Returns:
        [type]: [description]
    """
    sliced = tf.slice(data, slice_begin, size)
    length = sliced.shape[0]
    serialized = tf.reshape(sliced, [length])
    serialized = np.array(serialized)
    return serialized

if __name__ == '__main__':
    
    startDate = date(2020,1,1)
    endDate = date(2020,1,1)
    fridays = get_fridays(startDate, endDate)
    for friday in fridays:
        wss_id = get_weekly_suppliment(friday)

        # 1. wss_id is a dict. read the dict and pass call appropriate function.
        # 2. output of each function should be accumulated as consecutive dataframes
        # 3. call --> slice_tensor(tensor frm step-2, [0, 2, 1], [data.shape[0], 1, 1])
        # 4. plot, x-axis dates, y-axis (values from step-3)

        Liabilities_and_Assets()
        Foreign_Exchange_Reserves()
        Cash_Balances_of_SCB()
        SCB_Business_in_India()
        Ratio_and_Rates()
        Money_Stock()
        Reserve_Money()
        Liquidity_Operations()
        Major_Price_Indices()
        Certificates_of_Deposit()
        Commercial_Paper()
        Money_Markets()
        Treasury_Bills_Outstanding()
        Market_Borrowings()