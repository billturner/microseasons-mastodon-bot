CREATE TABLE "divisions" (
	"id"	INTEGER NOT NULL UNIQUE,
	"description"	TEXT,
	"description_jp"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
)

CREATE TABLE "microseasons" (
	"id"	INTEGER NOT NULL UNIQUE,
	"division_id"	INTEGER,
	"start_month"	INTEGER,
	"start_day"	INTEGER,
	"end_month"	INTEGER,
	"end_day"	INTEGER,
	"description_jp"	TEXT,
	"description"	TEXT,
	"active"	INTEGER NOT NULL DEFAULT 0 CHECK(active IN (0,1)),
	PRIMARY KEY("id" AUTOINCREMENT)
)
