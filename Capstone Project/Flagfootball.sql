-- 1) Create the database
CREATE DATABASE IF NOT EXISTS flagfootball;
USE flagfootball;

-- 2) Player master table
CREATE TABLE Player (
  player_id     INT            AUTO_INCREMENT PRIMARY KEY,
  name          VARCHAR(100)   NOT NULL,
  age           INT,
  position      VARCHAR(50),
  skill_level   VARCHAR(50)
) ENGINE=InnoDB;

-- 3) PracticeSession logs
CREATE TABLE PracticeSession (
  session_id     INT            AUTO_INCREMENT PRIMARY KEY,
  player_id      INT            NOT NULL,
  session_date   DATE           NOT NULL,
  duration_mins  INT,
  temperature_f  FLOAT,
  altitude_ft    INT,
  FOREIGN KEY (player_id)
    REFERENCES Player(player_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 4) GamePerformance stats
CREATE TABLE GamePerformance (
  performance_id INT            AUTO_INCREMENT PRIMARY KEY,
  player_id      INT            NOT NULL,
  game_date      DATE           NOT NULL,
  touchdowns     INT,
  passes         INT,
  plays          INT,
  FOREIGN KEY (player_id)
    REFERENCES Player(player_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 5) InjuryLog entries
CREATE TABLE InjuryLog (
  injury_id      INT            AUTO_INCREMENT PRIMARY KEY,
  player_id      INT            NOT NULL,
  injury_date    DATE           NOT NULL,
  injury_type    VARCHAR(100),
  recovery_days  INT,
  FOREIGN KEY (player_id)
    REFERENCES Player(player_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB;
