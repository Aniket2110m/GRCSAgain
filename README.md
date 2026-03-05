# GRCS Simulator

A comprehensive Golden Record Confidence Score (GRCS) Simulator with multiple calculation modules.

## Available Applications

### Script 1: Full GRCS Platform (`script1.py`)
- 🎯 **Simulator**: Calculate GRCS scores for data matching
- 📊 **GRCS Reference Table**: View complete attribute reference
- 📖 **Technical Documentation**: Detailed methodology documentation
- ⚖️ **Weight Calculation**: ACS model calculator with L, U, S, R parameters
- 📈 **LUSR Calculation**: LUSR methodology framework

### Script 2: Citizen Golden Record Simulator (`script2.py`)
- 🎯 **Simplified Simulator**: Calculate Identity Confidence Score (ICS)
- 📊 **Visual Analytics**: Interactive contribution charts
- 🎚️ **Scenario Testing**: Adjustable match strength and source authority
- 📈 **Real-time Classification**: Golden/Silver/Grey record classification

## Deployment

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Add logo images to the `assets/` folder (optional):
   - `bihargovt-logo.png` - Bihar Government logo
   - `cipl-logo.png` - CIPL logo

3. Run the application:

**For Script 1 (Full Platform):**
```bash
streamlit run script1.py
```

**For Script 2 (Citizen Simulator):**
```bash
streamlit run script2.py
```

### Streamlit Cloud Deployment

1. Push code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Select your repository and branch
5. Set main file path: `script1.py` or `script2.py`
6. Click "Deploy"

### Render Deployment

1. Push code to GitHub
2. Create new Web Service on [Render](https://render.com)
3. Connect your repository
4. Configuration:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command (Script 1)**: 
     ```
     streamlit run script1.py --server.port=$PORT --server.address=0.0.0.0
     ```
   - **Start Command (Script 2)**: 
     ```
     streamlit run script2.py --server.port=$PORT --server.address=0.0.0.0
     ```
5. Add environment variables if needed

### Heroku Deployment

1. Create `Procfile` in project root:
```
web: sh setup.sh && streamlit run script2.py --server.port=$PORT --server.address=0.0.0.0
```

2. Create `setup.sh`:
```bash
mkdir -p ~/.streamlit/
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
```

3. Deploy:
```bash
git push heroku main
```

## Project Structure

```
.
├── script1.py                 # Full GRCS Platform
├── script2.py                 # Citizen Golden Record Simulator
├── requirements.txt           # Python dependencies
├── data/                      # Reference data files
│   ├── GRCS.xlsx
│   ├── GRCS_Technical_Documentation.docx
│   ├── Weight Calculation.docx
│   └── LUSR Calculation.docx
├── assets/                    # Static assets (logos)
│   ├── bihargovt-logo.png
│   └── cipl-logo.png
└── .streamlit/
    └── config.toml           # Streamlit configuration
```

## Environment Requirements

- Python 3.8+
- Streamlit >= 1.28.0
- Pandas
- python-docx
- openpyxl

## Configuration

The app uses `.streamlit/config.toml` for configuration. Key settings:
- Theme colors matching Bihar Government branding
- Server settings optimized for deployment
- CORS and XSRF protection enabled
