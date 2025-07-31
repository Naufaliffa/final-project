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
            color: inherit !important;
            text-align: left !important;
            font-size: 16px;
        }
        [data-testid="stSidebar"] button:hover {
            background-color: rgba(0,0,0,0.1) !important;
            font-weight: bold;
        }

        /* For Light Theme */
        @media (prefers-color-scheme: light) {
            .risk-low    { background-color: #d4edda; color: #155724; }
            .risk-medium { background-color: #fff3cd; color: #856404; }
            .risk-high   { background-color: #f8d7da; color: #721c24; }
            .suggest-box { background-color: #f1f1f1; color: #333333; }
            .table-header { background-color: #e9ecef; color: #212529; }
        }

        /* For Dark Theme */
        @media (prefers-color-scheme: dark) {
            .risk-low    { background-color: #1f5c2e; color: white; }
            .risk-medium { background-color: #8a6d00; color: white; }
            .risk-high   { background-color: #7a1f1f; color: white; }
            .suggest-box { background-color: #1e1e1e; color: white; }
            .table-header { background-color: #444; color: white; }
        }

        .risk-box, .suggest-box {
            font-size: 26px;
            padding: 10px;
            border-radius: 5px;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation as pressable text
# ```
# Bagian ini buat sidebar bisa dipencet
# tanpa ada visual button
# ```
st.sidebar.markdown("### Navigation")
pages = ["Prediction", "Previous Predictions"]
for page in pages:
    if st.sidebar.button(page):
        st.session_state.page = page

selected_page = st.session_state.page

# Selected sidebar page
# ```
# Predictions
    # Buat input prediksi, mayoritas input
    # pake angka decimal, cuma fitur 2 & 3 yang float
    # Setelah di input, akan diteruskan ke model 
    # lalu di prediksi dengan predict_proba di backend
# ```

if selected_page == "Prediction":
    st.title("🔮 Churn Prediction")

    with st.form("prediction_form"):
        # --- PERBAIKAN: Menambahkan argumen 'value' untuk setiap input ---
        target = st.number_input("🎯 Target Achievement (%)", min_value=0, max_value=120, format="%d")
        hours = st.number_input("⏱️ Working Hours per Week", min_value=0, max_value=75, format="%d")
        satisfaction = st.slider("😊 Job Satisfaction (1-5)", min_value=0.0, max_value=5.0, step=0.01)
        manager = st.slider("👔 Manager Support Score (1-5)", min_value=0.0, max_value=5.0, step=0.01)
        tenure = st.number_input("🏢 Company Tenures (years)", min_value=0.0, max_value=10.0, step=0.25)
        distance = st.number_input("🚗 Distance to Office (km)", min_value=0.0, max_value=50.0, step=0.25)
        tenure_age = st.number_input("Tenure Age (years)", min_value=0.0, max_value=5.0, step=0.25)
        income_per_hour = st.number_input("💰 Income (Hourly)", min_value=0.0, max_value=100000.0, step=1000.0)
        exp_to_tenure = st.number_input("💰 Experience to Tenures (years)",min_value=0.0, max_value=10.0, step=0.25)
        marital_status = st.radio("💍 Marital Status", options=["Single", "Married"]) == "Single"
        submitted = st.form_submit_button("Predict")

    if submitted:
        payload = {
            "Target": target,
            "Hours": hours,
            "Satisfaction": satisfaction,
            "Manager": manager,
            "Tenure": tenure,
            "Distance": distance,
            "Age": tenure_age,
            "Salary": income_per_hour,
            "Experience": exp_to_tenure,
            "Marital": int(marital_status)
        }

        try:
            response = requests.post(API_URL, json=payload)
            try:
                result = response.json()
            except Exception:
                st.error(f"Unexpected server error:\n{response.text}")
                st.stop()

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
            text_color = "white"

            st.markdown(f"""
                <div class='risk-box risk-{risk.lower()}'>
                    <strong>Churn Probability:</strong> {probability:.0%}
                </div>
                <div class='risk-box risk-{risk.lower()}'>
                    <strong>Risk Group:</strong> {risk}
                </div>
                <div class='suggest-box'>
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

# Selected sidebar page
# ```
# History
    # Buat cek history prediksi 
    # gk ada file yang disimpan, semuanya bersifat lokal
# ```

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
                    <tr class='table-header'>
                        {''.join(f'<th style="padding: 8px; border: 1px solid #ccc;">{col}</th>' for col in feature_names)}
                    </tr>
                    <tr>
                        {''.join(f'<td style="padding: 8px; border: 1px solid #ccc;">{val}</td>' for val in feature_values)}
                    </tr>
                    <tr>
                        <td style="padding: 8px; border: 1px solid #ccc; background-color: {prob_color}; color: white;" colspan="{len(feature_names)//2}">
                            <strong>Probability:</strong> {probability:.0%}
                        </td>
                        <td style="padding: 8px; border: 1px solid #ccc; background-color: {risk_color}; color: white;" colspan="{len(feature_names) - len(feature_names)//2}">
                            <strong>Risk Group:</strong> {risk}
                        </td>
                    </tr>
                    <tr>
                        <td colspan="{len(feature_names)}" style="padding: 8px; border: 1px solid #ccc;"><strong>Suggestion:</strong> {record['suggestion']}</td>
                    </tr>
                </table>
            </div>
            <hr>
            """

            st.markdown(table_html, unsafe_allow_html=True)
