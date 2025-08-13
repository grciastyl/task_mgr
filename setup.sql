

--Create database table

CREATE TABLE IF NOT EXISTS task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(64),
    summary VARCHAR(128),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
);

--Insert some dummy data to test with
INSERT INTO task (
    name,
    summary,
    description
) VALUES
(
    "Wash the car",
    "Take the car to the car wash",
    "Make sure it gets vaccumed and waxed"
),
(
    "Walk the dog",
    "Fido needs daily exercise",
    "Three laps around the park"
),
(
    "Buy groceries",
    "Go to the supermarket",
    "Buy: milk, eggs and bread"
    );