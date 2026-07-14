import streamlit as st
from groq import Groq

# ---------------------
# 페이지 설정
# ---------------------
st.set_page_config(
    page_title="좌뇌 · 우뇌 사고 시뮬레이터",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 좌뇌 · 우뇌 사고 시뮬레이터")
st.write("같은 질문을 좌뇌, 우뇌, 통합 사고방식으로 분석합니다.")

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

def ask(question):

    prompt=f"""
다음 질문에 대해 세 가지 관점으로 답하라.

질문
{question}

출력 형식

### 좌뇌
(논리적 분석)

### 우뇌
(직관과 감정)

### 통합
(두 사고를 종합)

좌뇌 특징
- 언어
- 분석
- 분류
- 원인과 결과
- 과거와 미래

우뇌 특징
- 직관
- 현재
- 감정
- 연결성
- 전체적인 맥락
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content

question = st.text_input("질문")

if st.button("생성"):

    if question=="":

        st.warning("질문을 입력하세요.")

    else:

        with st.spinner("생성 중..."):

            result=ask(question)

        st.markdown(result)
