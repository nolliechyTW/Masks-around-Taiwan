import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# import open data from website
df = pd.read_csv("https://data.nhi.gov.tw/Datasets/Download.ashx?rid=A21030000I-D50001-001&l=https://data.nhi.gov.tw/resource/mask/maskdata.csv")
# if open data is downloaded, use this instead
# df = pd.read_csv(r"C:\Users\abc\Desktop\359_Python\maskdata.csv")

# get the first 5 rows
df.head()

# add up two columns to create "口罩總數"
df["口罩總數"] = df["兒童口罩剩餘數"] + df["成人口罩剩餘數"]

# total number of "口罩總數" will be 
# df["口罩總數"].sum()

# find out the district and city where each medical facility is located
df["縣市名"] = df["醫事機構地址"].apply(lambda addr : addr [0:3]) # call apply() to transform data
df.head()

# sum data by "縣市名"
df2 = df.groupby("縣市名").sum()

# compute mask% in each city
df2["比例%"] =  df2["口罩總數"] * 100 / df2["口罩總數"].sum()

# use round() to round the ratio
df2["比例%"] = df2["比例%"].round(2)

# order by "比例%", descending
df3 = df2.sort_values("比例%", ascending=False)


# draw a bar chart
plt.style.use("ggplot")

# set the size of chart
plt.rcParams["figure.figsize"] = (20,6)

# Since there is a problem with Matplotlib displaying Chinese, there are many different solutions to this problem.
# The simplest solution is to change the font.sans-serif of the font in the parameter word rcParams in Matplotlib to SimHei or Microsoft JhengHei.
# remeber to open the font folder, download SimHei or Microsoft JhengHei
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
# if the above method doesn't solve the problem, see this: https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/359974/

plt.bar(df3.index, df3["比例%"])
plt.ylabel("縣市名稱")
plt.xlabel("比例%")
plt.title("縣市口罩占比")
plt.show()
