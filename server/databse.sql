create database ebook;

--Dora@20f
create user ebook_user01;

ALTER USER ebook_user01 WITH PASSWORD 'Caonima1_';
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO ebook_user01;

\c ebook
drop table users;
CREATE TABLE "users" (
	"id" SERIAL NOT NULL UNIQUE,
	"username" VARCHAR,
	"email" VARCHAR,
	"phone" VARCHAR,
	"password" VARCHAR NOT NULL,
	-- 0:没有删除 1: 已经删除
	"deleted_flg" INTEGER NOT NULL DEFAULT 0,
	"created_at" TIMESTAMP NOT NULL,
	"updated_at" TIMESTAMP NOT NULL,
	"deleted_at" TIMESTAMP,
	PRIMARY KEY("id")
);

GRANT USAGE ON SEQUENCE users_id_seq TO ebook_user01;