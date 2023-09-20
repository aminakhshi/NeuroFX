# NeuroFX - A Cloud-Based Solution for Neural Recording Techniques

![Game Demo](https://github.com/aminakhshi/NeuroFX/blob/c441468eedcd45d247b39497282712c16fa6f772/static/images/game_output.gif)

## Overview

In recent years, neural recording techniques have become pivotal in both scientific research and clinical brain studies. With the proliferation of these methods, there exists a growing need for unified platforms and standardized metrics to measure individual differences.

**NeuroFX** offers a groundbreaking cloud-based solution, targeting the consolidation of protocols and analytical tools. As an introductory venture, it deploys game-based strategies to delve into the pathways involved in crucial brain functions. Participants undergo meticulously designed tasks and receive individualized feedback, normalized against a robust reference database.

## Features

- **Game-Based Strategy**: Engage in meticulously designed games that tap into key brain functions.
  
- **Individualized Feedback**: Obtain feedback, perfectly normalized against a predefined reference database.
  
- **Modularity**: NeuroFX offers the ability to adjust game-based experiments suitable to various conditions and recording tools. This comprehensive integration promotes efficient data centralization, setting standardized protocols, and boosting cross-lab collaborations and sharing.
  
## Web App Flow

1. **Home Page**: Welcomes users.
  
2. **Game Start**: Upon starting the game, a Flask-based backend runs the game script, fetching the game results and redirecting users to the results page.
  
3. **Results Page**: Displays bar plots showcasing the number of correct and incorrect answers. Histograms visualize latency times for correct and incorrect answers.

## Visualization Plots

Here's an example of the visualizations users will encounter on the results page:

![Correct vs Wrong Answers](https://github.com/aminakhshi/NeuroFX/blob/c441468eedcd45d247b39497282712c16fa6f772/static/images/performance_result.png)
![Latency Times for Correct Answers](https://github.com/aminakhshi/NeuroFX/blob/c441468eedcd45d247b39497282712c16fa6f772/static/images/performance_result2.png)
![Latency Times for Incorrect Answers](https://github.com/aminakhshi/NeuroFX/blob/c441468eedcd45d247b39497282712c16fa6f772/static/images/performance_result3.png)

(Note: Replace `path_to_*` placeholders with actual paths to your images or links if hosted online.)

## Release History
0.0.1 - Initial release

## Setting Up Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/NeuroFX.git
   ```
2. Navigate to the project directory:
   ```bash
   cd NeuroFX
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```

## To-Do

As NeuroFX continues to evolve, we have several enhancements and features lined up for future releases. Here's a sneak peek into what's next for our platform:

1. **Gaming Options Expansion**: Introduce a wider array of gaming options for diversified user experiences.

2. **Neural Recording Module**: Enhance the platform with a sophisticated recording module capable of reading various neural recording techniques such as EEG, MEG, fMRI, and more.

3. **User Role Differentiation**: Implement a comprehensive user access mechanism, enabling differential access levels for researchers and participants. This ensures a tailored experience based on user roles.

4. **Improved Visualization & Website Design**: While our current visualizations offer clarity, we aim to augment our design, making it more intuitive and visually appealing. Similarly, the website template will undergo improvements for a more engaging user journey.

5. **Server Deployment**: In order to make NeuroFX accessible to a broader audience, we are in the process of deploying the website on a more scalable and robust server.


## Contribute

This app is designed under open-source license agreement. Feel free to fork the project, open an issue, or submit a pull request to suggest any features you'd love to see in future iterations!


## License

MIT License


