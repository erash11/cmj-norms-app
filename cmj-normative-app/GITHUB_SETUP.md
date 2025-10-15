# GitHub Setup and Deployment Guide

## Step 1: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right and select "New repository"
3. Name your repository (e.g., `cmj-normative-app`)
4. Add a description: "Countermovement Jump Normative Performance Analysis Tool"
5. Choose "Public" or "Private"
6. **Do NOT** initialize with README, .gitignore, or license (we already have these)
7. Click "Create repository"

## Step 2: Push Your Code to GitHub

Open your terminal and navigate to the project directory, then run:

```bash
cd cmj-normative-app
git init
git add .
git commit -m "Initial commit: CMJ normative analysis app"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/cmj-normative-app.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

## Step 3: Deploy to Streamlit Cloud

### Option A: Direct Deployment (Recommended)

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "Sign in with GitHub"
3. Click "New app"
4. Fill in the form:
   - **Repository**: Select your `cmj-normative-app` repository
   - **Branch**: `main`
   - **Main file path**: `app.py`
5. Click "Deploy!"
6. Wait a few minutes for deployment to complete
7. Your app will be live at: `https://your-username-cmj-normative-app.streamlit.app`

### Option B: Deploy Button in README

Add this badge to your README.md:

```markdown
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)
```

## Step 4: Update Your App

To update your deployed app:

```bash
git add .
git commit -m "Description of changes"
git push
```

Streamlit Cloud will automatically redeploy your app when it detects changes.

## Troubleshooting

### Issue: App won't deploy
- Check that `requirements.txt` is in the root directory
- Verify all package versions are compatible
- Check Streamlit Cloud logs for error messages

### Issue: Data files not loading
- Ensure CSV/Excel files are properly formatted
- Check column names match configuration
- Verify file encoding is UTF-8

### Issue: Performance is slow
- Consider caching with `@st.cache_data` decorator
- Limit dataset size for initial testing
- Use efficient pandas operations

## Security Considerations

- Don't commit sensitive data files to public repositories
- Use `.gitignore` to exclude private data
- Consider using Streamlit secrets for API keys or passwords (if needed)
- For private apps, use Streamlit Cloud's access controls

## Custom Domain (Optional)

To use a custom domain with Streamlit Cloud:

1. Go to app settings in Streamlit Cloud
2. Navigate to "Custom subdomain"
3. Follow the instructions to set up DNS records

## Local Development Best Practices

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Test locally before pushing:
```bash
streamlit run app.py
```

3. Use git branches for new features:
```bash
git checkout -b feature-name
# Make changes
git add .
git commit -m "Add feature description"
git push origin feature-name
# Create pull request on GitHub
```

## Support

For Streamlit-specific issues, check:
- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Community Forum](https://discuss.streamlit.io)
- [Streamlit Cloud Documentation](https://docs.streamlit.io/streamlit-community-cloud)
