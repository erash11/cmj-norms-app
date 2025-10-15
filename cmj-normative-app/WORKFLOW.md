# App Workflow and Features

## 📋 Complete Workflow

### 1. Upload Phase
```
User uploads two files:
├── CMJ Data File (CSV/Excel)
│   ├── Athlete Name/ID
│   ├── Performance Metric (e.g., Jump Height)
│   └── Optional: Date, Trial, etc.
│
└── Team Roster File (CSV/Excel)
    ├── Athlete Name/ID (must match CMJ data)
    └── Position
```

### 2. Configuration Phase
```
Sidebar Settings:
├── CMJ Metric Column Name: "Jump Height (cm)"
├── Athlete ID Column: "Athlete Name"
└── Position Column Name: "Position"

(Adjust these if your files use different column names)
```

### 3. Processing Phase
```
App automatically:
├── Loads and previews both files
├── Merges data by athlete ID
├── Validates data quality
├── Groups athletes by position
└── Calculates normative percentiles
```

### 4. Analysis Output

#### A. Normative Values Table
```
Position | N  | Mean | SD  | Min  | P25  | P50  | P75  | P90  | Max
---------|-------|------|-----|------|------|------|------|------|------
Guard    | 8  | 50.8 | 2.1 | 47.3 | 49.1 | 50.7 | 52.5 | 53.8 | 53.8
Forward  | 7  | 46.0 | 1.8 | 43.5 | 45.2 | 46.3 | 46.9 | 48.2 | 48.7
Center   | 5  | 45.2 | 3.1 | 42.1 | 43.5 | 44.8 | 48.2 | 48.7 | 48.7
ALL      | 20 | 47.9 | 3.4 | 42.1 | 45.7 | 48.4 | 50.2 | 52.5 | 53.8

Color-coded: Green (high) → Yellow → Red (low)
```

#### B. Individual Performance Table
```
Athlete        | Position | Jump Height | Percentile | Category
---------------|----------|-------------|------------|------------------
Jennifer Lee   | Guard    | 53.8        | 100.0      | Elite (>P90)
Laura Harris   | Guard    | 52.6        | 87.5       | Above Average
Jane Doe       | Guard    | 52.3        | 75.0       | P75-P90
Emily Davis    | Guard    | 51.2        | 62.5       | Average
...

Sorted by percentile rank (highest to lowest)
```

#### C. Summary Statistics
```
┌─────────────────┬──────────────┬──────────────┬────────────────┐
│ Total Athletes  │  Positions   │    Elite     │  Overall Mean  │
│       20        │      3       │      4       │     47.9 cm    │
└─────────────────┴──────────────┴──────────────┴────────────────┘
```

### 5. Export Phase
```
Three Export Options:
├── 📥 Normative Values (CSV)
│   └── Position-based percentile table
│
├── 📥 Individual Results (CSV)
│   └── All athletes with percentile ranks
│
└── 📥 Complete Analysis (Excel)
    ├── Sheet 1: Normative Values
    ├── Sheet 2: Individual Results
    └── Sheet 3: Raw Merged Data
```

## 🎯 Key Features

### Data Validation
- ✅ Checks for required columns
- ✅ Identifies athletes without position data
- ✅ Validates data types
- ✅ Shows missing data warnings

### Statistical Analysis
- ✅ Calculates P25, P50, P75, P90 by position
- ✅ Computes mean, standard deviation
- ✅ Determines individual percentile ranks
- ✅ Categorizes performance levels

### User-Friendly Interface
- ✅ Drag-and-drop file uploads
- ✅ Side-by-side data preview
- ✅ Color-coded performance tables
- ✅ Sortable columns
- ✅ Responsive design

### Flexible Configuration
- ✅ Custom column name mapping
- ✅ Supports CSV and Excel formats
- ✅ Works with any position structure
- ✅ Handles multiple athletes per position

## 📊 Understanding the Output

### Percentile Interpretation

**P25 (25th Percentile)**
- 25% of athletes scored below this value
- 75% scored at or above this value
- Lower performance threshold

**P50 (Median)**
- 50% of athletes scored below this value
- 50% scored at or above this value
- Middle/typical performance

**P75 (75th Percentile)**
- 75% of athletes scored below this value
- 25% scored at or above this value
- Good performance threshold

**P90 (90th Percentile)**
- 90% of athletes scored below this value
- 10% scored at or above this value
- Elite performance threshold

### Performance Categories

| Category | Percentile Range | Interpretation |
|----------|------------------|----------------|
| Elite | ≥ P90 | Top 10% of performers in position |
| Above Average | P75 - P90 | Top 25% but not elite |
| Average | P25 - P75 | Middle 50% of performers |
| Below Average | < P25 | Bottom 25% of performers |

## 🔧 Technical Details

### Data Processing Pipeline
```python
1. File Upload → Pandas DataFrame
2. Data Validation → Check columns & types
3. Merge Operation → Join CMJ + Roster on athlete ID
4. Group By Position → Separate analysis per position
5. Calculate Percentiles → NumPy percentile function
6. Rank Individuals → Compare to position group
7. Generate Output → Tables + Export files
```

### Performance Optimization
- Efficient pandas operations
- Minimal memory footprint
- Fast percentile calculations
- Streamlined data flow

### Error Handling
- Missing column detection
- Data type validation
- Null value handling
- Merge conflict resolution

## 🚀 Future Enhancement Ideas

Consider adding these features:

1. **Multi-Metric Support**
   - Analyze multiple CMJ metrics simultaneously
   - Peak power, RSI, flight time, etc.

2. **Temporal Analysis**
   - Track changes over time
   - Compare testing sessions
   - Visualize trends

3. **Advanced Visualizations**
   - Box plots by position
   - Distribution curves
   - Radar charts for individuals

4. **Statistical Tests**
   - ANOVA between positions
   - Effect sizes
   - Confidence intervals

5. **Report Generation**
   - PDF reports with charts
   - Custom branding
   - Automated insights

6. **Database Integration**
   - Store historical data
   - Build longitudinal profiles
   - Team-wide dashboards

## 📚 Use Cases

**Strength & Conditioning Coaches**
- Monitor athlete development
- Identify training priorities
- Set performance standards

**Sports Scientists**
- Research normative values
- Compare across teams/sports
- Validate testing protocols

**Athletic Trainers**
- Return-to-play benchmarks
- Injury risk screening
- Performance monitoring

**Team Management**
- Player evaluation
- Recruitment decisions
- Position-specific standards
