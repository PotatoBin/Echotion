# Echotion

## Overview
Echotion is an open-source project focused on generating real-time subtitles reflecting the emotions conveyed in spoken Korean text. The project combines "Echo" and "Emotion," encapsulating its core function of understanding and interpreting emotions through voice. The primary objective is to develop an application capable of creating real-time Korean subtitles that accurately portray the emotional context of spoken content.

## Core Components and Technologies
### 1. Speech Recognition (STT)
- **API**: [ETRI Open API](https://aiopen.etri.re.kr/)

### 2. Emotion Analysis
- **Model**: [KoBERT](https://github.com/SKTBrain/KoBERT)
- **Pre-Trained Model**: [Pre-trained Model](https://drive.google.com/file/d/1ZWE5lphoBywRx5M7Ro_fqkG2fyo9SJHd/view?usp=sharing)
- **Implementation**: The pre-trained models we distribute are based on KoBERT, enabling analysis of text emotions across seven categories: "fear," "surprise," "angry," "sad," "neutral," "happy," and "hate." This allows for a detailed emotion analysis of text data leveraging the KoBERT model architecture. Please note that pre-trained models are not distributed with this repository. You will need to acquire and place any necessary pre-trained models in the designated directories as per the application's requirements before using the system.

### 3. Real-time Subtitle Generation and Display
- **Libraries**: [Html2image](https://github.com/vgalin/html2image), [PySide6](https://pypi.org/project/PySide6/)
- **Implementation**: Html2image is utilized to dynamically generate text-based images, allowing customization of font types, sizes, colors, and other visual elements, catering to diverse contextual requirements.

## Installation & Usage

It is recommended to use a virtual environment to prevent potential conflicts with other Python projects or dependencies.

1. Clone the repository:

    ```bash
    git clone https://github.com/PotatoBin/Echotion
    cd your_repository
    ```

2. Install required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. Setting API Key and .pt File:
   
    To open the [setting/config.ini](https://github.com/PotatoBin/Echotion/blob/main/setting/config.ini) file in a text editor
   
    ```ini
    [General]
    api_key=your_api_key
    pt_file_path=file_path
    background_color=#b9b9b9
    image_save_path=subtitle_history
    recording_interval=5
    ```
   - `api_key`: Obtain your API key from [ETRI Open API](https://aiopen.etri.re.kr/). Replace `your_api_key` in the 'config.ini' file with your specific API key.
   - `pt_file_path`: Set `file_path` with the absolute path to your deployed '.pt' file. This file is crucial for connecting to the model used in the application.

5. Run the application:

    After installing the dependencies, execute the main Python script:

    ```bash
    python main.py
    ```
    
## Customizing Subtitle Styles

In the [resources/css directory](https://github.com/PotatoBin/Echotion/tree/main/resources/css), you can customize the CSS for subtitles corresponding to different emotions. This customization allows you to tailor the visual style of subtitles according to each emotion category.

