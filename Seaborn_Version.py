import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

myfont=FontProperties(fname=r"C:\Users\abc\Desktop\359_Python\字體\msjh.ttf",size=14)
# myfont=FontProperties(fname=r"C:\ path to msjh.ttf",size=14)
sns.set(font=myfont.get_family())
sns.set_style({"font.sans-serif":["Microsoft JhengHei"]})

bar, ax = plt.subplots(figsize=(15,6))
# assign data for x, y axis
sns.barplot(x=df3.index, 
            y=df3["比例%"])
# assign title
plt.title("縣市口罩佔比%", fontsize=14)
# show chart
plt.show()
