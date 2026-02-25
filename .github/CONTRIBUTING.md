# Contributing to Chase Game

Thank you for your interest in contributing! This project was developed as a university assignment, but any improvements, bug fixes, or new ideas are more than welcome to make this strategic survival game even more challenging.

## How to Contribute

1. **Fork** the repository.
2. Create your branch: `git checkout -b feature/new-functionality`.
3. Make your changes and commit them: `git commit -m "Add new functionality"`.
4. Push your branch: `git push origin feature/new-functionality`.
5. Open a **Pull Request**.

## Ideas for Contribution

- **Advanced Robot AI:** Implement different types of robots (e.g., faster robots, or robots that avoid obstacles).
- **Level Progression:** Add a system where the number of robots or obstacles increases after clearing the board.
- **Visual Improvements:** Replace text symbols (♥, ☻) with custom sprites or add animations for robot collisions.
- **Power-ups:** Add items that the player can pick up to temporarily freeze robots or destroy nearby obstacles.
- **High Score System:** Implement a way to track how many moves or rounds a player survives.
- **Code Refactoring:** Improve the grid management logic or transition the project from structured programming to an Object-Oriented (OOP) architecture.

## Development Tips

- **Grid Logic:** The game relies on a coordinate system. Ensure that any movement (especially diagonal) correctly checks for boundaries to prevent index errors.
- **Collision Order:** Be careful with the order of movement updates. Robots should move after the player, and collisions should be evaluated immediately to ensure fair gameplay.
- **Gamelib Interaction:** Use the `gamelib` documentation to handle complex keyboard inputs for the 8-way movement system.

Thank you for your collaboration! 🎉
