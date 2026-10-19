
import streamlit as st

if "expenses" not in st.session_state:
    st.session_state.expenses = []

st.title("My Expense Tracker")

category = st.selectbox(
    "Choose an expense category",
    ["Food", "Travel", "Stationary"]
)

expense = st.number_input(
    "Enter your expense amount (₹)",
    min_value=0.0
)

st.write("Your expense is ₹", expense)

if st.button("Add Expense"):
    st.session_state.expenses.append({
    "amount": expense,
    "category": category
})
    st.success(
        f"Expense of ₹{expense} added to {category} category."
    )

if st.button("Show Total Expenses"):
    total_expense = sum(
    item["amount"] for item in st.session_state.expenses
)
    st.write(f"Total expenses: ₹{total_expense}")


st.subheader("Expense History")

for item in st.session_state.expenses:
    st.write(
        f"{item['category']}: ₹{item['amount']}"
    )

st.subheader("Spending by Category")

category_totals = {}

for item in st.session_state.expenses:
    category = item["category"]
    amount = item["amount"]
    if category not in category_totals:
        category_totals[category] = 0
    category_totals[category] += amount

for category, total in category_totals.items():
    st.write(f"{category}: ₹{total}")
