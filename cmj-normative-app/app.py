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


def load_data(file):
    """Load data from CSV or Excel file"""
    if file is not None:
        if file.name.endswith('.csv'):
            return pd.read_csv(file)
        else:
            return pd.read_excel(file)
    return None

def combine_name_columns(df, first_name_col, last_name_col, combined_col_name="Full Name"):
    """Combine first and last name columns into a single column"""
    df = df.copy()
    df[combined_col_name] = df[first_name_col].astype(str) + " " + df[last_name_col].astype(str)
    return df

def detect_name_columns(df):
    """Detect if dataframe has separate first/last name columns"""
    columns_lower = [col.lower() for col in df.columns]
    
    # Check for first name variations
    first_name_patterns = ['first name', 'firstname', 'first', 'fname', 'given name']
    last_name_patterns = ['last name', 'lastname', 'last', 'lname', 'surname', 'family name']
    
    first_col = None
    last_col = None
    
    for col, col_lower in zip(df.columns, columns_lower):
        if any(pattern in col_lower for pattern in first_name_patterns):
            first_col = col
        if any(pattern in col_lower for pattern in last_name_patterns):
            last_col = col
    
    return first_col, last_col

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

def get_numeric_columns(df):
    """Get list of numeric columns from dataframe"""
    return df.select_dtypes(include=[np.number]).columns.tolist()

def get_text_columns(df):
    """Get list of text/object columns from dataframe"""
    return df.select_dtypes(include=['object', 'string']).columns.tolist()

# Main application logic
if cmj_file is not None and roster_file is not None:
    
    # Load data
    cmj_data = load_data(cmj_file)
    roster_data = load_data(roster_file)
    
    if cmj_data is not None and roster_data is not None:
        
        # Check for split name columns in roster
        roster_first_col, roster_last_col = detect_name_columns(roster_data)
        cmj_first_col, cmj_last_col = detect_name_columns(cmj_data)
        
        # Handle split names in roster
        if roster_first_col and roster_last_col:
            st.info(f"📝 Detected split name columns in roster: '{roster_first_col}' and '{roster_last_col}'. Combining them...")
            roster_data = combine_name_columns(roster_data, roster_first_col, roster_last_col, "Full Name")
            st.success("✅ Combined roster names into 'Full Name' column")
        
        # Handle split names in CMJ data
        if cmj_first_col and cmj_last_col:
            st.info(f"📝 Detected split name columns in CMJ data: '{cmj_first_col}' and '{cmj_last_col}'. Combining them...")
            cmj_data = combine_name_columns(cmj_data, cmj_first_col, cmj_last_col, "Full Name")
            st.success("✅ Combined CMJ names into 'Full Name' column")
        
        # Configuration options - Dynamic based on uploaded data
        st.sidebar.header("⚙️ Configuration")
        
        # Get column suggestions
        cmj_numeric_cols = get_numeric_columns(cmj_data)
        cmj_text_cols = get_text_columns(cmj_data)
        roster_text_cols = get_text_columns(roster_data)
        
        # Find common columns between datasets for athlete ID
        common_cols = list(set(cmj_data.columns) & set(roster_data.columns))
        
        # Smart defaults
        default_athlete_col = common_cols[0] if common_cols else (cmj_text_cols[0] if cmj_text_cols else cmj_data.columns[0])
        default_metric_col = cmj_numeric_cols[0] if cmj_numeric_cols else cmj_data.columns[-1]
        default_position_col = roster_text_cols[1] if len(roster_text_cols) > 1 else (roster_text_cols[0] if roster_text_cols else roster_data.columns[-1])
        
        # Column selection dropdowns
        athlete_id_column = st.sidebar.selectbox(
            "Athlete ID Column",
            options=cmj_data.columns.tolist(),
            index=cmj_data.columns.tolist().index(default_athlete_col) if default_athlete_col in cmj_data.columns else 0,
            help="Column that identifies athletes (must exist in both files)"
        )
        
        metric_column = st.sidebar.selectbox(
            "CMJ Metric Column",
            options=cmj_data.columns.tolist(),
            index=cmj_data.columns.tolist().index(default_metric_col) if default_metric_col in cmj_data.columns else 0,
            help="Column containing jump performance metric (numeric)"
        )
        
        position_column = st.sidebar.selectbox(
            "Position Column",
            options=roster_data.columns.tolist(),
            index=roster_data.columns.tolist().index(default_position_col) if default_position_col in roster_data.columns else 0,
            help="Column containing athlete positions"
        )
        
        # Display data preview
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 CMJ Data Preview")
            st.dataframe(cmj_data.head(), width="stretch")
            st.caption(f"Total rows: {len(cmj_data)}")
            st.caption(f"Columns: {', '.join(cmj_data.columns.tolist())}")
        
        with col2:
            st.subheader("👥 Roster Preview")
            st.dataframe(roster_data.head(), width="stretch")
            st.caption(f"Total athletes: {len(roster_data)}")
            st.caption(f"Columns: {', '.join(roster_data.columns.tolist())}")
        
        # Manual name combination option
        st.sidebar.markdown("---")
        st.sidebar.subheader("🔧 Advanced Options")
        
        # Option to manually combine name columns
        combine_roster_names = st.sidebar.checkbox(
            "Combine Roster Name Columns",
            help="Check this if your roster has separate First/Last name columns that need to be combined"
        )
        
        if combine_roster_names:
            roster_text_cols = get_text_columns(roster_data)
            col1, col2 = st.sidebar.columns(2)
            with col1:
                roster_first = st.selectbox(
                    "First Name Column",
                    options=roster_text_cols,
                    key="roster_first"
                )
            with col2:
                roster_last = st.selectbox(
                    "Last Name Column", 
                    options=roster_text_cols,
                    key="roster_last"
                )
            
            if roster_first and roster_last:
                roster_data = combine_name_columns(roster_data, roster_first, roster_last, "Full Name")
                st.sidebar.success("✅ Combined into 'Full Name'")
        
        combine_cmj_names = st.sidebar.checkbox(
            "Combine CMJ Name Columns",
            help="Check this if your CMJ data has separate First/Last name columns that need to be combined"
        )
        
        if combine_cmj_names:
            cmj_text_cols = get_text_columns(cmj_data)
            col1, col2 = st.sidebar.columns(2)
            with col1:
                cmj_first = st.selectbox(
                    "First Name Column",
                    options=cmj_text_cols,
                    key="cmj_first"
                )
            with col2:
                cmj_last = st.selectbox(
                    "Last Name Column",
                    options=cmj_text_cols,
                    key="cmj_last"
                )
            
            if cmj_first and cmj_last:
                cmj_data = combine_name_columns(cmj_data, cmj_first, cmj_last, "Full Name")
                st.sidebar.success("✅ Combined into 'Full Name'")
        
        st.sidebar.markdown("---")
        
        # Check if required columns exist
        if athlete_id_column not in cmj_data.columns:
            st.error(f"❌ Column '{athlete_id_column}' not found in CMJ data")
            st.stop()
        
        if metric_column not in cmj_data.columns:
            st.error(f"❌ Column '{metric_column}' not found in CMJ data")
            st.stop()
            
        if athlete_id_column not in roster_data.columns:
            st.error(f"❌ Column '{athlete_id_column}' not found in Roster data")
            st.stop()
            
        if position_column not in roster_data.columns:
            st.error(f"❌ Column '{position_column}' not found in Roster data")
            st.stop()
        
        # Check if metric column is numeric
        if not pd.api.types.is_numeric_dtype(cmj_data[metric_column]):
            st.error(f"❌ Column '{metric_column}' must contain numeric values")
            st.info(f"Current data type: {cmj_data[metric_column].dtype}")
            st.stop()
        
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
                st.dataframe(no_position[[athlete_id_column]], width="stretch")
            
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
                width="stretch",
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
            
            st.dataframe(individual_df, width="stretch", height=400)
            
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
