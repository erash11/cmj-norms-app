# CMJ Normative Performance Analysis

A Streamlit web application for analyzing countermovement jump (CMJ) performance data and generating position-based normative values.

## Features

- 📊 Upload CMJ performance data and team rosters
- 📈 Calculate normative values by position (P25, P50, P75, P90)
- 👤 Individual athlete performance analysis with percentile rankings
- 💾 Export results in CSV and Excel formats
- 🎨 Interactive tables with color-coded performance metrics

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd cmj-normative-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Local Development

Run the Streamlit app locally:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository, branch, and `app.py`
6. Click "Deploy"

## Data Format Requirements

### CMJ Data File
Your CMJ data should include:
- **Athlete identifier** (name or ID)
- **Performance metric** (e.g., Jump Height in cm)
- Optional: date, trial number, additional metrics

Example:
```
Athlete Name,Jump Height (cm),Date
John Smith,45.2,2024-01-15
Jane Doe,52.3,2024-01-15
Mike Johnson,48.7,2024-01-15
```

### Team Roster File
Your roster should include:
- **Athlete identifier** (matching CMJ data exactly)
- **Position**

Example:
```
Athlete Name,Position
John Smith,Forward
Jane Doe,Guard
Mike Johnson,Center
```

## Usage

1. **Upload Files**: Use the sidebar to upload your CMJ data and team roster (CSV or Excel)
2. **Configure**: Adjust column names in the sidebar if your files use different column headers
3. **Analyze**: Review the normative values table showing percentiles by position
4. **Review Individual Performance**: See each athlete's percentile rank within their position
5. **Export**: Download results as CSV or Excel files

## Output

The app generates:

- **Normative Values Table**: Statistical summary by position including:
  - N (sample size)
  - Mean and Standard Deviation
  - Min and Max values
  - P25, P50 (Median), P75, P90 percentiles

- **Individual Results Table**: Each athlete's performance including:
  - Position
  - Performance metric value
  - Percentile rank within position
  - Performance category (Elite, Above Average, Average, Below Average)

- **Export Options**:
  - Normative values (CSV)
  - Individual results (CSV)
  - Complete analysis (Excel with multiple sheets)

## Configuration

You can customize column names in the sidebar:
- **CMJ Metric Column Name**: Default is "Jump Height (cm)"
- **Athlete ID Column**: Default is "Athlete Name"
- **Position Column Name**: Default is "Position"

## Example Screenshots

The app includes:
- Side-by-side data preview
- Color-coded normative values table
- Sortable individual performance rankings
- Summary statistics dashboard

## Requirements

- Python 3.8+
- streamlit
- pandas
- numpy
- openpyxl

## License

MIT License

## Support

For issues or questions, please open an issue on GitHub.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
