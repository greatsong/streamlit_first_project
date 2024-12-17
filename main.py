import streamlit as st

# MBTI 별 추천 데이터
mbti_data = {
    "INTJ": {
        "description": "독립적이고 전략적인 🧠 INTJ는 문제 해결에 뛰어나며 큰 그림을 그리는 데 능숙해요!",
        "jobs": "과학자 🔬, 엔지니어 🛠️, 기획자 💼",
        "matches": "ENTP 🤝 또는 INTP와 잘 맞아요!"
    },
    "ENTP": {
        "description": "열정적이고 도전적인 💡 ENTP는 창의적이고 논리적 사고를 바탕으로 새로운 아이디어를 만들어내요!",
        "jobs": "스타트업 CEO 🚀, 변호사 ⚖️, 발명가 🛠️",
        "matches": "INFJ 💞 또는 INTJ와 찰떡궁합이에요!"
    },
    "ESFJ": {
        "description": "사교적이고 배려심 넘치는 🤗 ESFJ는 사람을 도와주는 것을 좋아해요!",
        "jobs": "교사 📚, 간호사 🩺, 상담사 🗨️",
        "matches": "ISFP 💛 또는 ESTP와 함께하면 즐거워요!"
    },
    "ISTP": {
        "description": "현실적이면서도 탐구적인 🛠️ ISTP는 손재주가 뛰어나며 문제를 빠르게 해결해요!",
        "jobs": "기술자 🔧, 파일럿 ✈️, 스포츠 코치 🏋️",
        "matches": "ESFP 🎉 또는 ESTP와 모험을 즐겨보세요!"
    }
    # 다른 MBTI도 추가 가능
}

# Streamlit 앱 제목과 설명
st.title("MBTI로 알아보는 직업과 궁합💼")
st.write("### 당신의 MBTI를 선택해보세요! 어떤 직업이 어울릴지, 어떤 사람과 잘 맞는지 알려드릴게요 😊")

# 드롭다운 메뉴
mbti = st.selectbox("당신의 MBTI는 무엇인가요?", list(mbti_data.keys()), index=None, placeholder="MBTI를 선택해주세요!")

# MBTI에 따른 결과 출력
if mbti:
    st.subheader(f":sparkles: {mbti} 유형 분석 :sparkles:")
    st.write(f"{mbti_data[mbti]['description']}")

    st.write("**어울리는 직업**")
    st.write(f"{mbti_data[mbti]['jobs']}")

    st.write("**찰떡궁합인 사람**")
    st.write(f"{mbti_data[mbti]['matches']}")

    st.success("나와 잘 맞는 사람과 함께 꿈을 향해 나아가봐요! 🌟")
else:
    st.warning("MBTI를 선택해주시면 결과를 알려드릴게요! ☝️")
