drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  'text' text not null,
  'time' text not null,
  tones text not null
);
