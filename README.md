

# Elevator Simulation Game

This is an elevator simulation game implemented using Pygame. The simulation includes multiple floors and elevators, each responding to user inputs to simulate the operation of elevators in a building.

## Features

- Multiple elevators and floors
- Real-time elevator movements
- User interaction with floor buttons
- Visual representation of the building and elevators

## Installation and Setup

Follow these steps to set up and run the elevator simulation game on your local machine.

### Prerequisites

- Python 3.9 or later
- Git

### Steps

1. **Download and Install Python**:
   - Go to the [official Python website](https://www.python.org/downloads/).
   - Download the latest version of Python.
   - Run the installer and follow the instructions. Make sure to check the box that says "Add Python to PATH" during the installation process.
   - Verify the installation by opening a command prompt or terminal and running:
     ```bash
     python --version
     ```

2. **Clone the Repository**:
   - Open a command prompt or terminal.
   - Run the following command to clone the repository:
     ```bash
     git clone https://github.com/yourusername/elevator-simulation.git
     cd elevator-simulation
     ```

3. **Create and Activate Virtual Environment** (Optional but recommended):
   - Create a virtual environment:
     ```bash
     python -m venv env
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       .\env\Scripts\activate
       ```
     - On macOS and Linux:
       ```bash
       source env/bin/activate
       ```

4. **Install Dependencies**:
   - Install the required dependencies using `pip`:
     ```bash
     pip install pygame
     ```

### Running the Simulation


 **Run the Main Script**:
   - Execute the following command to start the simulation:
     ```bash
     python main.py
     ```

### Project Structure

- `main.py`: The main script that initializes and runs the simulation.
- `building.py`: Contains the `Building` class which manages the overall structure and behavior of the building.
- `elevator.py`: Contains the `Elevator` class which simulates the behavior of an individual elevator.
- `floor.py`: Contains the `Floor` class which represents an individual floor in the building.
- `timer.py`: Contains the `Timer` class which manages countdown timers for various events.
- `settings.py`: Configuration file for constants and settings.
- `README.md`: Provides an overview and setup instructions for the project.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

## License

This project is licensed under the MIT License.
