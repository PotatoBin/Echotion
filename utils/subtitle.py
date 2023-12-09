from html2image import Html2Image
import datetime

emotion = ["fear", "angry", "sad", "neutral", "surprise", "happy", "hate"]

def read_css_file(file_path):
    with open(file_path) as f:
        css_file = f.read()
    return css_file

def generate_subtitle(emotion_type, text):
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    hti = Html2Image(size=(1080, 256))
    hti.output_path = "subtitle_history" 
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
