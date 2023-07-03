CREATE TABLE "divisions" (
	"id"	INTEGER NOT NULL UNIQUE,
	"description"	TEXT,
	"description_jp"	TEXT,
	PRIMARY KEY("id")
);

CREATE TABLE microseasons (
	id INTEGER,
	division_id INTEGER,
	start_day INTEGER,
	end_day INTEGER,
	leap_start_day INTEGER,
	leap_end_day INTEGER,
	description TEXT,
	description_jp TEXT,
	active INTEGER DEFAULT (0),
	PRIMARY KEY("id")
);
