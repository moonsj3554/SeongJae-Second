import streamlit as st
import random

st.title("🎵 장르별 멜론 연간 Top 10 추천 (2020~2024)")

# 장르별 곡 데이터 (예시)
# 실제 곡명과 아티스트, 장르 정보를 임의로 분류한 예시입니다.
songs_by_genre = {
    "팝": [
        "IU – Celebrity (2021)",
        "Justin Bieber – Peaches (2021)",
        "Jungkook – Seven (2023)",
        "Crush (feat. j-hope) – Rush Hour (2023)",
        "NewJeans – Ditto (2023)",
    ],
    "댄스": [
        "NewJeans – Hype Boy (2023)",
        "IVE – LOVE DIVE (2022)",
        "(G)I-DLE – TOMBOY (2022)",
        "aespa – Supernova (2024)",
        "TWS – Plot Twist (2024)",
    ],
    "발라드": [
        "Lim Jae-hyun – Rhapsody of Sadness (2024)",
        "DAY6 – Time of Our Life (2024)",
        "Jang Beomjune – Your Shampoo Scent (2020)",
        "MeloMance – Love, Maybe (2022)",
        "Lim Youngwoong – Love Always Runs Away (2022)",
    ],
    "힙합": [
        "ZICO – Any Song (2020)",
        "CHANGMO – METEOR (2020)",
        "Kim Minseok – DrunKen Confession (2022)",
        "ILLIT – Magnetic (2024)",
        "QWER – T.B.H (2024)",
    ],
    "록": [
        "AKMU – Love Lee (2023)",
        "YOUNHA – Event Horizon (2023)",
        "Noel – Late Night (2020)",
        "DAY6 – You Were Beautiful (2024)",
        "BIGBANG – Still Life (2022)",
    ],
}

# 장르 선택 UI
genre = st.selectbox("원하는 장르를 선택하세요:", list(songs_by_genre.keys()))

if st.button("추천 받기"):
    recommended_song = random.choice(songs_by_genre[genre])
    st.success(f"🎉 추천 곡: {recommended_song}")
else:
    st.info("장르를 선택하고 '추천 받기' 버튼을 눌러주세요.")
