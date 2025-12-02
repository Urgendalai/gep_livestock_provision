### Access FAOSTAT dataset           ###
### Use the normalized full dataset  ###
### Haku Bo                          ###
### Sep 6, 2025                      ###



import os
import pandas as pd
import numpy as np

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

# livestock_value_codes = [
#     1012, 1017, 1018, 1019, 1020, 1025, 1032, 1035, 1036, 1037,
#     1044, 1055, 1058, 1062, 1069, 1070, 1073, 1077, 1080, 1084,
#     1087, 1089, 1091, 1094, 1097, 1098, 1108, 1111, 1120, 1122,
#     1124, 1127, 1128, 1129, 1130, 1137, 1141, 1144, 1151, 1154,
#     1158, 1161, 1163, 1166, 1176, 1182, 1183, 1185, 1770, 1780,
#     2044, 867, 868, 869, 882, 944, 947, 948, 949, 951, 972, 977,
#     978, 979, 982, 987, 995
# ]


livestock_value_codes = [
    1012, 1017, 1018, 1019, 1020, 1025, 1032, 1035, 1036, 1037,
    1044, 1055, 1058, 1062, 1069, 1070, 1073, 1077, 1080, 1084,
    1087, 1089, 1091, 1094, 1097, 1098, 1108, 1111, 1120, 1122,
    1124, 1127, 1128, 1129, 1130, 1137, 1141, 1144, 1151, 1154,
    1158, 1161, 1163, 1166, 1176, 1182, 1183, 1185,
    2044, 867, 868, 869, 882, 944, 947, 948, 949, 951, 972, 977,
    978, 979, 982, 987, 995
]

# check element coverage
df_v['Element'].value_counts()

ls_df_v = df_v[
  (df_v['Item Code'].isin(livestock_value_codes)) &
  (df_v['Area Code'] < 5000)
]

ls_df_v.head()

print(ls_df_v[['Element Code', 'Element']].drop_duplicates().reset_index(drop=True))

ls_df_v['Element'].value_counts()


# check the primary livestock production value, this is the first stage output of the total value
ls_df_v1 = ls_df_v[
  (df_v['Element Code'] == 152) &
  (df_v['Area Code'] < 5000)
]

ls_df_v1.head()
unique_vals = ls_df_v1["Area"].nunique()
print(unique_vals)


# export production data
ls_df_v.to_csv("D:/Netcapteems/faostat/df_v_livestock.csv", index=False)
ls_df_v1.to_csv("D:/Netcapteems/faostat/df_v_livestock_v1.csv", index=False)


# #######################################################
# # check the data between differen groups match or not 
# # #####################################################
# print(
#     ls_df_q[['Item Code', 'Item']]
#       .drop_duplicates()
#       .sort_values(['Item Code', 'Item'], ascending=True)
#       .reset_index(drop=True)
# )

# print(
#     ls_df_p[['Item Code', 'Item']]
#       .drop_duplicates()
#       .sort_values(['Item Code', 'Item'], ascending=False)
#       .reset_index(drop=True)
# )

# print(
#     ls_df_v[['Item Code', 'Item']]
#       .drop_duplicates()
#       .sort_values(['Item Code', 'Item'], ascending=True)
#       .reset_index(drop=True)
# )

# ###############################################################
# # Load the FAOSTAT employment data for validation
# ###############################################################

# # the employment data does not distinguish between crop and livestock production so being hold

# data_path4 = "D:/Netcapteems/faostat/Employment_Indicators_Agriculture_E_All_Data_(Normalized).csv"
# df_e = pd.read_csv(data_path4, low_memory=False)
# df_e.head(), df_e.columns

# # check element coverage
# df_e['Element'].value_counts()
# df_e['Indicator'].value_counts()
# sort_year = df_e['Year'].value_counts()
# print(sort_year.sort_index())

# ls_df_e = df_e[
#   (df_e['Indicator Code']== 21111) &
#   (df_e['Area Code'] < 5000)
# ]

# ls_df_e['Indicator'].value_counts()

# print(ls_df_e.describe())

# # export production data
# # ls_df_e.to_csv("D:/Netcapteems/faostat/df_e_livestock.csv", index=False)


#######################################################
# Livestock food share calculation 
# #####################################################

data_path5 = "D:/Netcapteems/faostat/Value_of_Production_E_ItemCodes.csv"
df_item = pd.read_csv(data_path5, low_memory=False)
df_itemd = df_item[df_item["livestock_id"] == 1]

df_itemd.head()

# Clean column names in df_itemd (remove leading/trailing spaces)
df_itemd = df_itemd.rename(columns=str.strip)

# Make sure Value is numeric
ls_df_v1["Value"] = pd.to_numeric(ls_df_v1["Value"], errors="coerce")

# ----------------------------------------------------
# 2. Prepare grouping info from df_itemd: meat / milk / other
# ----------------------------------------------------
agg_col = "aggreated(meat=1;milk=2;other=3)"
group_map = {1: "meat", 2: "milk", 3: "other"}

# Only rows with a group code and livestock_id == 1
df_itemd_groups = df_itemd[
    (df_itemd["livestock_id"] == 1) & (df_itemd[agg_col].notna())
].copy()
df_itemd_groups["group"] = df_itemd_groups[agg_col].astype(int).map(group_map)

# ----------------------------------------------------
# 3. Merge grouping info onto ls_df_v1 via Item Code
# ----------------------------------------------------
df = ls_df_v1.merge(
    df_itemd_groups[["Item Code", "group"]],
    on="Item Code",
    how="left"
)

# Keys that define a country-year slice
group_keys = [
    "Area Code", "Area Code (M49)", "Area",
    "Element Code", "Element",
    "Year Code", "Year", "Unit"
]

# ----------------------------------------------------
# 4. Aggregate by group (meat/milk/other) for each country & year
# ----------------------------------------------------
grouped = (
    df[df["group"].notna()]
    .groupby(group_keys + ["group"], as_index=False)["Value"]
    .sum()
)

# Turn grouping label into Item, clear Item Code columns
grouped = grouped.rename(columns={"group": "Item"})
grouped["Item Code"] = pd.NA
grouped["Item Code (CPC)"] = pd.NA

# Reorder columns similar to original
grouped = grouped[
    ["Area Code", "Area Code (M49)", "Area",
     "Item Code", "Item Code (CPC)", "Item",
     "Element Code", "Element", "Year Code", "Year",
     "Unit", "Value"]
]

# ----------------------------------------------------
# 5. Total row per country & year (sum of all 3 groups)
# ----------------------------------------------------
totals = (
    grouped
    .groupby(group_keys, as_index=False)["Value"]
    .sum()
)

totals["Item"] = "total"
totals["Item Code"] = pd.NA
totals["Item Code (CPC)"] = pd.NA

totals = totals[
    ["Area Code", "Area Code (M49)", "Area",
     "Item Code", "Item Code (CPC)", "Item",
     "Element Code", "Element", "Year Code", "Year",
     "Unit", "Value"]
]

# ----------------------------------------------------
# 6. Combine group rows and total rows
# ----------------------------------------------------
agg_all = pd.concat([grouped, totals], ignore_index=True)

# ----------------------------------------------------
# 7. Ratios: aggregated value / total value (per country-year)
# ----------------------------------------------------
totals_for_merge = totals[group_keys + ["Value"]].rename(
    columns={"Value": "total_value"}
)

agg_all = agg_all.merge(totals_for_merge, on=group_keys, how="left")

# ratio for meat / milk / other; total row gets NaN
agg_all["ratio"] = agg_all["Value"] / agg_all["total_value"]
agg_all.loc[agg_all["Item"] == "total", "ratio"] = pd.NA

# ----------------------------------------------------
# 8. Copy and preserve Item Code == 2044 rows from ls_df_v1
# ----------------------------------------------------
df_2044 = ls_df_v1[ls_df_v1["Item Code"] == 2044].copy()

# Attach total_value for corresponding country-year
df_2044 = df_2044.merge(totals_for_merge, on=group_keys, how="left")

# No ratio needed for 2044 row
df_2044["ratio"] = pd.NA

# ----------------------------------------------------
# 9. Check column: value of 2044 - total value
# ----------------------------------------------------
df_2044["diff_2044_minus_total"] = df_2044["Value"] - df_2044["total_value"]

# For aggregated rows, this check doesn’t apply → keep NaN
agg_all["diff_2044_minus_total"] = pd.NA

# ----------------------------------------------------
# 10. Combine aggregated rows + 2044 rows into final result
# ----------------------------------------------------
final = pd.concat([agg_all, df_2044], ignore_index=True, sort=False)

# Drop helper total_value column
final = final.drop(columns=["total_value"])

# Optional: sort nicely by country, year, then item
final = final.sort_values(
    ["Area Code", "Area Code (M49)", "Area", "Year", "Item"],
    kind="mergesort"
).reset_index(drop=True)

# ----------------------------------------------------
# 11. (Optional) Keep only desired columns + save
# ----------------------------------------------------
final = final[[
    "Area Code", "Area Code (M49)", "Area",
    "Item Code", "Item Code (CPC)", "Item",
    "Element Code", "Element", "Year Code", "Year",
    "Unit", "Value", "ratio", "diff_2044_minus_total"
]]

unique_val_f = final["Area"].nunique()
print(unique_val_f)

# # Save for immd check:
# final.to_csv("D:/Netcapteems/faostat/df_livestock_aggregated_with_ratios.csv", index=False)


#############################################################
# import modified data 
data_path6 = "D:/Netcapteems/faostat/df_livestock_aggregated_with_ratios.csv"
final_s1 = pd.read_csv(data_path6)

years_to_keep = [2014, 2015, 2016, 2019]
final_s1["Year"] = pd.to_numeric(final_s1["Year"], errors="coerce")
final_s1 = final_s1[final_s1["Year"].isin(years_to_keep)].copy()

final_s1['Year'].value_counts()


# Make sure this column exists
if "diff_2044_minus_total" not in final_s1.columns:
    final_s1["diff_2044_minus_total"] = np.nan

# 2. FAO price indices for 2019
price_index_2019 = {
    "meat": 99.5,
    "milk": 102.8,
    "other": 102.8
}

# Country–year grouping keys
group_keys = [
    "Area Code", "Area Code (M49)", "Area",
    "Element Code", "Element",
    "Year Code", "Year", "Unit"
]

# 3. For 2019: P = (price index) * ratio for meat/milk/other
final_s1["P"] = np.nan

mask_groups_2019 = (
    (final_s1["Year"] == 2019) &
    final_s1["Item"].isin(["meat", "milk", "other"])
)

final_s1.loc[mask_groups_2019, "P"] = (
    final_s1.loc[mask_groups_2019, "ratio"]
    * final_s1.loc[mask_groups_2019, "Item"].map(price_index_2019)
)

# 4. Sum those 3 values for each country & year (P2019),
#    store it as P on the "total" row
P_sum_2019 = (
    final_s1[mask_groups_2019]
    .groupby(group_keys)["P"]
    .sum()
    .rename("P_total_2019")
    .reset_index()
)

# Merge P_total_2019 back to all rows
final_s1 = final_s1.merge(P_sum_2019, on=group_keys, how="left")

# Put the summed P2019 onto the "total" row in 2019
mask_2019_total = (
    (final_s1["Year"] == 2019) &
    (final_s1["Item"] == "total")
)
final_s1.loc[mask_2019_total, "P"] = final_s1.loc[mask_2019_total, "P_total_2019"]

# 5. For 2019, Item Code == 2044:
#    V_2019_i$ = Value_2019 * (P2019 / 100)
final_s1["V_2019_i$"] = np.nan

mask_2019_2044 = (
    (final_s1["Year"] == 2019) &
    (final_s1["Item Code"] == 2044)
)

final_s1.loc[mask_2019_2044, "V_2019_i$"] = (
    final_s1.loc[mask_2019_2044, "Value"]
    * (final_s1.loc[mask_2019_2044, "P_total_2019"] / 100.0)
)

# Drop helper column
final_s1 = final_s1.drop(columns=["P_total_2019"])

# (Optional) Reorder columns like your example
final_s1 = final_s1[[
    "Area Code", "Area Code (M49)", "Area",
    "Item Code", "Item Code (CPC)", "Item",
    "Element Code", "Element", "Year Code", "Year",
    "Unit", "Value", "ratio", "diff_2044_minus_total",
    "P", "V_2019_i$"
]]

final_s1.head()
unique_val_f = final_s1["Area"].nunique()
print(unique_val_f)

# final_s1.to_csv("D:/Netcapteems/faostat/df_livestock_international2019.csv", index=False)
