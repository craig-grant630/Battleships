# Battleships #

## Description

Battleship, which originated as a pencil-and-paper game, has its roots in World War I, where it was played by Russian officers. In the 1930s, it emerged in the United States under the name "Salvo." The game was commercially launched in 1931 as "Broadsides: A Game of Naval Strategy" by the Starex company. In 1943, Milton Bradley introduced their own version, and in 1967, they released the well-known plastic board game featuring grids and pegs. The game's popularity increased significantly, paving the way for electronic adaptations such as "Electronic Battleship" in 1977 and "Electronic Talking Battleship" in 1989.

##  Game Rules
 ### Components
 
- Game Boards: Each player has two 10x10 grids. One grid is for placing their own ships, and the other grid is for tracking their guesses about the opponent's ship locations.
- Ships: Each player has a fleet consisting of five ships of varying lengths: 5, 4, 3, 2, 2.
- Markers: Used to track hits, misses, and ship placements on the grids.

### Setup

- Each player places their ships on their primary grid. Ships can be placed horizontally or vertically but cannot overlap or be placed diagonally.
- The placement of ships is hidden from the opponent.

### Gameplay

- Taking Turns: Players take turns calling out a coordinate on the opponent's grid (ex: row:5 column: 7) to attack.
- If the called out coordinate contains part of a ship, it's a hit, and the game marks this on the board with an "X".
- If it's a miss, the player marks it with "-".

 ### Winning the Game

 - The game continues with players alternating turns, calling out coordinates, and marking hits and misses. The first player to sink all of their opponent’s ships wins the game.


## User Experience

### Project Goals

- Provide straightforward instructions on how to play the game, including how to start, controls, and objectives.
- Provide feedback to users about their actions and the game state.

### Target Audience

- Casual Gamers: Fun and easy-to-understand gameplay, quick to start, and minimal setup.
- Players of all ages: Battleships is a game of strategy, memory, and logic, making it a timeless classic enjoyed by players of all ages.

## Features

Battleships game provides clear instructions and a straightforward interface. Players are welcomed with a set of easy-to-understand rules before starting the game. The game screen has dual-board display, where the user's board and the computer's board are shown side by side, making it easy to track progress. Placing ships is interactive and guided, ensuring that users understand how to position their fleet strategically. During gameplay, users make guesses by inputting row and column coordinates, receiving immediate feedback on their hits and misses. The alternating turns between the user and the computer keep the gameplay dynamic and exciting. Each turn is accompanied by clear prompts and visual updates, ensuring that players are always aware of the game state.

### Game Rules Screen

<img src="README-images/battleships-rules.webp" alt="Rules Screen"/> 

### Game Screen

<img src="README-images/game-display.webp" alt="Game Screen"/> 

## Testing
### Manual Testing 

**Initial Setup and Rules Display**

- Launch the game and verify that the rules are displayed correctly.
- Check for any typos or formatting issues in the rules.

**Board Creation**

- Ensure that both the user's and the computer's boards are created as 10x10 grids.
- Confirm that all cells are initially marked with 'O' to represent empty spaces.

**Ship Placement**

**1. Computer Ship Placement:**
- Start the game and observe the computer placing its ships.
- Ensure that ships are placed within the board boundaries.
- Verify that ships do not overlap and are placed in valid positions with the validate_ships fucnction.

**2. User Ship Placement:**
- Place ships as prompted by the game.
- Enter valid and invalid coordinates and directions to check input validation.
- Ensure ships are placed correctly on the board and displayed properly
- Test with edge cases such as placing ships at the board's boundaries.
- Enter out-of-range coordinates to check input validation.
- Attempt to place overlapping ships to ensure the game prevents this.

**Testing Scenarios**

- Place a ship starting at (0,0) heading North with a size of 2 (fail).
- Place a ship starting at (0,0) heading East with a size of 2 (succeed).
- Place a ship starting at (0,9) heading East with a size of 2 (fail)
- Place a ship starting at (0,9) heading West with a size of 2 (succeed)

**Gameplay Loop**

**1. User Guessing:**
- Enter valid and invalid guesses (row and column).
- Ensure invalid guesses are handled gracefully with appropriate error messages.
- Confirm that hits are marked with 'X' and misses with '-'.

**2. Computer Guessing:**
- Observe the computer's guessing logic.
- Ensure that the computer correctly identifies hits and misses.
- Verify that the user's board is updated accordingly.

**Win Condition**

- Play until all ships of one player are sunk.
- Verify that the game announces the correct winner.
- Ensure that the game terminates correctly after a win condition is met.

### Bugs

When user would input an incorrect row or column when placing their ships the game would output and "invalid" message to the user, it would then move onto the next ship placement rather than looping through and placing the ship that was invalid.

**Correction**

  <img src="README-images/looping-error-ship.webp" alt="Looping Error Correction"/> 

### Improvements

**Refactoring the validate_ships function:**

![Validator ship function](README-images/validate-ships-function.webp)

The validate_ships function is verifying if positions are within board limits, calculating the ship's endpoint based on direction and size, and checking for any overlapping ships along the path. Create separate smaller functions for each task, which improves code organization and readability. Integrate these smaller functions back into the main function, ensuring it first validates the initial and final positions of the ship, and then checks if the path is free of overlaps. This breakdown and delegation of responsibilities into smaller, focused functions makes the main function cleaner and easier to maintain.

**Game Logic**

To enhance the Battleships game we can introduce strategic game logic for the computer's guessing when it hits a ship. This improvement would not only increase the difficulty level but also make victories more rewarding and the game overall more compelling.

To acheive this game logic:

- Track Hits and Direction: Modify the computer_guess function to remember the location of hits and focus on adjacent cells for subsequent guesses.


 ### Validator Testing 

**CI Python Linter**

![Validator Test](README-images/validator-test.webp)

## Deployment

The project was deployed using Code Institute's mock terminal for Heroku.

**Manual Deployment**

- Create a new Heroku app.
- Set the buildpacks to **Python** and **NodeJS**, in that order.
- Link the Heroku app to the repository.
- Click on Deploy.

 **Forking Repository**
 
- Go to the GitHub repository.
- Select **"Fork"** button on the page.
- This will create a copy of the repository in your GitHub account.

**Clone Repository**

- Go to the GitHub Repository.
- Click the Code button and copy the link.
- In Gitpod, type "git clone **repository link copied**.git" and enter.

## Credits

- The use of the **map** function was from [Real Python](https://realpython.com/python-map-function/)
- The use of built in function **random** was taken from Code Institute course.

