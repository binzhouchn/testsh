# 5.20任务：

1. 看下最近7天浏览器push下文章title(和url)的曝光数，从大到小排序
2. 看下用户画像有哪些字段
3. 站内push，其中表中docid等于xmpush中的itemid等于snapshot中的id

粗粒度的可以按人群进行push；细粒度的话可以类似个性化push，这个还要想
活跃度，


# 5.21任务

站内push 1. 内容池 2. 线上服务；这些别人会做，我们需要想办法召回

1. app端模型，用户首刷
2. 运营会出一些好的资讯
3. 专门的用户人群
4. 目前线上服务能用的模型就是FM



今天的任务一：

i 看下哪些人群点击率比较高

ii 看下feed流和非feed流的点击率情况

# 5.22任务


export PYSPARK_DRIVER_PYTHON="ipython"

export PYSPARK_DRIVER_PYTHON_OPTS="notebook"

alias snotebook='$SPARK_PATH/bin/pyspark --masterlocal[2]'

# 5.23任务

# 5.24任务

# 5.27任务

# 5.28任务

跑出浏览器画像表和o2o_noenter表，通过deviceid进行join根据点击率看下用户画像特征

# 5.29任务
解析浏览器画像表feeds_behavior字段
# 5.30任务
