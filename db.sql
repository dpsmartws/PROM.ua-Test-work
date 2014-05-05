/*
Navicat SQLite Data Transfer

Source Server         : PROM ua
Source Server Version : 30714
Source Host           : :0

Target Server Type    : SQLite
Target Server Version : 30714
File Encoding         : 65001

Date: 2014-05-05 05:21:08
*/

PRAGMA foreign_keys = OFF;

-- ----------------------------
-- Table structure for author
-- ----------------------------
DROP TABLE IF EXISTS "main"."author";
CREATE TABLE author (
	id INTEGER NOT NULL, 
	name VARCHAR(30), 
	second_name VARCHAR(30), 
	last_name VARCHAR(30), 
	PRIMARY KEY (id)
);

-- ----------------------------
-- Records of author
-- ----------------------------
INSERT INTO "main"."author" VALUES (1, 'Ганс', 'Хрестиан', 'Андерсен');
INSERT INTO "main"."author" VALUES (2, 'Стив', 'Перри', '');
INSERT INTO "main"."author" VALUES (3, 'Айзек', 'Азимов', '');

-- ----------------------------
-- Table structure for book
-- ----------------------------
DROP TABLE IF EXISTS "main"."book";
CREATE TABLE "book" (
"id"  INTEGER NOT NULL,
"name"  VARCHAR(60),
"author_id"  INTEGER,
"add_date"  DATE DEFAULT NULL,
PRIMARY KEY ("id" ASC),
CONSTRAINT "fkey0" FOREIGN KEY ("author_id") REFERENCES "author" ("id"),
UNIQUE ("name" ASC)
);

-- ----------------------------
-- Records of book
-- ----------------------------
INSERT INTO "main"."book" VALUES (1, 'Эльф розового куста', 1, '2014-04-28');
INSERT INTO "main"."book" VALUES (2, 'Через тысячу лет', 1, '2014-04-28');
INSERT INTO "main"."book" VALUES (3, 'Цветы маленькой Иды', 1, '2014-04-28');
INSERT INTO "main"."book" VALUES (4, 'Тернистый путь славы', 1, '2014-04-28');
INSERT INTO "main"."book" VALUES (5, 'Черная сталь', 2, '2014-04-28');
INSERT INTO "main"."book" VALUES (6, 'Тень имерии', 2, '2014-04-28');
INSERT INTO "main"."book" VALUES (8, 'Индиана Джонс и армия трупов', 2, '2014-04-28');
INSERT INTO "main"."book" VALUES (9, 'Двухсотлетний человек', 3, '2014-04-28');
INSERT INTO "main"."book" VALUES (10, 'Основание', 3, '2014-04-28');

-- ----------------------------
-- Table structure for migrate_version
-- ----------------------------
DROP TABLE IF EXISTS "main"."migrate_version";
CREATE TABLE migrate_version (
	repository_id VARCHAR(250) NOT NULL, 
	repository_path TEXT, 
	version INTEGER, 
	PRIMARY KEY (repository_id)
);

-- ----------------------------
-- Records of migrate_version
-- ----------------------------
INSERT INTO "main"."migrate_version" VALUES ('database repository', 'C:\workspace\Dropbox\Work\flask\test\test\app\db\db_repo', 3);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS "main"."user";
CREATE TABLE user (
	id INTEGER NOT NULL, 
	nickname VARCHAR, 
	password VARCHAR, 
	category_id INTEGER, 
	is_online BOOLEAN, 
	last_visite_date DATE, 
	registration_date DATE, 
	PRIMARY KEY (id), 
	CHECK (is_online IN (0, 1))
);

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO "main"."user" VALUES (1, 'admin', 'admin', 1, 0, '2014-05-04', '2014-04-28');
INSERT INTO "main"."user" VALUES (2, 'noadmin', 'noadmin', 2, 0, '2014-05-04', '2014-05-04');

-- ----------------------------
-- Table structure for usercategory
-- ----------------------------
DROP TABLE IF EXISTS "main"."usercategory";
CREATE TABLE usercategory (
	id INTEGER NOT NULL, 
	name VARCHAR(25), 
	short_description VARCHAR(150), 
	PRIMARY KEY (id), 
	UNIQUE (name)
);

-- ----------------------------
-- Records of usercategory
-- ----------------------------
INSERT INTO "main"."usercategory" VALUES (1, 'Администраторы', 'Группа имеет наибольшее количестов прав.');
INSERT INTO "main"."usercategory" VALUES (2, 'Посетитель', 'Группа с наименьшим количеством прав.');
