import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 HR Analytics Dashboard")
st.write("Employee Data Analysis and HR Insights")

# Load Data
df = pd.read_csv("HR_Analytics.csv")

# =========================
# SIDEBAR FILTERS
# =========================

st.sidebar.header("🔎 Filters")

data = df.copy()

# Department Filter
if "Department" in df.columns:

    departments = ["All"] + list(df["Department"].dropna().unique())

    department = st.sidebar.selectbox(
        "Department",
        departments
    )

    if department != "All":
        data = data[data["Department"] == department]


# Gender Filter
if "Gender" in df.columns:

    genders = ["All"] + list(df["Gender"].dropna().unique())

    gender = st.sidebar.selectbox(
        "Gender",
        genders
    )

    if gender != "All":
        data = data[data["Gender"] == gender]


# =========================
# KPI SECTION
# =========================

st.subheader("📌 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

# Total Employees
with col1:
    st.metric(
        "Total Employees",
        len(data)
    )


# Average Age
with col2:
    if "Age" in data.columns:
        avg_age = data["Age"].mean()

        st.metric(
            "Average Age",
            f"{avg_age:.1f}"
        )


# Average Salary
with col3:
    if "MonthlyIncome" in data.columns:
        avg_salary = data["MonthlyIncome"].mean()

        st.metric(
            "Average Salary",
            f"₹{avg_salary:,.0f}"
        )


# Attrition Rate
with col4:
    if "Attrition" in data.columns:

        total = len(data)

        attrition_yes = (
            data["Attrition"]
            .astype(str)
            .str.lower()
            .eq("yes")
            .sum()
        )

        if total > 0:
            attrition_rate = (
                attrition_yes / total
            ) * 100
        else:
            attrition_rate = 0

        st.metric(
            "Attrition Rate",
            f"{attrition_rate:.2f}%"
        )


# =========================
# EMPLOYEE DATA
# =========================

st.subheader("👨‍💼 Employee Data")

st.dataframe(
    data,
    use_container_width=True
)


# =========================
# DEPARTMENT ANALYSIS
# =========================

if "Department" in data.columns:

    st.subheader("🏢 Employees by Department")

    department_count = data["Department"].value_counts()

    st.bar_chart(
        department_count
    )


# =========================
# GENDER ANALYSIS
# =========================

if "Gender" in data.columns:

    st.subheader("👥 Employees by Gender")

    gender_count = data["Gender"].value_counts()

    st.bar_chart(
        gender_count
    )


# =========================
# ATTRITION ANALYSIS
# =========================

if "Attrition" in data.columns:

    st.subheader("📉 Attrition Analysis")

    attrition_count = data["Attrition"].value_counts()

    st.bar_chart(
        attrition_count
    )


# =========================
# JOB ROLE ANALYSIS
# =========================

if "JobRole" in data.columns:

    st.subheader("💼 Employees by Job Role")

    jobrole_count = data["JobRole"].value_counts()

    st.bar_chart(
        jobrole_count
    )


# =========================
# SALARY ANALYSIS
# =========================

if "MonthlyIncome" in data.columns:

    st.subheader("💰 Salary Analysis")

    salary_data = data[
        "MonthlyIncome"
    ].sort_values()

    st.line_chart(
        salary_data
    )


# =========================
# AGE ANALYSIS
# =========================

if "Age" in data.columns:

    st.subheader("🎂 Age Distribution")

    age_data = data["Age"].value_counts().sort_index()

    st.bar_chart(
        age_data
    )


# =========================
# OVERTIME ANALYSIS
# =========================

if "OverTime" in data.columns:

    st.subheader("⏰ Overtime Analysis")

    overtime_count = data["OverTime"].value_counts()

    st.bar_chart(
        overtime_count
    )


# =========================
# JOB SATISFACTION
# =========================

if "JobSatisfaction" in data.columns:

    st.subheader("😊 Job Satisfaction")

    satisfaction_count = (
        data["JobSatisfaction"]
        .value_counts()
        .sort_index()
    )

    st.bar_chart(
        satisfaction_count
    )


# =========================
# YEARS AT COMPANY
# =========================

if "YearsAtCompany" in data.columns:

    st.subheader("🏢 Years at Company")

    years_count = (
        data["YearsAtCompany"]
        .value_counts()
        .sort_index()
    )

    st.bar_chart(
        years_count
    )


# =========================
# EDUCATION ANALYSIS
# =========================

if "Education" in data.columns:

    st.subheader("🎓 Education Level")

    education_count = (
        data["Education"]
        .value_counts()
        .sort_index()
    )

    st.bar_chart(
        education_count
    )


# =========================
# BUSINESS TRAVEL
# =========================

if "BusinessTravel" in data.columns:

    st.subheader("✈️ Business Travel")

    travel_count = data[
        "BusinessTravel"
    ].value_counts()

    st.bar_chart(
        travel_count
    )


# =========================
# FINAL MESSAGE
# =========================

st.success(
    "HR Analytics Dashboard completed successfully!")
