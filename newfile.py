import matplotlib.pyplot as plt

# Data for Team A and Team B
team_a_scores = [35, 22, 50, 42, 18, 60, 33, 24, 5, 16, 12]
team_b_scores = [45, 32, 10, 28, 38, 40, 23, 44, 15, 6, 10]

# Player labels
players = ['Player1', 'Player2', 'Player3', 'Player4', 'Player5', 
           'Player6', 'Player7', 'Player8', 'Player9', 'Player10', 'Player11']

# Create the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Bar width
bar_width = 0.35

# X-axis positions for Team A and Team B
index = range(len(players))

# Plotting the bar charts
bar1 = ax.bar(index, team_a_scores, bar_width, label='Team A', color='blue')
bar2 = ax.bar([i + bar_width for i in index], team_b_scores, bar_width, label='Team B', color='green')

# Adding labels, title, and legend
ax.set_xlabel('Players')
ax.set_ylabel('Scores')
ax.set_title('Cricket Match Scorecard: Team A vs Team B')
ax.set_xticks([i + bar_width / 2 for i in index])
ax.set_xticklabels(players, rotation=45)
ax.legend()

# Display the plot
plt.tight_layout()
plt.show()