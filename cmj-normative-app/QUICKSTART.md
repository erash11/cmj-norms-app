# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Download the Files
All files are in the `cmj-normative-app` folder.

### Step 2: Install Python Dependencies
```bash
cd cmj-normative-app
pip install -r requirements.txt
```

### Step 3: Run the App Locally
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

### Step 4: Test with Sample Data
Use the included sample files:
- `sample_cmj_data.csv` - Example CMJ performance data
- `sample_roster.csv` - Example team roster

1. Click "Browse files" under "Upload CMJ Data"
2. Select `sample_cmj_data.csv`
3. Click "Browse files" under "Upload Team Roster"
4. Select `sample_roster.csv`
5. View the generated normative values!

## 📊 What You'll See

The app will display:

1. **Data Preview** - Quick view of your uploaded files
2. **Normative Values by Position** - Color-coded table showing:
   - P25 (25th percentile)
   - P50 (50th percentile/median)
   - P75 (75th percentile)
   - P90 (90th percentile)
   - Plus mean, SD, min, max for each position

3. **Individual Athlete Performance** - Each athlete's percentile rank and category:
   - Elite (>P90)
   - Above Average (P75-P90)
   - Average (P25-P75)
   - Below Average (<P25)

4. **Export Options** - Download as CSV or Excel

## 🎯 Using Your Own Data

### Your CMJ Data File Should Have:
- Column with athlete names/IDs
- Column with performance metric (e.g., jump height)
- Any additional columns (optional)

### Your Roster File Should Have:
- Column with athlete names/IDs (matching CMJ data)
- Column with positions

### Important:
- Athlete names must match EXACTLY between files
- Files can be CSV or Excel (.xlsx)
- Update column names in the sidebar if yours are different

## 📤 Deploy to GitHub and Streamlit Cloud

Follow the instructions in `GITHUB_SETUP.md` to:
1. Push your code to GitHub
2. Deploy to Streamlit Cloud for free hosting
3. Share the link with your team!

## ❓ Common Questions

**Q: What if my columns have different names?**
A: Use the sidebar configuration to update column names to match your files.

**Q: Can I use multiple metrics?**
A: Currently supports one metric at a time. Run the app separately for each metric.

**Q: What if some athletes don't have positions?**
A: The app will show a warning and exclude them from position-specific analysis.

**Q: Can I export the data?**
A: Yes! Three export options:
- Normative values (CSV)
- Individual results (CSV)
- Complete analysis (Excel with multiple sheets)

## 🆘 Need Help?

- Check `README.md` for detailed documentation
- Review `GITHUB_SETUP.md` for deployment instructions
- Open an issue on GitHub for technical problems

## 🎨 Customization Ideas

Want to enhance the app? Consider adding:
- Multiple metric support
- Time-series tracking
- Visualization charts (line graphs, box plots)
- Comparison between testing dates
- Z-score calculations
- Custom report generation

The code is well-commented and easy to modify!

---

**You're all set!** Run `streamlit run app.py` and start analyzing your CMJ data! 🏀
