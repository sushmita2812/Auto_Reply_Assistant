import streamlit as st
from AssistantLogic import generate_responses

# --- Streamlit UI ---
st.set_page_config(page_title="AI Auto-Reply Assistant", layout="centered")

st.title("🤖 AI Auto-Reply Assistant")
st.write("Paste a LinkedIn message below and get polite, ready-to-use replies.")

# Step 1: Input message
user_message = st.text_area("📩 Paste the LinkedIn message here:", height=200)

# Step 2: Generate button
if st.button("Generate Responses"):
    if user_message.strip():
        # Show spinner while generating responses
        with st.spinner("🤔 Generating smart replies... Please wait..."):
            responses = generate_responses(user_message)

        st.success("✅ Replies generated successfully!")

        st.subheader("Suggested Replies")
        for i, resp in enumerate(responses, 1):
            col1, col2 = st.columns([8, 2])
            with col1:
                st.write(f"**Reply {i}:** {resp}")
            with col2:
                # Copy box
                st.code(resp, language="text")
    else:
        st.warning("⚠️ Please paste a message before generating replies.")
