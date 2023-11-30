from PIL import Image, ImageDraw, ImageFont
from PySide6.QtCore import QSettings
import datetime
settings = QSettings("setting/config.ini", QSettings.IniFormat)

width = 1080
height = 256
font_size = height//2

def fear(sentence) :
    font = ImageFont.truetype("resources/fonts/Cafe24Supermagic-Bold-v1.0.ttf", font_size)
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0)) 
    d = ImageDraw.Draw(img)
    d.text((width//2, height//2), sentence, fill="black", anchor="mm", font=font)
    return img

def angry(sentence) :
    font = ImageFont.truetype("resources/fonts/Baemin-Yeonsung.ttf", font_size)
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0)) 
    d = ImageDraw.Draw(img)
    d.text((width//2, height//2), sentence, fill="black", anchor="mm", font=font)
    return img

def sadness(sentence) :
    font = ImageFont.truetype("resources/fonts/NanumBrushGothicGoding.ttf", font_size)
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0)) 
    d = ImageDraw.Draw(img)
    d.text((width//2, height//2), sentence, fill="black", anchor="mm", font=font)
    return img

def neutral(sentence) :
    font = ImageFont.truetype("resources/fonts/NanumSquareRoundB.ttf", font_size)
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0)) 
    d = ImageDraw.Draw(img)
    d.text((width//2, height//2), sentence, fill="black", anchor="mm", font=font)
    return img

def surprise(sentence) :
    font = ImageFont.truetype("resources/fonts/Cafe24Ohsquare-v2.0.ttf", font_size)
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0)) 
    d = ImageDraw.Draw(img)
    d.text((width//2, height//2), sentence, fill="black", anchor="mm", font=font)
    return img

def happiness(sentence) :
    font = ImageFont.truetype("resources/fonts/Cafe24Moyamoya-Face-v1.0.ttf", font_size)
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0)) 
    d = ImageDraw.Draw(img)
    d.text((width//2, height//2), sentence, fill="black", anchor="mm", font=font)
    return img

def hate(sentence) :
    font = ImageFont.truetype("resources/fonts/BlackHanSans-Regular.ttf", font_size)
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0)) 
    d = ImageDraw.Draw(img)
    d.text((width//2, height//2), sentence, fill="black", anchor="mm", font=font)
    return img

emotion = [fear, angry, sadness, neutral, surprise, happiness, hate]

def generate_subtitle(emotion_type, text):
    img = emotion[emotion_type](text)
    image_save_path = settings.value("image_save_path", defaultValue="subtitle_history")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    save_path = f"{image_save_path}/{current_datetime}_{emotion_type}.png"
    img.save(save_path)
    return