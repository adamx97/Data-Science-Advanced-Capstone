# Datafiles

import glob
import pandas as pd
import re


def CsvToDf(file, **kwargs):
    df = pd.read_csv(file, **kwargs)
    #print (df.columns)
    return df

def FixUpBuzzfeed(df):
    # rename column 'original_article_text_phase2' to 'text'
    df = df.rename(columns={'original_article_text_phase2':'text'})
    # add 'source' column of "buzzfeed-top"
    bftl = ['buzzfeed-top'] * df.shape[0]
    df = df.assign(source = bftl)
    # add id column of buzzfeedrow_[#]
    zi = df.index
    ld = {k: 'buzzfeed_line_' + str(k)  for k in zi }
    df.rename(index = ld, inplace=True)
    # add 'TruthValue' column with value 0
    tv = [0]  * df.shape[0]
    df = df.assign(truthvalue = tv)
    df.drop(['title', 'url', 'Politifact', 'Politifact FB', 'Snopes', 'Snopes FB','Factcheck', 'Factcheck FB', 'ABC', 'ABC FB', 'error_phase2',
             'article_title_phase2','publish_date_phase2', 'author_phase2'],axis=1, inplace=True)

    return df

def FixUpSnopes(df):
    # rename original_article_text_phase2 column to text
    df = df.rename(columns={'original_article_text_phase2':'text'})
    # add 'source' column of "snopes-checked"
    bftl = ['snopes-checked'] * df.shape[0]
    df = df.assign(source = bftl)    
    # set id to 'snopes_line_
    zi = df.index
    ld = ld = {k: 'snopes_line_' + str(k)  for k in zi }
    df.rename(index = ld, inplace=True)
    # Only save true and false stories (remove mostly false, mostly true, and mixed)
    # add truthvalue column
    truedf = df[ df['fact_rating_phase1'] == 'TRUE' ]
    tv = [1] * truedf.shape[0]
    truedf = truedf.assign(truthvalue = tv) 

    falsedf = df[ df['fact_rating_phase1'] == 'FALSE']
    fv = [0] * falsedf.shape[0]
    falsedf = falsedf.assign(truthvalue = fv) 
    frames =[truedf, falsedf]
    df = pd.concat(frames)
    df.drop(['fact_rating_phase1', 'snopes_url_phase1', 'article_title_phase1', 'article_category_phase1', 'article_date_phase1', 'article_claim_phase1', 
            'article_origin_url_phase1', 'index_paragraph_phase1',  'page_is_first_citation_phase1', 'error_phase2', 
             'article_title_phase2', 'publish_date_phase2', 'author_phase2', 'Jerry-label', 'Jill-label', 'Fatemeh-label', 'notes', 'original order', 'Agreement'], 
             axis=1, inplace=True)
    #df.head()
    return df

    


files = glob.glob("..\\dataset\\*.csv")
for a in files:
    print (a)
    if "buzzfeed-top" in a:
        print ("buzzfeed-top")
        dfBuzzfeedTop = CsvToDf(a)
        dfBuzzfeedTop = FixUpBuzzfeed(dfBuzzfeedTop)
        print (dfBuzzfeedTop.columns)
        print ("Rows: {} Columns: {}".format(dfBuzzfeedTop.shape[0], dfBuzzfeedTop.shape[1]))

    if 'snopes_checked_v02' in a: 
        print ("snopes_checked_v02")
        dfSnopes_Checked = CsvToDf(a, encoding="ISO-8859-1", engine='python')
        dfSnopes_Checked = FixUpSnopes(dfSnopes_Checked)
        print (dfSnopes_Checked.columns)
        print ("Rows: {} Columns: {}".format(dfSnopes_Checked.shape[0], dfSnopes_Checked.shape[1]))


mihalceaNewsDirs = glob.glob(R"..\dataset\Mihalcea\fakeNewsDataset")
mihalceaCelebDirs = glob.glob(R"..\dataset\Mihalcea\celebrityDataset")
mihalFakeDict = {}
mihalLegitDict ={}
for a in mihalceaNewsDirs:
    print (a)
    for b in glob.glob(a + "\\fake\\*"):
        #print (a,b)
        with open(b, 'r') as myfile:
            data = myfile.read().replace('\n', '')
        ididx = re.search(r"[a-z]+[0-9]+", b).span()
        _id = b[ididx[0]: ididx[1]] + 'fake'
        item  = {}
        item['text'] = data
        item['source'] = "MihalceaNewsFake"
        item['truthvalue'] = 0
        mihalFakeDict[_id]=  item
    for b in glob.glob(a + "\\legit\\*"):
        #print (a,b)
        with open(b, 'r') as myfile:
            data = myfile.read().replace('\n', '')
        ididx = re.search(r"[a-z]+[0-9]+", b).span()
        _id = b[ididx[0]: ididx[1]] + 'legit'
        item  = {}
        item['text'] = data
        item['source'] = "MihalceaNewsLegit"
        item['truthvalue'] = 1
        mihalLegitDict[_id]=  item
    
for a in mihalceaCelebDirs:
    print (a)
    for b in glob.glob(a + "\\fake\\*"):
        #print (a,b)
        with open(b, 'r', encoding='utf-8') as myfile:
            data = myfile.read().replace('\n', '')
        ididx = re.search(r"[0-9]+[a-z]+", b).span()
        _id = 'celeb' + b[ididx[0]: ididx[1]]
        item  = {}
        item['source'] = "MihalceaCelebFake"
        item['text'] = data
        item['truthvalue'] = 0
        mihalFakeDict[_id]=  item
    for b in glob.glob(a + "\\legit\\*"):
        #print (a,b)
        with open(b, 'r', encoding='utf-8') as myfile:
            data = myfile.read().replace('\n', '')
        ididx = re.search(r"[0-9]+[a-z]+", b).span()
        _id = 'celeb' + b[ididx[0]: ididx[1]]
        item  = {}
        item['source'] = "MihalceaCelebLegit"
        item['text'] = data
        item['truthvalue'] = 1
        mihalLegitDict[_id]=  item

dfMihalFake = pd.DataFrame(mihalFakeDict)
dfMihalFake = dfMihalFake.transpose()
print ("Rows: {} Columns: {}".format(dfMihalFake.shape[0], dfMihalFake.shape[1]))
print (dfMihalFake.columns)


dfMihalLegit = pd.DataFrame(mihalLegitDict)
dfMihalLegit = dfMihalLegit.transpose()

print (dfMihalLegit.columns)
print ("Rows: {} Columns: {}".format(dfMihalLegit.shape[0], dfMihalLegit.shape[1]))

# df: dfMihalLegit, dfMihalFake, dfBuzzfeedTop, dfSnopes_Checked
frames =[dfMihalLegit, dfMihalFake, dfBuzzfeedTop, dfSnopes_Checked]
dfTrueFalseNews = pd.concat(frames)

print (dfTrueFalseNews.columns)
print ("Rows: {} Columns: {}".format(dfTrueFalseNews.shape[0], dfTrueFalseNews.shape[1]))
dfTrueFalseNews.to_pickle("dfTrueFalseNews.pkl", protocol=4 ) # use protocol 4 to maintain compatibility with Watson Studio Python 3.6
