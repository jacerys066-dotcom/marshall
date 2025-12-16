import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import random
import math
import folium
from folium.plugins import AntPath
from streamlit_folium import st_folium

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="West Java Graph Visualization",
    layout="wide"
)

# =========================
# HELPER FUNCTION
# =========================
def haversine(coord1, coord2):
    R = 6371  # Earth radius (km)
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2)**2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))

# =========================
# SIDEBAR
# =========================
st.sidebar.title("📌 Navigation")
menu = st.sidebar.radio(
    "Select Page",
    [
        "Home",
        "Profile",
        "Random Graph",
        "West Java Graph Visualization",
        "About"
    ]
)

# =========================
# HOME
# =========================
if menu == "Home":
    st.markdown(
        "<h1 style='text-align:center;'>🌍 Graph & Route Visualization</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align:center;'>Professional graph visualization using Streamlit, NetworkX & Folium</p>",
        unsafe_allow_html=True
    )

# =========================
# PROFILE
# =========================
elif menu == "Profile":
    st.title("👤 Profile")

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(
            "https://raw.githubusercontent.com/jacerys066-dotcom/marshall/fda35c750e15b5c3efb175dcad73aa74d68e938b/foto_profil.png",
            width=200
        )

    with col2:
        st.subheader("Name")
        st.write("Marshall Ramdhani")
        st.subheader("Field")
        st.write("Actuarial Science")

# =========================
# RANDOM GRAPH
# =========================
elif menu == "Random Graph":
    st.title("📊 Random Graph Visualization")

    nodes = st.slider("Number of Nodes", 2, 20, 6)
    edges = st.slider("Number of Edges", 1, nodes * (nodes - 1) // 2, nodes + 2)

    G = nx.gnm_random_graph(nodes, edges, seed=42)

    fig, ax = plt.subplots(figsize=(6, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="#6A5ACD", node_size=2000)
    st.pyplot(fig)

# =========================
# WEST JAVA GRAPH
# =========================
elif menu == "West Java Graph Visualization":
    st.title("🗺️ West Java Cities & Regencies Graph")

    cities = {
        "Bandung City": (-6.9175, 107.6191),
        "Bekasi City": (-6.2383, 106.9756),
        "Bogor City": (-6.5971, 106.8060),
        "Depok City": (-6.4025, 106.7942),
        "Cimahi City": (-6.8841, 107.5413),
        "Cirebon City": (-6.7372, 108.5506),
        "Sukabumi City": (-6.9277, 106.9298),
        "Tasikmalaya City": (-7.3274, 108.2207),
        "Banjar City": (-7.3707, 108.5343),
        "Bandung Regency": (-7.0186, 107.6856),
        "West Bandung Regency": (-6.8320, 107.4880),
        "Bekasi Regency": (-6.2645, 107.1407),
        "Bogor Regency": (-6.4797, 106.8250),
        "Ciamis Regency": (-7.3321, 108.3533),
        "Cianjur Regency": (-6.8223, 107.1425),
        "Cirebon Regency": (-6.6899, 108.4750),
        "Garut Regency": (-7.2166, 107.9015),
        "Indramayu Regency": (-6.3260, 108.3200),
        "Karawang Regency": (-6.3054, 107.3000),
        "Kuningan Regency": (-6.9756, 108.4831),
        "Majalengka Regency": (-6.8360, 108.2270),
        "Pangandaran Regency": (-7.6833, 108.6500),
        "Purwakarta Regency": (-6.5569, 107.4433),
        "Subang Regency": (-6.5714, 107.7587),
        "Sukabumi Regency": (-6.8649, 106.8300),
        "Sumedang Regency": (-6.8580, 107.9230),
        "Tasikmalaya Regency": (-7.3506, 108.2172)
    }

    G = nx.Graph()

    # FULLY CONNECTED GRAPH
    for c1, coord1 in cities.items():
        for c2, coord2 in cities.items():
            if c1 != c2:
                dist = haversine(coord1, coord2)
                G.add_edge(c1, c2, weight=round(dist, 2))

    col1, col2 = st.columns(2)
    start = col1.selectbox("Start Location", cities.keys())
    end = col2.selectbox("Destination", cities.keys())

    path = nx.shortest_path(G, start, end, weight="weight")
    distance = nx.shortest_path_length(G, start, end, weight="weight")

    st.success(f"Shortest Distance: {distance:.2f} km")
    st.write(" ➜ ".join(path))

    # MAP
    m = folium.Map(location=[-6.9, 107.6], zoom_start=8)

    for city, coord in cities.items():
        folium.CircleMarker(
            coord,
            radius=5,
            color="blue",
            fill=True,
            popup=city
        ).add_to(m)

    route_coords = [cities[p] for p in path]
    AntPath(route_coords, color="red", weight=5).add_to(m)

    st_folium(m, width=1200, height=500)

# =========================
# ABOUT
# =========================
elif menu == "About":
    st.title("📖 About This App")
    st.write("""
    **Professional Graph Visualization Application**
    
    Features:
    - Random Graph Visualization
    - Fully Connected West Java Graph
    - Realistic Distance Calculation (Haversine)
    - Automatic Shortest Path
    - Animated Route Mapping

    Built with **Streamlit, NetworkX, and Folium**.
    """)
