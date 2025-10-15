# 📑 CMJ Normative Analysis App - File Index

Welcome! This index will help you navigate all the files in this project.

## 🎯 START HERE

**New to this project?** Read these files in order:

1. **PROJECT_SUMMARY.md** ⭐ - Overview of what's included (5 min read)
2. **QUICKSTART.md** ⭐ - Get running in 5 minutes
3. **README.md** - Full documentation (10 min read)

## 📂 File Guide

### Core Application Files
| File | Description | Lines |
|------|-------------|-------|
| **app.py** | Main Streamlit application | 313 |
| **requirements.txt** | Python dependencies | 4 |

### Documentation Files
| File | Purpose | Best For |
|------|---------|----------|
| **PROJECT_SUMMARY.md** | Complete overview | First-time users |
| **QUICKSTART.md** | Fast setup guide | Getting started quickly |
| **README.md** | Full documentation | Complete reference |
| **GITHUB_SETUP.md** | Deployment guide | Publishing your app |
| **WORKFLOW.md** | Feature details | Understanding capabilities |
| **QUICK_REFERENCE.md** | Command cheat sheet | Daily use |
| **INDEX.md** | This file | Navigation |

### Sample Data Files
| File | Description | Records |
|------|-------------|---------|
| **sample_cmj_data.csv** | Example CMJ data | 20 athletes |
| **sample_roster.csv** | Example roster | 20 athletes, 3 positions |

### Configuration Files
| File | Purpose |
|------|---------|
| **.gitignore** | Git exclusions |
| **.github/workflows/test.yml** | CI/CD automation |

## 🎓 Learning Path

### For First-Time Users
```
1. PROJECT_SUMMARY.md    → Understand what you have
2. QUICKSTART.md         → Get it running
3. Test with sample data → See it in action
4. Try your own data     → Real analysis
```

### For Deployment
```
1. GITHUB_SETUP.md       → Step-by-step deployment
2. Create GitHub repo    → Version control
3. Deploy to Streamlit   → Go live
4. Share with team       → Collaborate
```

### For Customization
```
1. WORKFLOW.md           → Understand features
2. Review app.py         → See the code
3. Make modifications    → Customize
4. Test changes          → Verify
```

## 🚀 Quick Actions

### Run the App Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

### Test with Sample Data
1. Run the app
2. Upload `sample_cmj_data.csv`
3. Upload `sample_roster.csv`
4. Explore the results!

### Deploy to Streamlit Cloud
See **GITHUB_SETUP.md** for complete instructions

## 📊 What Each File Does

### app.py (Main Application)
The Streamlit web application that:
- Handles file uploads
- Processes and merges data
- Calculates normative percentiles
- Displays interactive tables
- Exports results

**Key Functions:**
- `load_data()` - Loads CSV/Excel files
- `calculate_percentiles()` - Computes statistical measures
- `to_excel()` - Creates multi-sheet Excel exports

### requirements.txt (Dependencies)
Lists required Python packages:
- streamlit - Web framework
- pandas - Data manipulation
- numpy - Statistical calculations
- openpyxl - Excel file support

### Sample Files (For Testing)
- **sample_cmj_data.csv** - 20 athletes, various jump heights
- **sample_roster.csv** - Position assignments (Guard/Forward/Center)

Use these to test the app before using your own data!

## 🎯 Use Case Examples

### Scenario 1: Quick Analysis
**Goal**: Analyze team data once
**Files**: QUICKSTART.md → app.py → your data
**Time**: 10 minutes

### Scenario 2: Share with Team
**Goal**: Deploy app for team use
**Files**: GITHUB_SETUP.md → GitHub → Streamlit Cloud
**Time**: 30 minutes

### Scenario 3: Custom Reports
**Goal**: Modify app for specific needs
**Files**: WORKFLOW.md → app.py (customize) → test
**Time**: 1-2 hours

## 📈 Data Flow

```
Your CMJ Data (CSV/Excel)
         ↓
     Upload to App
         ↓
Your Roster (CSV/Excel)
         ↓
     Upload to App
         ↓
   Data Validation
         ↓
    Merge by Athlete
         ↓
  Group by Position
         ↓
Calculate Percentiles
         ↓
Display Results + Export
```

## 🔍 Finding Information

**Need to know...**

- How to get started? → **QUICKSTART.md**
- What the app can do? → **PROJECT_SUMMARY.md** or **WORKFLOW.md**
- How to deploy? → **GITHUB_SETUP.md**
- Data format requirements? → **README.md** or **QUICK_REFERENCE.md**
- Command reference? → **QUICK_REFERENCE.md**
- Complete details? → **README.md**

## 📱 URLs and Links

### Development
- Local app: `http://localhost:8501`
- Streamlit docs: `https://docs.streamlit.io`

### Deployment
- Streamlit Cloud: `https://share.streamlit.io`
- Your deployed app: `https://[your-username]-cmj-normative-app.streamlit.app`

### Support
- Streamlit Community: `https://discuss.streamlit.io`
- Claude Support: `https://support.claude.com`

## ✅ Verification Checklist

Before using the app, verify you have:
- [ ] Python 3.8 or higher installed
- [ ] All files from this package
- [ ] Your CMJ data file ready
- [ ] Your team roster file ready
- [ ] Matching athlete identifiers in both files

## 🎨 Customization Guide

Want to modify the app? Check these parts of `app.py`:

- **Line 5-6**: Page configuration and title
- **Lines 30-35**: Default column names
- **Lines 47-58**: Percentile calculations
- **Lines 170-184**: Performance categories
- **Lines 227-241**: Export formats

## 💡 Pro Tips

1. **Start Simple**: Test with sample data first
2. **Verify Names**: Athlete names must match exactly
3. **Save Often**: Export your results regularly
4. **Customize Gradually**: Make one change at a time
5. **Use Git**: Version control your modifications

## 🆘 Troubleshooting

**App won't start?**
→ Check QUICKSTART.md installation steps

**Data won't load?**
→ See README.md data format section

**Deployment issues?**
→ Review GITHUB_SETUP.md troubleshooting

**Need more help?**
→ Check the specific documentation file for your task

## 📦 Complete File List

```
cmj-normative-app/
├── app.py                          (Main application)
├── requirements.txt                (Dependencies)
├── .gitignore                      (Git config)
├── PROJECT_SUMMARY.md              (Project overview)
├── README.md                       (Full documentation)
├── QUICKSTART.md                   (Quick start guide)
├── GITHUB_SETUP.md                 (Deployment guide)
├── WORKFLOW.md                     (Feature details)
├── QUICK_REFERENCE.md              (Command reference)
├── INDEX.md                        (This file)
├── sample_cmj_data.csv             (Sample data)
├── sample_roster.csv               (Sample roster)
└── .github/
    └── workflows/
        └── test.yml                (GitHub Actions)
```

## 🎉 You're All Set!

Everything you need is organized and documented. Start with **QUICKSTART.md** and you'll be analyzing CMJ data in minutes!

**Questions?** Each documentation file covers its topic in detail. The code is well-commented too!

**Ready to begin?** Run: `streamlit run app.py`

---

*Happy analyzing! 🏀📊*
