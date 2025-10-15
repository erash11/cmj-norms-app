# Quick Reference Card - CMJ Norms App

## 🚀 One-Page Setup Guide

### Step 1: Update GitHub (2 minutes)
```
1. Go to: github.com/YOUR-USERNAME/cmj-norms-app
2. Click: cmj-normative-app/app.py
3. Click: ✏️ Edit button
4. Delete all → Paste new code
5. Commit: "Remove matplotlib dependency"
6. Wait 2-3 minutes
```

### Step 2: Upload Files (1 minute)
```
1. Go to: cmj-norms.streamlit.app
2. Upload: CMJ_Data_Cleaned.csv
3. Upload: Roster_Cleaned.csv
```

### Step 3: Select Columns (30 seconds)
```
Athlete ID: Name
Metric: Jump Height (Imp-Mom) in Inches [in]
Position: Position
```

### Step 4: View Results! 🎉
```
✅ 6,023 records analyzed
✅ 114 athletes ranked
✅ 13 positions compared
```

---

## 📥 Download Links

**Latest App Code:**
- [app.py v2.1.2](computer:///mnt/user-data/outputs/cmj-normative-app/app.py)

**Your Data Files:**
- [CMJ_Data_Cleaned.csv](computer:///mnt/user-data/outputs/CMJ_Data_Cleaned.csv)
- [Roster_Cleaned.csv](computer:///mnt/user-data/outputs/Roster_Cleaned.csv)

**Complete Guide:**
- [FINAL_DEPLOYMENT_CHECKLIST.md](computer:///mnt/user-data/outputs/FINAL_DEPLOYMENT_CHECKLIST.md)

---

## 📊 Your Data at a Glance

| Metric | Value |
|--------|-------|
| Total Tests | 6,023 |
| Unique Athletes | 114 |
| Positions | 13 |
| Jump Height Range | 6.9 - 28.8 inches |
| Average Jump | 16.5 inches |
| Top Position | OL (988 tests) |
| Most Athletes | WR (18 athletes) |

---

## 🎯 What You'll Get

### Normative Values Table
- Statistics for each position
- Mean, SD, Percentiles (P25, P50, P75, P90)
- Sample sizes

### Individual Rankings
- Every athlete's performance
- Percentile rank within position
- Performance category

### Export Options
- CSV files (normative + individual)
- Excel workbook (all data)

---

## ⚡ Quick Troubleshooting

**Error after update?**
→ Wait 3 more minutes, hard refresh (Ctrl+Shift+R)

**"No valid data"?**
→ Use the cleaned CSV files, check column names exactly

**Column not in dropdown?**
→ Re-upload files, make sure you're using cleaned versions

**Still broken?**
→ Download new logs, share with support

---

## 🔄 Version History

- **v1.0**: Initial release
- **v2.0**: Added column detection + dropdowns
- **v2.1**: Added split name handling
- **v2.1.1**: Fixed indentation bug
- **v2.1.2**: Removed matplotlib dependency
- **v2.2.0**: Simplified - single name column only ⭐ **CURRENT**

---

## 📞 App URL

**Your Live App:**
`cmj-norms.streamlit.app`

**Your GitHub Repo:**
`github.com/YOUR-USERNAME/cmj-norms-app`

---

## ✅ Success Indicators

You'll know it's working when you see:

```
✅ Successfully merged data: 6,023 records ready for analysis

📈 Normative Values by Position
[Table with 13 positions + ALL POSITIONS row]

👤 Individual Athlete Performance  
[Table with 114 athletes ranked by percentile]

💾 Export Data
[Three download buttons]

📊 Summary Statistics
Total Athletes: 114 | Positions: 13 | Elite Performers: ~11
```

---

**Last Updated:** October 15, 2025
**Status:** Production Ready (Simplified - Single Name Column)
**Version:** 2.2.0
**Next Step:** Update GitHub with app.py v2.2.0! 🚀
