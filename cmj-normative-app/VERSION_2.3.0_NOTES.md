# Version 2.3.0 - Date/Year Filtering & Time-Series Analysis

## 🎯 New Features

### 1. Date/Year Range Filtering
Filter your CMJ data by specific years or date ranges to:
- Track performance changes over time
- Compare different seasons or training periods
- Analyze trends in normative values
- Identify when athletes hit peak performance

### 2. Test Date Column in Results
Individual athlete results now include test dates so you can:
- See exactly when each test was taken
- Track individual athlete progress over time
- Identify patterns in performance timing
- Correlate performance with training phases

## 📊 How It Works

### Step 1: Enable Date Filtering

After selecting your columns, you'll see a new section in the sidebar:

```
📅 Date Filtering (Optional)
☐ Filter by Date/Year
```

Check this box to enable date filtering.

### Step 2: Select Date Column

The app will automatically detect columns with "date", "time", or "year" in the name.

Select the column containing your test dates (e.g., "Date", "Test Date", "Timestamp")

### Step 3: Choose Filter Type

**Option A: Filter by Year**
- Select one or multiple years
- Example: Select "2023" and "2024" to compare two seasons
- Great for year-over-year comparisons

**Option B: Filter by Date Range**
- Select start and end dates
- Example: "January 1, 2024" to "March 31, 2024" for spring training
- Perfect for specific training blocks

### Step 4: View Filtered Results

All analysis will update automatically:
- Normative values calculated only for selected period
- Individual rankings based on filtered data
- Test dates shown in athlete table

## 🎯 Use Cases

### 1. Year-Over-Year Comparison

**Compare 2023 vs 2024:**
1. First run: Select "2023" only
2. Export normative values
3. Second run: Select "2024" only
4. Export normative values
5. Compare the two files to see improvements

**Example Insights:**
- WR average jump height: 17.2" (2023) → 18.1" (2024) ✅ +0.9"
- P90 threshold increased from 19.5" to 20.2"
- More athletes reaching "Elite" status

### 2. Track Individual Progress

**Find athlete's performance trajectory:**
1. Enable date filtering
2. Select all years
3. Look at individual results table
4. Sort by athlete name, then by test date
5. See how each athlete's percentile changed over time

**Example:**
```
Athlete: John Smith, Position: WR
Test Date    Jump Height    Percentile    Category
2023-08-15   16.2"         P45           Average
2023-10-30   17.1"         P62           Average  
2024-01-15   18.3"         P78           Above Avg
2024-03-20   19.2"         P88           Above Avg
2024-08-10   20.5"         P92           Elite ✅
```

### 3. Seasonal Analysis

**Compare pre-season vs in-season vs off-season:**

**Pre-Season (Aug 1 - Aug 31):**
- Average: 16.8"
- P90: 19.5"

**In-Season (Sep 1 - Nov 30):**
- Average: 17.2"
- P90: 20.1"

**Off-Season (Dec 1 - Jul 31):**
- Average: 17.5"
- P90: 20.4"

**Insight:** Athletes perform best after off-season training!

### 4. Training Program Evaluation

**Did the new jump program work?**

**Before Program (Jan-Mar 2023):**
- Team average: 16.5"
- Elite performers: 8 athletes

**After Program (Jan-Mar 2024):**
- Team average: 17.8" ✅ +1.3"
- Elite performers: 14 athletes ✅ +6

**Conclusion:** Program was successful!

### 5. Position-Specific Trends

**Track position group improvements:**

Filter to 2023 → Record WR P50 = 17.0"
Filter to 2024 → Record WR P50 = 18.2"

**WRs improved by 1.2" on average!**

## 📋 New Table Format

### Individual Results Table (With Dates)

When date filtering is enabled, the table includes:

| Athlete | Position | Jump Height | Percentile Rank | Category | Test Date |
|---------|----------|-------------|-----------------|----------|-----------|
| John Smith | WR | 20.5 | 92.3 | Elite (>P90) | 2024-08-10 |
| Jane Doe | CB | 19.8 | 89.1 | Above Average | 2024-08-12 |
| ... | ... | ... | ... | ... | ... |

**Benefits:**
- ✅ See exactly when each test occurred
- ✅ Sort by date to see chronological progression
- ✅ Filter in Excel to analyze specific athletes over time
- ✅ Identify testing frequency patterns

## 🎓 Advanced Analysis Workflows

### Workflow 1: Multi-Year Comparison Report

1. **Export 2023 Data:**
   - Filter to 2023
   - Download normative values CSV
   - Rename file: "normative_2023.csv"

2. **Export 2024 Data:**
   - Filter to 2024
   - Download normative values CSV
   - Rename file: "normative_2024.csv"

3. **Compare in Excel:**
   - Open both files
   - Create comparison table
   - Calculate % change for each position

### Workflow 2: Individual Athlete Timeline

1. **Export All Data:**
   - Enable date filter but select ALL years
   - Download individual results CSV
   - File includes ALL tests with dates

2. **Analyze in Excel:**
   - Filter by athlete name
   - Sort by Test Date
   - Create line chart of percentile over time
   - Identify trends and patterns

### Workflow 3: Cohort Analysis

**Track a recruiting class:**

1. Filter to when they arrived (e.g., Aug 2022)
2. Export baseline data
3. Filter to each subsequent year
4. Track their collective improvement

### Workflow 4: Training Block Analysis

**Evaluate specific training periods:**

1. **Block 1 (Jan-Mar):** Strength focus
   - Export data, average = 16.5"

2. **Block 2 (Apr-Jun):** Power focus
   - Export data, average = 17.8" (+1.3")

3. **Block 3 (Jul-Aug):** Speed focus
   - Export data, average = 17.2" (-0.6")

**Insight:** Power training most effective for jump height!

## 🔍 Date Column Detection

The app automatically detects date columns by looking for these keywords:
- "date"
- "time" 
- "year"
- "timestamp"

**Supported Date Formats:**
- MM/DD/YYYY (10/08/2025)
- YYYY-MM-DD (2025-10-08)
- DD/MM/YYYY (08/10/2025)
- Mon DD, YYYY (Oct 08, 2025)
- And most other common formats

**Your Data:** Based on your CMJ file, you have a "Date" column in format: MM/DD/YYYY ✅

## 📊 Filtering Status Display

### In Data Preview

When filtering is active, you'll see:
```
📊 CMJ Data Preview
📅 Filtered to: 2024
Total rows: 3,245
(Filtered from 6,023 total records)
```

### In Results Section

```
👤 Individual Athlete Performance
📅 Filtered to: 2024 | Showing 3,245 test records
```

Clear visual indicators so you always know what data you're analyzing!

## ⚙️ Configuration Options

### Year Filter
- **Type:** Multi-select dropdown
- **Options:** All years found in your data
- **Default:** All years selected
- **Can Select:** Single year or multiple years
- **Example:** Select [2023, 2024] to compare two seasons

### Date Range Filter
- **Type:** Date picker (start and end)
- **Range:** Limited to dates in your data
- **Default:** Full date range
- **Example:** Jan 1, 2024 to Dec 31, 2024

## 💡 Pro Tips

### Tip 1: Compare Before/After Training
1. Filter to 4 weeks before program starts
2. Export data (baseline)
3. Filter to 4 weeks after program ends
4. Export data (post-training)
5. Compare percentiles to measure improvement

### Tip 2: Identify Seasonal Fatigue
1. Compare early season (Aug-Sep) vs late season (Nov-Dec)
2. Look for drops in average or P90 values
3. May indicate need for recovery protocols

### Tip 3: Track Elite Athlete Development
1. Filter to current year
2. Sort individual results by percentile (descending)
3. Note top performers
4. Filter to previous year
5. Check if same athletes were elite then
6. Identifies emerging vs. consistent elite athletes

### Tip 4: Position Group Benchmarking
1. Filter to most recent month
2. Check position P50 values
3. Use as current recruiting benchmarks
4. Update monthly for latest standards

### Tip 5: Longitudinal Analysis
Export individual results with ALL years selected, then:
- Import to Excel
- Create pivot table
- Athlete name as rows
- Year as columns  
- Average jump height as values
- See everyone's year-by-year progression

## 🎯 Expected Results

### Your Data (With Filtering)

**Full Dataset:**
- 6,023 tests total
- Date range: October 2022 - October 2025
- 114 athletes

**Filter to 2024:**
- ~2,000 tests (estimated)
- 100+ athletes tested
- Single season analysis

**Filter to Recent (Last 3 months):**
- ~500 tests (estimated)
- Current performance snapshot
- Most relevant for present decisions

## 📈 Visual Indicators

### Sidebar Status
```
☑ Filter by Date/Year  [ENABLED]
Date Column: Date
Filter by: Year
Select Year(s): [2024] ✓
```

### Data Preview
```
📊 CMJ Data Preview
📅 Filtered to: 2024
Total rows: 2,156
(Filtered from 6,023 total records)
```

### Results Header
```
📈 Normative Values by Position
📅 Filtered to: 2024 | Based on 2,156 records
```

## ⚠️ Important Notes

### Note 1: Percentiles Recalculate
When you filter by date, percentiles are recalculated based ONLY on the filtered data.

**Example:**
- 2023: John Smith's 18.5" = P75 (above average that year)
- 2024: John Smith's 18.5" = P60 (average - team improved!)

**This is correct behavior!** Percentiles are relative to the comparison group.

### Note 2: Sample Size Matters
If you filter to a very small date range (e.g., one week), sample sizes will be small and percentiles less reliable.

**Recommendation:** Aim for at least 20-30 tests per position for reliable statistics.

### Note 3: Missing Dates
If some tests don't have dates, they will be excluded when date filtering is enabled.

**Solution:** Make sure all tests in your CMJ data have dates recorded.

### Note 4: Multiple Tests Per Day
If an athlete has multiple tests on the same date, all will be included in the analysis.

**Best Practice:** Use the "best" test from each day in your CMJ export.

## 🔄 Workflow Example: Complete Analysis

### Goal: Evaluate 2024 Performance vs. Historical

**Step 1: Export Historical Baseline (2022-2023)**
1. Enable date filter
2. Select years: 2022, 2023
3. Download normative values
4. Save as "baseline_2022-2023.csv"

**Step 2: Export Current Performance (2024)**
1. Change filter to: 2024
2. Download normative values  
3. Save as "current_2024.csv"

**Step 3: Create Comparison Table**
Open Excel, create:

| Position | 2022-23 P50 | 2024 P50 | Change | % Change |
|----------|-------------|----------|--------|----------|
| WR | 17.0" | 18.2" | +1.2" | +7.1% ✅ |
| CB | 16.8" | 17.9" | +1.1" | +6.5% ✅ |
| RB | 17.5" | 18.0" | +0.5" | +2.9% |
| ... | ... | ... | ... | ... |

**Step 4: Identify Top Improvers**
1. Export individual results (all years)
2. Sort by athlete, then date
3. Calculate each athlete's change
4. Top 10 improvers get recognition!

## 📥 Updated Files

**Latest Version:**
- [app.py v2.3.0](computer:///mnt/user-data/outputs/cmj-normative-app/app.py) ⭐

**Your Data Files:**
- [CMJ_Data_Cleaned.csv](computer:///mnt/user-data/outputs/CMJ_Data_Cleaned.csv) - Ready to use!
- [Roster_Cleaned.csv](computer:///mnt/user-data/outputs/Roster_Cleaned.csv) - Ready to use!

## 🚀 Deployment

1. Download app.py v2.3.0
2. Update GitHub: `cmj-normative-app/app.py`
3. Commit: "Add date filtering and time-series analysis - v2.3.0"
4. Wait 2-3 minutes
5. Test with your data!

---

**Version:** 2.3.0
**Date:** October 15, 2025
**Status:** Production Ready
**Key Feature:** Time-series analysis with date filtering 🎉
