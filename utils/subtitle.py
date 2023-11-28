from PIL import Image, ImageDraw, ImageFont
from PIL.ImageQt import ImageQt
from PySide6.QtGui import QPixmap

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
    image_qt = ImageQt(img)
    return QPixmap.fromImage(image_qt)
