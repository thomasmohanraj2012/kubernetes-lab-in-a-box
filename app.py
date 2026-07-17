import streamlit as st

st.set_page_config(
    page_title="Kubernetes Lab in a Box",
    page_icon="🚀",
    layout="wide"
)

# HERO BANNER

st.markdown("""
<div style="
padding:25px;
border-radius:15px;
background:linear-gradient(135deg,#0F172A,#1E3A8A);
text-align:center;
">

<h1 style="color:white;">
🚀 Kubernetes Lab in a Box
</h1>

<p style="color:#CBD5E1;">
Learn Kubernetes Through Hands-On Labs
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# KPI SECTION

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("Active Labs", "1")

with col2:
    st.metric("Pods Running", "1")

with col3:
    st.metric("Progress", "0%")

with col4:
    st.metric("Score", "0")

st.divider()

# POD LAB CARD

st.markdown("""
<div style="
background:#1E293B;
padding:20px;
border-radius:12px;
border-left:5px solid #3B82F6;
">

<h3 style="color:white;">
📦 Pod Fundamentals Lab
</h3>

<p style="color:#CBD5E1;">
Learn how Pods work in Kubernetes.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# OBJECTIVES

st.subheader("✅ Learning Objectives")

st.success("Create Pods")
st.success("Describe Pods")
st.success("View Logs")
st.success("Port Forward Applications")
st.success("Delete Pods")

st.write("")

# BUTTON

if st.button(
    "🚀 Launch Pod Lab",
    use_container_width=True
):
    st.success("Pod Lab Launched!")

st.divider()

# COMMANDS

st.subheader("💻 Lab Commands")

st.code("""
kubectl get pods

kubectl describe pod nginx-pod

kubectl logs nginx-pod
""")

st.divider()

# CHALLENGE

st.subheader("🎯 Challenge")

st.warning("""
Find the IP Address of nginx-pod

Reward: +10 XP
""")

st.progress(0)

st.divider()

st.button(
    "🗑 Destroy Lab",
    use_container_width=True
)