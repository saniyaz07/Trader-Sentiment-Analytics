import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Trader Dashboard", layout="wide")

# ---------------- TITLE ----------------
st.title("📊 Trader Performance vs Market Sentiment")
st.markdown("Analyze trading behavior, sentiment impact, and trader performance 🚀")

# ---------------- LOAD DATA ----------------
try:
    df = pd.read_csv("final_data.csv")
    
    # Ensure date is properly formatted
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date']).dt.date

except FileNotFoundError:
    st.error("⚠️ Please ensure 'final_data.csv' is uploaded to the Colab files section.")
    st.stop()

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("🔎 Filters")

# Sentiment filter (Using your 'classification' column)
if 'classification' in df.columns:
    sentiment_list = ["All"] + list(df['classification'].dropna().unique())
    selected_sentiment = st.sidebar.selectbox("Market Sentiment", sentiment_list)
    if selected_sentiment != "All":
        df = df[df['classification'] == selected_sentiment]

# ---------------- METRICS ----------------
st.subheader("📌 Key Metrics")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total PnL", f"${round(df['pnl'].sum(), 2)}")
col2.metric("Win Rate", f"{round(df['win'].mean() * 100, 1)}%")
col3.metric("Total Trades Logged", len(df))
col4.metric("Avg PnL per Trade", f"${round(df['pnl'].mean(), 2)}")

# ---------------- PNL TREND ----------------
st.subheader("📈 Daily PnL Over Time")
# Grouping by your 'date' column
pnl_time = df.groupby('date')['pnl'].sum()
st.line_chart(pnl_time)

# ---------------- CLUSTER PLOT ----------------
st.subheader("🧠 Trader Segmentation")

# We aggregate by account to get one dot per trader. 
# Since trade_count is repeated in your rows, we just take the first one.
trader_stats = df.groupby('account').agg({
    'pnl': 'sum',
    'trade_count': 'first',
    'cluster_name': 'first'
}).reset_index()

fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(
    data=trader_stats,
    x='trade_count',
    y='pnl',
    hue='cluster_name',
    palette='viridis',
    ax=ax
)
plt.title("Trader Segments (PnL vs Trade Volume)")
plt.xlabel("Total Trade Count")
plt.ylabel("Cumulative PnL")
st.pyplot(fig)

# ---------------- SENTIMENT ANALYSIS ----------------
st.subheader("📈 Sentiment vs PnL")
sentiment_pnl = df.groupby('classification')['pnl'].mean().reset_index()

fig4, ax4 = plt.subplots(figsize=(6, 4))
sns.barplot(data=sentiment_pnl, x='classification', y='pnl', ax=ax4, palette='coolwarm')
ax4.set_ylabel("Average PnL per Trade")
ax4.set_xlabel("Market Sentiment")
st.pyplot(fig4)

# ---------------- WIN / LOSS ----------------
st.subheader("🎯 Win vs Loss Distribution")
fig2, ax2 = plt.subplots(figsize=(5, 3))
sns.countplot(x='win', data=df, ax=ax2, palette='Set2')
ax2.set_xticklabels(['Loss (0)', 'Win (1)'])
st.pyplot(fig2)

# ---------------- TOP TRADERS ----------------
st.subheader("🏆 Top 10 Traders")
top_traders = df.groupby('account')['pnl'].sum().sort_values(ascending=False).head(10)
st.dataframe(top_traders)

# ---------------- INSIGHTS & RISK ----------------
st.subheader("💡 Insights & Risk")
max_loss = df['pnl'].min()
max_profit = df['pnl'].max()

st.write(f"🔻 **Maximum Single Trade Loss:** ${round(max_loss, 2)}")
st.write(f"🔺 **Maximum Single Trade Profit:** ${round(max_profit, 2)}")

best_sentiment = df.groupby('classification')['pnl'].mean().idxmax()
st.info(f"Traders showed the highest average performance during **{best_sentiment}** market conditions.")

# ---------------- DOWNLOAD ----------------
st.divider()
st.subheader("⬇️ Download Current View")
st.download_button(
    "Download Filtered Data",
    df.to_csv(index=False),
    file_name="filtered_trader_data.csv"
)
