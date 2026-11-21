import streamlit as st
import json
from scorer import score_post, WEIGHTS, NEGATIVE_WEIGHTS

st.set_page_config(page_title="X Algorithm Toolkit", layout="wide")

st.title("X Algorithm Toolkit")
st.caption("Combined tools based on the open-source xai-org/x-algorithm repo")

tab1, tab2, tab3, tab4 = st.tabs(["Post Scorer", "Reach Diagnostic", "Cadence Planner", "Weights"])

with tab1:
    st.header("Post Scorer & Optimizer")
    draft = st.text_area("Paste your draft post", height=150)
    if st.button("Score Draft") and draft:
        result = score_post(draft)
        st.metric("Estimated Score", result["score"])
        st.json(result["breakdown"])
        st.subheader("Tips")
        for tip in result["tips"]:
            st.write("- " + tip)

with tab2:
    st.header("Reach Diagnostic (Under the Hood)")
    uploaded = st.file_uploader("Upload Under the Hood JSON", type="json")
    if uploaded:
        data = json.load(uploaded)
        st.write("Labels found (example parsing):")
        # Simple display — real parser would map to visibility rules
        st.json(data if isinstance(data, dict) else {"raw": str(data)[:500]})
        st.info("Map these labels against visibility-filtering/ and under-the-hood/ in the official repo for full context.")

with tab3:
    st.header("Cadence Planner")
    st.write("Author diversity decay means later posts from the same author are discounted in a feed load.")
    posts_per_day = st.slider("Target posts per day", 1, 10, 3)
    st.write(f"Suggested: space posts at least 4–6 hours apart to reduce diversity penalty.")
    st.write("Cold-start boosts are strongest for newer accounts or first posts in a window.")

with tab4:
    st.header("Published Weight Reference")
    st.subheader("Positive (approximate)")
    st.json(WEIGHTS)
    st.subheader("Negative")
    st.json(NEGATIVE_WEIGHTS)
    st.warning("These are illustrative defaults. Always check the latest param.rs in xai-org/x-algorithm.")
