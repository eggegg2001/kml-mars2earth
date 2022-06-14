kml-mars2earth
===========

概述：
众所周知，Google map采用的是高德的数据，而高德地图的坐标是被“加偏”过的，这么做的目的是国家处于安全考虑，对于国内地图坐标都进行了加密。
所以当我们从Google map绘制好路线，导出为kml再导入google earth后，就会发现路径上的一系列点与google earth上的卫星地图的正确的一系列点产生了偏移。
本程序的目的就是通过以下项目提供的算法，对kml文件进行“纠偏处理”：
纠偏前：
![image](https://user-images.githubusercontent.com/28710721/173500759-9d4d0d02-bb29-420d-9a9d-7427a697ead6.png)
纠偏后：
![image](https://user-images.githubusercontent.com/28710721/173500734-3efd2952-a180-40fe-a595-3b5aca163da9.png)

参考项目：
Transport coordinate算法：https://github.com/googollee/eviltransform
早期的kml纠正程序：https://github.com/JohnWong/fix-kml-kmz （由于作者长期不维护，该程序已经不可用）

使用方法：
``` shell
python main.py xxx.kml
```
