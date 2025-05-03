# Flag Football Performance & Injury Analytics Platform

## 1. Introduction  
My capstone project is a Flag Football Performance & Injury Analytics Platform designed to help casual or recreational flag football players track their personal performance and monitor injury trends. The goal is to give players a better understanding of how their physical performance, habits, and environment may contribute to both progress and setbacks. Although this system isn’t intended for official leagues, it still serves a purpose especially for students, weekend athletes, or anyone interested in sports performance and health

## 2. Metrics Tracked  
- **Touchdowns per Game:** Total touchdowns scored in each matchup  
- **Total Plays:** Number of offensive plays executed per game  
- **Practice Duration:** Session length in minutes  
- **Environmental Conditions:** Temperature (°F) and altitude (ft) during practices  
- **Injury Details:** Type of injury and recovery time in days

## 3. Software Systems (SS) 
Software Systems is about designing and building technology that works for people. It’s not just about writing code it’s about creating a solution that makes sense, is easy to use, and solves a real problem. For this project, I wanted to create a simple, intuitive system where players could enter performance stats and injury-related information without needing any technical experience. I started by outlining what the user experience should look like: who’s using it, what kind of data they’re entering, and how they’d want to see their stats. From there, I drafted mock-ups and planned out the structure of the system keeping things lightweight, especially since the users are everyday players, not professional analysts.

- **Wireframes & Mock-ups:** Excel and mobile sketches to map intuitive workflows  
- **Prototype Code:**  
  - `ss_loader.py` demonstrates end-to-end data ingestion  
  - `flagfootball_demo.py` shows role-based access control  
- **Architecture:** Applied MVC and design patterns for a scalable, modular API

## 4. Business Analytics (BA) 
Business Analytics is about more than just crunching numbers. It’s the ability to look at raw data and extract meaning from it turning those insights into something useful. It’s about finding trends, spotting problems, and helping people make smarter decisions based on facts. Whether it’s through visualizations, reports, or simple metrics, business analytics helps turn data into action. In this project, analytics plays a central role. The goal isn’t just to collect stats, but to help players understand how their habits, performance, and recovery are affecting their overall progress. Using the data logged like the number of games played, injuries sustained, or practice duration I apply basic analytics to highlight patterns that matter. 

- **Trend Charts:**  
  - Bar chart of weekly touchdowns
  - Line graph of weekly plays 
- **Heat Map:** Injury frequency vs. temperature bands 
- **Tools:** Excel, Tableau, RapidMiner for cleaning, visualization, and dashboards

## 5. Data Management (DM)  
Data Management is all about structure and responsibility. It’s not just about where you store your data it’s about how well it’s organized, how easy it is to retrieve, and how carefully it’s protected. It includes planning what kind of data to collect, deciding how to categorize it, and making sure the system stays consistent and reliable over time. If Business Analytics is about making sense of the data, Data Management is about making sure the data is even usable in the first place. In this project, I treated each type of data game stats, practice logs, injury reports, and even environmental conditions as something that needs to be handled carefully. I started by deciding what fields were necessary, how they’d be formatted, and how the data would be stored in a way that made analysis easier down the line.

- **Schema Design:** Four core tables: `Player`, `PracticeSession`, `GamePerformance`, `InjuryLog`  
- **ERD:** Enforced referential integrity and clear relationships  
- **Data Governance:** Standardized formats and validation rules to ensure consistency

## 6. Cybersecurity & Networking (CN)  
Cybersecurity and Networking is about keeping systems and data safe while making sure everything stays connected and functional. It’s about understanding what threats could exist, how data travels, and how to put safeguards in place to reduce risk. Whether it’s setting access controls, identifying vulnerabilities, or preparing for incidents, cybersecurity plays a critical role in any system especially one that handles sensitive or personal information. Even though this project is a prototype, I still made cybersecurity a priority. Injury and health-related data can be sensitive, so I included basic security practices in my system design.

- **Access Control:** Decorator-based role checks (`player` vs. `coach`)  
- **Audit Logging:** Append-only log table capturing every data interaction  
- **Secure Architecture:**  
  - Firewall/WAF protecting API DMZ  
  - Encrypted database subnet  
  - SIEM-ready logging service
 
## 7. Conclusion
This capstone project brought together everything I’ve learned in the MS-CISBA program. Through it, I was able to design a system that not only functions but also reflects real-world challenges how to collect data, make sense of it, store it properly, and protect it. Every decision I made was influenced by something I learned along the way, whether it was organizing data structures, designing user workflows, or simulating threat scenarios.

What makes this project meaningful to me is that it grew out of something personal my love for flag football, but it still pushed me to apply everything I’ve gained from this degree in a practical, cross-functional way. It’s not just a school project to me it’s proof that I can take an idea, shape it through multiple disciplines, and turn it into something useful.

## 8. Getting Started  
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
python3 SoftwareSystems/prototype.py        # Software Systems demo
python3 SoftwareSystems/flagfootball_demo.py # CN access control demo

