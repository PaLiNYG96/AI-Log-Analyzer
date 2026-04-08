import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from preprocess import extract_failure_lines
from analyze import analyze_failure

st.title("AI Test Failure Analyzer")

log_input = st.text_area("Paste test log here")

if st.button("Analyze"):
    failures = extract_failure_lines(log_input)
    result = analyze_failure(failures)
    st.text_area("Analysis Result", result, height=200)