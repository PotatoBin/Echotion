import urllib3
import json
import base64
from PySide6.QtCore import QSettings

def recognize_audio(audio_file_path):
    settings = QSettings("setting/config.ini", QSettings.IniFormat)
    openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Recognition"
    accessKey = settings.value("api_key", defaultValue="your_api_key_here")
    languageCode = "korean"

    with open(audio_file_path, "rb") as file:
        audioContents = base64.b64encode(file.read()).decode("utf8")

    requestJson = {
        "argument": {
            "language_code": languageCode,
            "audio": audioContents
        }
    }

    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        openApiURL,
        headers={"Content-Type": "application/json; charset=UTF-8", "Authorization": accessKey},
        body=json.dumps(requestJson)
    )
    
    result_text = json.loads(response.data.decode('utf-8'))['return_object']['recognized']
    return result_text