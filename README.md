# Echotion

## Overview
Echotion is an open-source project that aims to build a system capable of converting spoken Korean into text in real time, and then analyzing the emotions conveyed in the text to generate real-time subtitles that reflect these emotions. The project's name, "Echotion," combines "Echo" and "Emotion," encapsulating the project's core function of understanding and interpreting emotions through voice. The main goal of Echotion is to develop an application that generates real-time Korean subtitles that accurately reflect the emotional context of the spoken content.

## Core Components and Technologies
### 1. Speech Recognition (STT)
- **Model**: [KoSpeech](https://github.com/sooftware/KoSpeech)
- **Implementation**: We are currently working on features for real-time audio streaming processing, specifically optimized for Korean speech recognition. Our plan is to retrain the model for this project using a Korean conversation dataset. We are in the process of identifying the most suitable architecture for this project and plan to determine the optimal one through various experiments.

### 2. Emotion Analysis
- **Model**: [KoBERT](https://github.com/SKTBrain/KoBERT)
- **Implementation**: We are setting up an emotion analysis system by fine-tuning a multi-emotion classification model using a Korean emotion-specific conversation dataset. We chose KoBERT, a model that has trained the original BERT model, specialized in Korean due to its superior understanding of Korean text data. We plan to design an emotion analysis model that is divided into 7 stages, compared to the existing 3 stages (positive, negative, neutral).

### 3. Real-time Subtitle Generation and Display
- **Libraries**: [Html2image](https://github.com/vgalin/html2image), [PySide6](https://pypi.org/project/PySide6/)
- **Implementation**: We're currently building an interface that converts outcomes from both the Speech-to-Text (STT) and emotion analysis modules into real-time subtitles. To convert text into visual representations, we've opted for the html2image library. Leveraging html2image, we can dynamically generate images from text, allowing for various fonts, colors, sizes, and other visual modifications. This versatility empowers users to customize font types, sizes, borders, and even incorporate shape elements based on contextual needs. Our roadmap includes pre-designed subtitle styles tailored to distinct emotional classifications.

## Installation & Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/PotatoBin/Echotion
    cd your_repository
    ```

2. Install required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    After installing the dependencies, execute the main Python script:

    ```bash
    python main.py
    ```

4. Setting API Key and .pt File:

    - Launch the application and navigate to the Preferences section.
    - Enter your API Key in the designated field. [here](https://aiopen.etri.re.kr/)
    - Choose the .pt file for model connection.

    The API Key is essential for certain features of the application. The .pt file is crucial for connecting to the model used in the application.

It's recommended to run the application in a virtual environment to avoid potential conflicts with other Python projects or dependencies.


## Pre-trained Models

Please note that pre-trained models are not distributed with this repository. You will need to acquire and place any necessary pre-trained models in the designated directories as per the application's requirements before using the system. If needed, refer to the documentation or respective model repositories to obtain the required pre-trained models.
