# Police Search Engine

Welcome to the Police Search Engine, an ingenious application that empowers law enforcement agencies to swiftly gather crucial information related to SIM-to-cell tower connections. With this Neo4j-based project, investigators can input specific details and obtain comprehensive connection information for SIMs and cell towers. This powerful tool assists in localizing suspects, identifying individuals linked to specific cell towers, and uncovering potential suspects within a crime zone. Prepare to enhance your investigative prowess!

## Prerequisites

Before you begin your investigation, ensure you have the following tools ready:

- Python (version 3.10 or above)
- Neo4j module for Python (Refer to step 2 in the **Getting Started** section below for installation instructions)

## Getting Started

Let's kickstart your investigation:

1. Begin by cloning the repository to your local machine. Open your command prompt and execute the following command:

   ```
   git clone https://github.com/LeonardoRocca-13/Police_Search_Engine.git
   ```

2. Once the repository is cloned, install the necessary dependencies. In the command prompt, run the following command:

   ```
   pip install -r requirements.txt
   ```

3. Establish the connection to Neo4j. The project utilizes Neo4j as its powerful graph database, providing lightning-fast data retrieval for your investigations. Please ensure you have a Neo4j database set up and running.

4. Navigate to the project directory in your command prompt. Execute the following command:

   ```
   cd Police_Search_Engine
   ```

5. Get ready to dive into the depths of the Police Search Engine. Run the `main.py` file to launch the application:

   ```
   python main.py
   ```

6. The stage is set, and the application is now running. Follow the intuitive on-screen instructions to utilize the Police Search Engine's functionality and unleash the full potential of your investigation.

## Usage

The Police Search Engine equips you with three key functionalities, designed to elevate your investigation process:

1. **Search for Suspect's SIM-to-Cell Connections**: With a specific date, time, and person's name, retrieve a comprehensive list of cell towers connected to SIM cards registered to the suspect. This level 1 search provides valuable insights into the suspect's communication patterns.

2. **Identify Suspects in a Crime Zone**: Given a date, time, and cell tower, retrieve a list of individuals associated with SIM cards connected to that particular tower at the specified time. This level 2 search helps identify potential suspects within a crime zone.

3. **Search by Location Coordinates**: With geographical coordinates, a date, and time, discover individuals associated with SIM cards connected to cell towers within a specified radius of the provided coordinates. This level 3 search expands the investigation radius, aiding in identifying suspects near specific locations.

## Contributing

Become an integral part of our investigative community! We welcome contributions, ideas, and feedback to enhance the Police Search Engine. If you encounter any issues or have brilliant improvements in mind, please open an issue or submit a pull request. Together, let's strengthen the investigative capabilities!

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

- This project was completed on for educational purposes and should not be used in any real-life scenarios.
- The data used in this project is not real and is only used for as a simulation.
