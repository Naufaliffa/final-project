import streamlit as st
import requests

# API endpoint
API_URL = "http://127.0.0.1:8000/predict"

# Page name (At browser tab)
st.set_page_config(page_title="Employee Churn App - TalentaHub", page_icon="📊")

# Initialize session state for history
if "history" not in st.session_state:
    st.session_state.history = []
if "page" not in st.session_state:
    st.session_state.page = "Prediction"

# Custom styling
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            padding: 0;
        }
        .element-container:nth-child(1) label, .element-container:nth-child(2) label {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        .block-container {
            padding-top: 2rem;
        }
        [data-testid="stSidebar"] button {
            background-color: transparent !important;
            color: white !important;
            text-align: left !important;
            font-size: 16px;
        }
        [data-testid="stSidebar"] button:hover {
            background-color: #333 !important;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation as pressable text
st.sidebar.markdown("### Navigation")
pages = ["Prediction", "Previous Predictions"]
for page in pages:
    if st.sidebar.button(page):
        st.session_state.page = page

selected_page = st.session_state.page

if selected_page == "Prediction":
    st.title("🔮 Churn Prediction")

    with st.form("prediction_form"):
        target = st.number_input("🎯 Target Achievement (%)", min_value=0, format="%d")
        satisfaction = st.slider("😊 Job Satisfaction (1-5)", min_value=0.0, max_value=5.0, step=0.01)
        manager = st.slider("👔 Manager Support Score (1-5)", min_value=0.0, max_value=5.0, step=0.01)
        hours = st.number_input("⏱️ Working Hours per Week", min_value=0, format="%d")
        distance = st.number_input("🚗 Distance to Office (km)", min_value=0, format="%d")

        submitted = st.form_submit_button("Predict")

    if submitted:
        payload = {
            "Target": target,
            "Satisfaction": satisfaction,
            "Manager": manager,
            "Hours": hours,
            "Distance": distance
        }

        try:
            response = requests.post(API_URL, json=payload)
            result = response.json()

            probability = result["probability"]
            risk = result["risk"]
            suggestion = result["suggestion"]

            # Color coding based on risk
            if probability < 0.33:
                prob_color = "#1f5c2e"
                risk_color = "#1f5c2e"
            elif probability < 0.66:
                prob_color = "#8a6d00"
                risk_color = "#8a6d00"
            else:
                prob_color = "#7a1f1f"
                risk_color = "#7a1f1f"

            # Display results with emphasis
            st.markdown(f"""
                <div style='font-size: 26px; padding: 10px; background-color: {prob_color}; color: white; border-radius: 5px;'>
                    <strong>Churn Probability:</strong> {probability:.0%}
                </div>
                <div style='font-size: 26px; padding: 10px; background-color: {risk_color}; color: white; border-radius: 5px;'>
                    <strong>Risk Group:</strong> {risk}
                </div>
                <div style='font-size: 22px; padding: 10px; background-color: #1e1e1e; color: white; border-radius: 5px;'>
                    🧠 <strong>Suggestion:</strong> {suggestion}
                </div>
            """, unsafe_allow_html=True)

            # Store result in session history
            st.session_state.history.append({
                "input": payload,
                "probability": probability,
                "risk": risk,
                "suggestion": suggestion
            })

        except Exception as e:
            st.error(f"Prediction failed: {e}")

elif selected_page == "Previous Predictions":
    st.title("⏱️ Previous Predictions")

    if not st.session_state.history:
        st.warning("No predictions made yet.")
    else:
        for i, record in enumerate(reversed(st.session_state.history), start=1):
            input_data = record["input"]
            feature_names = list(input_data.keys())
            feature_values = list(input_data.values())

            probability = record['probability']
            risk = record['risk']

            # Color coding for table
            if probability < 0.33:
                prob_color = "#1f5c2e"
                risk_color = "#1f5c2e"
            elif probability < 0.66:
                prob_color = "#8a6d00"
                risk_color = "#8a6d00"
            else:
                prob_color = "#7a1f1f"
                risk_color = "#7a1f1f"

            table_html = f"""
            <div style='margin-top: 20px;'>
                <h4>Prediction #{len(st.session_state.history) - i + 1}</h4>
                <table style='width: 100%; border-collapse: collapse;'>
                    <tr style='background-color: #282828; color: white;'>
                        {''.join(f'<th style="padding: 8px; border: 1px solid #ccc;">{col}</th>' for col in feature_names)}
                    </tr>
                    <tr>
                        {''.join(f'<td style="padding: 8px; border: 1px solid #ccc;">{val}</td>' for val in feature_values)}
                    </tr>
                    <tr>
                        <td style="padding: 8px; border: 1px solid #ccc; background-color: {prob_color}; color: white;" colspan="{len(feature_names)//2}"><strong>Probability:</strong> {probability:.0%}</td>
                        <td style="padding: 8px; border: 1px solid #ccc; background-color: {risk_color}; color: white;" colspan="{len(feature_names) - len(feature_names)//2}"><strong>Risk Group:</strong> {risk}</td>
                    </tr>
                    <tr>
                        <td colspan="{len(feature_names)}" style="padding: 8px; border: 1px solid #ccc;"><strong>Suggestion:</strong> {record['suggestion']}</td>
                    </tr>
                </table>
            </div>
            <hr>
            """

            st.markdown(table_html, unsafe_allow_html=True)
