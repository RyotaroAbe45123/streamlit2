import streamlit as st

st.title("補助金診断ツール")

# st.write("### Nヶ月以内にXXX万円貰える可能性があります")

st.write("### 該当補助金一覧")

subsidy_candidates = [
    "令和６年度 中小企業のサプライチェーンにおける脱炭素化促進支援事業助成金",
    "令和６年度 テレワーク促進助成金",
    "令和６年度 働くパパママ育業応援奨励金【もっとパパコース】",
    "令和６年度 事業再構築補助金（交付申請用）"
]
checked_subsidy_candidates = []

for subsidy in subsidy_candidates:
    # 改行位置を調整した。もっと横長にしたい。
    l, r = st.columns([10, 0.1])
    l.write("#### " + subsidy)
    if r.checkbox("", key=subsidy):
        checked_subsidy_candidates.append(subsidy)

left, middle, right = st.columns(3)
if middle.button("詳細診断", type="primary"):
    st.switch_page("pages/questions.py")