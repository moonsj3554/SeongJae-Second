import streamlit as st

# 연도별 멜론 연간 Top 10 데이터
melon_chart = {
    2020: [
        "1. ZICO – Any Song",
        "2. CHANGMO – METEOR",
        "3. Cho Jungseok – Aloha",
        "4. Jang Beomjune – Your Shampoo Scent",
        "5. IU – eight (Prod. SUGA)",
        "6. IU – Blueming",
        "7. Noel – Late Night",
        "8. Gaho – Start Over",
        "9. BTS (feat. Halsey) – Boy With Luv",
        "10. Red Velvet – Psycho",
    ],
    2021: [
        "1. IU – Celebrity",
        "2. Brave Girls – Rollin’",
        "3. BTS – Dynamite",
        "4. Justin Bieber – Peaches",
        "5. IU – LILAC",
        "6. IU – Hold My Hand",
        "7. BTS – Butter",
        "8. BTS – Permission to Dance",
        "9. BTS – Life Goes On",
        "10. BTS – Boy With Luv",
    ],
    2022: [
        "1. IVE – LOVE DIVE",
        "2. (G)I‑DLE – TOMBOY",
        "3. Kim Minseok – DrunKen Confession",
        "4. MeloMance – Love, Maybe",
        "5. Lim Youngwoong – Love Always Runs Away",
        "6. IVE – ELEVEN",
        "7. BIGBANG – Still Life",
        "8. GyeongseoYeji & Jeon Gunho – If you lovingly call my name",
        "9. PSY (feat. SUGA) – That That",
        "10. BIG Naughty (feat. 10CM) – Beyond Love",
    ],
    2023: [
        "1. NewJeans – Ditto",
        "2. NewJeans – Hype Boy",
        "3. IVE – I AM",
        "4. YOUNHA – Event Horizon",
        "5. AKMU – Love Lee",
        "6. NMIXX – Love Me Like This",
        "7. NewJeans – OMG",
        "8. Crush (feat. j‑hope) – Rush Hour",
        "9. Jungkook – Seven",
        "10. Lim Jae‑hyun – Heaven (2023)",
    ],
    2024: [
        "1. TWS – Plot Twist",
        "2. (G)I‑DLE – Fate",
        "3. aespa – Supernova",
        "4. IU – Love wins all",
        "5. DAY6 – Time of Our Life",
        "6. Lim Jae‑hyun – Rhapsody of Sadness",
        "7. DAY6 – You Were Beautiful",
        "8. ILLIT – Magnetic",
        "9. Lee Chang‑sub – Heavenly fate",
        "10. QWER – T.B.H",
    ]
}

# 웹앱 제목
st.title("🎵 멜론 연간 Top 10 (2020 ~ 2024)")

# 연도 선택
year = st.selectbox("연도를 선택하세요:", list(melon_chart.keys()))

# 차트 출력
st.subheader(f"{year}년 멜론 연간 Top 10")
for song in melon_chart[year]:
    st.write(song)
