import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取数据文件
f = open("F:/python资料/资料/资料/资料/可视化案例数据/地图数据/疫情.txt", "r", encoding="UTF-8")
data = f.read()  # 全部数据

# 关闭文件
f.close()

# 取到各省数据

# 将字符串json转换为python字典
data_dict = json.loads(data)  # 基础数据字典

# 从字典中取到各省的数据
province_data_list = data_dict["areaTree"][0]["children"]

# 组装每个省份和确诊人数为元组，并将各个省的数据封装如列表内
data_list = []  # 绘图需要用的数据列表
for province_data in province_data_list:
    province_name = province_data["name"]  # 省份名称
    province_confirm = province_data["total"]["confirm"]  # 确诊人数
    data_list.append((province_name, province_confirm))

# 创建地图对象
chinaMap = Map()

# 添加数据
chinaMap.add("各省份确诊人数", data_list, "china")

# 设置全局配置，定制分段的视觉映射
chinaMap.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000-4999", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000-9999", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000-99999", "color": "#CC3333"},
            {"min": 100000, "label": "100000+", "color": "#990033"}
        ]
    )
)

# 绘制
chinaMap.render(path="国内疫情地图.html")
