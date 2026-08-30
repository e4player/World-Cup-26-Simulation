# FIFA World Cup '26 Elo-based Monte Carlo Simulator

## Intro

In the recent World Cup 2026, FIFA expanded their format to include 48 teams for the first time ever. With this addition of 16 teams, predicting World Cup results proved harder than ever with countries like Cape Verde surprising everyone. This project simulates the most recent World Cup using Elo, a mathematically derived rating used famously in games such as Chess. After running n simulations, it determines the win probability for particular countries. (As a sad England fan, I can see how many times football could've come home.)

## Features

- Elo-based match simulation: Uses team Elo ratings (derived from official FIFA rankings) to calculate expected game outcomes.
- Draw probability model: Incorporates the likelihood of a draw based on the difference between teams' Elo ratings.
- 48-team group stage: Simulates all group-stage matches identical to the WC '26 and calculates standings.
- Group-stage tiebreakers: Resolves tied teams differently from the WC by using playoff matches and performance-based tiebreakers.
- Third-place qualification: Determines which third-place teams advance to the knockout stage based on performance Elo.
- FIFA-style knockout phase: Assigns qualified teams to the Round of 32 according to the WC '26 bracket structure.
- Knockout simulation: Simulates the Round of 32 through the final.
- Monte Carlo simulation: Runs multiple tournaments to estimate each team's probability of winning the World Cup.

## Running the Simulator

- Clone the repository
- To return the winning team winner = simulate_world_cup()
- To run e.g. 10000 tournaments and calculate countries' win percentages win_probabilities = simulate_n_tournaments(10000)
  - This returns a dictionary containing each country's estimated probability of winning the tournament



