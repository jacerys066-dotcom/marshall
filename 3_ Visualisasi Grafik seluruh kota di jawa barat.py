import streamlit as st
import networkx as nx
import folium
from streamlit_folium import st_folium

st.title("🗺️ Graf Seluruh Kota & Kabupaten Jawa Barat")

# ==================================
# DATA KOTA & KABUPATEN JAWA BARAT
# ==================================
cities = {
    # KOTA
    "Kota Bandung": (-6.9175, 107.6191),
    "Kota Bekasi": (-6.2383, 106.9756),
    "Kota Bogor": (-6.5971, 106.8060),
    "Kota Depok": (-6.4025, 106.7942),
    "Kota Cimahi": (-6.8841, 107.5413),
    "Kota Cirebon": (-6.7372, 108.5506),
    "Kota Sukabumi": (-6.9277, 106.9298),
    "Kota Tasikmalaya": (-7.3274, 108.2207),
    "Kota Banjar": (-7.3707, 108.5343),

    # KABUPATEN
    "Kab. Bandung": (-7.0186, 107.6856),
    "Kab. Bandung Barat": (-6.8320, 107.4880),
    "Kab. Bekasi": (-6.2645, 107.1407),
    "Kab. Bogor": (-6.4797, 106.8250),
    "Kab. Ciamis": (-7.3321, 108.3533),
    "Kab. Cianjur": (-6.8223, 107.1425),
    "Kab. Cirebon": (-6.6899, 108.4750),
    "Kab. Garut": (-7.2166, 107.9015),
    "Kab. Indramayu": (-6.3260, 108.3200),
    "Kab. Karawang": (-6.3054, 107.3000),
    "Kab. Kuningan": (-6.9756, 108.4831),
    "Kab. Majalengka": (-6.8360, 108.2270),
    "Kab. Pangandaran": (-7.6833, 108.6500),
    "Kab. Purwakarta": (-6.5569, 107.4433),
    "Kab. Subang": (-6.5714, 107.7587),
    "Kab. Sukabumi": (-6.8649, 106.8300),
    "Kab. Sumedang": (-6.8580, 107.9230),
    "Kab. Tasikmalaya": (-7.3506, 108.2172)
}

# ==================================
# GRAF & KONEKSI (JARAK KM - PERKIRAAN)
# ==================================
edges = [
    ("Kota Bandung", "Kab. Bandung", 20),
    ("Kota Bandung", "Kab. Bandung Barat", 15),
    ("Kab. Bandung Barat", "Kab. Cianjur", 45),
    ("Kab. Cianjur", "Kab. Sukabumi", 60),
    ("Kab. Sukabumi", "Kota Sukabumi", 10),
    ("Kab. Sukabumi", "Kab. Bogor", 70),
    ("Kab. Bogor", "Kota Bogor", 5),
    ("Kab. Bogor", "Kota Depok", 20),
    ("Kota Depok", "Kota Bekasi", 25),
    ("Kota Bekasi", "Kab. Bekasi", 10),
    ("Kab. Bekasi", "Kab. Karawang", 30),
    ("Kab. Karawang", "Kab. Purwakarta", 35),
    ("Kab. Purwakarta", "Kab. Subang", 40),
    ("Kab. Subang", "Kab. Indramayu", 60),
    ("Kab. Indramayu", "Kab. Cirebon", 45),
    ("Kab. Cirebon", "Kota Cirebon", 5),
    ("Kab. Cirebon", "Kab. Kuningan", 35),
    ("Kab. Kuningan", "Kab. Majalengka", 25),
    ("Kab. Majalengka", "Kab. Sumedang", 40),
    ("Kab. Sumedang", "Kota Bandung", 30),
    ("Kab. Sumedang", "Kab. Tasikmalaya", 70),
    ("Kab. Tasikmalaya", "Kota Tasikmalaya", 10),
    ("Kab. Tasikmalaya", "Kab. Garut", 55),
    ("Kab. Garut", "Kab. Ciamis", 65),
    ("Kab. Ciamis", "Kota Banjar", 20),
    ("Kab. Ciamis", "Kab. Pangandaran", 60)
]

G = nx.Graph()
G.add_weighted_edges_from(edges)

# ==================================
# PILIH KOTA ASAL & TUJUAN
# ==================================
col1, col2 = st.columns(2)
with col1:
    start = st.selectbox("Kota / Kabupaten Asal", cities.keys())
with col2:
    end = st.selectbox("Kota / Kabupaten Tujuan", cities.keys())

# ==================================
# RUTE TERPENDEK
# ==================================
if start != end:
    path = nx.shortest_path(G, start, end, weight="weight")
    distance = nx.shortest_path_length(G, start, end, weight="weight")

    st.success("➡️ Rute Terpendek:")
    st.write(" → ".join(path))
    st.info(f"📏 Total Jarak: {distance} km")

# ==================================
# PETA FOLIUM
# ==================================
m = folium.Map(location=[-6.9, 107.6], zoom_start=8)

# Marker kota/kabupaten
for city, coord in cities.items():
    folium.CircleMarker(
        location=coord,
        radius=5,
        popup=city,
        fill=True
    ).add_to(m)

# Garis koneksi
for u, v, w in edges:
    folium.PolyLine(
        [cities[u], cities[v]],
        tooltip=f"{u} ↔ {v} ({w} km)"
    ).add_to(m)

st_folium(m, width=900, height=550)