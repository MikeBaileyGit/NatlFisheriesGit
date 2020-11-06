## Depdencies
import tabula
import pandas as pd

## Specify PDF filename
file = "2_data/raw/FSIS/Siluriformes-Fish-Species-FSIS.pdf"

## Import PDF
table = tabula.read_pdf(file, pages= "all", multiple_tables= True)

## Check values
table[1]

def tokenize(text):
    '''
    GOAL: Remove punctuation
    INPUT: Text
    OUTPUT: Text
    '''
    text = text.lower()
    text = text.replace('.','')
    text = text.replace('\\\\','')
    text = text.replace('-','')
    text = text.replace(',','')
    text = text.replace('\\\"','')
    text = text.replace('[','')
    text = text.replace(']\"','')
    text = text.replace('(','')
    text = text.replace(')','')
    text = text.replace('?','')
    text = text.replace(';','')
    text = text.replace(':','')
    return text

## Initiate empty list
word_list = []

## Loop through each data frame
for i in range(len(table)):
    ## Convert to list of values
    list = table[i].values.tolist()
    ## Loop through each list of values
    for j in range(len(list)):
        ## Loop through value
        for k in range(len(list[j])):
            ## If a list is string objects...
            if type(list[j][k]) == str:
                ## Convert to lower case and split using spaces
                words = list[j][k].lower().split()
                ## For each word...
                for word in words:
                    ## Remove punctuation
                    token = tokenize(word)
                    ## And add unique words to word list
                    if token in word_list: continue
                    else: word_list.append(token)

## Check word list
word_list

## Convert to pandas data frame
df0 = pd.DataFrame(word_list)

## Check data frame
df0

## Remove first 9 indices as they are related to headers
df1 = df0.drop(range(0,9)).copy()

## Rename column
df2 = df1.rename(columns={0:"word"})

## Check data frame
df2

## Export to CSV
df2.to_csv("2_data/output/build/fsisSiluriformesWords.csv", index= False)
