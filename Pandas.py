# Pandas is a software Library written in python programming language for data manipulation and analysis
# pandas module is mainly works with the tabular data
# There are three main data structures in pandas
#  series - 1d data
# Data Farme - 2d data
# Panel  - 3d
#  Series - single column in a table and holding data of any type
# DataFrame - is the 2 dimensional data like rows and columns in a table

""" data without empty values"""
import pandas as pd
print(pd.__version__)
# df = pd.read_excel(r'C:\Users\venkatesh\Desktop\StudentsMarks.xlsx')
# Empty_df = pd.read_excel(r'C:\Users\venkatesh\Desktop\StudentsMarks.xlsx', sheet_name='Students_Marks_Empty')
Duplicate_df  = pd.read_excel(r'C:\Users\venkatesh\Desktop\StudentsMarks.xlsx', sheet_name='Marks_Duplicates')
# print(df)

# Creating DataFrame By using dictionary
# di = {'Name':['Venky','Lucky'],'Roll':[16,18],'Percentage':[96.4,99]}
# dict_to_df = pd.DataFrame(di)
# print(dict_to_df)

#  Creating DataFrame by using List of Tuples
# LOT = [('Venky',25),('Lucky',16)]
# LOT_to_df = pd.DataFrame(LOT)
# print(LOT_to_df)
""" series"""
# a = [1,2,3]
# myseries = pd.Series(a)
# print(myseries)

""" Data slicing"""
# print(df.head(7))
# print(df.tail(10))
""" Shape give us the number of rows and columns like 8X4"""
# print(df.shape)

""" Describe() - gives the statistical info"""

# print(df.describe())

"""      Maths    Physics  Chemistry
count    8.000000   8.000000   8.000000
mean    78.625000  87.250000  94.250000
std     16.035118   6.881653   3.991061
min     57.000000  75.000000  85.000000
25%     64.000000  84.250000  94.500000
50%     85.500000  87.500000  95.500000
75%     88.250000  91.250000  96.000000
max    100.000000  96.000000  98.000000

"""

# print(df[0:3])
# print(df[['Name','Maths','Chemistry']][:5])

#  iterrows()- iterates over the rows and return data in tuple format
# for rec in df.iterrows():
#     print(rec)


""" LOC- stands for"""
# print(df.to_string())
# print(df.info())

""" Cleaning Empty cells"""
# print(Empty_df)
# new_df = Empty_df.fillna(80)
# new_df = Empty_df.dropna()
# print(new_df)


""" Duplicates data finding"""
file_path = r'C:\Users\venkatesh\Desktop\StudentsMarks_without_duplicates.xlsx'
print(Duplicate_df)
print(Duplicate_df.duplicated())
new_df = Duplicate_df.drop_duplicates(inplace = True)



# new_df.to_excel(r'C:\Users\venkatesh\Desktop\StudentsMarks.xlsx', sheet_name='Marks_Duplicates', index = False)
print(dir(pd))

