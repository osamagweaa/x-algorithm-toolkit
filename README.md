# X Algorithm Toolkit

A practical toolkit combining the most useful tools derived from the open-source [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) repository.

**Features:**
- **Post Scorer**: Estimate how well a draft aligns with high-weight actions (replies, shares, dwell).
- **Reach Diagnostic**: Analyze Under the Hood JSON reports for visibility labels.
- **Cadence Planner**: Suggest posting schedules that respect author diversity decay.
- **Weight Reference**: Current known production-style weights and notes.

This is an approximation tool based on published code. Live ranking uses a full Phoenix model and may differ.

## Quick Start

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Disclaimer

Weights and logic are based on publicly published defaults in the x-algorithm repo. Always verify against the latest commit. Not affiliated with X or xAI.
