CREATE TABLE IF NOT EXISTS tickets (
    ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    email TEXT,
    message TEXT NOT NULL,
    date DATE,
    ai_analysis TEXT,          -- stores category + sentiment from OpenAI
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
