import torch
import numpy as np
from transformers import BertModel
from utils.kobert_tokenizer import KoBERTTokenizer
from torch import nn

# Softmax 함수 정의
def softmax(vals, idx):
    valscpu = vals.cpu().detach().squeeze(0)
    a = 0
    for i in valscpu:
        a += np.exp(i)
    return ((np.exp(valscpu[idx])) / a).item() * 100

# 모델 정의
class BERTClassifier(nn.Module):
    def __init__(self, bert, hidden_size=768, num_classes=7, dr_rate=None):
        super(BERTClassifier, self).__init__()
        self.bert = bert
        self.dr_rate = dr_rate
        self.classifier = nn.Linear(hidden_size, num_classes)
        if dr_rate:
            self.dropout = nn.Dropout(p=dr_rate)

    def forward(self, token_ids, valid_length, segment_ids):
        attention_mask = self.gen_attention_mask(token_ids, valid_length)
    
        # bert 모델의 출력값에서 튜플 형태로 출력을 받음
        output = self.bert(input_ids=token_ids, token_type_ids=segment_ids.long(), attention_mask=attention_mask.float().to(token_ids.device))
    
        # pooler 출력을 추출
        pooler = output[1]

        # pooler가 텐서인지 확인
        if not isinstance(pooler, torch.Tensor):
            raise TypeError(f"Expected torch.Tensor, but got {type(pooler)}")

        if self.dr_rate:
            out = self.dropout(pooler)
        else:
            out = pooler
        return self.classifier(out)
    
    def gen_attention_mask(self, token_ids, valid_length):
        attention_mask = torch.zeros_like(token_ids)
        for i, v in enumerate(valid_length):
            attention_mask[i][:v] = 1
        return attention_mask.float()

# 모델 로드
model = BERTClassifier(BertModel.from_pretrained('skt/kobert-base-v1'), dr_rate=0.5)
model.load_state_dict(torch.load("C:/Users/yudam/Downloads/kobert_model (1).pt"), strict=False)
model.eval()

# 토크나이저 로드
tokenizer = KoBERTTokenizer.from_pretrained('skt/kobert-base-v1')

# 디바이스 설정
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# 감정 분류 함수
def classify_emotion(sentence):
    # 토큰화 및 디바이스 할당
    tokens = tokenizer.encode(sentence, return_tensors="pt", add_special_tokens=True).to(device)
    valid_length = torch.tensor([len(tokens[0])])
    segment_ids = torch.zeros(tokens.size(), dtype=torch.long).to(device)  # 변경됨

    # 모델 추론
    with torch.no_grad():
        output = model(tokens, valid_length, segment_ids)
    
    # 결과 처리
    idx = output.argmax().cpu().item()
    confidence = softmax(output, idx)
    emotions = ["공포", "놀람", "분노", "슬픔", "중립", "행복", "혐오"]
    return idx
