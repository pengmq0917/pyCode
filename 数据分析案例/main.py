from __future__ import annotations
from 数据分析案例.file_define import FileReader, TextFileReader, JsonFileReader
from 数据分析案例.data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

text_file_reader = TextFileReader("F:/python资料/第13章/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("F:/python资料/第13章/2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 将两个月份的数据合并为1个list来存储
all_data: list[Record] = jan_data + feb_data

# 开始进行数据计算
data_dict = {}
for record in all_data:
    if record in data_dict.keys():
        # 当前日期已经有记录了，所以和老记录做累加即可
        data_dict[record.date] += record.money
        pass
    else:
        data_dict[record.date] = record.money

# 可视化图表开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(list(data_dict.keys()))   # 添加x轴数据
bar.add_yaxis("销售额", list(data_dict.values()),label_opts=LabelOpts(is_show=False))  # 添加y轴数据
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

bar.render("销售额.html")
