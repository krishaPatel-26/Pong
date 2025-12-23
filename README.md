# 🏓 Pong Game

A modern implementation of the classic Pong arcade game featuring enhanced physics, dual scoring systems, and smooth gameplay mechanics.

## 🎯 Features

### **Enhanced Gameplay Mechanics**
- **Dual Scoring System**: Earn points by saving the ball, lose lives when you miss
- **Random Ball Direction**: Fair starting positions with no player advantage
- **Paddle-Induced Spin**: Ball trajectory changes based on where it hits the paddle
- **Progressive Difficulty**: Ball speed increases with each hit (up to maximum)

### **Player Modes**
- **Two-Player Local Multiplayer**: Competitive head-to-head action
- **Customizable Controls**: WASD for Player A, Arrow Keys for Player B

### **Game Variations**
- **Classic Mode**: First to 10 points wins
- **Lives Mode**: Last player with remaining lives wins
- **Hybrid Mode**: Win by either reaching 10 points OR eliminating opponent's lives

## 🎮 Game Rules

### **Scoring System**
- **+1 Point**: Successfully hit/save the ball with your paddle
- **-1 Life**: Fail to save the ball (ball passes your paddle)
- **Win Conditions**:
  1. First player to reach **10 points** (classic Pong)
  2. Opponent loses all **3 lives** (elimination mode)

### **Physics & Mechanics**
- **Speed Boost**: Ball accelerates 5% with each paddle hit
- **Spin Control**: Hit ball near paddle edges for curved trajectories
- **Speed Limit**: Maximum ball speed capped for playability
- **Random Resets**: Ball starts in random direction after each point

## 🕹️ Controls

| Player | Move Up | Move Down |
|--------|---------|-----------|
| **Player A (Left)** | `W` Key | `S` Key |
| **Player B (Right)** | `↑` Arrow | `↓` Arrow |

## 🚀 Quick Start

### **Prerequisites**
- Python 3.6 or higher
- Turtle module (included with Python)

### **Run the Game**
```bash
# Clone/download the repository
git clone https://github.com/yourusername/pong-game.git
cd pong-game

# Run the game
python pong.py
