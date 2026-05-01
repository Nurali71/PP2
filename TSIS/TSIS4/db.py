import psycopg2

# Database connection parameters
DB_CONFIG = {
    "dbname": "snake_db",
    "host": "localhost",
    "user": "postgres",
    "password": "15012008",
    "port": "5432"
}

def get_conn():
    return psycopg2.connect(**DB_CONFIG)

def init_db():
    """Create tables if they don't exist using safe SQL execution"""
    with get_conn() as conn:
        with conn.cursor() as cur:
            # Table for unique players
            cur.execute("""
            CREATE TABLE IF NOT EXISTS players (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL
            );
            """)
            # Table for game history linked to players
            cur.execute("""
            CREATE TABLE IF NOT EXISTS game_sessions (
                id SERIAL PRIMARY KEY,
                player_id INTEGER REFERENCES players(id),
                score INTEGER NOT NULL,
                level_reached INTEGER NOT NULL,
                played_at TIMESTAMP DEFAULT NOW()
            );
            """)
            conn.commit()

def get_or_create_player(username):
    """Check if player exists, otherwise create new one. Returns player_id."""
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM players WHERE username=%s", (username,))
            result = cur.fetchone()
            if result:
                return result[0]
            
            cur.execute("INSERT INTO players (username) VALUES (%s) RETURNING id", (username,))
            player_id = cur.fetchone()[0]
            conn.commit()
            return player_id

def get_personal_best(player_id):
    """Fetch the maximum score for a specific player ID"""
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT MAX(score) FROM game_sessions WHERE player_id=%s", (player_id,))
            res = cur.fetchone()
            return res[0] if res[0] is not None else 0

def save_game(player_id, score, level):
    """Insert final game results into game_sessions table"""
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO game_sessions (player_id, score, level_reached) VALUES (%s, %s, %s)", 
                        (player_id, score, level))
            conn.commit()

def get_leaderboard():
    """Fetch Top 10 scores using JOIN to get usernames and scores together"""
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT p.username, g.score, g.level_reached, g.played_at
                FROM game_sessions g
                JOIN players p ON p.id = g.player_id
                ORDER BY g.score DESC LIMIT 10
            """)
            return cur.fetchall()