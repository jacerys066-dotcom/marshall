import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import random

st.title("📊 Visualisasi Graf (Input Node & Edge)")

st.write("Masukkan jumlah node dan edge, lalu graf akan dibuat otomatis.")

# =========================
# INPUT USER
# =========================
num_nodes = st.number_input(
    "Masukkan jumlah node",
    min_value=1,
    max_value=20,
    value=5,
    step=1
)

max_edges = num_nodes * (num_nodes - 1) // 2

num_edges = st.number_input(
    "Masukkan jumlah edge",
    min_value=0,
    max_value=max_edges,
    value=min(4, max_edges),
    step=1
)

# =========================
# BUAT GRAF
# =========================
G = nx.Graph()

# Tambahkan node
nodes = [f"V{i+1}" for i in range(num_nodes)]
G.add_nodes_from(nodes)

# Generate edge secara acak
possible_edges = [(nodes[i], nodes[j]) for i in range(len(nodes)) for j in range(i+1, len(nodes))]
edges = random.sample(possible_edges, num_edges)
G.add_edges_from(edges)

# =========================
# VISUALISASI GRAF
# =========================
st.subheader("Visualisasi Graf")

fig, ax = plt.subplots()
pos = nx.spring_layout(G, seed=42)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2000,
    font_size=10,
    ax=ax
)
st.pyplot(fig)

# =========================
# DERAJAT SIMPUL
# =========================
st.subheader("Derajat Setiap Simpul")

degree_data = dict(G.degree())
df_degree = pd.DataFrame.from_dict(
    degree_data, orient="index", columns=["Derajat"]
)
st.dataframe(df_degree)

# =========================
# MATRIKS KETETANGGAAN
# =========================
st.subheader("Matriks Ketetanggaan")

adj_matrix = nx.to_pandas_adjacency(G)
st.dataframe(adj_matrix)