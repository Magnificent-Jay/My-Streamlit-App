import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to get real-time data from Raspberry Pi (replace with actual data retrieval)
def get_data():
    # Replace this part with your actual real-time data fetching logic
    # For example, if you're reading from a CSV file generated by your system:
    df = pd.read_csv('Edited_Generated_Energy_Data.csv')  # Replace with the actual path
    return df

# Load real-time data from Raspberry Pi
df = get_data()

# Title of the dashboard
st.title("Real-time Energy Consumption Dashboard")

# Real-time table display
st.subheader("Energy Data Table (Live Update)")
st.dataframe(df)  # Display the data as a table

# Select graph type (Bar chart or Line chart)
chart_type = st.radio("Select Chart Type:", ["Line Chart", "Bar Chart"])

# Plot energy consumption per hour
st.subheader("Energy Consumed Per Hour")

if chart_type == "Line Chart":
    st.line_chart(df[['Timestamp', 'Power (W)']].set_index('Timestamp'))
elif chart_type == "Bar Chart":
    st.bar_chart(df[['Timestamp', 'Power (W)']].set_index('Timestamp'))

# Optionally, you can add more detailed custom graphs using matplotlib
def plot_custom_graph(df, chart_type):
    fig, ax = plt.subplots()
    if chart_type == "Line Chart":
        ax.plot(df['Timestamp'], df['Power (W)'], marker='o', linestyle='-', color='b', label='Energy Consumed')
    elif chart_type == "Bar Chart":
        ax.bar(df['Timestamp'], df['Power (W)'], color='orange', label='Energy Consumed')

    ax.set_title("Energy Consumed Per Hour")
    ax.set_xlabel("Hour")
    ax.set_ylabel("Energy Consumed (kWh)")
    ax.legend()
    return fig

# Display matplotlib graph (optional)
st.pyplot(plot_custom_graph(df, chart_type))

# Add auto-refresh every minute to simulate real-time updates
st.experimental_rerun()
