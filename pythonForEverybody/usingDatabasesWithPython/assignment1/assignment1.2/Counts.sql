BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Counts" (
	"org"	TEXT,
	"count"	INTEGER
);
INSERT INTO "Counts" VALUES ('uct.ac.za',96);
INSERT INTO "Counts" VALUES ('media.berkeley.edu',56);
INSERT INTO "Counts" VALUES ('umich.edu',491);
INSERT INTO "Counts" VALUES ('iupui.edu',536);
INSERT INTO "Counts" VALUES ('caret.cam.ac.uk',157);
INSERT INTO "Counts" VALUES ('gmail.com',25);
INSERT INTO "Counts" VALUES ('indiana.edu',178);
INSERT INTO "Counts" VALUES ('et.gatech.edu',17);
INSERT INTO "Counts" VALUES ('vt.edu',110);
INSERT INTO "Counts" VALUES ('lancaster.ac.uk',14);
INSERT INTO "Counts" VALUES ('ucdavis.edu',1);
INSERT INTO "Counts" VALUES ('ufp.pt',28);
INSERT INTO "Counts" VALUES ('txstate.edu',17);
INSERT INTO "Counts" VALUES ('stanford.edu',12);
INSERT INTO "Counts" VALUES ('whitman.edu',17);
INSERT INTO "Counts" VALUES ('rsmart.com',8);
INSERT INTO "Counts" VALUES ('fhda.edu',1);
INSERT INTO "Counts" VALUES ('bu.edu',14);
INSERT INTO "Counts" VALUES ('unicon.net',9);
INSERT INTO "Counts" VALUES ('loi.nl',9);
INSERT INTO "Counts" VALUES ('utoronto.ca',1);
COMMIT;
