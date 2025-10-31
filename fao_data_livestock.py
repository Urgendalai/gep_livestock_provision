### Access FAOSTAT dataset           ###
### Use the normalized full dataset  ###
### Haku Bo                          ###
### Sep 6, 2025                      ###



import os
import pandas as pd

# for showing all columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


#########################################################
# Load the FAOSTAT production data
#########################################################

data_path1 = "D:/Netcapteems/faostat/Production_Crops_Livestock_E_All_Data_(Normalized).csv"
df_q = pd.read_csv(data_path1, low_memory=False)

print(df_q[['Element Code', 'Element']].drop_duplicates().reset_index(drop=True))
print(df_q[['Item Code', 'Item']].drop_duplicates().reset_index(drop=True))

# Define key codes related to livestock in item
livestock_prod_codes = [
    866, 867, 868, 869, 882, 885, 886, 887, 888, 889, 890, 891, 894, 895, 896,
    897, 898, 899, 900, 901, 904, 919, 946, 947, 948, 949, 951, 952, 953, 955,
    957, 976, 977, 978, 979, 982, 983, 984, 987, 995, 1016, 1017, 1018, 1019,
    1020, 1021, 1022, 1025, 1034, 1035, 1036, 1037, 1043, 1057, 1058, 1062,
    1068, 1069, 1072, 1073, 1079, 1080, 1083, 1089, 1091, 1096, 1097, 1098,
    1107, 1108, 1110, 1111, 1126, 1127, 1128, 1129, 1130, 1140, 1141, 1150,
    1151, 1157, 1158, 1163, 1166, 1745, 1746, 1749, 1756, 1765, 1176, 1777, 
    1780, 1181, 1182, 1183, 1185, 1186, 1225, 1783, 1806, 1807, 1808, 1809, 
    1811, 1816, 2029
]

# apply filtering
ls_df_q = df_q[
  (df_q['Item Code'].isin(livestock_prod_codes)) &
  (df_q['Element Code'] == 5510) &
  (df_q['Unit'] == "t")&
  (df_q['Area Code'] < 5000)
]

print(ls_df_q.head(30))

# list the unique elements and items
print(ls_df_q[['Element Code', 'Element']].drop_duplicates().reset_index(drop=True))
print(ls_df_q[['Item Code', 'Item']].drop_duplicates().reset_index(drop=True))

# export production data
# ls_df_q.to_csv("D:/Netcapteems/faostat/df_q_livestock.csv", index=False)

# use the filtered data to get the number of livestock data
data_path_q1 = "D:/Netcapteems/faostat/df_q_livestock.csv"
df_num = pd.read_csv(data_path_q1, low_memory=False)

ls_stock_q = df_num[
  (df_num['Element Code'] == 5111) &
  (df_num['Unit'] == "An" or "1000 An")&
  (df_num['Area Code'] < 5000)
]
# ls_stock_q.to_csv("D:/Netcapteems/faostat/df_stock_q_livestock.csv", index=False)



##################################################################
# Load the FAOSTAT price data 
##################################################################

data_path2 = "D:/Netcapteems/faostat/Prices_E_All_Data_(Normalized).csv"
df_p = pd.read_csv(data_path2, low_memory=False)
df_p.head(), df_p.columns

# check element coverage
df_p['Element'].value_counts()

livestock_price_codes = [
  867, 882, 945, 947, 951, 973, 977, 982, 987, 1013, 1017, 1020, 1033, 1035, 1056,
  1058, 1062, 1069, 1071, 1073, 1078, 1080, 1085, 1088, 1089, 1091, 1095, 1097,
  1108, 1111, 1121, 1123, 1125, 1127, 1130, 1138, 1141, 1145, 1151, 1155, 1158,
  1162, 1163, 1166, 1176, 1182, 1183, 1185, 1765, 1769, 1780, 1783, 2044
]

# apply filtering
ls_df_p = df_p[
  (df_p['Item Code'].isin(livestock_price_codes)) &
  (df_p['Element Code'] == 5530) &
  (df_p['Months'] == "Annual value") &
  (df_p['Area Code'] < 5000)
]

ls_df_p['Item'].value_counts()

# export production data
# ls_df_p.to_csv("D:/Netcapteems/faostat/df_p_livestock.csv", index=False)


########################################################################
# Load the FAOSTAT value data for validation and extraction
########################################################################

data_path3 = "D:/Netcapteems/faostat/Value_of_Production_E_All_Data_(Normalized).csv"
df_v = pd.read_csv(data_path3, low_memory=False)
df_v.head(), df_v.columns

livestock_value_codes = [
    1012, 1017, 1018, 1019, 1020, 1025, 1032, 1035, 1036, 1037,
    1044, 1055, 1058, 1062, 1069, 1070, 1073, 1077, 1080, 1084,
    1087, 1089, 1091, 1094, 1097, 1098, 1108, 1111, 1120, 1122,
    1124, 1127, 1128, 1129, 1130, 1137, 1141, 1144, 1151, 1154,
    1158, 1161, 1163, 1166, 1176, 1182, 1183, 1185, 1770, 1780,
    2044, 867, 868, 869, 882, 944, 947, 948, 949, 951, 972, 977,
    978, 979, 982, 987, 995
]

# check element coverage
df_v['Element'].value_counts()

ls_df_v = df_v[
  (df_v['Item Code'].isin(livestock_value_codes)) &
  (df_v['Area Code'] < 5000)
]

print(ls_df_v[['Element Code', 'Element']].drop_duplicates().reset_index(drop=True))

ls_df_v['Element'].value_counts()


# check the primary livestock production value, this is the first stage output of the total value
ls_df_v1 = df_v[
  (df_v['Item Code'] == 2044) &
  (df_v['Area Code'] < 5000)
]
ls_df_v1['Element'].value_counts()


# export production data
# ls_df_v.to_csv("D:/Netcapteems/faostat/df_v_livestock.csv", index=False)
# ls_df_v1.to_csv("D:/Netcapteems/faostat/df_v_livestock_v1.csv", index=False)


#######################################################
# check the data between differen groups match or not 
# #####################################################
print(
    ls_df_q[['Item Code', 'Item']]
      .drop_duplicates()
      .sort_values(['Item Code', 'Item'], ascending=True)
      .reset_index(drop=True)
)

print(
    ls_df_p[['Item Code', 'Item']]
      .drop_duplicates()
      .sort_values(['Item Code', 'Item'], ascending=False)
      .reset_index(drop=True)
)

print(
    ls_df_v[['Item Code', 'Item']]
      .drop_duplicates()
      .sort_values(['Item Code', 'Item'], ascending=True)
      .reset_index(drop=True)
)

###############################################################
# Load the FAOSTAT employment data for validation
###############################################################

# the employment data does not distinguish between crop and livestock production so being hold

data_path4 = "D:/Netcapteems/faostat/Employment_Indicators_Agriculture_E_All_Data_(Normalized).csv"
df_e = pd.read_csv(data_path4, low_memory=False)
df_e.head(), df_e.columns

# check element coverage
df_e['Element'].value_counts()
df_e['Indicator'].value_counts()
sort_year = df_e['Year'].value_counts()
print(sort_year.sort_index())

ls_df_e = df_e[
  (df_e['Indicator Code']== 21111) &
  (df_e['Area Code'] < 5000)
]

ls_df_e['Indicator'].value_counts()

print(ls_df_e.describe())

# export production data
# ls_df_e.to_csv("D:/Netcapteems/faostat/df_e_livestock.csv", index=False)

