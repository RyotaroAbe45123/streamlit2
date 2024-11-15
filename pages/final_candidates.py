import streamlit as st


st.title("補助金診断ツール")

# st.write("### Nヶ月以内にYYY万円貰える可能性があります")

st.write("### 該当補助金一覧")

subsidy_candidates = [
    "令和６年度 中小企業のサプライチェーンにおける脱炭素化促進支援事業助成金",
    "令和６年度 テレワーク促進助成金",
    "令和６年度 働くパパママ育業応援奨励金【もっとパパコース】",
]

for subsidy in subsidy_candidates:
    l, r = st.columns([10, 0.1])
    l.write("#### " + subsidy)
