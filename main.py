import streamlit as st


def calculate_password_strength(password):
    score = 0
    feedback = []

    # Rule 1: Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make the password at least 8 characters long.")

    # Rule 2: Uppercase Check
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Rule 3: Lowercase Check
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Rule 4: Digit Check
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Include at least one digit (0-9).")

    # Rule 5: Special Character Check
    special_characters = "!@#$%^&*"
    if any(c in special_characters for c in password):
        score += 1
    else:
        feedback.append("Use at least one special character (!@#$%^&*).")

    return score, feedback


def get_strength_level(score):
    if score <= 2:
        return "❌ Weak", "red"
    elif score <= 4:
        return "⚠️ Moderate", "orange"
    else:
        return "✅ Strong", "green"


def main():
    st.title("🔐 Password Strength Meter")
    password = st.text_input("Enter your password", type="password")

    if password:
        score, feedback = calculate_password_strength(password)
        strength, color = get_strength_level(score)

        st.markdown(f"### Strength: :{color}[{strength}]")

        if score < 5:
            st.subheader("Suggestions to improve:")
            for tip in feedback:
                st.markdown(f"- {tip}")
        else:
            st.success("Great! Your password is strong and secure. ✅")


if __name__ == "__main__":
    main()
