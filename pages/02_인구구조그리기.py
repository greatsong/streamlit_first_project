import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# Load data
data_path = 'age2411.csv'
df = pd.read_csv(data_path)

# Streamlit app
def main():
    st.title("지역별 인구 구조 시각화")
    st.write("원하는 지역의 인구 구조를 확인해보세요!")

    # 지역 선택 옵션 설정
    regions = df['\ud589\uc815\uad6c\uc5ed'].unique()
    selected_region = st.selectbox("지역을 선택하세요:", regions)

    # 선택한 지역의 데이터 필터링
    region_data = df[df['\ud589\uc815\uad6c\uc5ed'] == selected_region]

    # 연령별 데이터만 추출
    age_columns = [col for col in df.columns if '계_' in col and '연령구간' not in col]
    age_data = region_data[age_columns].T
    age_data.columns = ['인구 수']
    age_data = age_data.iloc[1:]  # 첫 번째 행 제외

    # 인덱스에서 나이를 안전하게 추출
    def extract_age(col):
        try:
            return int(col.split('_')[1][:-1])
        except (IndexError, ValueError):
            return None
    
    age_data['나이'] = [extract_age(col) for col in age_data.index]
    age_data = age_data.dropna(subset=['나이'])
    age_data = age_data.set_index('나이')

    # 그래프 그리기
    st.subheader(f"{selected_region}의 인구 구조")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(age_data.index, age_data['인구 수'], color='skyblue')
    ax.set_xlabel('나이')
    ax.set_ylabel('인구 수')
    ax.set_title(f'{selected_region}의 나이별 인구 분포')
    st.pyplot(fig)

if __name__ == "__main__":
    main()
