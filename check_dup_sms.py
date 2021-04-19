import pandas as pd
import sys
filename = sys.argv[1]
sheetname = sys.argv[2]
stype = sys.argv[3]
df = pd.read_excel(filename, sheetname)
df = df.sort_values(["originationNumber","deliveryTime"])
print(df.head(1))
duplicates = []
i = 0
j=i+1
while j< len(df):  
   row1 = df.iloc[i]
   row2 = df.iloc[j]
   if row1['originationNumber'] == row2['originationNumber']:
      if row1['deliveryTime'] == row2['deliveryTime']:
         print ("MSISDN " + str(row1['originationNumber']) + " ANSWER TIME " + str(row2['deliveryTime']) )
         duplicates.append(row1)
         duplicates.append(row2)
      else:
         print ("MSISDN " + str(row1['originationNumber']) + " ANSWER1 " + str(row1['deliveryTime']) + " ANSWER2 " + str(row2['deliveryTime']))
   else:
      print ("MSISDN " + str(row1['originationNumber']) + " CALLING NUMBER " + str(row2['originationNumber']))
   i=i+1
   j=j+1

df_dup = pd.DataFrame(duplicates) 
df_dup.to_csv('output_dup_'+ stype + ".txt")

