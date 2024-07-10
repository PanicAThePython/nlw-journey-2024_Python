CREATE TABLE IF NOT EXISTS 'trips' (
    id TEXT PRIMARY KEY,
    destination TEXT NOT NULL,
    start_date DATETIME,
    end_date DATETIME,
    onwer_name TEXT NOT NULL,
    owner_email TEXT NOT NULL,
    status INTEGER -- 1 pra verdadeiro e 0 pra falso
);

CREATE TABLE IF NOT EXISTS 'emails_to_invite' (
    id TEXT PRIMARY KEY,
    trip_id TEXT,
    email TEXT NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES trip(id)
);

CREATE TABLE IF NOT EXISTS 'links' (
    id TEXT PRIMARY KEY,
    trip_id TEXT,
    link TEXT NOT NULL,
    title text not null,
    FOREIGN KEY (trip_id) REFERENCES trip(id)
);

CREATE TABLE IF NOT EXISTS 'participants' (
    id TEXT PRIMARY KEY,
    trip_id TEXT NOT NULL,
    emails_to_invite TEXT NOT NULL,
    name TEXT NOT NULL,
    is_confirmed INTEGER, 
    FOREIGN KEY (trip_id) REFERENCES trips(id),
    FOREIGN KEY (emails_to_invite) REFERENCES emails_to_invite(id)
);

CREATE TABLE IF NOT EXISTS 'activities' (
    id TEXT PRIMARY KEY,
    trip_id TEXT NOT NULL,
    title TEXT NOT NULL,
    occurs_at DATETIME,
    FOREIGN KEY (trip_id) REFERENCES trips(id)
);
