# Notes-App-FastAPI-
Just a small notes app made using FastAPI
## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Git

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/adityaDev-2005/Notes-App-FastAPI-
cd Notes-App-FastAPI-
```

**2. Create and activate a virtual environment**
```bash
python -m venv .venv

# Linux/Mac
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

### Running the App

**4. Start the backend (Terminal 1)**
```bash
uvicorn main:app --reload
```
Backend runs at `http://127.0.0.1:8000`

**5. Serve the frontend (Terminal 2)**
```bash
python -m http.server 3000
```

**6. Open in browser**
