import pandas as pd
import sys
filename = sys.argv[1]
sheetname = sys.argv[2]
stype = sys.argv[3]
df = pd.read_excel(filename, sheetname)
df = df.sort_values(["callingNumber","answerTime"])
print(df.head(1))
duplicates = []
i = 0
j=i+1
while j< len(df):  
   row1 = df.iloc[i]
   row2 = df.iloc[j]
   if row1['callingNumber'] == row2['callingNumber']:
      if row1['answerTime'] == row2['answerTime']:
         print ("MSISDN " + str(row1['callingNumber']) + " ANSWER TIME " + str(row2['answerTime']) )
         duplicates.append(row2)
      else:
         print ("MSISDN " + str(row1['callingNumber']) + " ANSWER1 " + str(row1['answerTime']) + " ANSWER2 " + str(row2['answerTime']))
   else:
      print ("MSISDN " + str(row1['callingNumber']) + " CALLING NUMBER " + str(row2['callingNumber']))
   i=i+1
   j=j+1

df_dup = pd.DataFrame(duplicates) 
df_dup.to_csv('output_dup_'+ stype + ".txt")

