from html2image import Html2Image
from PySide6.QtCore import QSettings
import datetime

emotion = ["fear", "surprise", "angry", "sad", "neutral", "happy", "hate"]

def read_css_file(file_path):
    with open(file_path, encoding='utf-8') as f:
        css_file = f.read()
    return css_file

def generate_subtitle(emotion_type, text):
    settings = QSettings('setting/config.ini', QSettings.IniFormat)
    hti = Html2Image(size=(1080, 256))
    output_path = settings.value('image_save_path')
    hti.output_path = output_path
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_image = f"{current_datetime}_{emotion_type}.png"

    css_file_path = f'resources/css/{emotion[emotion_type]}.css'

    css = read_css_file(css_file_path)

    html = f"""<!DOCTYPE html>
            <html>
            <body>
                <div class="container">
                    <p class="styled-text">{text}</p>
                </div>
            </body>
            </html>
            """

    hti.screenshot(html_str=html, css_str=css, save_as=output_image)
    save_history(f"{current_datetime}:{text}:{emotion[emotion_type]}")

def save_history(new_text):
    with open("subtitle_history/history.txt", 'r+', encoding='utf-8') as file:
        content = file.read()
        file.seek(0, 0)
        file.write(new_text.rstrip('\r\n') + '\n' + content)