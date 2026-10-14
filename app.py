import streamlit as st
import random
import pandas as pd

# Load custom CSS
def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Conversion Functions
def convert_fractional_part(fractional, from_base, precision=10):
    result = 0.0
    for i in range(1, precision+1):
        if i-1 >= len(fractional): break
        digit = fractional[i-1].upper()
        result += int(digit, from_base) * (from_base ** -i)
    return result

def base_to_decimal(number_str, from_base):
    number_str = str(number_str).strip()
    negative = False
    if number_str.startswith('-'):
        negative = True
        number_str = number_str[1:]
    
    if '.' in number_str:
        integer_part, fractional_part = number_str.split('.')
    else:
        integer_part = number_str
        fractional_part = ''
    
    # Convert integer part
    decimal_int = int(integer_part, from_base) if integer_part else 0
    
    # Convert fractional part
    decimal_frac = convert_fractional_part(fractional_part, from_base) if fractional_part else 0.0
    
    result = decimal_int + decimal_frac
    return -result if negative else result

def decimal_to_base(number, to_base, precision=10):
    if isinstance(number, str):
        number = float(number) if '.' in number else int(number)
    
    negative = False
    if number < 0:
        negative = True
        number = abs(number)
    
    integer_part = int(number)
    fractional_part = number - integer_part
    
    # Convert integer part
    int_result = []
    if integer_part == 0:
        int_result = ['0']
    else:
        while integer_part > 0:
            int_result.append("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[integer_part % to_base])
            integer_part = integer_part // to_base
    int_result = ''.join(reversed(int_result))
    
    # Convert fractional part
    frac_result = []
    for _ in range(precision):
        fractional_part *= to_base
        digit = int(fractional_part)
        frac_result.append("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[digit])
        fractional_part -= digit
        if fractional_part <= 1e-10:
            break
    
    result = int_result
    if frac_result:
        result += '.' + ''.join(frac_result)
    
    return ('-' if negative else '') + result

def convert_base(number_str, from_base, to_base, precision=10):
    try:
        decimal = base_to_decimal(number_str, from_base)
        return decimal_to_base(decimal, to_base, precision)
    except ValueError:
        return "Invalid input for base"
    except Exception as e:
        return f"Error: {str(e)}"
    
# Main Tabs
def main_tabs():
    tab1, tab2 = st.tabs(["🔢 Universal Converter", "🎓 Learn & Practice"])

    with tab1:
        base_converter_tab()
    
    with tab2:
        educational_mode_tab()

# Base Converter Tab
def base_converter_tab():
    st.header("Universal Base Converter")
    
    col1, col2, col3 = st.columns([3,1,1])
    with col1:
        number = st.text_input("Enter number (supports negatives and fractions):", "1010.101")
    with col2:
        from_base = st.number_input("From Base:", 2, 36, 2)
    with col3:
        to_base = st.number_input("To Base:", 2, 36, 10)
    
    precision = st.slider("Fraction Precision", 1, 5, 3)
    
    if st.button("Convert"):
        result = convert_base(number, from_base, to_base, precision)
        st.success(f"**Result:** {result}")
    
    with st.expander("📚 Quick Reference"):
        ref_col1, ref_col2 = st.columns([0.7,1])
        with ref_col1:
            st.write("**Common Bases**")
            bases = pd.DataFrame({
                "Base": [2, 8, 10, 16],
                "Digits": ["0-1", "0-7", "0-9", "0-9, A-F"],
                "Prefix": ["0b", "0o", "", "0x"]
            })
            st.dataframe(bases)
        
        with ref_col2:
            st.write("**Examples**")
            examples = pd.DataFrame({
                "Type": ["Integer", "Negative", "Fraction", "Hex Fraction"],
                "Input": ["1101", "-A5", "101.101", "FF.A"],
                "From": [2, 16, 2, 16],
                "To": [10, 10, 10, 10],
                "Result": ["13", "-165", "5.625", "255.625"]
            })
            st.dataframe(examples)

# Educational Mode Tab
def educational_mode_tab():
    st.header("Learning Center")
    subtab1, subtab2 = st.tabs(["📚 Concepts", "✍️ Practice"])
    
    with subtab1:
        st.subheader("Comprehensive Number Base Guide")
        concept = st.selectbox("Choose Topic", [
            "Understanding Number Bases", 
            "Binary System Deep Dive",
            "Hexadecimal Essentials",
            "Fractional Conversions",
            "Negative Number Representations",
            "Real-World Applications"
        ])

        if concept == "Understanding Number Bases":
            st.markdown("""
            ## Number Systems Fundamentals
            
            **Key Concepts:**
            - Base determines the number of digits used
            - Positional value system (right to left)
            - Importance in computing and mathematics
            
            ```math
            Value = Σ (digit × base^position)
            ```
            """)
            st.image("images/pnumber .jpg", 
                    caption="Positional Number System Visualization")

        elif concept == "Binary System Deep Dive":
            st.markdown("""
            ## Binary Number System (Base 2)
            
            **Core Principles:**
            - Foundation of digital electronics
            - Two states: 0 (off) and 1 (on)
            - Conversion methods:
              1. Division-by-2 for integers
              2. Multiplication-by-2 for fractions
            
            **Conversion Example:**
            ```math
            1011.101_2 = 1×2^3 + 0×2^2 + 1×2^1 + 1×2^0 + 1×2^{-1} + 0×2^{-2} + 1×2^{-3}
                       = 11.625_{10}
            ```
            """)
            st.image("images/bcon.jpg",
                    caption="Binary Conversion Process", width=350)

        elif concept == "Hexadecimal Essentials":
            st.markdown("""
            ## Hexadecimal System (Base 16)
            
            **Why Hexadecimal?**
            - Compact representation of binary
            - Direct mapping to 4-bit binary groups
            - Essential in memory addressing and color codes
            
            **Conversion Table:**
            """)
            hex_table = pd.DataFrame({
                "Decimal": range(16),
                "Hex": [f"{i:X}" for i in range(16)],
                "Binary": [f"{i:04b}" for i in range(16)]
            })
            st.dataframe(hex_table, use_container_width=True)

        elif concept == "Fractional Conversions":
            st.markdown("""
            ## Fractional Number Conversion
            
            **Step-by-Step Process:**
            1. Separate integer and fractional parts
            2. Convert integer part normally
            3. For fractional part:
               - Multiply by target base
               - Record integer part
               - Repeat with new fraction
            4. Combine results
            
            **Example: 0.625_{10} to Binary**
            ```math
            0.625 × 2 = 1.25 → 1 (MSB)
            0.25 × 2 = 0.5 → 0
            0.5 × 2 = 1.0 → 1 (LSB)
            Result: 0.101_2
            ```
            """)
            st.image("images/fraction .png",
                    caption="Fraction Conversion Steps", width=350)

        elif concept == "Negative Number Representations":
            st.markdown("""
            ## Handling Negative Numbers
            
            **Common Methods:**
            1. Sign-Magnitude:
               - First bit as sign (0=+, 1=-)
               - Rest as magnitude
            
            2. Two's Complement (Binary):
               - Invert bits + 1
               - Most common in computing
            
            **Example: -5 in 4-bit Two's Complement**
            ```math
            +5 = 0101
            Invert → 1010
            Add 1 → 1011 (-5)
            ```
            """)
            st.image("images/Two's compliment.jpg",
                    caption="Two's Complement Visualization", width=350)

        elif concept == "Real-World Applications":
            st.markdown("""
            ## Practical Applications
            
            **1. Computer Systems:**
            - Memory addressing (hexadecimal)
            - Binary data representation
            
            **2. Digital Electronics:**
            - Logic gates and circuit design
            - Binary-coded decimals
            
            **3. Color Representation:**
            - Hex color codes (#RRGGBB)
            """)
            st.image("images/Hex .jpg",
                    caption="Hex Color Model Example", width=350)

    with subtab2:
        st.subheader("Practice Quizzes")
        quiz_type = st.selectbox("Select Quiz Type", [
            "Binary Conversions", "Hex Challenges",
            "Fractional Numbers", "Negative Numbers"
        ])
        
        if st.button("🎲 Generate New Question"):
            st.session_state.quiz = generate_quiz(quiz_type)
        
        if 'quiz' in st.session_state:
            st.markdown(f"**{st.session_state.quiz['question']}**")
            user_answer = st.text_input("Your Answer:")
            
            if st.button("Check Answer"):
                if validate_answer(user_answer, st.session_state.quiz['answer']):
                    st.success("Correct! 🎉")
                    st.balloons()
                else:
                    st.error(f"Incorrect. Correct answer: {st.session_state.quiz['answer']}")

def generate_quiz(quiz_type):
    bases = {
        "Binary Conversions": (2, 10),
        "Hex Challenges": (16, 10), 
        "Negative Numbers": (2, 10),
        "Fractional Numbers": (2, 10)
    }
    
    from_base, to_base = bases[quiz_type]
    
    if quiz_type == "Negative Numbers":
        num = -random.randint(1, 255)
        problem = f"{decimal_to_base(num, from_base)} (Base {from_base}) to Decimal(base 10)"
        answer = str(num)
    elif quiz_type == "Fractional Numbers":
        num = round(random.uniform(1, 100), 3)
        problem = f"{decimal_to_base(num, from_base)} (Base {from_base}) to Decimal(base 10)"
        answer = f"{num:.3f}"
    else:
        num = random.randint(1, 255)
        problem = f"{decimal_to_base(num, from_base)} (Base {from_base}) to Decimal(base 10)"
        answer = str(num)
    
    return {'question': problem, 'answer': answer}

def validate_answer(user, correct):
    try:
        return abs(float(user) - float(correct)) < 0.001
    except:
        return user.upper() == correct.upper()

# Main App
def main():
    st.set_page_config(page_title="Ze Base Converter")
    load_css()
    st.title("ZE BASE: Number Base Converter")
    main_tabs()

if __name__ == "__main__":
    main()