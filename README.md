# O-sul (Python)

## Overview
O-sul is a terminal-based interactive narrative game built in Python that uses branching story logic, player state tracking, and conditional progression to create a dynamic storytelling experience. Player choices directly influence story paths, outcomes, and accessibility to future events.

The project emphasizes programmatic storytelling, modular narrative design, and user interaction rather than static text adventure scripting.

## Program Design
1. Story Architecture
	- The narrative is built using function-based story nodes, where:
		- Each function represents a point of decision
		- Player input determines which function is executed
		- Structure allows non-linear progression
	- This makes the story easy to expand with new branches without rewriting core logic

2. State & Progress Tracking
	- Player progress is tracked through:
 		- Boolean flags
		- Conditional checks
		- Function routing
	- Allowing:
 		- Locked paths
		- Choice consequences
    	- Replayability with different outcomes

3. Password / Access System
	- The game include a hidden input password gate using getpass:
 		- Input isn't echoed in the terminal
		- Used to unlock restricted narrative paths
		- Mimics basic authentication logic
	- This was intentionally designed to reflect security-based thinking

4. Testing & Debugging Mechanism
	- The game includes:
 		- Isolated story paths that can be invoked independently
      	- Clear function boundaries for unit-style testing
      	- Deterministic logic paths for debugging outcomes
	- Allowing the developer to test specfic narrative branches w/o replaying the entire game

5. Immersive Features
	- Time output using `time.sleep()` for pacing
	- ASCII and terminal formatting
	- Dynamic narrative tone changes
	- Virtual asset display via Pillow
	- Input validation to prevent crashes

## Repository Contents
- `main.py`
  - Core game engine containing:
    - Story Logic
    - Choice Branching
    - State Tracking
    - Input validation
    - Narrative testing framework
    - Security-style password gate
- `ssamblu.gif`
  - Visual asset displayed during a key narrative moment using Pillow (PIL)

## Dependencies & Setup
Requirements:
		- Python 3.8+
		- Pillow (Python Imaging Library) ~ `pip install pillow`
Imported libraries:
		- time (pacing and immersion)
		- sys (controlled exits)
		- os (env interaction)
		- getpass (hidden password input)
		- PIL.Image (visual asset rendering)

## How to Run
1. `python main.py`
2. Ensure that `ssamblu.gif` is in the same directory as `main.py`
3. Enjoy the game, your choices have consequences.
