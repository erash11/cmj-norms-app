# Handling Split Name Columns - User Guide

## 🎯 The Problem

Your data files have **different name formats**:

**CMJ Data (Combined Names):**
```
Athlete Name
John Smith
Jane Doe
```

**Roster (Split Names):**
```
First Name | Last Name
John       | Smith
Jane       | Doe
```

The app can't match athletes because the column structures don't match!

## ✅ The Solution

The app now has **TWO ways** to handle this:

### Method 1: Automatic Detection (Easiest!) ⭐

The app automatically detects and combines split name columns!

**How it works:**
1. Upload your files
2. App looks for columns named:
   - "First Name", "First", "FirstName", "Given Name"
   - "Last Name", "Last", "LastName", "Surname"
3. If found, automatically combines them into "Full Name"
4. You'll see a message: ✅ "Combined roster names into 'Full Name' column"

**Supported column name variations:**
- First Name / Last Name
- FirstName / LastName
- First / Last
- Given Name / Surname
- FName / LName

### Method 2: Manual Combination (For Custom Column Names)

If your columns have unique names, use the manual option:

**Steps:**
1. Upload your files
2. In the sidebar, check ☑️ "Combine Roster Name Columns"
3. Select your first name column from dropdown
4. Select your last name column from dropdown
5. App combines them into "Full Name"
6. Continue with column selection

## 📊 Example Scenarios

### Scenario 1: Roster has split names, CMJ has combined

**Your Files:**
```
roster.csv:
├── First Name
├── Last Name
└── Position

cmj_data.csv:
├── Athlete Name
└── Jump Height
```

**What the app does:**
1. Detects "First Name" and "Last Name" in roster
2. Combines them into "Full Name"
3. You select:
   - Athlete ID: "Athlete Name" (from CMJ) or "Full Name" (from roster)
   - Both will now match!

### Scenario 2: Both files have split names

**Your Files:**
```
roster.csv:
├── First
├── Last
└── Pos

cmj_data.csv:
├── FirstName
├── LastName
└── Height
```

**What the app does:**
1. Detects and combines roster: "First" + "Last" → "Full Name"
2. Detects and combines CMJ: "FirstName" + "LastName" → "Full Name"
3. Both files now have matching "Full Name" column!

### Scenario 3: Custom column names (Manual mode needed)

**Your Files:**
```
roster.csv:
├── GivenName    ← Not auto-detected
├── FamilyName   ← Not auto-detected
└── Position

cmj_data.csv:
├── Player
└── JumpHeight
```

**What you do:**
1. Check ☑️ "Combine Roster Name Columns"
2. Select "GivenName" as first name
3. Select "FamilyName" as last name
4. App creates "Full Name"
5. Select "Full Name" as Athlete ID column

## 🔧 Step-by-Step Walkthrough

### Using Automatic Detection

```
1. Upload roster file with split names
   ↓
2. Upload CMJ file with combined names
   ↓
3. App displays: "📝 Detected split name columns..."
   ↓
4. App displays: "✅ Combined roster names into 'Full Name' column"
   ↓
5. In data preview, you'll see new "Full Name" column
   ↓
6. Select "Full Name" from Athlete ID dropdown
   ↓
7. Continue with analysis!
```

### Using Manual Combination

```
1. Upload both files
   ↓
2. Scroll down in sidebar to "🔧 Advanced Options"
   ↓
3. Check ☑️ "Combine Roster Name Columns"
   ↓
4. Two dropdowns appear side-by-side
   ↓
5. Left dropdown: Select first name column
   ↓
6. Right dropdown: Select last name column
   ↓
7. App displays: "✅ Combined into 'Full Name'"
   ↓
8. Refresh data preview - see new "Full Name" column
   ↓
9. Select "Full Name" in Athlete ID dropdown
   ↓
10. Continue with analysis!
```

## 📱 User Interface Elements

### Automatic Detection Message
```
┌────────────────────────────────────────────────┐
│  ℹ️ Detected split name columns in roster:    │
│     'First Name' and 'Last Name'.              │
│     Combining them...                          │
├────────────────────────────────────────────────┤
│  ✅ Combined roster names into 'Full Name'     │
│     column                                     │
└────────────────────────────────────────────────┘
```

### Manual Combination Controls
```
┌─────────────────────────────────┐
│  🔧 Advanced Options            │
├─────────────────────────────────┤
│  ☑️ Combine Roster Name Columns│
│                                  │
│  First Name Column    Last Name │
│  [First Name ▼]      [Last ▼]  │
│                                  │
│  ✅ Combined into 'Full Name'   │
└─────────────────────────────────┘
```

## ⚠️ Common Issues & Solutions

### Issue 1: Names still don't match after combining
**Symptom:** Warning message shows athletes without positions

**Causes & Solutions:**
1. **Extra spaces:** "John Smith " vs "John Smith"
   - Solution: The app trims spaces automatically
   
2. **Different capitalization:** "john smith" vs "John Smith"
   - Solution: Names are case-sensitive; ensure consistent formatting
   
3. **Middle names:** "John A Smith" vs "John Smith"
   - Solution: Ensure both files have same format
   
4. **Nicknames:** "Mike Johnson" vs "Michael Johnson"
   - Solution: Use consistent names in both files

### Issue 2: Automatic detection doesn't work
**Symptom:** No message about combining names

**Solution:** Use manual combination:
- Check your column names
- They might not match common patterns
- Use the "Combine Name Columns" checkbox

### Issue 3: Wrong columns combined
**Symptom:** "Full Name" column has weird values

**Solution:**
1. Uncheck the manual combination box
2. Refresh the page (F5)
3. Re-upload files
4. Select correct columns in manual mode

### Issue 4: "Full Name" column not appearing in dropdown
**Symptom:** Don't see "Full Name" in Athlete ID dropdown

**Solution:**
1. Refresh the data preview
2. Check that combination was successful (look for ✅ message)
3. Scroll through dropdown - it might be at the bottom
4. Try re-uploading files

## 🎨 Visual Comparison

### Before Name Combination
```
Roster:                          CMJ Data:
┌──────────┬──────────┐         ┌────────────────┐
│ First    │ Last     │         │ Athlete Name   │
├──────────┼──────────┤         ├────────────────┤
│ John     │ Smith    │         │ John Smith     │
│ Jane     │ Doe      │         │ Jane Doe       │
└──────────┴──────────┘         └────────────────┘
        ↓                                ↓
    NO MATCH! ❌                   NO MATCH! ❌
```

### After Name Combination
```
Roster:                          CMJ Data:
┌──────────────────┐             ┌────────────────┐
│ Full Name        │             │ Athlete Name   │
├──────────────────┤             ├────────────────┤
│ John Smith       │   ←→        │ John Smith     │
│ Jane Doe         │   ←→        │ Jane Doe       │
└──────────────────┘             └────────────────┘
        ↓                                ↓
    PERFECT MATCH! ✅            PERFECT MATCH! ✅
```

## 📋 Quick Reference

| Situation | Detection | Action Required |
|-----------|-----------|-----------------|
| Roster has "First Name" & "Last Name" | Automatic ✅ | None - just upload |
| CMJ has "FirstName" & "LastName" | Automatic ✅ | None - just upload |
| Custom column names | Manual 🔧 | Check box + select columns |
| Both files have split names | Automatic ✅ | None - both combined |
| Names already match | None needed | Just upload and go! |

## 💡 Pro Tips

1. **Preview First:** Always check the data preview to see if "Full Name" was created
2. **Consistent Formatting:** Make sure name formats match in both files
3. **Test with Sample Data:** Use the included sample files to understand the feature
4. **One at a Time:** Combine roster names first, check preview, then select columns
5. **Save Time:** If you regularly have split names, ask your data provider to combine them

## 🎯 Best Practices

### For Data Preparation
```
✅ GOOD: Use consistent name format in all files
✅ GOOD: "First Name" and "Last Name" (will auto-detect)
✅ GOOD: Trim extra spaces
✅ GOOD: Consistent capitalization

❌ AVOID: Mixing "FirstName" with "first_name"
❌ AVOID: Extra spaces in names
❌ AVOID: Inconsistent formats between files
❌ AVOID: Using nicknames in one file, full names in other
```

### For Using the App
```
✅ Upload files → Check for auto-detection message
✅ Verify "Full Name" in data preview
✅ Select "Full Name" in Athlete ID dropdown
✅ Check for "athletes without position" warning

❌ Don't skip the data preview
❌ Don't assume columns matched
❌ Don't ignore warning messages
```

## 🧪 Test Cases

Use these sample files to test the feature:

1. **sample_roster_split_names.csv** - Has First Name, Last Name columns
2. **sample_cmj_combined_names.csv** - Has Athlete Name column
3. Upload both and watch the app combine them automatically!

## 🆘 Still Having Issues?

### Checklist
- [ ] Both files uploaded successfully?
- [ ] Saw the "Combined names" success message?
- [ ] "Full Name" column appears in data preview?
- [ ] Selected "Full Name" (or equivalent) in Athlete ID dropdown?
- [ ] Names spelled exactly the same in both files?
- [ ] No extra spaces or special characters?

### Debug Mode
1. Export the "Raw Data" sheet from Excel export
2. Look at the merged data to see what's matching
3. Check for any discrepancies in name formatting

---

**The name combination feature makes it easy to work with different file formats!** 🎉
