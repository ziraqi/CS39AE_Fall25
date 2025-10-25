import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("📊 Interactive Pie Chart")

# Create the data folder path
data_path = "data/pie_demo.csv"

# Check if the CSV file exists
if os.path.exists(data_path):
    # Load the data
    @st.cache_data
    def load_data():
        return pd.read_csv(data_path)
    
    df = load_data()
    
    # Display the title - you can change this title later for testing
    chart_title = "Monthly Expense Distribution"
    
    st.markdown(f"### {chart_title}")
    
    # Add interactivity with a checkbox
    show_values = st.checkbox("Show values on chart", value=True)
    show_legend = st.checkbox("Show legend", value=True)
    
    # Color scheme selector
    color_scheme = st.selectbox(
        "Choose color scheme:",
        ["blues", "reds", "greens", "viridis", "plotly"]
    )
    
    # Create the pie chart
    fig = px.pie(
        df, 
        values='amount', 
        names='category',
        title=chart_title,
        color_discrete_sequence=getattr(px.colors.sequential, color_scheme.capitalize()) if color_scheme != "plotly" else px.colors.qualitative.Plotly
    )
    
    # Update layout based on checkboxes
    if show_values:
        fig.update_traces(textposition='inside', textinfo='percent+label')
    else:
        fig.update_traces(textinfo='none')
    
    fig.update_layout(showlegend=show_legend)
    
    # Display the chart
    st.plotly_chart(fig, use_container_width=True)
    
    # Show the data in an expander
    with st.expander("View Data"):
        st.dataframe(df)
        total = df['amount'].sum()
        st.write(f"**Total: ${total:,.2f}**")
        
    # Add ability to edit data
    st.markdown("### Edit Data")
    edited_df = st.data_editor(df, num_rows="dynamic")
    
    if st.button("Update Chart with New Data"):
        # Save the edited data back to CSV
        edited_df.to_csv(data_path, index=False)
        st.success("Data updated! The chart will refresh.")
        st.rerun()
        
else:
    st.error(f"Data file not found at: {data_path}")
    st.info("Creating a sample data file for you...")
    
    # Create sample data
    sample_data = pd.DataFrame({
        'category': ['Housing', 'Food', 'Transportation', 'Entertainment', 'Utilities', 'Healthcare', 'Savings'],
        'amount': [1200, 400, 300, 250, 150, 100, 600]
    })
    
    # Create the data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    
    # Save the sample data
    sample_data.to_csv(data_path, index=False)
    st.success("Sample data created! Please refresh the page.")
    st.balloons()