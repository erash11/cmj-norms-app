# Quick Reference Card

## 🚀 Essential Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py

# Push to GitHub
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR-USERNAME/REPO-NAME.git
git push -u origin main
```

## 📊 Required Data Format

### CMJ Data File (CSV/Excel)
```
Athlete Name,Jump Height (cm),Date
John Smith,45.2,2024-01-15
Jane Doe,52.3,2024-01-15
```

### Roster File (CSV/Excel)
```
Athlete Name,Position
John Smith,Forward
Jane Doe,Guard
```

## 🎯 Default Column Names

- **Athlete ID**: "Athlete Name"
- **CMJ Metric**: "Jump Height (cm)"
- **Position**: "Position"

💡 Change these in the sidebar if your files differ!

## 📈 Output Metrics

| Metric | Description |
|--------|-------------|
| P25 | 25th percentile |
| P50 | Median (50th percentile) |
| P75 | 75th percentile |
| P90 | 90th percentile |
| Mean | Average value |
| SD | Standard deviation |
| N | Sample size |

## 🏆 Performance Categories

| Category | Percentile | Description |
|----------|------------|-------------|
| Elite | ≥P90 | Top 10% |
| Above Average | P75-P90 | Top 25% |
| Average | P25-P75 | Middle 50% |
| Below Average | <P25 | Bottom 25% |

## 📥 Export Options

1. **Normative Values CSV** - Percentiles by position
2. **Individual Results CSV** - All athlete rankings
3. **Complete Excel** - All data in multiple sheets

## 🔧 Sidebar Configuration

**CMJ Metric Column Name**: The column with performance data
**Athlete ID Column**: The column that identifies athletes (must match in both files)
**Position Column Name**: The column with position information

## ⚠️ Common Issues

| Issue | Solution |
|-------|----------|
| Column not found | Update column names in sidebar |
| Athletes without position | Check athlete names match exactly |
| No data showing | Verify file format (CSV/Excel) |
| Import error | Run `pip install -r requirements.txt` |

## 📱 Access URLs

- **Local**: http://localhost:8501
- **Streamlit Cloud**: https://your-app-name.streamlit.app
- **Deploy**: https://share.streamlit.io

## 📚 Documentation Files

| File | Purpose |
|------|---------|
| QUICKSTART.md | 5-minute setup |
| GITHUB_SETUP.md | Deployment guide |
| README.md | Full documentation |
| WORKFLOW.md | Feature details |
| PROJECT_SUMMARY.md | Overview |

## 💡 Tips

✅ Test with sample files first
✅ Athlete names must match EXACTLY between files
✅ Use UTF-8 encoding for CSV files
✅ Keep position names consistent
✅ Export data before closing browser

## 🆘 Support

- Check error messages in the app
- Review documentation files
- Verify data format requirements
- Test with sample data files

## 🎨 Customization

Edit `app.py` to modify:
- Color schemes
- Percentile values
- Category thresholds
- Export formats
- Statistical measures

---

**Quick Start**: Install → Run → Upload → Export!
