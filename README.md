Game Title: Sunny beach    (OPEN DesignDoc.docx TO SEE SCREENSHOTS)

Game Purpose/Genre: The game's core purpose is to control two characters, a fish and a submarine, and navigate them around the screen within a time limit. The genre of the game is a simple arcade-style game with movement controls and collision detection.

Target Audience: The game is suitable for a general audience of all ages, as it doesn't contain any mature or objectionable content. It can be enjoyed by casual gamers and those with basic gaming experience.

Platform: The game is developed using the Pygame library in Python, which makes it compatible with multiple platforms, including Windows, macOS, and Linux. Any computer with Pygame and Python will be able to run this game.

ESRB Game Rating: Based on the game's content and lack of mature themes, it would likely receive an ESRB rating of "E" for Everyone.

Game Description: The game takes place in an underwater setting, where the player controls both a fish and a submarine using the arrow keys or WASD keys. The objective is to move the fish and submarine around the screen within a 10-second time limit. If the fish and submarine collide, the game declares the submarine as the winner. If the time limit is reached without a collision, the fish is declared the winner. The game features a simple background image and sprite graphics for the fish and submarine.

Level Design (Storyboard): The game has a single level with a static underwater background. There are no distinct stages or level progressions.

Graphics: The game uses the following graphics:
1.	Background image (Graphics/background.png): This image represents the underwater environment and serves as the background for the game.
 
2.	Fish sprite (Graphics/fish.png): This sprite represents the fish character that the player controls.
 
3.	Submarine sprite (Graphics/submarine.png): This sprite represents the submarine character that the player controls.
 
4.	Music (Graphics/sailor_waltz_with_water_effects_c64_style.ogg): The background music that plays throughout the game.
The sprites are loaded from the provided file paths, and the fish and submarine sprites are scaled down to smaller sizes using the pygame.transform.scale function.

Characters and Objects with Behaviors: The game features two main characters:
1.	Fish: The fish character is represented by the fish sprite. The player can control its movement using the WASD keys. The fish's position is updated based on the user's input.
2.	Submarine: The submarine character is represented by the submarine sprite. The player can control its movement using the arrow keys. The submarine's position is updated based on the user's input.
Both characters have collision detection implemented using pygame.mask and pygame.mask.from_surface. When the fish and submarine collide, the game declares the submarine as the winner and displays a message on the screen.

Instructions for Players: To play the game, the player needs to control both the fish and the submarine using the following controls:
•	Fish movement:
•	W: Move up
•	A: Move left
•	S: Move down
•	D: Move right
•	Submarine movement:
•	Up Arrow: Move up
•	Left Arrow: Move left
•	Down Arrow: Move down
•	Right Arrow: Move right

The objective is to navigate the fish and submarine around the screen within a 10-second time limit. If the fish and submarine collide, the submarine wins. If the time limit is reached without a collision, the fish wins.
Scoring, Win/Lose Conditions, and Objectives: The game does not have a scoring system. The win/lose conditions are as follows:
•	Win conditions:
•	For the submarine: Collide with the fish before the time limit expires.
•	For the fish: Avoid colliding with the submarine until the 10-second time limit is reached.
•	Lose conditions:
•	For the submarine: Fail to collide with the fish before the time limit expires.
•	For the fish: Collide with the submarine before the 10-second time limit is reached.
T
he primary objective for the player is to control both the fish and the submarine skillfully to achieve the respective win condition for each character.
Format: The code you provided is written in Python and uses the Pygame library for game development. It follows a structured format with comments explaining the different sections and functionality. The code is organized into several sections, such as initializing Pygame, loading graphics, setting up initial positions and speeds, handling game events (user input), updating character positions, collision detection, and rendering the game elements on the screen.
![image](https://github.com/Atanas5611/SunnyBeach/assets/124590675/ddd1e910-a23e-42c4-91b5-17a985fc3e79)
