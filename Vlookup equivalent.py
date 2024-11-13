# import pandas 
import pandas as pd 

# read csv data 
df1 = pd.read_csv('G:\\My Drive\\Fixflo\FixfloIncorrect properties.csv') 
df2 = pd.read_csv('G:\\My Drive\\Fixflo\Report666323_13112024.csv') 

Left_join = pd.merge(df1, 
					df2, 
					on ='ExternalPropertyRef', 
					how ='inner') 
recordset = Left_join[['ExternalPropertyRef','Issue Id']]

#remove duplicates
recordset['ExternalPropertyRef']    = recordset['ExternalPropertyRef'].drop_duplicates()
recordset['Issue Id']               = recordset['Issue Id'].drop_duplicates()
#print(recordset)

#create new DataFrame that only contains rows without NaNs
no_nans = recordset[~recordset.isnull().any(axis=1)]

print(no_nans[['ExternalPropertyRef','Issue Id']])
#no_nans.count()

