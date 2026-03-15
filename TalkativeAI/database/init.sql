-- ==============================
-- USERS
-- ==============================

CREATE TABLE IF NOT EXISTS users (

    id SERIAL PRIMARY KEY,

    username TEXT UNIQUE NOT NULL,

    password_hash TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);



-- ==============================
-- PRACTICE SESSIONS
-- ==============================

CREATE TABLE IF NOT EXISTS sessions (

    id SERIAL PRIMARY KEY,

    user_id INT NOT NULL,

    scenario TEXT,

    start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    end_time TIMESTAMP,

    FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE

);



-- ==============================
-- CONVERSATION HISTORY
-- ==============================

CREATE TABLE IF NOT EXISTS messages (

    id SERIAL PRIMARY KEY,

    session_id INT NOT NULL,

    role TEXT CHECK (role IN ('user','ai')),

    message TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (session_id)
        REFERENCES sessions(id)
        ON DELETE CASCADE

);



-- ==============================
-- SPEECH ANALYSIS METRICS
-- ==============================

CREATE TABLE IF NOT EXISTS speech_metrics (

    id SERIAL PRIMARY KEY,

    session_id INT NOT NULL,

    speaking_speed FLOAT,

    pause_rate FLOAT,

    filler_word_ratio FLOAT,

    pronunciation_score FLOAT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (session_id)
        REFERENCES sessions(id)
        ON DELETE CASCADE

);



-- ==============================
-- EMOTION TIMELINE (VISION SERVICE)
-- ==============================

CREATE TABLE IF NOT EXISTS emotion_frames (

    id SERIAL PRIMARY KEY,

    session_id INT NOT NULL,

    timestamp_seconds FLOAT,

    emotion TEXT,

    confidence FLOAT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (session_id)
        REFERENCES sessions(id)
        ON DELETE CASCADE

);



-- ==============================
-- FINAL SESSION EVALUATION
-- ==============================

CREATE TABLE IF NOT EXISTS evaluations (

    id SERIAL PRIMARY KEY,

    session_id INT NOT NULL,

    clarity_score FLOAT,

    confidence_score FLOAT,

    emotion_score FLOAT,

    overall_score FLOAT,

    feedback TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (session_id)
        REFERENCES sessions(id)
        ON DELETE CASCADE

);



-- ==============================
-- USER LONG TERM PROGRESS
-- ==============================

CREATE VIEW IF NOT EXISTS user_progress AS

SELECT

    u.id AS user_id,

    u.username,

    s.id AS session_id,

    s.scenario,

    e.clarity_score,

    e.confidence_score,

    e.emotion_score,

    e.overall_score,

    s.start_time

FROM users u

JOIN sessions s
    ON u.id = s.user_id

JOIN evaluations e
    ON s.id = e.session_id;



-- ==============================
-- INDEXES (PERFORMANCE)
-- ==============================

CREATE INDEX IF NOT EXISTS idx_sessions_user
ON sessions(user_id);

CREATE INDEX IF NOT EXISTS idx_messages_session
ON messages(session_id);

CREATE INDEX IF NOT EXISTS idx_emotion_session
ON emotion_frames(session_id);

CREATE INDEX IF NOT EXISTS idx_eval_session
ON evaluations(session_id);
