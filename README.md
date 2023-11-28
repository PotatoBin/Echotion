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
- **Libraries**: [Pillow](https://pypi.org/project/Pillow/), [PySide6](https://pypi.org/project/PySide6/)
- **Implementation**: We are developing an interface that converts the results from the STT and emotion analysis components into real-time subtitles. We need a function to visualize text as an image, which is why we chose to use an image processing library such as Pillow. With Pillow, we can apply various fonts, colors, and sizes to the text. Users will be able to customize font types, text sizes, borders, and use shape elements depending on the situation. We plan to implement preset subtitle styles for each classified emotion.

## Installation & Usage
(Work in progress)

## Project Timeline & Roadmap
Echotion project is currently in the planning phase. Our future plans include improving the accuracy of Korean speech recognition, enhancing the precision of emotion analysis, creating suitable subtitle styles for each emotion, and developing a user-friendly GUI.
