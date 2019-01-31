import pandas as pd

my_list = [[10, 13, 17], [3, 5, 1], [13, 11, 12]]

df = pd.DataFrame(my_list, columns=['A', 'B', 'C'])
df.to_csv('file.csv')
df.to_excel('exe11.xlsx')

#df = pd.DataFrame(list1)
#df.to_csv('file.csv')

# print(type(df))
# print(df)
#df.to_csv('file.csv', index=False, columns=['', 'E', 'F'])
