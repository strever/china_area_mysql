# china_area_mysql

## 中国5级行政区域mysql库

  爬取国家统计局官网的行政区域数据,包括省市县镇村5个层级;
  
  港澳地区的数据只有3级;台湾地区4级;
  
  包含大陆地区的邮政编码和经纬度信息.
  
---------------------------------------
####  cnarea20150930.7z是最新爬取2015年的数据,截止2015年09月30日.

  全部共749756条
  
  ·大陆数据共714048条,其中
  
  省/直辖市 31
  
  市/州 346
  
  县/区 3196
  
  乡/镇 40798
  
  村/社区 667519
  
  ·新增台湾数据,共37833条,具体到街/路/村


### 表结构

```sql

CREATE TABLE `china_area` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `parent_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '父级ID',
  `level` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '层级',
  `area_code` bigint(12) unsigned NOT NULL DEFAULT '0' COMMENT '行政代码',
  `zip_code` varchar(6) COLLATE utf8_unicode_ci NOT NULL DEFAULT '' COMMENT '邮政编码',
  `city_code` varchar(32) COLLATE utf8_unicode_ci NOT NULL DEFAULT '' COMMENT '区号',
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT '' COMMENT '名称',
  `short_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT '' COMMENT '简称',
  `merger_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT '' COMMENT '组合名',
  `pinyin` varchar(30) COLLATE utf8_unicode_ci NOT NULL DEFAULT '' COMMENT '拼音',
  `longitude` decimal(10,6) NOT NULL DEFAULT '0.000000' COMMENT '经度',
  `latitude` decimal(10,6) NOT NULL DEFAULT '0.000000' COMMENT '维度',
  PRIMARY KEY (`id`),
  KEY `idx_lev` (`level`,`parent_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3289 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='中国行政地区表';


```
