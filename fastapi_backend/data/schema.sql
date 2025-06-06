create table "images" (
  "id" serial primary key,
  "image_filename" varchar(255) not null,
  "image_uuid" varchar(255) not null,
  "timestamp" varchar(255) not null DEFAULT NOW(),
  "is_processed" BOOLEAN not null DEFAULT false
)