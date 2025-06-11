import pandas as pd
import streamlit as st
# Streamlit app to display Vision 2030 projects data

# Sample projects from the Vision 2030 Progress Report 2020/21
projects_data = [
    {
        "Project": "Smart Driving License System",
        "Pillar": "Foundations",
        "Sector": "Transport",
        "Status": "Operational",
        "Location": "National",
        "Progress Note": "395,597 smart driving licenses issued"
    },
    {
        "Project": "Naivasha Inland Container Depot Link",
        "Pillar": "Foundations",
        "Sector": "Transport",
        "Status": "Under Construction",
        "Location": "Naivasha",
        "Progress Note": "23.5 km link to the meter gauge railway under development"
    },
    {
        "Project": "Lamu Port (1st Berth)",
        "Pillar": "Foundations",
        "Sector": "Ports",
        "Status": "Operational",
        "Location": "Lamu",
        "Progress Note": "Commissioned and functional as of FY 2020/21"
    },
    {
        "Project": "Digital Literacy Programme (DLP)",
        "Pillar": "Economic",
        "Sector": "Education",
        "Status": "Ongoing",
        "Location": "National",
        "Progress Note": "Over 300 schools equipped with digital devices"
    },
    {
        "Project": "Kipevu Oil Terminal II",
        "Pillar": "Foundations",
        "Sector": "Energy",
        "Status": "Near Completion",
        "Location": "Mombasa",
        "Progress Note": "Progress at 89.6% in FY 2020/21"
    },
    {
        "Project": "Kenya National Digital Master Plan",
        "Pillar": "Economic",
        "Sector": "ICT",
        "Status": "Ongoing",
        "Location": "National",
        "Progress Note": "Implementation of digital infrastructure across the country"
    },
    {
        "Project": "Mombasa Port Development Project",
        "Pillar": "Foundations",
        "Sector": "Ports",
        "Status": "Ongoing",
        "Location": "Mombasa",
        "Progress Note": "Enhancing port capacity and efficiency"
    },
    {
        "Project": "National Optic Fibre Backbone Infrastructure (NOFBI)",
        "Pillar": "Economic",
        "Sector": "ICT",
        "Status": "Operational",
        "Location": "National",
        "Progress Note": "Extending broadband connectivity across the country"
    },
    {
        "Project": "Standard Gauge Railway (SGR) Phase II",
        "Pillar": "Foundations",
        "Sector": "Transport",
        "Status": "Operational",
        "Location": "Nairobi to Naivasha",
        "Progress Note": "Enhancing transport connectivity and efficiency"
    },
    {
        "Project": "Kenya Vision 2030 Delivery Secretariat",
        "Pillar": "Governance",
        "Sector": "Administration",
        "Status": "Ongoing",
        "Location": "National",
        "Progress Note": "Coordinating implementation of Vision 2030 projects"

    }
]

df = pd.DataFrame(projects_data)
#df.to_csv("vision2030_sample.csv", index=False)
# Display the first few rows of the DataFrame
#print("Sample projects data for Vision 2030:")
#print(df.head())

st.set_page_config(page_title="Vision 2030 Projects Dashboard", layout="wide")
st.title("Vision 2030 Projects Progress 2020/2021 Dashboard")
st.write("This dashboard displays key projects under the Vision 2030 initiative, focusing on infrastructure development across various sectors. The data was last updated in 2021/2022.")
st.dataframe(df)

# Add a sidebar for navigation
with st.sidebar:
    st.header("📊 Filter Projects")
    st.write("Use this sidebar to navigate through the Vision 2030 projects data.")
    st.write("You can filter projects by Pillar, Sector, or Status using the options below.")
    selected_pillars = st.multiselect(
        "Select Pillars",
        options=["All"] + df["Pillar"].unique().tolist(),
        default=["All"]
    )
    selected_status = st.multiselect(
        "Select Status",
        options=["All"] + df["Status"].unique().tolist(),
        default=["All"]
    )

    # Filter options
    #pillar_filter = st.selectbox("Select Pillar", ["All"] + df["Pillar"].unique().tolist())
    #sector_filter = st.selectbox("Select Sector", ["All"] + df["Sector"].unique().tolist())
    #status_filter = st.selectbox("Select Status", ["All"] + df["Status"].unique().tolist())

    filtered_df = df[
        (df["Pillar"].isin(selected_pillars if "All" not in selected_pillars else df["Pillar"])) &
        (df["Status"].isin(selected_status if "All" not in selected_status else df["Status"]))
    ]

    
    st.dataframe(filtered_df, use_container_width=True)

st.subheader("📈 Project by sector")
sector_counts = filtered_df["Sector"].value_counts()
st.bar_chart(sector_counts)

st.subheader("📊 Project Status Distribution")
status_counts = filtered_df["Status"].value_counts()
st.bar_chart(status_counts)

with st.expander("📚 About Vision 2030"):
    for i, row in filtered_df.iterrows():
       st.markdown(f"**Project:** {row['Progress Note']}")
