CREATE TABLE "teachers_table" (
	"iin_key" integer(12) NOT NULL,
	"first_name" varchar(50) NOT NULL,
	"second_name" varchar(50) NOT NULL,
	"third_name" varchar(50) NOT NULL,
	"rate_value" FLOAT(3),
	"rate_value_change" FLOAT(3),
	"code_access" varchar(100) NOT NULL,
	CONSTRAINT teachers_table_pk PRIMARY KEY ("iin_key")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "maneger_persons" (
	"iin_key" integer(12) NOT NULL,
	"first_name" varchar(50) NOT NULL,
	"second_name" varchar(50) NOT NULL,
	"third_name" varchar(50) NOT NULL,
	"privileges_value" varchar(50) NOT NULL,
	"password" varchar(255) NOT NULL,
	CONSTRAINT maneger_persons_pk PRIMARY KEY ("iin_key")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "inf_teachers" (
	"iin_key" integer(12) NOT NULL,
	"something_info" varchar(100) NOT NULL
) WITH (
  OIDS=FALSE
);





ALTER TABLE "inf_teachers" ADD CONSTRAINT "inf_teachers_fk0" FOREIGN KEY ("iin_key") REFERENCES "teachers_table"("iin_key");

