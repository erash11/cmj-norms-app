import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO

st.set_page_config(page_title="CMJ Normative Performance Analysis", layout="wide")

st.title("⚡ Countermovement Jump Normative Performance Analysis")
st.markdown("Upload your CMJ data and team roster to generate position-based normative values")

# Sidebar for file uploads
st.sidebar.header("📁 Upload Files")

# File upload for CMJ data
cmj_file = st.sidebar.file_uploader(
    "Upload CMJ Data (CSV/Excel)", 
    type=['csv', 'xlsx'],
    help="Upload your countermovement jump performance data"
)

# File upload for roster
roster_file = st.sidebar.file_uploader(
    "Upload Team Roster (CSV/Excel)", 
    type=['csv', 'xlsx'],
    help="Upload team roster with athlete names and positions"
)

# Configuration options
st.sidebar.header("⚙️ Configuration")
metric_column = st.sidebar.text_input("CMJ Metric Column Name", value="Jump Height (cm)", 
                                       help="Name of the column containing jump performance metric")
athlete_id_column = st.sidebar.text_input("Athlete ID Column", value="Athlete Name",
                                          help="Column name for athlete identifier")
position_column = st.sidebar.text_input("Position Column Name", value="Position",
                                        help="Column name for athlete position")

def load_data(file):
    """Load data from CSV or Excel file"""
    if file is not None:
        if file.name.endswith('.csv'):
            return pd.read_csv(file)
        else:
            return pd.read_excel(file)
    return None

def calculate_percentiles(data, metric_col):
    """Calculate percentile values for the data"""
    return {
        'P25': np.percentile(data[metric_col].dropna(), 25),
        'P50': np.percentile(data[metric_col].dropna(), 50),
        'P75': np.percentile(data[metric_col].dropna(), 75),
        'P90': np.percentile(data[metric_col].dropna(), 90),
        'Mean': data[metric_col].mean(),
        'SD': data[metric_col].std(),
        'Min': data[metric_col].min(),
        'Max': data[metric_col].max(),
        'N': data[metric_col].notna().sum()
    }

def to_excel(dataframes_dict):
    """Convert multiple dataframes to Excel file in memory"""
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        for sheet_name, df in dataframes_dict.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    output.seek(0)
    return output

# Main application logic
if cmj_file is not None and roster_file is not None:
    
    # Load data
    cmj_data = load_data(cmj_file)
    roster_data = load_data(roster_file)
    
    if cmj_data is not None and roster_data is not None:
        
        # Display data preview
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 CMJ Data Preview")
            st.dataframe(cmj_data.head(), use_container_width=True)
            st.caption(f"Total rows: {len(cmj_data)}")
        
        with col2:
            st.subheader("👥 Roster Preview")
            st.dataframe(roster_data.head(), use_container_width=True)
            st.caption(f"Total athletes: {len(roster_data)}")
        
        # Check if required columns exist
        required_cols_cmj = [athlete_id_column, metric_column]
        required_cols_roster = [athlete_id_column, position_column]
        
        missing_cmj = [col for col in required_cols_cmj if col not in cmj_data.columns]
        missing_roster = [col for col in required_cols_roster if col not in roster_data.columns]
        
        if missing_cmj:
            st.error(f"❌ Missing columns in CMJ data: {missing_cmj}")
            st.info(f"Available columns: {list(cmj_data.columns)}")
        elif missing_roster:
            st.error(f"❌ Missing columns in Roster data: {missing_roster}")
            st.info(f"Available columns: {list(roster_data.columns)}")
        else:
            # Merge datasets
            merged_data = pd.merge(
                cmj_data, 
                roster_data[[athlete_id_column, position_column]], 
                on=athlete_id_column, 
                how='left'
            )
            
            # Check for athletes without position
            no_position = merged_data[merged_data[position_column].isna()]
            if len(no_position) > 0:
                st.warning(f"⚠️ {len(no_position)} athletes found in CMJ data without position information")
                with st.expander("View athletes without position"):
                    st.dataframe(no_position[[athlete_id_column]], use_container_width=True)
            
            # Remove rows without position or metric
            analysis_data = merged_data.dropna(subset=[position_column, metric_column])
            
            st.success(f"✅ Successfully merged data: {len(analysis_data)} records ready for analysis")
            
            # Calculate normative values by position
            st.header("📈 Normative Values by Position")
            
            positions = sorted(analysis_data[position_column].unique())
            
            # Create normative table
            normative_results = []
            
            for position in positions:
                position_data = analysis_data[analysis_data[position_column] == position]
                percentiles = calculate_percentiles(position_data, metric_column)
                
                result_row = {
                    'Position': position,
                    'N': int(percentiles['N']),
                    'Mean': round(percentiles['Mean'], 2),
                    'SD': round(percentiles['SD'], 2),
                    'Min': round(percentiles['Min'], 2),
                    'P25': round(percentiles['P25'], 2),
                    'P50 (Median)': round(percentiles['P50'], 2),
                    'P75': round(percentiles['P75'], 2),
                    'P90': round(percentiles['P90'], 2),
                    'Max': round(percentiles['Max'], 2)
                }
                normative_results.append(result_row)
            
            normative_df = pd.DataFrame(normative_results)
            
            # Calculate overall normative values
            overall_percentiles = calculate_percentiles(analysis_data, metric_column)
            overall_row = {
                'Position': 'ALL POSITIONS',
                'N': int(overall_percentiles['N']),
                'Mean': round(overall_percentiles['Mean'], 2),
                'SD': round(overall_percentiles['SD'], 2),
                'Min': round(overall_percentiles['Min'], 2),
                'P25': round(overall_percentiles['P25'], 2),
                'P50 (Median)': round(overall_percentiles['P50'], 2),
                'P75': round(overall_percentiles['P75'], 2),
                'P90': round(overall_percentiles['P90'], 2),
                'Max': round(overall_percentiles['Max'], 2)
            }
            normative_df = pd.concat([normative_df, pd.DataFrame([overall_row])], ignore_index=True)
            
            # Display normative table
            st.dataframe(
                normative_df.style.background_gradient(
                    subset=['P25', 'P50 (Median)', 'P75', 'P90'], 
                    cmap='RdYlGn'
                ),
                use_container_width=True,
                height=400
            )
            
            # Individual athlete analysis
            st.header("👤 Individual Athlete Performance")
            
            # Add percentile ranks to merged data
            def calculate_percentile_rank(value, position_data, metric_col):
                """Calculate what percentile an individual value falls into"""
                if pd.isna(value):
                    return None
                position_values = position_data[metric_col].dropna().values
                percentile = (position_values < value).sum() / len(position_values) * 100
                return round(percentile, 1)
            
            individual_results = []
            for _, row in analysis_data.iterrows():
                position_data = analysis_data[analysis_data[position_column] == row[position_column]]
                percentile_rank = calculate_percentile_rank(row[metric_column], position_data, metric_column)
                
                individual_results.append({
                    'Athlete': row[athlete_id_column],
                    'Position': row[position_column],
                    metric_column: round(row[metric_column], 2),
                    'Percentile Rank': percentile_rank,
                    'Category': 'Elite (>P90)' if percentile_rank and percentile_rank >= 90 else
                               'Above Average (P75-P90)' if percentile_rank and percentile_rank >= 75 else
                               'Average (P25-P75)' if percentile_rank and percentile_rank >= 25 else
                               'Below Average (<P25)' if percentile_rank else 'N/A'
                })
            
            individual_df = pd.DataFrame(individual_results)
            individual_df = individual_df.sort_values('Percentile Rank', ascending=False)
            
            st.dataframe(individual_df, use_container_width=True, height=400)
            
            # Export options
            st.header("💾 Export Data")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                # Export normative data as CSV
                csv_normative = normative_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download Normative Values (CSV)",
                    data=csv_normative,
                    file_name="cmj_normative_values.csv",
                    mime="text/csv"
                )
            
            with col2:
                # Export individual data as CSV
                csv_individual = individual_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download Individual Results (CSV)",
                    data=csv_individual,
                    file_name="cmj_individual_results.csv",
                    mime="text/csv"
                )
            
            with col3:
                # Export all data as Excel
                excel_data = to_excel({
                    'Normative Values': normative_df,
                    'Individual Results': individual_df,
                    'Raw Data': analysis_data
                })
                st.download_button(
                    label="📥 Download All Data (Excel)",
                    data=excel_data,
                    file_name="cmj_complete_analysis.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            
            # Summary statistics
            st.header("📊 Summary Statistics")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Total Athletes", len(individual_df))
            
            with col2:
                st.metric("Positions", len(positions))
            
            with col3:
                elite_count = len(individual_df[individual_df['Category'] == 'Elite (>P90)'])
                st.metric("Elite Performers", elite_count)
            
            with col4:
                st.metric("Overall Mean", f"{overall_percentiles['Mean']:.2f}")

else:
    # Instructions when no files uploaded
    st.info("👆 Please upload both CMJ data and team roster files to begin analysis")
    
    with st.expander("📋 Data Format Requirements"):
        st.markdown("""
        ### CMJ Data File
        Your CMJ data should include:
        - **Athlete identifier** (name or ID)
        - **Performance metric** (e.g., Jump Height in cm)
        - Can include additional columns (date, trial number, etc.)
        
        ### Team Roster File
        Your roster should include:
        - **Athlete identifier** (matching CMJ data)
        - **Position** (e.g., Guard, Forward, Center)
        
        ### Example Format
        
        **CMJ Data:**
        | Athlete Name | Jump Height (cm) | Date |
        |--------------|------------------|------|
        | John Smith   | 45.2            | 2024-01-15 |
        | Jane Doe     | 52.3            | 2024-01-15 |
        
        **Roster:**
        | Athlete Name | Position |
        |--------------|----------|
        | John Smith   | Forward  |
        | Jane Doe     | Guard    |
        """)
    
    with st.expander("ℹ️ How to Use This App"):
        st.markdown("""
        1. **Upload your CMJ data file** (CSV or Excel) containing performance metrics
        2. **Upload your team roster** (CSV or Excel) with athlete positions
        3. **Configure column names** in the sidebar if they differ from defaults
        4. **Review the normative values** calculated for each position (P25, P50, P75, P90)
        5. **Analyze individual athletes** and their percentile ranks
        6. **Export the results** in CSV or Excel format
        """)

# Footer
st.markdown("---")
st.markdown("Built with Streamlit | CMJ Normative Performance Analysis")
