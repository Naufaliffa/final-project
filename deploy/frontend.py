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
        target = st.number_input("🎯 Target Achievement (%)", min_value=0, max_value=120, format="%d")
        satisfaction = st.slider("😊 Job Satisfaction (1-5)", min_value=0.0, max_value=5.0, step=0.01)
        manager = st.slider("👔 Manager Support Score (1-5)", min_value=0.0, max_value=5.0, step=0.01)
        distance = st.number_input("🚗 Distance to Office (km)", min_value=0, format="%d")
        marital_status = st.radio("💍 Marital Status", options=["Single", "Married"]) == "Single"
        hours = st.number_input("⏱️ Working Hours per Week", min_value=0, max_value=75, format="%d")
        tenure = st.number_input("🏢 Company Tenure (years)", min_value=0.0, max_value=5.0, step=0.25)
        commission = st.number_input("💰 Commission Rate", min_value=0.0, max_value=0.1, step=0.01)
        age = st.number_input("🎂 Age", min_value=18, max_value=100, format="%d")

        submitted = st.form_submit_button("Predict")

    if submitted:
        payload = {
            "Target": target,
            "Satisfaction": satisfaction,
            "Manager": manager,
            "Distance": distance,
            "Marital": int(marital_status),
            "Hours": hours,
            "Tenure": tenure,
            "Commission": commission,
            "Age": age
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
            
# Bulk Predictions
    # Buat input prediksi, tapi satu file, jadi banyak output di history
    # Auto cek kolom dengan nama fitur yang mirip
    # Kalau gk ada yg mirip atau kosong, print error
# ``` 
    st.markdown("---")
    st.subheader("📂 Input CSV file for bulk prediction")

    with st.form("bulk_prediction_form"):
        uploaded_file = st.file_uploader("Upload CSV file for bulk prediction", type=["csv"])
        bulk_submit = st.form_submit_button("Predict in Bulk")

    if bulk_submit and uploaded_file:
        try:
            bulk_response = requests.post("http://127.0.0.1:8000/bulk_predict", files={"file": uploaded_file.getvalue()})
            result = bulk_response.json()
            if "error" in result:
                st.error(result["error"])
            else:
                st.success("Bulk prediction completed!")
                # Count risk groups
                risk_counts = {"High": 0, "Medium": 0, "Low": 0}

                for entry in result["results"]:
                    prob = entry["probability"]
                    risk = entry["risk"]
                    suggestion = entry["suggestion"]
                    features = entry["features"]

                    # Count risk level
                    risk_counts[risk] += 1

                    # Save to frontend history
                    st.session_state.history.append({
                        "input": features,
                        "probability": prob,
                        "risk": risk,
                        "suggestion": suggestion
                    })

                # Display summary
                st.success("✅ Bulk prediction completed!")
                st.markdown(f"""
                - 🔴 High Risk: **{risk_counts['High']}**
                - 🟠 Medium Risk: **{risk_counts['Medium']}**
                - 🟢 Low Risk: **{risk_counts['Low']}**
                """)
        except Exception as e:
            st.error(f"Failed to process bulk file: {e}")

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

            # Mapping display names to raw keys
            display_key_map = {
                "Target": "target_achievement",
                "Satisfaction": "job_satisfaction",
                "Manager": "manager_support_score",
                "Distance": "distance_to_office_km",
                "Marital": "marital_status_Single",
                "Hours": "working_hours_per_week",
                "Tenure": "company_tenure_years",
                "Commission": "commission_rate",
                "Age": "age"
            }

            # Final display labels
            display_keys = list(display_key_map.keys())

            # Extract values in display order using internal/raw keys
            feature_values = []
            for k in display_keys:
                backend_key = display_key_map[k]
                val = input_data.get(backend_key)
                if val is None:
                    val = input_data.get(k, "")
                if isinstance(val, float) and val.is_integer():
                    val = int(val)
                feature_values.append(val)


            probability = record['probability']
            risk = record['risk']
            suggestion = record['suggestion']

            # Risk color coding
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
            <div style='margin-top: 20px; max-width: 900px; overflow-x: auto;'>
                <h4>Prediction #{len(st.session_state.history) - i + 1}</h4>
                <table style='width: 100%; border-collapse: collapse; table-layout: auto;'>
                    <tr class='table-header'>
                        {''.join(f'<th style="padding: 8px; border: 1px solid #ccc;">{col}</th>' for col in display_keys)}
                    </tr>
                    <tr>
                        {''.join(f'<td style="padding: 8px; border: 1px solid #ccc;">{val}</td>' for val in feature_values)}
                    </tr>
                    <tr>
                        <td style="padding: 8px; border: 1px solid #ccc; background-color: {prob_color}; color: white;" colspan="5">
                            <strong>Probability:</strong> {probability:.0%}
                        </td>
                        <td style="padding: 8px; border: 1px solid #ccc; background-color: {risk_color}; color: white;" colspan="4">
                            <strong>Risk Group:</strong> {risk}
                        </td>
                    </tr>
                    <tr>
                        <td colspan="9" style="padding: 8px; border: 1px solid #ccc;">
                            <strong>Suggestion:</strong> {suggestion}
                        </td>
                    </tr>
                </table>
            </div>
            <hr>
            """

            st.markdown(table_html, unsafe_allow_html=True)



