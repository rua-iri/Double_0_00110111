create table "images" (
  "id" serial primary key,
  "image_filename" varchar(255) not null,
  "image_uuid" varchar(255) not null,
  "timestamp" DATETIME not null,
  "image_location" varchar(255) not null,
  "is_processed" BOOLEAN not null
)