# 豆果美食 API
使用toapi实现的豆果美食API。
目前实现的接口有：
- 主页
- 搜索
- 菜谱详情

## Overview
基于开源项目toapi实现的豆果美食api服务。

## Usage
下载代码或克隆源码到本地  
```
git clone git@github.com:ididid8/toapi-douguo.git
```  
安装依赖  
```
cd toapi-douguo
pip install -r requirements.txt
```  

运行项目  
```
python wsgi.py
```  
访问项目  
```
curl http://your_server_ip:5000
```  

## Problem
1. toapi==2.1.2使用`defaultdict`做页面缓存，并且不支持自定义缓存。本项目需要定义缓存时间，所以把toapi==2.1.2源码中缓存部分删除，实现无缓存运行，后续考虑增加缓存  
2. toapi==2.1.2中使用的htmlparsing==0.1.5在解析空html元素（例如：`<div></div>`）时会出现IndexError报错，导致请求出错，在htmlparsing源码中增加了捕获IndexError异常代码避免报错。

## Example
现有3个可用于请求的API：
- /search/{keyword}/{page}
- /index
- /cookbook/{id}  

搜索菜谱  
> GET `/search/口水鸡`
```
{
	"Page": {
		"current": 0,
		"total": 180
	},
	"Repic": [{
		"img": "https://cp1.douguo.com/upload/caiku/b/8/0/400x266_b895359a1dbb7b1f76b725fa28e85050.jpg",
		"major": "土鸡,花生,辣椒粉,小葱,生姜,香菜,独蒜,花椒,香油,生抽,盐,白糖,醋,味精,花椒粉,鸡汤 ",
		"title": "口水鸡",
		"url": "/cookbook/1402490.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/2/c/3/400x266_2c17c014872c2ec6ec8b3dde4b759a93.jpg",
		"major": "鸡腿 ",
		"title": "上海年夜饭必备--口水鸡",
		"url": "/cookbook/1114067.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/c/4/2/400x266_c4c86a2e262ac42884ab60fc367e4122.jpeg",
		"major": "鸡全腿,熟花生米碎 ",
		"title": "懒人版口水鸡",
		"url": "/cookbook/205491.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/2/c/7/400x266_2c929fa20eb09964d07bf07c6f32a397.jpg",
		"major": "麻鸡 ",
		"title": "口水鸡",
		"url": "/cookbook/177757.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/4/4/d/400x266_4457add22a445d48a707889a1f4c07ed.jpg",
		"major": "三黄鸡 ",
		"title": "“川味口水鸡”怎样做又滑又嫩，麻辣酸甜口口留香",
		"url": "/cookbook/1523586.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/d/3/1/400x266_d3a19e7910579b63b29e288db1584091.jpg",
		"major": "鸡腿 ",
		"title": "口水鸡",
		"url": "/cookbook/1397447.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/8/e/4/400x266_8edb9f177f04b58c559718a841677fc4.jpg",
		"major": "鸡腿或三黄鸡,黄瓜 ",
		"title": "口水鸡",
		"url": "/cookbook/205951.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/0/a/1/400x266_0a2a40d6541dc6e1dea4034a884b9d11.jpeg",
		"major": "鸡腿,生抽,醋,白糖,葱,大蒜,辣椒面,花椒,生姜,料酒,花生 ",
		"title": "惹人流口水的口水鸡",
		"url": "/cookbook/1400006.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/3/8/5/400x266_387db2c95c24ba5e18262dba0f6fedf5.jpg",
		"major": "鸡腿,花生米,葱,姜,蒜,小米椒,料酒,生抽,醋,白砂糖,辣椒红油,芝麻油 ",
		"title": "口水鸡---简易版做法",
		"url": "/cookbook/1411278.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/b/5/7/400x266_b5558bd244b1421195cc184fcbe6ad57.jpeg",
		"major": "土鸡,冰块（或冰冻矿泉水、冰袋）,植物油（菜油最佳）,生姜（炼油用）,花椒（炼油用）,藤椒（青花椒，炼油用）,八角（炼油用）,草果（炼油用）,干辣椒（炼油用）,红油辣椒,花椒油,生姜,大蒜,生抽,白糖,盐,花椒粉,鸡精（选用）,凉拌醋（选用）,小米辣 ",
		"title": "川味口水鸡",
		"url": "/cookbook/1345844.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/a/0/e/400x266_a0df065ef4e4a074649c0018572f58ce.jpg",
		"major": "鸡腿,葱,姜,蒜,麻椒油,辣椒油,酱油,醋,熟花生碎 ",
		"title": "麻辣口水鸡",
		"url": "/cookbook/1356785.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/8/2/8/400x266_823b87e2cbc9aa4b9eeb6d80b6c6c0d8.jpg",
		"major": "鸡腿,鸡翅 ",
		"title": "口水鸡#单挑夏天#",
		"url": "/cookbook/1582431.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/7/0/8/400x266_70840af850bce44d29fc54420ef2a608.jpeg",
		"major": "三黄鸡 ",
		"title": "川香口水鸡",
		"url": "/cookbook/180415.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/c/9/1/400x266_c93bf20c943bf9e82a304eb862dd91b1.jpg",
		"major": "鸡腿肉,黄瓜 ",
		"title": "【辣椒私房菜】口水鸡",
		"url": "/cookbook/1305158.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/2/8/f/400x266_28fbad743ab4745bf3349ae20b88ce5f.jpg",
		"major": "鸡腿,葱姜,红油,花生芝麻,醋,生抽,白糖,香料,香油,葱 ",
		"title": "桌饭年夜菜 | 香辣口水鸡",
		"url": "/cookbook/1504535.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/7/3/a/400x266_73027dfc7f30d82dc27469c768ec754a.jpg",
		"major": "鸡腿两个,花生米 ",
		"title": "家常版口水鸡----让你夏天也有食欲大口吃肉",
		"url": "/cookbook/1202865.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/e/d/4/400x266_ed259d5ab2110c7b29c3346f49c49354.jpg",
		"major": "冰鲜鸡腿 ",
		"title": "川菜名片【口水鸡】",
		"url": "/cookbook/1348916.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/7/0/0/400x266_70cb7c68059a26c1778011a8f2d24ef0.jpg",
		"major": "鸡腿 ",
		"title": "减辣版口水鸡",
		"url": "/cookbook/176683.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/9/0/4/400x266_903ef38ea956d6e2b9f04b9ae18a0c24.jpg",
		"major": "鸡腿,香菜,葱,生姜,大蒜,花生米,桂皮,香叶,八角,白醋,花椒,辣椒油,生抽,盐,陈醋,冰水 ",
		"title": "口水鸡",
		"url": "/cookbook/1725341.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/d/c/1/400x266_dc84e1da8040305c65fb0ba364f560c1.jpg",
		"major": "三黄鸡 ",
		"title": "口水流了一地的《口水鸡》",
		"url": "/cookbook/1431010.html"
	}]
}
```  

> GET `/index`
```
{
	"Selected": [{
		"img": "https://cp1.douguo.com/upload/caiku/9/5/4/220x220_950b5ba78c3f612915ad9553478f68d4.jpg",
		"title": "双色厚蛋烧 宝宝辅食食谱",
		"url": "/cookbook/2064252.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/8/2/b/220x220_8275d9da05b706a7b0bb361a95db967b.jpg",
		"title": "酸菜鱼",
		"url": "/cookbook/2064162.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/4/8/b/220x220_48a3920722028e843dfe0c53e781dd2b.jpeg",
		"title": "红薯粑粑",
		"url": "/cookbook/2064123.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/5/8/6/220x220_586f12e6cdf53cf9743f2d1ca727b496.jpg",
		"title": "#初春润燥正当时#桂圆山药红枣汤，给姐们的养颜汤～能补气血哦",
		"url": "/cookbook/2064092.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/d/c/0/220x220_dcf3b7000785a04cfee09ba939a825b0.jpg",
		"title": "可乐鸡翅 #精品菜谱挑战赛#",
		"url": "/cookbook/2064105.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/3/e/c/220x220_3e4d9f7bac762f547850bba5905a05cc.jpg",
		"title": "#初春润燥正当时#醋溜藕丁",
		"url": "/cookbook/2064160.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/2/a/c/220x220_2a60959901e9efbca40619307a96047c.jpg",
		"title": "还原小时候的味道 | 自制安心油条",
		"url": "/cookbook/2064081.html"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/7/7/0/220x220_77b41737d757254a4150a56ddd817b20.jpg",
		"title": "蔓越莓酸奶条",
		"url": "/cookbook/2064292.html"
	}]
}
```  
> GET `/cookbook/2064252`
```
{
	"Cookbook": {
		"browse_count": "69129 浏览",
		"collect_count": "2304 收藏",
		"img": "https://cp1.douguo.com/upload/caiku/9/5/4/690x390_950b5ba78c3f612915ad9553478f68d4.jpg",
		"intro": "\r\n            “参考月龄：12个月以上\r\n姐妹们都知道，鸡蛋是最好的营养来源之一，可以给宝宝补充最优质的蛋白质，再加上补钙效果棒棒的奶酪，整个蛋卷营养更赞了！\r\n切成小块后，宝宝看见小零食黄色中带绿又带红，开心得不行！也不挑食了，抢着要抓这个五颜六色的新鲜玩意呢！”\r\n我给宝宝做的辅食都拍成了视频，收录在了我的公众号《宝宝辅食达人》里，包括主食、汤羹、烘焙、食疗等，关注我，不再为宝宝吃啥发愁啦！\r\n        ",
		"tip": "辅食制作和喂养问题都可以私我哦：shipu993需要的话可以私聊我进辅食群",
		"title": "双色厚蛋烧 宝宝辅食食谱"
	},
	"Ingredients": [{
		"ingredient": "玉米淀粉",
		"weight": "10克"
	}, {
		"ingredient": "奶酪",
		"weight": "15克"
	}, {
		"ingredient": "菠菜",
		"weight": "10克"
	}, {
		"ingredient": "鸡蛋",
		"weight": "2个"
	}, {
		"ingredient": "西红柿",
		"weight": "35克"
	}, {
		"ingredient": "",
		"weight": ""
	}],
	"Step": [{
		"img": "https://cp1.douguo.com/upload/caiku/4/0/d/200_402fa0053cf59f3a332d66b016dcd10d.jpg",
		"step": "步骤1\r\n                    参考月龄：12个月以上，对食材不过敏的宝宝\r\n食材准备：玉米淀粉10克、奶酪15克、菠菜10克、鸡蛋2个、西红柿35克\r\n操作时间：20分钟\r\n难度分析：初级"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/f/b/d/200_fbcaecf3cf8968fc90c66d47f4b673cd.jpg",
		"step": "步骤2\r\n                    将西红柿表面用小刀划“十字口”。"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/a/c/6/200_ac7f7b6ecb4c5d1e179b76e100cad806.jpg",
		"step": "步骤3\r\n                    西红柿倒入沸水中烫1分钟，这么做是为了能更轻松的去掉西红柿的皮。"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/0/8/4/200_08cc962374dd686bc77010e54a7e5c84.jpg",
		"step": "步骤4\r\n                    接着把西红柿剥皮、切小丁。"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/0/5/d/200_05d721445e0a29db1b51fc4821bc667d.jpg",
		"step": "步骤5\r\n                    菠菜放入沸水中焯水。"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/2/3/e/200_23f4f2abbd04767884ea490e11a5c9be.jpg",
		"step": "步骤6\r\n                    沥干水分捞出来，切成小末。"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/0/3/2/200_03bae22756b79f753c71e37de12c3c92.gif",
		"step": "步骤7\r\n                    将玉米淀粉分为两份，并分别加入15克清水，搅拌均匀。"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/d/8/6/200_d87f765a78709a8f6467a2f3d35dad56.gif",
		"step": "步骤8\r\n                    两个碗中分别加入1个鸡蛋，搅打均匀。\r\n\r\n*周岁以上的宝宝可以加入适量的盐来提味哦~"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/c/a/f/200_cac302ceb3010b5a25917cc4619c877f.jpg",
		"step": "步骤9\r\n                    再分别加入菠菜、35克西红柿，继续搅拌均匀。"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/3/b/e/200_3b6dd286545f4bdc588a442365b293ae.gif",
		"step": "步骤10\r\n                    热锅刷油，倒入西红柿蛋液。"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/7/6/7/200_76d045d0909acf127e020b32bb4452a7.jpg",
		"step": "步骤11\r\n                    煎至蛋液凝固时，撒入奶酪碎。\r\n\r\n*这里的奶酪建议姐妹们选择原制的奶酪，具体的挑选方法君君之前有总结过小技巧哦，直接在后台回复“奶酪”就可以看到了。"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/0/9/8/200_098ef1d7d026ead09fd9bd673065f4c8.gif",
		"step": "步骤12\r\n                    用铲子和筷子，把蛋饼慢慢的卷起来，就形成一个蛋卷了。\r\n\r\n*这时候火大了不容易控制，一定要用小火来操作哦。"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/1/6/e/200_161344ae747cb82a645c20dcbc45130e.jpg",
		"step": "步骤13\r\n                    继续在锅中刷油，倒入菠菜蛋液。"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/7/d/8/200_7de37ac1c736db57c255755e52328eb8.gif",
		"step": "步骤14\r\n                    煎至稍微凝固后，裹着西红柿蛋饼一起圈起来。\r\n\r\n*不要等彻底凝固了再圈，那样两层蛋饼之间会脱开的。"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/8/0/a/200_80b41760df4f0c51f2829998f20338ca.jpg",
		"step": "步骤15\r\n                    烙熟后，热气腾腾又美味的双层蛋烧就可以出锅啦~"
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/1/1/7/200_11b2d107204da33c0555215dc1cb6827.gif",
		"step": "步骤16\r\n                    最后我们切成小段，方便宝宝用手抓着吃."
	}, {
		"img": "https://cp1.douguo.com/upload/caiku/6/8/7/200_6855c4035f9d2ba2379767e6400dd6b7.jpg",
		"step": "步骤17\r\n                    颜值超高，营养也多元，碳水化合物、蛋白质、微生物、矿物质等，一站式凑齐，再搭配一份粥品，搞定早餐~ \r\n\r\n好啦，明天早餐就是它吧，君君等你们交作业喽。"
	}]
}
```
