# Gobblet Gobblers

## Description

Gobblet Gobblers is a two-player abstract strategy game designed by Thierry Denoual. It is played on a 4x4 board and is similar to tic-tac-toe but with a twist. Players aim to line up three of their pieces of the same size horizontally, vertically, or diagonally, while also being able to gobble up smaller pieces and move their own pieces to different locations on the board.

### Rules:

1. Each player starts with 12 pieces of different sizes: 4 small, 4 medium, and 4 large.
2. Players take turns either placing a new piece onto the board or moving an existing piece to an empty space.
3. A larger piece can gobble up a smaller piece, removing it from the game.
4. Players cannot place a piece on top of a larger piece, but they can place a larger piece on top of a smaller one.
5. The game ends when one player aligns three of their pieces of the same size horizontally, vertically, or diagonally, or when the board is filled with pieces and no player has won.

## Supported Modes

Gobblet Gobblers supports the following modes:

1. **Human vs Human**: Play against another human player.
2. **Human vs Computer**: Play against an AI opponent.
3. **Computer vs Computer**: Watch two AI opponents play against each other.

### Human vs Human Mode

In this mode, two human players can compete against each other. If both players agree, there is an option to end the game in a draw.

### Human vs Computer Mode

In this mode, you can play against the computer with varying difficulty levels:

- **Easy**: The computer uses the minimax algorithm with a depth of 1.
- **Medium**: The computer uses alpha-beta pruning with a depth of 2.
- **Difficult**: The computer uses iterative deepening starting from a depth of 1, limiting the AI's move time to a maximum of 5 seconds.

### Computer vs Computer Mode

In this mode, two AI opponents face off against each other. The level of AI is randomized between medium and easy for both AI players.

## How to Play

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Compile and run the game.
4. Choose your desired mode and options.
5. Enjoy playing Gobblet Gobblers!

## Snapshots of the game:
![image](https://github.com/mohamdhassan0x7/Gobblet_game/assets/105478629/bee41e2b-e300-430c-a6ae-6ee55c9120c9)
![image](https://github.com/mohamdhassan0x7/Gobblet_game/assets/105478629/4d5164f9-64ec-4312-9606-31e23a58b294)
![image](https://github.com/mohamdhassan0x7/Gobblet_game/assets/105478629/d38dfec2-1d57-479a-baf0-9cfe96a6641f)

## Download .exe & Video Link:
https://engasuedu-my.sharepoint.com/:f:/g/personal/1900819_eng_asu_edu_eg/EueEa5kPTQBNr32J2uXCzb8BuE718oP0-tNWAIe0gFsDzA?e=yiWU9b

Feel free to explore the source code for more details on the game implementation and AI strategies. Happy gaming!
