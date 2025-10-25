import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO

st.set_page_config(page_title="CMJ Normative Performance Analysis", layout="wide")

# Custom CSS for Baylor branding and font
st.markdown("""
<style>
    /* Baylor Branding */
    :root {
        --baylor-green: #003015;
        --baylor-gold: #FFB81C;
    }

    /* Font styling - Helvetica */
    html, body, [class*="css"] {
        font-family: Helvetica, Arial, sans-serif;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: Helvetica, Arial, sans-serif;
        color: var(--baylor-green);
    }

    /* Streamlit specific overrides */
    .stApp {
        font-family: Helvetica, Arial, sans-serif;
    }

    /* Button styling */
    .stButton > button {
        background-color: var(--baylor-green);
        color: white;
        border: none;
    }

    .stButton > button:hover {
        background-color: var(--baylor-gold);
        color: var(--baylor-green);
    }
</style>
""", unsafe_allow_html=True)

st.title("Countermovement Jump Normative Performance Analysis")
st.markdown("Upload your CMJ data and team roster to generate position-based normative values")

st.markdown("---")

# File uploads at the top
st.header("Upload Files")
col1, col2 = st.columns(2)

with col1:
    cmj_file = st.file_uploader(
        "Upload CMJ Data (CSV/Excel)",
        type=['csv', 'xlsx'],
        help="Upload your countermovement jump performance data"
    )

with col2:
    roster_file = st.file_uploader(
        "Upload Team Roster (CSV/Excel)",
        type=['csv', 'xlsx'],
        help="Upload team roster with athlete names and positions"
    )


def load_data(file):
    """Load data from CSV or Excel file"""
    if file is not None:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)
        
        # Strip whitespace from column names
        df.columns = df.columns.str.strip()
        return df
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

def sanitize_sheet_name(name, max_length=31):
    """Sanitize string to be a valid Excel sheet name

    Excel sheet name rules:
    - Max 31 characters
    - Cannot contain: \ / ? * [ ] :
    - Cannot start or end with apostrophe
    """
    # Remove invalid characters
    invalid_chars = ['\\', '/', '?', '*', '[', ']', ':']
    for char in invalid_chars:
        name = name.replace(char, '_')

    # Remove leading/trailing apostrophes and spaces
    name = name.strip().strip("'")

    # Truncate to max length
    if len(name) > max_length:
        name = name[:max_length]

    # Ensure not empty
    if not name:
        name = "Sheet"

    return name

def to_excel(dataframes_dict):
    """Convert multiple dataframes to Excel file in memory"""
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        for sheet_name, df in dataframes_dict.items():
            # Sanitize sheet name to ensure it's valid for Excel
            clean_sheet_name = sanitize_sheet_name(sheet_name)
            df.to_excel(writer, sheet_name=clean_sheet_name, index=False)
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

        st.markdown("---")

        # Configuration options - Auto-detect with manual override option
        st.header("Configuration")

        # Get column suggestions
        cmj_numeric_cols = get_numeric_columns(cmj_data)
        cmj_text_cols = get_text_columns(cmj_data)
        roster_text_cols = get_text_columns(roster_data)

        # AUTO-DETECT ATHLETE ID COLUMN
        # Find common columns between datasets - this is almost always the athlete ID
        common_cols = list(set(cmj_data.columns) & set(roster_data.columns))
        auto_athlete_col = common_cols[0] if common_cols else (cmj_text_cols[0] if cmj_text_cols else cmj_data.columns[0])

        # AUTO-DETECT POSITION COLUMN
        # Look for columns with "position" in the name
        position_candidates = [col for col in roster_data.columns if 'position' in col.lower()]
        auto_position_col = position_candidates[0] if position_candidates else (roster_text_cols[1] if len(roster_text_cols) > 1 else (roster_text_cols[0] if roster_text_cols else roster_data.columns[-1]))

        # Default athlete ID and position (can be overridden in advanced settings)
        athlete_id_column = auto_athlete_col
        position_column = auto_position_col

        # METRIC SELECTION - This is the main user choice
        # Filter to only numeric columns for metric selection
        metric_options = cmj_numeric_cols if cmj_numeric_cols else cmj_data.columns.tolist()

        # Default to first 3 numeric columns (or fewer if less available)
        default_metrics = metric_options[:min(3, len(metric_options))]

        metric_columns = st.multiselect(
            "Select Performance Metrics (3-4 recommended)",
            options=metric_options,
            default=default_metrics,
            help="Choose 3-4 performance metrics to analyze simultaneously (e.g., Jump Height, Peak Power, Velocity)"
        )

        # Validate metric selection
        if not metric_columns:
            st.warning("Please select at least one metric")
        elif len(metric_columns) > 6:
            st.warning("Selecting more than 6 metrics may make tables difficult to read")

        # Advanced settings for manual column override
        with st.expander("Advanced Column Settings"):
            st.caption("Auto-detection usually works. Only change if needed.")

            col1, col2 = st.columns(2)

            with col1:
                athlete_id_column = st.selectbox(
                    "Athlete ID Column",
                    options=cmj_data.columns.tolist(),
                    index=cmj_data.columns.tolist().index(auto_athlete_col) if auto_athlete_col in cmj_data.columns else 0,
                    help="Column that identifies athletes (must exist in both files)",
                    key="advanced_athlete_id"
                )

            with col2:
                position_column = st.selectbox(
                    "Position Column",
                    options=roster_data.columns.tolist(),
                    index=roster_data.columns.tolist().index(auto_position_col) if auto_position_col in roster_data.columns else 0,
                    help="Column containing athlete positions",
                    key="advanced_position"
                )

        # Show what columns are being used (after advanced settings so overrides are reflected)
        metrics_display = ", ".join(metric_columns) if metric_columns else "None selected"
        st.info(f"**Using:** Athlete ID: {athlete_id_column} | Position: {position_column} | Metrics: {metrics_display}")

        # Date column selection for filtering
        # Try to detect date columns
        potential_date_cols = [col for col in cmj_data.columns if any(word in col.lower() for word in ['date', 'time', 'year'])]

        # Auto-select first date column for display (always show in individual results)
        display_date_column = potential_date_cols[0] if potential_date_cols else None

        use_date_filter = False
        date_column = None
        filtered_cmj_data = cmj_data.copy()
        date_filter_info = ""

        with st.expander("Date Filtering (Optional)"):
            st.caption("Filter data by specific date range or year")

            use_date_filter = st.checkbox(
                "Enable Date/Year Filtering",
                value=False,
                help="Enable to filter data by specific date range or year"
            )

            if use_date_filter and potential_date_cols:
                date_column = st.selectbox(
                    "Date Column",
                    options=potential_date_cols,
                    help="Select the column containing test dates"
                )

                # Try to convert to datetime
                try:
                    filtered_cmj_data[date_column] = pd.to_datetime(filtered_cmj_data[date_column])

                    # Get min and max dates
                    min_date = filtered_cmj_data[date_column].min()
                    max_date = filtered_cmj_data[date_column].max()

                    # Filter type selection
                    filter_type = st.radio(
                        "Filter by:",
                        options=["Year", "Date Range"],
                        help="Choose to filter by specific year(s) or custom date range"
                    )

                    if filter_type == "Year":
                        # Extract years
                        filtered_cmj_data['Year'] = filtered_cmj_data[date_column].dt.year
                        available_years = sorted(filtered_cmj_data['Year'].dropna().unique())

                        selected_years = st.multiselect(
                            "Select Year(s)",
                            options=available_years,
                            default=available_years,
                            help="Select one or more years to include in analysis"
                        )

                        if selected_years:
                            filtered_cmj_data = filtered_cmj_data[filtered_cmj_data['Year'].isin(selected_years)]
                            date_filter_info = f"Filtered to: {', '.join(map(str, selected_years))}"
                        else:
                            st.warning("Please select at least one year")
                            use_date_filter = False

                    else:  # Date Range
                        col1, col2 = st.columns(2)
                        with col1:
                            start_date = st.date_input(
                                "Start Date",
                                value=min_date,
                                min_value=min_date,
                                max_value=max_date
                            )
                        with col2:
                            end_date = st.date_input(
                                "End Date",
                                value=max_date,
                                min_value=min_date,
                                max_value=max_date
                            )

                        # Filter by date range
                        filtered_cmj_data = filtered_cmj_data[
                            (filtered_cmj_data[date_column] >= pd.to_datetime(start_date)) &
                            (filtered_cmj_data[date_column] <= pd.to_datetime(end_date))
                        ]
                        date_filter_info = f"Filtered to: {start_date} to {end_date}"

                except Exception as e:
                    st.error(f"Could not parse dates in column '{date_column}': {str(e)}")
                    use_date_filter = False

            elif use_date_filter and not potential_date_cols:
                st.warning("No date columns detected in CMJ data")
                use_date_filter = False
        
        # Use filtered data for analysis
        cmj_data_for_analysis = filtered_cmj_data if use_date_filter else cmj_data

        st.markdown("---")

        # Display data preview
        st.header("Data Preview")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("CMJ Data Preview")
            if use_date_filter:
                st.info(date_filter_info)
            st.dataframe(cmj_data_for_analysis.head(), width="stretch")
            st.caption(f"Total rows: {len(cmj_data_for_analysis)}")
            if use_date_filter:
                st.caption(f"(Filtered from {len(cmj_data)} total records)")
            st.caption(f"Columns: {', '.join(cmj_data_for_analysis.columns.tolist())}")
        
        with col2:
            st.subheader("Roster Preview")
            st.dataframe(roster_data.head(), width="stretch")
            st.caption(f"Total athletes: {len(roster_data)}")
            st.caption(f"Columns: {', '.join(roster_data.columns.tolist())}")
        
        st.markdown("---")

        # Stop if no metrics selected
        if not metric_columns:
            st.info("Please select at least one performance metric to analyze")
            st.stop()

        # Check if required columns exist
        if athlete_id_column not in cmj_data.columns:
            st.error(f"Column '{athlete_id_column}' not found in CMJ data")
            st.stop()

        for metric_col in metric_columns:
            if metric_col not in cmj_data.columns:
                st.error(f"Column '{metric_col}' not found in CMJ data")
                st.stop()

        if athlete_id_column not in roster_data.columns:
            st.error(f"Column '{athlete_id_column}' not found in Roster data")
            st.stop()

        if position_column not in roster_data.columns:
            st.error(f"Column '{position_column}' not found in Roster data")
            st.stop()

        # Check if metric columns are numeric
        for metric_col in metric_columns:
            if not pd.api.types.is_numeric_dtype(cmj_data[metric_col]):
                st.error(f"Column '{metric_col}' must contain numeric values")
                st.info(f"Current data type: {cmj_data[metric_col].dtype}")
                st.stop()
        
        # Merge datasets
        merged_data = pd.merge(
            cmj_data_for_analysis, 
            roster_data[[athlete_id_column, position_column]], 
            on=athlete_id_column, 
            how='left'
        )
        
        # Check for athletes without position
        no_position = merged_data[merged_data[position_column].isna()]
        if len(no_position) > 0:
            st.warning(f"{len(no_position)} athletes found in CMJ data without position information")
            with st.expander("View athletes without position"):
                st.dataframe(no_position[[athlete_id_column]], width="stretch")
        
        # Remove rows without position or any of the selected metrics
        columns_to_check = [position_column] + metric_columns
        analysis_data = merged_data.dropna(subset=columns_to_check)

        # Check if we have any data left to analyze
        if len(analysis_data) == 0:
            st.error("No valid data to analyze after removing rows with missing position or metric values.")
            st.info("Please check that:")
            st.markdown("- Athletes in CMJ data match athletes in roster")
            st.markdown("- Position column has values")
            st.markdown("- Metric columns have numeric values")
            st.stop()

        st.success(f"Successfully merged data: {len(analysis_data)} records ready for analysis")
        
        # Calculate normative values by position for all selected metrics
        st.header("Normative Values by Position")

        positions = sorted(analysis_data[position_column].unique())

        # Function to apply color gradient based on percentile column level
        def color_percentile_columns(df):
            """Apply gold-to-green gradient to entire percentile columns (Baylor branding)"""
            # Map column names to their percentile level (0-100 scale)
            column_percentile_map = {
                'P25': 25,
                'P50 (Median)': 50,
                'P75': 75,
                'P90': 90,
                'Mean': 50  # Mean typically around median
            }

            def get_color_for_percentile(percentile_level):
                """Get RGB color for a given percentile level (0-100)
                Baylor colors: Gold (#FFB81C) to Green (#003015)
                """
                # Normalize to 0-1
                norm = percentile_level / 100.0

                # Baylor Gold RGB: (255, 184, 28)
                # Baylor Green RGB: (0, 48, 21)

                # Create gradient: gold (low percentile) -> green (high percentile)
                r = int(255 * (1 - norm))
                g = int(184 - (184 - 48) * norm)
                b = int(28 - (28 - 21) * norm)

                # Text color: white for dark backgrounds
                text_color = 'white' if norm > 0.5 else 'black'

                return f'background-color: rgb({r},{g},{b}); color: {text_color}; font-weight: bold;'

            styles = pd.DataFrame('', index=df.index, columns=df.columns)

            # Apply color to entire columns based on percentile level
            for col_name, percentile_level in column_percentile_map.items():
                if col_name in df.columns:
                    color = get_color_for_percentile(percentile_level)
                    # Apply same color to all cells in this column
                    styles[col_name] = [color] * len(df)

            return styles

        # Calculate normative values for each metric
        normative_dfs = {}
        for metric_col in metric_columns:
            normative_results = []

            for position in positions:
                position_data = analysis_data[analysis_data[position_column] == position]
                percentiles = calculate_percentiles(position_data, metric_col)

                result_row = {
                    'Position': position,
                    'P25': round(percentiles['P25'], 2),
                    'P50 (Median)': round(percentiles['P50'], 2),
                    'P75': round(percentiles['P75'], 2),
                    'P90': round(percentiles['P90'], 2),
                    'Mean': round(percentiles['Mean'], 2),
                    'SD': round(percentiles['SD'], 2),
                    'Min': round(percentiles['Min'], 2),
                    'Max': round(percentiles['Max'], 2),
                    'N': int(percentiles['N'])
                }
                normative_results.append(result_row)

            normative_df = pd.DataFrame(normative_results)

            # Ensure column order is correct
            column_order = ['Position', 'P25', 'P50 (Median)', 'P75', 'P90', 'Mean', 'SD', 'Min', 'Max', 'N']
            normative_df = normative_df[column_order]

            # Calculate overall normative values
            overall_percentiles = calculate_percentiles(analysis_data, metric_col)
            overall_row = {
                'Position': 'ALL POSITIONS',
                'P25': round(overall_percentiles['P25'], 2),
                'P50 (Median)': round(overall_percentiles['P50'], 2),
                'P75': round(overall_percentiles['P75'], 2),
                'P90': round(overall_percentiles['P90'], 2),
                'Mean': round(overall_percentiles['Mean'], 2),
                'SD': round(overall_percentiles['SD'], 2),
                'Min': round(overall_percentiles['Min'], 2),
                'Max': round(overall_percentiles['Max'], 2),
                'N': int(overall_percentiles['N'])
            }
            normative_df = pd.concat([normative_df, pd.DataFrame([overall_row])], ignore_index=True)

            normative_dfs[metric_col] = normative_df

        # Display normative tables in tabs
        if len(metric_columns) == 1:
            # Single metric - no tabs needed
            styled_df = normative_dfs[metric_columns[0]].style.apply(color_percentile_columns, axis=None)
            st.dataframe(styled_df, width="stretch", height=400, use_container_width=True)

            # Download button for single metric
            csv_norm = normative_dfs[metric_columns[0]].to_csv(index=False).encode('utf-8')
            st.download_button(
                label=f"Download {metric_columns[0]} Normative Values (CSV)",
                data=csv_norm,
                file_name=f"normative_values_{metric_columns[0]}.csv",
                mime="text/csv"
            )
        else:
            # Multiple metrics - use tabs
            tabs = st.tabs(metric_columns)
            for i, metric_col in enumerate(metric_columns):
                with tabs[i]:
                    styled_df = normative_dfs[metric_col].style.apply(color_percentile_columns, axis=None)
                    st.dataframe(styled_df, width="stretch", height=400, use_container_width=True)

                    # Download button for each metric
                    csv_norm = normative_dfs[metric_col].to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label=f"Download {metric_col} Normative Values (CSV)",
                        data=csv_norm,
                        file_name=f"normative_values_{metric_col}.csv",
                        mime="text/csv",
                        key=f"download_norm_{i}"
                    )

        st.markdown("---")

        # Individual athlete analysis
        st.header("Individual Athlete Performance")

        if use_date_filter:
            st.info(f"{date_filter_info} | Showing {len(analysis_data)} test records")

        # Add percentile ranks to merged data
        def calculate_percentile_rank(value, position_data, metric_col):
            """Calculate what percentile an individual value falls into"""
            if pd.isna(value):
                return None
            position_values = position_data[metric_col].dropna().values
            if len(position_values) == 0:
                return None
            percentile = (position_values < value).sum() / len(position_values) * 100
            return round(percentile, 2)

        # Color function for individual percentile ranks
        def color_individual_percentiles(df):
            """Apply gold-to-green gradient to percentile rank columns (Baylor branding)"""
            styles = pd.DataFrame('', index=df.index, columns=df.columns)

            percentile_rank_cols = [col for col in df.columns if 'Percentile' in col]

            for col in percentile_rank_cols:
                def percentile_to_color(val):
                    if pd.isna(val) or not isinstance(val, (int, float)):
                        return ''
                    # Normalize to 0-1 (percentile is already 0-100)
                    norm = val / 100.0

                    # Baylor Gold RGB: (255, 184, 28)
                    # Baylor Green RGB: (0, 48, 21)
                    # Create gradient: gold (low) -> green (high)
                    r = int(255 * (1 - norm))
                    g = int(184 - (184 - 48) * norm)
                    b = int(28 - (28 - 21) * norm)

                    # Text color: white for dark backgrounds (higher percentiles)
                    text_color = 'white' if norm > 0.5 else 'black'

                    return f'background-color: rgb({r},{g},{b}); color: {text_color}; font-weight: bold;'

                styles[col] = df[col].apply(percentile_to_color)

            return styles

        individual_results = []
        for _, row in analysis_data.iterrows():
            position_data = analysis_data[analysis_data[position_column] == row[position_column]]

            result = {
                'Athlete': row[athlete_id_column],
                'Position': row[position_column],
            }

            # Always add test date if we have a date column
            if display_date_column and display_date_column in row.index:
                try:
                    if pd.notna(row[display_date_column]):
                        # Try to format as date
                        date_val = pd.to_datetime(row[display_date_column])
                        result['Test Date'] = date_val.strftime('%Y-%m-%d')
                    else:
                        result['Test Date'] = 'N/A'
                except:
                    # If conversion fails, show as string
                    result['Test Date'] = str(row[display_date_column]) if pd.notna(row[display_date_column]) else 'N/A'

            # Add each metric and its percentile rank (keep as floats for color styling)
            for metric_col in metric_columns:
                result[metric_col] = round(row[metric_col], 2) if pd.notna(row[metric_col]) else None
                percentile_rank = calculate_percentile_rank(row[metric_col], position_data, metric_col)
                result[f'{metric_col}_Percentile'] = percentile_rank

            individual_results.append(result)

        individual_df = pd.DataFrame(individual_results)

        # Sort by first metric's percentile rank
        first_metric_percentile = f'{metric_columns[0]}_Percentile'
        if first_metric_percentile in individual_df.columns:
            individual_df = individual_df.sort_values(first_metric_percentile, ascending=False)

        # Function to format numbers without trailing zeros
        def format_number(val):
            """Format number to remove trailing zeros"""
            if pd.isna(val) or not isinstance(val, (int, float)):
                return val
            # Format to 2 decimals, then remove trailing zeros and decimal point if needed
            return f"{val:.2f}".rstrip('0').rstrip('.')

        # Apply color styling and number formatting
        styled_individual_df = individual_df.style.apply(color_individual_percentiles, axis=None)

        # Format numeric columns (metrics and percentiles) to remove trailing zeros
        numeric_cols = [col for col in individual_df.columns if col in metric_columns or 'Percentile' in col]
        for col in numeric_cols:
            styled_individual_df = styled_individual_df.format({col: format_number})

        st.dataframe(styled_individual_df, width="stretch", height=400, use_container_width=True)
        
        # Export options
        st.header("Export Data")

        col1, col2 = st.columns(2)

        with col1:
            # Export individual data as CSV
            csv_individual = individual_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Individual Results (CSV)",
                data=csv_individual,
                file_name="cmj_individual_results.csv",
                mime="text/csv"
            )

        with col2:
            # Export all data as Excel with multiple sheets
            # Create Excel workbook with normative values for each metric
            excel_sheets = {'Individual Results': individual_df, 'Raw Data': analysis_data}
            # Add each metric's normative table as a separate sheet
            for i, metric_col in enumerate(metric_columns, 1):
                # Create short sheet name to fit within 31 char limit (including 'Norms_' prefix)
                # Truncate metric name to fit: 'Norms_' (6 chars) + metric name (25 chars max)
                short_name = metric_col[:25] if len(metric_col) > 25 else metric_col
                sheet_name = f'Norms_{short_name}'
                excel_sheets[sheet_name] = normative_dfs[metric_col]

            excel_data = to_excel(excel_sheets)
            st.download_button(
                label="Download All Data (Excel)",
                data=excel_data,
                file_name="cmj_complete_analysis.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        # Summary statistics
        st.header("Summary Statistics")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Records", len(individual_df))

        with col2:
            st.metric("Positions Analyzed", len(positions))

        with col3:
            st.metric("Metrics Analyzed", len(metric_columns))

else:
    # Instructions when no files uploaded
    st.info("Please upload both CMJ data and team roster files to begin analysis")
    
    with st.expander("Data Format Requirements"):
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
    
    with st.expander("How to Use This App"):
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
