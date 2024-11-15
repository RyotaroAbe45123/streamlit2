import streamlit as st

st.title("補助金診断ツール")

st.write("### 詳細質問")

questions = [
    "都内の中小事業者で、CO2排出量削減を計画されていますか？",
    "都内の事業者で、従業員が2人以上1000人未満かつテレワーク助成金を受給されていないですか？",
    "都内在勤の男性従業員の方が、2歳未満のお子さんの育休を30日以上取得されており、また、環境の整備をされる予定ですか？",
]
checked_questions = []

for question in questions:
    l, r = st.columns([10, 0.1])
    l.write("#### " + question)
    if r.checkbox("#### Yes", key=question):
        checked_questions.append(question)

left, middle, right = st.columns(3)
if middle.button("診断", type="primary"):
    st.switch_page("pages/final_candidates.py")