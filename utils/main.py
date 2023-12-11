import etri_stt_api
import record
import kobert

def main():
    audio_file_path = "stt_output.wav"
    
    # 오디오 녹음
    record.record_audio(audio_file_path)

    # 녹음된 오디오 인식
    recognized_text = etri_stt_api.recognize_audio(audio_file_path)
    print("인식된 텍스트:", recognized_text)
    
    # 예측 실행
    emotion, confidence = kobert.classify_emotion(recognized_text)
    print(f"감정: {emotion}")
    
if __name__ == "__main__":
    main()
