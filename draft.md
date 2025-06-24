# Project Overview

This project analyzes play-by-play data for the 828 MAGIC youth basketball team. The goal is to build a personal portfolio and prepare for a larger-scale NBA analytics project. The focus is on statistical analysis using RAPM (Regularized Adjusted Plus-Minus) and APM (Adjusted Plus-Minus), with an emphasis on optimizing processes and exploring custom modeling for lineup regression.

The data consists primarily of substitution events tracked by hand at the play-by-play level for the 828 MAGIC team. This serves as a foundation for future work with more complex NBA datasets.

## Workflow

1. **Raw Play-by-Play Data Collection**
   - Source: Unformatted, unstructured `.txt` files.
   - Content: Hand-tracked play-by-play events.

2. **Expanded Play-by-Play Data Creation**
   - Output: Structured `.json` files (one per game).
   - Fields:
     - Game number
     - Entry number
     - Stint number
     - Possession number
     - Period number
     - Game clock
     - Home points
     - Away points
     - Point differential
     - On-court players

3. **Stint-Level Data Generation**
   - Output: Structured `.json` files (one per game).
   - Fields:
     - Game number
     - Stint number
     - Starting/ending possession numbers
     - Possession count
     - On-court players
     - ORTG (Offensive Rating: points scored per 100 possessions)
     - DRTG (Defensive Rating: points allowed per 100 possessions)
     - NRTG (Net Rating: ORTG minus DRTG)

4. **Box Score Data Creation**
   - Output: Structured `.json` files (one per game).
   - Fields:
     - Game number
     - Player ID
     - Possessions played
     - On-court ORTG/DRTG/NRTG
     - Off-court ORTG/DRTG/NRTG
     - On/Off ORTG/DRTG/NRTG

5. **Regression Analysis (RAPM & APM)**
   - Output: Structured `.json` files (per game and full season).
   - Fields:
     - Game number (`0` for full season)
     - Player ID
     - Possessions played
     - O-RAPM & O-APM (offense)
     - D-RAPM & D-APM (defense)
     - Net RAPM & APM

6. **Final Dataset Synthesis**
   - Output: Structured `.csv` files (season, game, player, team, etc.) for analysis and spreadsheet display.

---
