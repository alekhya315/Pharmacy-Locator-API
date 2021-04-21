use mysql;

CREATE TABLE pharmacies (
  name varchar(50),
  address varchar(100),
  city varchar(20),
  state varchar(3),
  zip int,
  latitude Decimal(10,5),
  longitude Decimal(10,4)
  );

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/pharmacies.csv' INTO TABLE pharmacies
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 rows;

select * from pharmacies;


