import streamlit as st
import time

st.set_page_config(page_title="AI Research Agent", layout="wide")
st.title("🧪 My Local AI Scientist Dashboard")

# 상단 탭 구성
tab1, tab2, tab3 = st.tabs(["💡 1. 아이디어 생성", "⚙️ 2. 실험 모니터링", "📝 3. 논문 및 리뷰"])

with tab1:
    st.subheader("초기 연구 주제 및 베이스 코드 입력")
    base_code = st.text_area("Base Python Code를 입력하세요:", height=150)
    
    if st.button("연구 아이디어 브레인스토밍 🚀"):
        with st.spinner("AI가 문헌을 검색하고 아이디어를 생성 중입니다..."):
            time.sleep(2) # LLM API 호출 대기 시간 시뮬레이션
            st.success("3개의 연구 아이디어가 도출되었습니다!")
            
            # 아이디어 선택 UI
            idea = st.radio("진행할 연구 방향을 선택하세요:", 
                            ["아이디어 A: 하이퍼파라미터 최적화 자동화 알고리즘 도입", 
                             "아이디어 B: 새로운 손실 함수(Loss function) 제안", 
                             "아이디어 C: 데이터 증강(Data Augmentation) 기법 적용"])
            st.button("이 아이디어로 실험 시작 ➡️")

with tab2:
    st.subheader("실시간 에이전트 작업 로그")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("**Agent Terminal Log**")
        log_box = st.empty()
        # 실시간 로그가 찍히는 연출
        log_text = "> Agent: Modifying train.py...\n"
        log_box.code(log_text, language='bash')
        
    with col2:
        st.markdown("**현재 성능 (Metric)**")
        st.metric(label="현재 최고 정확도", value="85.4%", delta="1.2% 상승")

with tab3:
    st.subheader("최종 생성 논문 및 AI 리뷰어 평가")
    st.markdown("**(이곳에 생성된 PDF 파일이나 Markdown 형태의 논문이 렌더링됩니다.)**")
    
    with st.expander("🔍 AI Reviewer 평가 결과 보기", expanded=True):
        st.write("- **독창성 (Novelty):** 6.5 / 10")
        st.write("- **기술적 완성도:** 8.0 / 10")
        st.warning("수정 제안: 3번 그래프의 축 설명이 부족합니다. 보완이 필요합니다.")
