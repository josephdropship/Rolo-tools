import streamlit as st

# 頁面設定
st.set_page_config(page_title="Rolo Tools - Product Research for AliExpress", layout="centered")

# 主標題
st.title("Rolo Tools")

# 副標題
st.subheader("Discover Trending Products on AliExpress")

# 工具簡介
st.write("""
🛠️ **What is Rolo Tools?**

Rolo Tools is a lightweight product research assistant designed for **dropshippers**, **content creators**, and **e-commerce explorers** who want to discover winning products on AliExpress fast.

Instead of browsing endlessly, Rolo Tools provides structured insights — and we're just getting started.
""")

# 目前功能
st.write("""
📊 **Current Features:**

- 🔍 Trend analysis on AliExpress
- 🏷️ Product insights & popularity signals
- 🛒 Easy access to product purchase links
""")

# 未來規劃
st.write("""
🚀 **Coming Soon Features:**

- 🎥 TikTok product trend scraping
- 💬 Engagement analytics (likes, saves, shares)
- 🛍️ One-click add to Shopify / WooCommerce
- 📈 AI-driven product recommendation engine

We're building tools that solve real-world problems for modern e-commerce businesses. Stay tuned!
""")

# 裝飾圖片 (你之後可以放品牌 logo 或示意圖)
st.image("https://via.placeholder.com/600x200.png?text=Rolo+Tools+Product+Discovery", caption="Empowering your product research journey 🚀")

# Footer / 聯絡資訊
st.write("---")
st.write("© 2025 Rolo Tools | Built with ❤️ by the Rolo Tools Dev Team")
