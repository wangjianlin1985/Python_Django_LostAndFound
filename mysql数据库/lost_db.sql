/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50620
Source Host           : localhost:3306
Source Database       : lost_db

Target Server Type    : MYSQL
Target Server Version : 50620
File Encoding         : 65001

Date: 2020-02-20 16:00:12
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `t_admin`
-- ----------------------------
DROP TABLE IF EXISTS `t_admin`;
CREATE TABLE `t_admin` (
  `username` varchar(20) NOT NULL DEFAULT '',
  `password` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_admin
-- ----------------------------
INSERT INTO `t_admin` VALUES ('a', 'a');

-- ----------------------------
-- Table structure for `t_area`
-- ----------------------------
DROP TABLE IF EXISTS `t_area`;
CREATE TABLE `t_area` (
  `areaId` int(11) NOT NULL AUTO_INCREMENT COMMENT '区域id',
  `areaName` varchar(20) NOT NULL COMMENT '区域名称',
  PRIMARY KEY (`areaId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_area
-- ----------------------------
INSERT INTO `t_area` VALUES ('1', '成华区');
INSERT INTO `t_area` VALUES ('2', '锦江区');
INSERT INTO `t_area` VALUES ('3', '武侯区');

-- ----------------------------
-- Table structure for `t_claim`
-- ----------------------------
DROP TABLE IF EXISTS `t_claim`;
CREATE TABLE `t_claim` (
  `claimId` int(11) NOT NULL AUTO_INCREMENT COMMENT '认领id',
  `lostFoundObj` int(11) NOT NULL COMMENT '招领信息',
  `personName` varchar(20) NOT NULL COMMENT '认领人',
  `claimTime` varchar(20) DEFAULT NULL COMMENT '认领时间',
  `contents` varchar(500) DEFAULT NULL COMMENT '描述说明',
  `addTime` varchar(20) DEFAULT NULL COMMENT '发布时间',
  PRIMARY KEY (`claimId`),
  KEY `lostFoundObj` (`lostFoundObj`),
  CONSTRAINT `t_claim_ibfk_1` FOREIGN KEY (`lostFoundObj`) REFERENCES `t_lostfound` (`lostFoundId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_claim
-- ----------------------------
INSERT INTO `t_claim` VALUES ('1', '1', '张曦', '2020-02-20 12:08:11', '找到失主了', '2020-02-20 12:09:12');

-- ----------------------------
-- Table structure for `t_lookingfor`
-- ----------------------------
DROP TABLE IF EXISTS `t_lookingfor`;
CREATE TABLE `t_lookingfor` (
  `lookingForId` int(11) NOT NULL AUTO_INCREMENT COMMENT '寻物id',
  `title` varchar(30) NOT NULL COMMENT '标题',
  `goodsName` varchar(40) NOT NULL COMMENT '丢失物品',
  `goodsPhoto` varchar(60) NOT NULL COMMENT '物品照片',
  `lostTime` varchar(20) DEFAULT NULL COMMENT '丢失时间',
  `lostPlace` varchar(20) NOT NULL COMMENT '丢失地点',
  `goodDesc` varchar(500) NOT NULL COMMENT '物品描述',
  `reward` varchar(40) NOT NULL COMMENT '报酬',
  `telephone` varchar(20) NOT NULL COMMENT '联系电话',
  `userObj` varchar(20) NOT NULL COMMENT '发布用户',
  `addTime` varchar(20) DEFAULT NULL COMMENT '发布时间',
  PRIMARY KEY (`lookingForId`),
  KEY `userObj` (`userObj`),
  CONSTRAINT `t_lookingfor_ibfk_1` FOREIGN KEY (`userObj`) REFERENCES `t_userinfo` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_lookingfor
-- ----------------------------
INSERT INTO `t_lookingfor` VALUES ('1', '我的苹果手机丢了', '苹果手机', 'img/1.jpg', '2020-02-20 12:06:20', '学校门口', '刚买的手机掉了,哪个同学捡到了给我吧！', '100元', '13300812342', 'user1', '2020-02-20 11:12:33');
INSERT INTO `t_lookingfor` VALUES ('2', '我的硬盘掉了谁捡到了', '移动硬盘', 'img/2.jpg', '2020-02-20 12:50:51', '图书馆自习室', '我昨天晚去自习后忘记带走，今天去看，找不到了，哪个朋友有看到麻烦联系我！', '30', '13980813421', 'user2', '2020-02-20 12:50:56');
INSERT INTO `t_lookingfor` VALUES ('3', '我家泰迪狗狗走丢了', '宠物狗', 'img/3.jpg', '2020-02-19 20:09:53', '小区门口', '昨晚去遛狗的时候，走了一回神，然后发现狗狗不见了！', '200', '13083081134', 'user1', '2020-02-20 15:46:26');

-- ----------------------------
-- Table structure for `t_lostfound`
-- ----------------------------
DROP TABLE IF EXISTS `t_lostfound`;
CREATE TABLE `t_lostfound` (
  `lostFoundId` int(11) NOT NULL AUTO_INCREMENT COMMENT '招领id',
  `title` varchar(40) NOT NULL COMMENT '标题',
  `goodsName` varchar(20) NOT NULL COMMENT '物品名称',
  `pickUpTime` varchar(20) DEFAULT NULL COMMENT '捡得时间',
  `pickUpPlace` varchar(20) NOT NULL COMMENT '拾得地点',
  `contents` varchar(2000) NOT NULL COMMENT '描述说明',
  `userObj` varchar(20) NOT NULL COMMENT '发布人',
  `phone` varchar(20) NOT NULL COMMENT '联系电话',
  `addTime` varchar(20) DEFAULT NULL COMMENT '发布时间',
  PRIMARY KEY (`lostFoundId`),
  KEY `userObj` (`userObj`),
  CONSTRAINT `t_lostfound_ibfk_1` FOREIGN KEY (`userObj`) REFERENCES `t_userinfo` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_lostfound
-- ----------------------------
INSERT INTO `t_lostfound` VALUES ('1', '捡到一个u盘', 'u盘', '2020-02-20 12:07:18', '食堂桌上', '一个金士顿u盘，谁不小心掉的？', 'user1', '13980123423', '2020-02-20 12:08:11');
INSERT INTO `t_lostfound` VALUES ('2', '捡到一个钱包', '钱包', '2020-02-20 15:06:06', '6教学楼', '我在302教室捡到一个钱包，是哪个同学落下了？', 'user2', '13508013508', '2020-02-20 15:06:11');
INSERT INTO `t_lostfound` VALUES ('3', '捡到一个u盘的书包', '书包', '2020-02-20 15:48:44', '小区花园', '是哪个业主的小朋友的书包忘记带走了？', 'user1', '13985080183', '2020-02-20 15:49:27');

-- ----------------------------
-- Table structure for `t_notice`
-- ----------------------------
DROP TABLE IF EXISTS `t_notice`;
CREATE TABLE `t_notice` (
  `noticeId` int(11) NOT NULL AUTO_INCREMENT COMMENT '通知id',
  `title` varchar(50) NOT NULL COMMENT '标题',
  `content` varchar(2000) NOT NULL COMMENT '内容',
  `addTime` varchar(20) DEFAULT NULL COMMENT '发布时间',
  PRIMARY KEY (`noticeId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_notice
-- ----------------------------
INSERT INTO `t_notice` VALUES ('1', '失物招领系统上线', '朋友们丢了东西或者捡到东西可以来这里发布哦', '2020-02-20 12:09:22');

-- ----------------------------
-- Table structure for `t_praise`
-- ----------------------------
DROP TABLE IF EXISTS `t_praise`;
CREATE TABLE `t_praise` (
  `praiseId` int(11) NOT NULL AUTO_INCREMENT COMMENT '表扬id',
  `lostFoundObj` int(11) NOT NULL COMMENT '招领信息',
  `title` varchar(40) NOT NULL COMMENT '标题',
  `contents` varchar(300) NOT NULL COMMENT '表扬内容',
  `addTime` varchar(20) DEFAULT NULL COMMENT '表扬时间',
  PRIMARY KEY (`praiseId`),
  KEY `lostFoundObj` (`lostFoundObj`),
  CONSTRAINT `t_praise_ibfk_1` FOREIGN KEY (`lostFoundObj`) REFERENCES `t_lostfound` (`lostFoundId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_praise
-- ----------------------------
INSERT INTO `t_praise` VALUES ('1', '1', '奖励20元', '对于这种拾金不昧精神予以表演', '2020-02-20 12:08:56');

-- ----------------------------
-- Table structure for `t_userinfo`
-- ----------------------------
DROP TABLE IF EXISTS `t_userinfo`;
CREATE TABLE `t_userinfo` (
  `user_name` varchar(20) NOT NULL COMMENT 'user_name',
  `password` varchar(20) NOT NULL COMMENT '登录密码',
  `areaObj` int(11) NOT NULL COMMENT '所在区域',
  `name` varchar(20) NOT NULL COMMENT '姓名',
  `sex` varchar(4) NOT NULL COMMENT '性别',
  `userPhoto` varchar(60) NOT NULL COMMENT '用户照片',
  `birthday` varchar(20) DEFAULT NULL COMMENT '出生日期',
  `telephone` varchar(20) NOT NULL COMMENT '联系电话',
  `address` varchar(50) NOT NULL COMMENT '家庭地址',
  PRIMARY KEY (`user_name`),
  KEY `areaObj` (`areaObj`),
  CONSTRAINT `t_userinfo_ibfk_1` FOREIGN KEY (`areaObj`) REFERENCES `t_area` (`areaId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_userinfo
-- ----------------------------
INSERT INTO `t_userinfo` VALUES ('user1', '123', '1', '双鱼林', '男', 'img/9.jpg', '2020-02-18', '13980813423', '滨江路10号');
INSERT INTO `t_userinfo` VALUES ('user2', '123', '1', '张晓彤', '女', 'img/12.jpg', '2020-02-19', '13598081234', '双流大道10号');
