import pandas as pd

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
df.to_csv("vision2030_sample.csv", index=False)
# Display the first few rows of the DataFrame
df.head()
