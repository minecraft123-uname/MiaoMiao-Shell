# MiaoMiao-Shell

在开始游玩前，请先阅读这篇文档自学相关信息。

欢迎来到妙妙炮弹！

游戏主程序为main.py，开发环境为python3.10.9。

配置数据存储在config.Settings类中，所有数据都可修改。

我暂时没有添加记录历史最高分数的功能，如有要求联系我。

子弹图片我找了3个，如需更多可自行查找，存储到images/targetTypes目录。不要重命名images/targetTypes/mrp.jpg!

游戏共有5条命，每击中一个MRP都会减少一条命，并将得分清零。同时血量数据下的MRP头像会改变。

在我的设计中，击中一个细胞图片增加2分，击中一个染色体图片增加1分。要修改这个，请修改config.Settings.targetDict属性。

当MRP数量在总目标数量中占比达到一定值时，系统将从MRP中随机选取一半并替换成任意非MRP目标种类。这个检测阈值为config.Settings.clearMRPsRate属性。

每个MRP移动方向(水平或垂直)随机，其移动范围和速度均随得分增加而增加。当因击中MRP导致得分重置时，MRP移动范围和速度不会重置！

如想暂时关闭血量机制以获得更好的游戏体验，把tools.check_collisions函数中lives.reduceLives(mrps)改成注释。

That's all I wanna tell u. Wish u a good time! 

	——SX
