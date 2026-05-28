# Ze Base — Universal Number Base Converter

**Live Demo:** [ze-base.streamlit.app](https://ze-base.streamlit.app)

A high-precision number base converter and learning platform. Converts integers, fractions, and negative numbers between any base from 2 to 36, with an interactive educational mode and practice quizzes.

## Features

- **Universal Conversion**: Integers, fractions (floating-point), and negatives across bases 2–36
- **Adjustable Precision**: User-defined slider for fractional conversion depth
- **Two's Complement**: Signed integer representation as used in modern CPUs
- **Learning Center**: Guides on binary, hex, fractional conversions, and two's complement
- **Practice Mode**: Randomly generated quizzes with instant feedback (Binary, Hex, Fractional)
- **Dark/Light Mode**: Glassmorphism UI that adapts to system theme

## Setup

```bash
pip install streamlit pandas
streamlit run pyres.py
```

## File Structure

```
ZE-BASE-Number-Base-Converter/
├── pyres.py      Main application
├── styles.css    Custom UI styling
└── images/       Educational diagrams
```

## Tech Stack
Python · Streamlit · Pandas · LaTeX (math rendering) · CSS3

## License
MIT License — v1.0.0 — Developed by Giscard
