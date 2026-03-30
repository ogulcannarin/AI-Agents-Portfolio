import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from streamlit_folium import st_folium
import folium
from graph import app
import json

# Sayfa Ayarları
st.set_page_config(page_title="Otonom Şehir Kaşifi", page_icon="🌍", layout="wide")

st.title("🌍 Otonom Şehir Kaşifi")
st.markdown("""
Bu uygulama, **AI Ajanlarını** kullanarak istediğiniz şehirdeki en iyi mekanları bulur ve haritaya işler.
""")

# Sidebar
with st.sidebar:
    st.header("Keşif Ayarları")
    city = st.text_input("Şehir/İlçe İsmi:", placeholder="Örn: Kadıköy, İstanbul")

    st.write("Arama Seçenekleri:")
    show_museums = st.checkbox("Müzeleri Bul", value=True)
    show_food = st.checkbox("Yemek Yerlerini Bul", value=True)

    search_button = st.button("Ajanları Çalıştır! 🚀")

# Ana Mantık
if search_button:
    if not city:
        st.error("Lütfen bir şehir ismi girin!")
    else:
        # checkbox → interest map
        interests = []
        if show_museums:
            interests.append("museum")
        if show_food:
            interests.append("restaurant")

        if not interests:
            st.warning("En az bir kategori seçmelisin!")
        else:
            with st.spinner(f"Ajanlar {city} sokaklarında geziniyor..."):
                initial_state = {
                    "location": city,
                    "interests": interests,
                    "found_places": []
                }

                final_output = app.invoke(initial_state)
                # Sonuçları state içine kaydet
                st.session_state['final_output'] = final_output
                st.session_state['searched_city'] = city

if 'final_output' in st.session_state:
    final_output = st.session_state['final_output']
    searched_city = st.session_state['searched_city']
    places = final_output.get("found_places", [])

    if places:
        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader(f"📍 {searched_city} Haritası")

            m = folium.Map(
                location=[places[0]['lat'], places[0]['lon']],
                zoom_start=14,
                tiles="cartodbpositron"
            )

            for p in places:
                category = p.get('category', '').lower()

                if "museum" in category:
                    color = "red"
                elif "restaurant" in category:
                    color = "blue"
                else:
                    color = "green"

                folium.Marker(
                    [p['lat'], p['lon']],
                    popup=p['name'],
                    tooltip=p['name'],
                    icon=folium.Icon(color=color)
                ).add_to(m)

            st_folium(m, width=800, height=500)

        with col2:
            st.subheader("📊 Mekan Listesi")

            for p in places:
                category = p.get('category', '').lower()

                if "museum" in category:
                    icon = "🏛️"
                elif "restaurant" in category:
                    icon = "🍴"
                else:
                    icon = "📍"

                st.write(f"{icon} **{p['name']}**")
                st.caption(p.get('address', '')[:60] + "...")

        # JSON güvenli gösterim
        with st.expander("Geliştirici İçin JSON Verisi"):
            st.json(final_output.get("final_json", {}))

    else:
        st.warning("Ajanlar uygun mekan bulamadı.")

st.info("İpucu: OpenStreetMap verileri kullanılıyor.")