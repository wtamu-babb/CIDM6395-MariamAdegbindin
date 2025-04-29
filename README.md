# Flag Football Performance & Injury Analytics Platform

## 1. Introduction  
The Flag Football Performance & Injury Analytics Platform is a capstone prototype that empowers recreational athletes to log games, practices, and injuries—and turn that raw data into actionable insights. By synthesizing Software Systems, Business Analytics, Data Management, and Cybersecurity & Networking, this tool demonstrates how cross-disciplinary skills can solve real-world problems.

## 2. Metrics Tracked  
- **Touchdowns per Game:** Total touchdowns scored in each matchup  
- **Total Plays:** Number of offensive plays executed per game  
- **Practice Duration:** Session length in minutes  
- **Environmental Conditions:** Temperature (°F) and altitude (ft) during practices  
- **Injury Details:** Type of injury and recovery time in days

## 3. Software Systems (SS)  
- **Wireframes & Mock-ups:** Excel and mobile sketches to map intuitive workflows  
- **Prototype Code:**  
  - `ss_loader.py` demonstrates end-to-end data ingestion  
  - `flagfootball_demo.py` shows role-based access control  
- **Architecture:** Applied MVC and design patterns for a scalable, modular API

## 4. Business Analytics (BA)  
- **Trend Charts:**  
  - Bar chart of weekly touchdowns
  - Line graph of weekly plays 
- **Heat Map:** Injury frequency vs. temperature bands 
- **Tools:** Excel, Tableau, RapidMiner for cleaning, visualization, and dashboards

## 5. Data Management (DM)  
- **Schema Design:** Four core tables: `Player`, `PracticeSession`, `GamePerformance`, `InjuryLog`  
- **ERD:** Enforced referential integrity and clear relationships  
- **Data Governance:** Standardized formats and validation rules to ensure consistency

## 6. Cybersecurity & Networking (CN)  
- **Access Control:** Decorator-based role checks (`player` vs. `coach`)  
- **Audit Logging:** Append-only log table capturing every data interaction  
- **Secure Architecture:**  
  - Firewall/WAF protecting API DMZ  
  - Encrypted database subnet  
  - SIEM-ready logging service

## 7. Getting Started  
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
