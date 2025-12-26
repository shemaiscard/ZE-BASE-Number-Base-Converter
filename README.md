ZE BASE: UNIVERSAL NUMBER BASE CONVERTER & LEARNING PLATFORM
===========================================================

OVERVIEW
--------
ZE BASE is a high-precision mathematical tool designed to facilitate the 
conversion and study of positional number systems. Unlike standard converters, 
ZE BASE handles complex mathematical scenarios including floating-point 
fractions, negative numbers, and arbitrary bases ranging from 2 to 36.

TECHNICAL CONSTRUCTION
----------------------
This project was engineered as a full-stack Python application optimized for 
mathematical accuracy and user education.

1. MATHEMATICAL LOGIC ENGINE (BACKEND):
   - Precision Fractional Algorithm: Implements a custom recursive 
     multiplication-by-base algorithm to convert fractional parts (e.g., 0.625) 
     across different bases without losing floating-point precision.
   - Arbitrary Base Logic: Built on the core positional summation formula, 
     allowing users to move between any base from binary (2) to 
     hexatrigesimal (36).
     
   - Two's Complement Integration: Includes logic for representing and 
     converting negative numbers, simulating how modern CPUs handle 
     signed integers.

2. FRONTEND ENGINEERING (STREAMLIT + CSS3):
   - Adaptive Design System: Utilizes an external 'styles.css' to implement a 
     "Glassmorphism" UI that automatically adapts to the user's system 
     theme (Dark/Light mode).
   - State-Driven Quizzes: Leverages Streamlit Session State to create an 
     interactive "Practice" environment that generates dynamic challenges 
     and provides instant validation without full-page reloads.

KEY FEATURES
------------
* Universal Conversion: Seamlessly convert integers, negatives, and fractions 
  between bases 2 through 36.
* Adjustable Accuracy: User-defined "Fraction Precision" slider to control 
  the depth of fractional conversions.
* Learning Center: A comprehensive guide covering:
    - Binary and Hexadecimal fundamentals.
    - Step-by-step fractional conversion techniques.
      
    - Negative number representations (Two's Complement).
* Interactive Practice: Randomly generated quizzes for Binary, Hex, and 
  Fractional math with instant feedback on success.

TECHNOLOGY STACK
----------------
* Language: Python 3.x
* Framework: Streamlit
* Data Management: Pandas
* Styling: CSS3
* Visuals: LaTeX for mathematical rendering

INSTALLATION & DEPLOYMENT
-------------------------
1. Prerequisites:
   Ensure Python 3.8+ is installed on your Linux server.

2. Install Requirements:
   pip install streamlit pandas

3. Directory Structure:
   - pyres.py: Main application script
   - styles.css: Custom UI styling
   - images/: Educational diagrams

4. Launch:
   streamlit run pyres.py

HOW TO USE
----------
1. CONVERT: Navigate to the "Universal Converter" tab, input your number, 
   choose your bases, and hit "Convert."
2. LEARN: Browse the "Concepts" sub-tab to view deep-dive guides and visual 
   diagrams.
3. PRACTICE: Use the "Practice" tab to generate a random problem and test 
   your conversion skills.

CREDITS
-------
Developed by Giscard
Version 1.0.0 (2025)
