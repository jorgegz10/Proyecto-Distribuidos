CREATE TABLE IF NOT EXISTS books (
  code TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  author TEXT NOT NULL,
  copies_total INT NOT NULL,
  copies_available INT NOT NULL
);

CREATE TABLE IF NOT EXISTS loans (
  id SERIAL PRIMARY KEY,
  book_code TEXT REFERENCES books(code),
  user_id TEXT NOT NULL,
  site_id TEXT NOT NULL,
  due_date DATE NOT NULL,
  renewals_count INT NOT NULL DEFAULT 0,
  status TEXT NOT NULL CHECK (status IN ('active','returned')) DEFAULT 'active'
);

CREATE TABLE IF NOT EXISTS operations_log (
  id SERIAL PRIMARY KEY,
  type TEXT NOT NULL,
  book_code TEXT,
  user_id TEXT,
  site_id TEXT,
  ts TIMESTAMP NOT NULL DEFAULT now(),
  payload_json JSONB
);
