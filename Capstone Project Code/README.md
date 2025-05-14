# Flag Football Performance & Injury Analytics Platform

## About Me  
Hi there! My name is **Mariam Adegbindin**, a soon-to-be MS-CISBA graduate from West Texas A&M University (May 2025). When I’m not crunching data or building prototypes, you’ll find me on the flag football field or exploring new ways to turn real-world problems into data-driven solutions. Welcome to my portfolio let’s dive in!

## Getting Started  
```bash
# 1. Clone the repo
git clone https://github.com/<org>/CIDM6395-MariamAdegbindin.git
cd CIDM6395-MariamAdegbindin

# 2. Load SQLite database
sqlite3 flagfootball.db < schema.sql
sqlite3> .mode csv
sqlite3> .import Data/practice_sessions.csv PracticeSession
sqlite3> .import Data/game_performance.csv GamePerformance
sqlite3> .import Data/injury_log.csv InjuryLog

# 3. Run demos
python3 SoftwareSystems/ss_loader.py        # Software Systems demo
python3 SoftwareSystems/flagfootball_demo.py # CN access control demo

