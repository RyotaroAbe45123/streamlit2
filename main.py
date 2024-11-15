import streamlit as st
import pandas as pd

def load_sample_data():
    """サンプルの補助金データを生成"""
    return pd.DataFrame({
        '補助金名': [
            '中小企業デジタル化支援補助金',
            '令和６年度 中小企業のサプライチェーンにおける脱炭素化促進支援事業助成金',
            '令和６年度働くパパママ育業応援奨励金【もっとパパコース】',
            '令和6年度テレワーク促進助成金',
            '事業継続支援補助金'
        ],
        '補助金額上限': [
            '100万円',
            '200万円',
            '300万円',
            '450万円',
            '150万円'
        ],
        '利用目的': [
            '新規事業',
            '研究開発',
            '人材育成',
            'リモート導入',
            'リモート導入'
        ],
        '概要': [
            'デジタルツール導入、DX推進に関する費用の補助',
            'この助成金は、「中小企業のサプライチェーンにおける脱炭素化促進支援事業」のハンズオン支援の決定を受け、グループとしてCO2排出量削減計画の策定を行い、公社から同計画策定が完了したことを認められていることが申請要件です。',
            '（公財）東京しごと財団（以下「財団」という。）は、複数の男性従業員に育業させるとともに、継続的に育業しやすい職場環境を複数整備した企業等に奨励金を支給することで、男性の育児参加を促進し、育業しやすい職場環境の改善を図ります。 ',
            'テレワークのさらなる定着・促進を図るため、都内中堅、中小企業等に対し、テレワークの導入に必要な機器やソフトウェア等の経費を助成します。',
            '事業継続・再構築に必要な投資の支援'
        ],
        '申請期限': [
            '2024年12月31日',
            '2024年9月30日',
            '2024年10月31日',
            '2024年11月30日',
            '2024年8月31日'
        ],
        '業種': [
            '農業',
            '製造業',
            '農業',
            'サービス業',
            '金融業'
        ],
        '従業員数': [
            '制約なし',
            '制約なし',
            '5名以下',
            '20名以下',
            '100名以下'
        ],
    })

def search_subsidies(df, keyword='', company_category='', num_of_employee='', company_type=''):
    """補助金を検索する関数"""
    if keyword:
        # mask = (
        #     df['補助金名'].str.contains(keyword, case=False) |
        #     df['概要'].str.contains(keyword, case=False)
        # )
        mask = (
            df['補助金名'].str.contains(keyword, case=False)
        )
        df = df[mask]

    if company_category:
        df = df[df['業種'].str.contains(company_category, case=False)]
    
    if num_of_employee:
        df = df[df['従業員数'].str.contains(num_of_employee, case=False)]
    
    if company_type:
        df = df[df['利用目的'].str.contains(company_type, case=False)]
    
    return df

def main():
    st.title('補助金検索システム')
    
    # サイドバーに検索条件を配置
    st.sidebar.header('検索条件')
    
    # キーワード検索
    keyword = st.sidebar.text_input('キーワード検索')

    # 業種
    company_category = ['', '農業', '製造業', '金融業', 'サービス業']
    company_category = st.sidebar.selectbox(
        '業種',
        company_category
    )

    # 従業員数
    num_of_employees = ['', '制約なし', '5名以下', '20名以下', '100名以下']
    num_of_employee = st.sidebar.selectbox(
        '従業員数',
        num_of_employees
    )

    # # 企業種別による絞り込み
    # company_types = ['', '中小企業', '小規模事業者', '全企業']
    # company_type = st.sidebar.selectbox(
    #     '対象企業種別',
    #     company_types
    # )
    company_types = ['', '新規事業', '研究開発', '人材育成', 'リモート導入']
    company_type = st.sidebar.selectbox(
        '利用目的',
        company_types
    )
    
    # データの読み込み（実際のアプリケーションではデータベースやAPIから取得）
    df = load_sample_data()
    
    # 検索実行
    # results = search_subsidies(df, keyword, company_type)
    results = search_subsidies(df, keyword, company_category, num_of_employee, company_type)
    
    # 検索結果の表示
    st.subheader('検索結果')
    if len(results) > 0:
        # 各補助金の詳細を表示
        for _, row in results.iterrows():
            with st.expander(f"📋 {row['補助金名']}"):
                st.write(f"**補助金額上限:** {row['補助金額上限']}")
                st.write(f"**利用目的:** {row['利用目的']}")
                st.write(f"**概要:** {row['概要']}")
                st.write(f"**業種:** {row['業種']}")
                st.write(f"**従業員数:** {row['従業員数']}")
                st.write(f"**申請期限:** {row['申請期限']}")
                
                # 仮の申請ボタン
                if st.button('申請する', key=row['補助金名']):
                    st.success('申請ページへ移動します（デモ用のメッセージ）')
    else:
        st.warning('条件に一致する補助金が見つかりませんでした。')
    
    # 補助金データの一覧表示（オプション）
    # if st.sidebar.checkbox('補助金一覧を表示'):
    #     st.subheader('補助金一覧')
    #     st.dataframe(df)

if __name__ == '__main__':
    main()