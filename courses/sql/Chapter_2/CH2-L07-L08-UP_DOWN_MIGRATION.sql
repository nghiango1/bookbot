-- Drop if table existed
DROP TABLE IF EXISTS transactions;

CREATE TABLE transactions (
  id INTEGER, 
  recipient_id INTEGER, 
  sender_id INTEGER, 
  note TEXT, 
  amount INTEGER
);

-- Lesson 7's Assignment
ALTER TABLE transactions
ADD COLUMN was_successful BOOLEAN;

ALTER TABLE transactions
ADD COLUMN transaction_type TEXT;

-- Lesson 8's Assignment
ALTER TABLE transactions
DROP COLUMN was_successful;

ALTER TABLE transactions
DROP COLUMN transaction_type;

-- We doesn't have this in postgres though, use our alternative function instead
-- PRAGMA TABLE_INFO('transactions')
SELECT * FROM TABLE_INFO('transactions');
