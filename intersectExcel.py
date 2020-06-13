import pandas as pd
df = pd.read_excel("File1.xlsx")
inList=[]

for index, row in df.iterrows():
	no=str(row['Number'])
	inList.append(no)
inList=[i.strip(' ') for i in inList]
outList=[]
df = pd.read_excel("File2.xlsx")
for index, row in df.iterrows():
	no=str(row['Number'])
	if(no not in inList):
		outList.append(no)
print(outList)
print()
print(len(inList),len(outList))


