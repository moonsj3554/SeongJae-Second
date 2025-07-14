import streamlit as st
import plotly.graph_objects as go

# 연도별 곡별 이용자 수 데이터
melon_data = {
    "ZICO – Any Song (2020)": 5900000,
    "CHANGMO – METEOR (2020)": 5100000,
    "Cho Jungseok – Aloha (2020)": 4800000,
    "IU – Celebrity (2021)": 6200000,
    "Brave Girls – Rollin’ (2021)": 6100000,
    "IVE – LOVE DIVE (2022)": 6500000,
    "(G)I-DLE – TOMBOY (2022)": 6300000,
    "NewJeans – Ditto (2023)": 7000000,
    "NewJeans – Hype Boy (2023)": 6900000,
    "TWS – Plot Twist (2024)": 7200000,
    "(G)I-DLE – Fate (2024)": 7000000,
    "aespa – Supernova (2024)": 6900000,
    "IU – Love wins all (2024)": 6700000,
}

# 상위 10곡만 정렬
top10 = sorted(melon_data.items(), key=lambda x: x[1], reverse=True)[:10]
songs = [item[0] for item in top10]
users = [item[1] for item in top10]

# 제목
st.title("🎵 2020–2024 역대 멜론 이용자 수 Top 10")

# Plotly 수평 막대그래프
fig = go.Figure(data=go.Bar(
    x=users,
    y=songs,
    orientation='h',
    marker=dict(color='rgba(30,144,255,0.7)')
))

fig.update_layout(
    title="역대 멜론 연간 차트 Top 10 (이용자 수 기준)",
    xaxis_title="이용자 수",
    yaxis_title="곡명 (연도)",
    yaxis=dict(autorange='reversed'),
    height=600,
)

st.plotly_chart(fig)
