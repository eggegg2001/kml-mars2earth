kml-mars2earth
===========

概述：
众所周知，Google map采用的是高德的数据，而高德地图的坐标是被“加偏”过的，这么做的目的是国家处于安全考虑，对于国内地图坐标都进行了加密。
所以当我们从Google map绘制好路线，导出为kml再导入google earth后，就会发现路径上的一系列点与google earth上的卫星地图的正确的一系列点产生了偏移。
本程序的目的就是通过以下项目提供的算法，对kml文件进行“纠偏处理”

纠偏前：\n
<img src="https://user-images.githubusercontent.com/28710721/173501048-01055968-0eff-4b0f-9339-3694071376d6.png" width="600" align='right'/>

纠偏后：
<img src="https://user-images.githubusercontent.com/28710721/173501116-7b319631-612b-4653-b5d9-80abe3ee8555.png" width="600" />


使用方法：
``` shell
python main.py xxx.kml
```

参考项目：
Transport coordinate算法：https://github.com/googollee/eviltransform
早期的kml纠正程序：https://github.com/JohnWong/fix-kml-kmz （由于作者长期不维护，该程序已经不可用）


