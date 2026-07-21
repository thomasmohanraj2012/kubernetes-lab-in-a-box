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
    # st.metric("Active Labs", "1")
    # st.metric("XP Earned", "0")
    st.metric("🎯 Labs Completed", "1")

with col2:
    # st.metric("Pods Running", "1")
    # st.metric("Labs Completed", "0")
    st.metric("🏆 XP Earned", "10")

with col3:
    # st.metric("Progress", "0%")
    st.metric("🎖️Badges", "0")

with col4:
    # st.metric("Score", "0")
    # st.metric("Progress", "0%")
    st.metric("📈 Progress", "10%")

st.subheader("🗺️ Kubernetes Learning Path")

roadmap = {
    "Pod Fundamentals": "✅",
    "Deployments": "⬜",
    "Services": "⬜",
    "Ingress": "⬜",
    "Storage": "⬜",
    "Troubleshooting": "⬜"
}

for lab_name, status in roadmap.items():
    st.write(f"{status} {lab_name}")

# ==========================
# XP DASHBOARD
# ==========================

st.subheader("🏆 Kubernetes Journey")

col1, col2 = st.columns(2)

with col1:
    st.progress(10)

    st.info("""
Current Rank: 🌱 Kubernetes Beginner

XP Earned: 10

Next Badge:
☸️ Pod Explorer
""")

# with col2:
#     st.success("""
# 🎯 Current Mission

# Complete Pod Fundamentals Lab

# Reward:
# +50 XP
# +1 Badge
# """)

# st.divider()

# # POD LAB CARD

with col2:
    st.success("""
🎯 Current Mission

Complete Pod Fundamentals Lab

Reward:
+50 XP
+1 Badge
""")

# ==================================================
# AVAILABLE LABS
# ==================================================

st.divider()

st.subheader("🚀 Available Labs")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
📦 Pod Fundamentals

Difficulty: Easy

Duration: 15 mins

Reward: +50 XP
""")

with col2:
    st.warning("""
🚀 Deployments

Difficulty: Medium

Duration: 20 mins

Reward: +75 XP
""")

with col3:
    st.success("""
🌐 Services

Difficulty: Medium

Duration: 25 mins

Reward: +100 XP
""")

col4, col5, col6 = st.columns(3)

with col4:
    st.info("""
🔀 Ingress

Difficulty: Hard

Duration: 30 mins

Reward: +150 XP
""")

with col5:
    st.warning("""
💾 Storage

Difficulty: Hard

Duration: 35 mins

Reward: +150 XP
""")

with col6:
    st.success("""
🛠 Troubleshooting

Difficulty: Expert

Duration: 45 mins

Reward: +200 XP
""")

st.divider()

st.subheader("📚 Current Active Lab")

col1, col2 = st.columns([2,1])

with col1:
    st.info("""
### 📦 Pod Fundamentals Lab

Learn Kubernetes Pods from scratch.

Topics Covered:

✅ Create Pods

✅ Describe Pods

✅ Logs

✅ Port Forward

✅ Delete Pods
""")

with col2:
    st.metric("XP Reward", "50")
    st.metric("Difficulty", "Easy")
    st.metric("Duration", "15 min")

# # POD LAB CARD

# st.markdown("""
# <div style="
# background:#1E293B;
# padding:20px;
# border-radius:12px;
# border-left:5px solid #3B82F6;
# ">

# <h3 style="color:white;">
# 🚀 Lab Action
# </h3>

# <p style="color:#CBD5E1;">
# Learn how Pods work in Kubernetes.
# </p>

# </div>
# """, unsafe_allow_html=True)

# st.write("")

# =====================================
# LAB ACTIONS
# =====================================

st.subheader("🚀 Lab Actions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button(
        "🚀 Launch Lab",
        key="launch_lab_btn",
        use_container_width=True
    ):
        st.success("Lab Started!")

with col2:
    if st.button(
        "✅ Validate Lab",
        key="validate_lab",
        use_container_width=True
    ):
        st.success("Validation Complete!")

with col3:
    if st.button(
        "🗑 Destroy Lab",
        key="destroy_lab_top",
        use_container_width=True
    ):
        st.warning("Lab Destroyed!")

st.write("")

# OBJECTIVES

st.subheader("✅ Learning Objectives")

st.success("Create Pods")
st.success("Describe Pods")
st.success("View Logs")
st.success("Port Forward Applications")
st.success("Delete Pods")

st.write("")

# SIDEBAR NAVIGATION

st.sidebar.title("🚀 Lab Modules")

lab = st.sidebar.radio(
    "Select Lab",
    [
        "Pod Fundamentals",
        "Deployments",
        "Services",
        "Ingress",
        "Storage",
        "Troubleshooting"
    ]
)

st.header(f"📦 {lab}")

# BUTTON

if st.button(
    "🚀 Launch Pod Lab",
    key="launch_pod_lab",
    use_container_width=True
):
    st.success("Pod Lab Launched!")

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
    key="destroy_lab_bottom",
    use_container_width=True
)