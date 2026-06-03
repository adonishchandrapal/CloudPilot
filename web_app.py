import streamlit as st
from cloud_recommender import recommend

st.title("☁️ CloudPilot")
st.subheader("Cloud Infrastructure Recommendation System")

provider_choice = st.selectbox(
    "Select Cloud Provider",
    ["AWS", "Azure", "Google Cloud"]
)

project = st.text_input(
    "Describe your application or project:"
)

users = st.number_input(
    "Expected monthly users:",
    min_value=0,
    step=100
)

if st.button("Generate Recommendation"):

    result = recommend(project, provider_choice)

    if users < 1000:
        scale = "Small"
    elif users < 10000:
        scale = "Medium"
    else:
        scale = "Large"

    st.success("Recommendation Generated!")

    st.write("### CloudPilot Report")
    st.write("**Cloud Provider:**", provider_choice)
    st.write("**Frontend:**", result["frontend"])
    st.write("**Backend:**", result["backend"])
    st.write("**Database:**", result["database"])
    st.write("**Estimated Cost:**", result["cost"])
    st.write("**Scale:**", scale)

    st.write("### Architecture Summary")

    st.code(
        f"{result['frontend']} -> "
        f"{result['backend']} -> "
        f"{result['database']}"
    )
    

    if "terraform" in result:
        st.write("### Terraform Template")

        st.code(
            result["terraform"],
            language="terraform"
        )