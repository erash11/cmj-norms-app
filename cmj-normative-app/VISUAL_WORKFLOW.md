# Visual Workflow - How Everything Fits Together

## 🔄 Complete System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    YOUR WORKFLOW                             │
└─────────────────────────────────────────────────────────────┘

1️⃣ DATA COLLECTION
   ┌──────────────┐         ┌──────────────┐
   │ Force Decks  │         │ Team Roster  │
   │ CMJ Testing  │         │ Spreadsheet  │
   └──────┬───────┘         └──────┬───────┘
          │                        │
          ↓                        ↓
   BUFB_forcedecks.csv      2025Roster.csv
   (6,023 records)          (116 athletes)


2️⃣ DATA PREPARATION (Done ✅)
   ┌──────────────────────────────────────┐
   │ Remove trailing spaces from columns  │
   │ Ensure name formats match            │
   │ Verify position data exists          │
   └──────┬───────────────────────────────┘
          ↓
   CMJ_Data_Cleaned.csv + Roster_Cleaned.csv


3️⃣ APPLICATION DEPLOYMENT
   ┌──────────────┐
   │ GitHub Repo  │
   │ cmj-norms-app│
   └──────┬───────┘
          │
          ↓ (Auto-deploy)
   ┌──────────────────┐
   │ Streamlit Cloud  │
   │ cmj-norms.app    │
   └──────────────────┘


4️⃣ USER INTERACTION
   ┌─────────────────────────────────────┐
   │ Upload Files                        │
   │ ├─ CMJ Data (cleaned)               │
   │ └─ Roster (cleaned)                 │
   └─────────┬───────────────────────────┘
             ↓
   ┌─────────────────────────────────────┐
   │ Select Columns                      │
   │ ├─ Athlete ID: Name                 │
   │ ├─ Metric: Jump Height              │
   │ └─ Position: Position               │
   └─────────┬───────────────────────────┘
             ↓
   ┌─────────────────────────────────────┐
   │ Data Processing                     │
   │ ├─ Merge CMJ + Roster               │
   │ ├─ Calculate percentiles            │
   │ ├─ Rank athletes                    │
   │ └─ Generate statistics              │
   └─────────┬───────────────────────────┘
             ↓
   ┌─────────────────────────────────────┐
   │ Results Display                     │
   │ ├─ Normative values by position     │
   │ ├─ Individual athlete rankings      │
   │ ├─ Summary statistics               │
   │ └─ Export options                   │
   └─────────────────────────────────────┘


5️⃣ OUTPUT & ANALYSIS
   ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
   │ Normative Values │  │ Individual       │  │ Complete Excel   │
   │ CSV              │  │ Rankings CSV     │  │ Workbook         │
   └──────────────────┘  └──────────────────┘  └──────────────────┘
            │                     │                       │
            └─────────────────────┴───────────────────────┘
                                  ↓
                    ┌─────────────────────────────┐
                    │ Use for:                    │
                    │ • Training decisions        │
                    │ • Recruiting standards      │
                    │ • Progress tracking         │
                    │ • Performance research      │
                    └─────────────────────────────┘
```

---

## 📊 Data Flow Diagram

```
INPUTS                PROCESSING              OUTPUTS
─────────────────────────────────────────────────────

CMJ Data              ┌──────────────┐
6,023 tests      ────▶│              │
                      │  Column      │
Roster               │  Detection   │
116 athletes     ────▶│              │
                      └──────┬───────┘
                             │
                             ↓
                      ┌──────────────┐
                      │              │
                      │  Data Merge  │────▶ Merged Dataset
                      │  (on Name)   │     6,023 records
                      │              │     with positions
                      └──────┬───────┘
                             │
                             ↓
                      ┌──────────────┐
                      │              │
                      │  Calculate   │────▶ Position Stats
                      │  Percentiles │     (13 positions)
                      │              │
                      └──────┬───────┘
                             │
                             ↓
                      ┌──────────────┐
                      │              │
                      │  Rank        │────▶ Athlete Rankings
                      │  Athletes    │     (114 athletes)
                      │              │
                      └──────┬───────┘
                             │
                             ↓
                      ┌──────────────┐
                      │              │
                      │  Generate    │────▶ Export Files
                      │  Reports     │     (CSV + Excel)
                      │              │
                      └──────────────┘
```

---

## 🎯 Column Mapping

```
CMJ Data File                    App Internal              Display
─────────────────────────────────────────────────────────────────

Name                        →    athlete_id            →   Athlete
Jump Height (Imp-Mom)...    →    metric_column         →   Jump Height
[merged from Roster]        →    position_column       →   Position


Roster File                      App Internal              Display
─────────────────────────────────────────────────────────────────

Name                        →    athlete_id            →   (key)
Position                    →    position_column       →   Position
Jersey Number               →    (not used)            →   (ignored)
```

---

## 🔀 Data Transformation Pipeline

```
STEP 1: LOAD & CLEAN
┌─────────────────────────────────────────┐
│ Raw CSV Files                           │
│ • May have trailing spaces              │
│ • May have inconsistent formatting      │
└─────────────┬───────────────────────────┘
              ↓
         Strip whitespace
         from column names
              ↓
┌─────────────────────────────────────────┐
│ Clean DataFrames                        │
│ • Consistent column names               │
│ • Ready for processing                  │
└─────────────┬───────────────────────────┘


STEP 2: MERGE
┌─────────────┐         ┌─────────────┐
│ CMJ Data    │         │ Roster      │
│ 6,023 rows  │         │ 116 rows    │
└──────┬──────┘         └──────┬──────┘
       │                       │
       └───────┬───────────────┘
               ↓
          LEFT JOIN on Name
               ↓
┌─────────────────────────────────────────┐
│ Merged Dataset                          │
│ • 6,023 rows (all CMJ records)          │
│ • Each has position from roster         │
│ • 2 roster athletes missing (not tested)│
└─────────────┬───────────────────────────┘


STEP 3: VALIDATE
              ↓
    Remove rows with missing:
    • Position (0 rows removed)
    • Metric values (0 rows removed)
              ↓
┌─────────────────────────────────────────┐
│ Valid Analysis Dataset                  │
│ • 6,023 rows (100% valid)               │
│ • 114 unique athletes                   │
│ • 13 positions                          │
└─────────────┬───────────────────────────┘


STEP 4: CALCULATE
              ↓
    For each position:
    ├─ Calculate percentiles (P25, P50, P75, P90)
    ├─ Calculate mean & standard deviation
    ├─ Find min & max values
    └─ Count sample size
              ↓
┌─────────────────────────────────────────┐
│ Normative Values Table                  │
│ • 13 position rows                      │
│ • 1 "ALL POSITIONS" row                 │
│ • 10 statistical columns                │
└─────────────┬───────────────────────────┘


STEP 5: RANK
              ↓
    For each athlete test:
    ├─ Find their position group
    ├─ Calculate percentile rank
    ├─ Assign category (Elite/Above Avg/etc)
    └─ Sort by percentile
              ↓
┌─────────────────────────────────────────┐
│ Individual Rankings Table               │
│ • 6,023 test rows                       │
│ • Sorted by percentile (high to low)   │
│ • 5 columns                             │
└─────────────┬───────────────────────────┘


STEP 6: EXPORT
              ↓
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ Normative    │  │ Individual   │  │ Excel        │
│ Values CSV   │  │ Rankings CSV │  │ (3 sheets)   │
└──────────────┘  └──────────────┘  └──────────────┘
```

---

## 🎨 User Interface Layout

```
┌─────────────────────────────────────────────────────────────┐
│  ⚡ Countermovement Jump Normative Performance Analysis     │
│                                                             │
│  Upload your CMJ data and team roster...                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐                  ┌─────────────────────┐  │
│  │ SIDEBAR     │                  │ MAIN CONTENT        │  │
│  │             │                  │                     │  │
│  │ 📁 Upload   │                  │ 📊 CMJ Data Preview │  │
│  │ Files       │                  │ ┌─────────────────┐ │  │
│  │ ┌─────────┐ │                  │ │ [Data Table]    │ │  │
│  │ │ CMJ Data│ │                  │ └─────────────────┘ │  │
│  │ └─────────┘ │                  │                     │  │
│  │ ┌─────────┐ │                  │ 👥 Roster Preview   │  │
│  │ │ Roster  │ │                  │ ┌─────────────────┐ │  │
│  │ └─────────┘ │                  │ │ [Data Table]    │ │  │
│  │             │                  │ └─────────────────┘ │  │
│  │ ⚙️ Config   │                  │                     │  │
│  │ [Dropdowns] │                  │ 📈 Normative Values │  │
│  │ • Athlete ID│                  │ ┌─────────────────┐ │  │
│  │ • Metric    │                  │ │ [Stats Table]   │ │  │
│  │ • Position  │                  │ └─────────────────┘ │  │
│  │             │                  │                     │  │
│  │             │                  │ 👤 Individual       │  │
│  │             │                  │ ┌─────────────────┐ │  │
│  │             │                  │ │ [Rankings]      │ │  │
│  │             │                  │ └─────────────────┘ │  │
│  │             │                  │                     │  │
│  │             │                  │ 💾 Export           │  │
│  │             │                  │ [Download Buttons]  │  │
│  │             │                  │                     │  │
│  │             │                  │ 📊 Summary Stats    │  │
│  │             │                  │ [Metrics Display]   │  │
│  └─────────────┘                  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔢 Statistics Explained

### Percentiles
```
P90 ─────────────────────────  ←  Top 10% (Elite)
         
P75 ─────────────────  ←  Top 25% (Above Average)
              
P50 ─────────  ←  Median (Average)
         
P25 ───  ←  Bottom 25% (Below Average)

P10 ─  ←  Bottom 10% (Needs Improvement)
```

### Example for WR Position
```
Jump Height Distribution (Wide Receivers)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Max: 22.5"     ▲
P90: 20.1"     │ Elite
P75: 18.7"     │ Above Avg
─────────────────────────────────
Mean: 17.2"    │ Average
P50: 17.0"     │
─────────────────────────────────
P25: 15.8"     │ Below Avg
P10: 14.2"     │ Needs Work
Min: 12.1"     ▼
```

---

**This visual guide shows how everything connects!**
**Follow the workflow top to bottom for success.** 🎯
