import streamlit as st
import plotly.express as px
from fraud_backend import check_number, classify_risk, report_number, load_database

st.set_page_config(page_title="TrustPay", layout="wide")

st.title("💳 TrustPay - Spam & Fraud Detector")
st.caption("Truecaller-style protection for UPI users")

# ---------------- SIDEBAR ----------------

st.sidebar.header("🔍 Search Phone Number")

phone = st.sidebar.text_input("Enter Phone Number")

if st.sidebar.button("Check Number"):

    result = check_number(phone)

    if result is None:

        st.success("✅ No fraud reports found. Number is SAFE.")

    else:

        status = classify_risk(result["risk_score"])

        col1, col2 = st.columns(2)

        with col1:
            st.subheader(f"Status: {status}")
            st.metric("Risk Score", f"{result['risk_score']}%")
            st.metric("Reports", result["reports"])
            st.write("Fraud Tag:", result["fraud_tag"])

        with col2:

            fig = px.pie(
                values=[result["risk_score"], 100-result["risk_score"]],
                names=["Risk", "Safe"],
                hole=0.5
            )

            st.plotly_chart(fig, use_container_width=True)


# ---------------- REPORT ----------------

st.divider()
st.subheader("🚨 Report a Fraud Number")

report = st.text_input("Enter number to report")

if st.button("Report Now"):

    report_number(report)

    st.success("Number reported successfully!")


# ---------------- DASHBOARD ----------------

st.divider()
st.subheader("📊 Fraud Analytics")

df = load_database()

col3, col4 = st.columns(2)

with col3:
    fig = px.histogram(df, x="risk_score", title="Risk Score Distribution")
    st.plotly_chart(fig, use_container_width=True)

with col4:
    top = df.sort_values(by="reports", ascending=False).head(10)

    fig2 = px.bar(top,
                  x="phone_number",
                  y="reports",
                  title="Most Reported Numbers")

    st.plotly_chart(fig2, use_container_width=True)


st.divider()
st.subheader("📁 Database Preview")
st.dataframe(df.head(50), use_container_width=True)
