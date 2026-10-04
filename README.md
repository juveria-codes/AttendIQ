# AttendIQ 🎯

**Making attendance faster using AI.**

AttendIQ is a web-based smart attendance system built with Python and Streamlit. Teachers create classes and share a QR/join link, students enroll in one click, and attendance is verified using AI-based face and voice recognition, replacing slow, manual roll calls.


---

## ✨ Features

- **Role-based access:** separate dashboards for teachers and students
- **Secure authentication:** passwords hashed with bcrypt
- **QR-code class enrollment:** teachers share a QR code or join link, and students are enrolled automatically via a `join-code` URL parameter
- **Face recognition:** identifies students from a photo using dlib-based face embeddings
- **Voice recognition:** speaker embeddings (Resemblyzer + Librosa) as an additional verification layer
- **Cloud database:** user, class and attendance data stored in Supabase
- **Clean, responsive UI** built entirely in Streamlit

## 🛠️ Tech Stack

| Area | Technology |
|---|---|
| Language | Python |
| Frontend / App framework | Streamlit |
| Computer vision | dlib, face_recognition_models |
| Audio / speaker recognition | Librosa, Resemblyzer |
| Data & ML utilities | NumPy, pandas, scikit-learn |
| Database / Backend | Supabase |
| Security | bcrypt |
| QR codes | Segno |
| Image handling | Pillow |

## 📁 Project Structure

```
AttendIQ/
├── app.py                # Entry point: routes between home, teacher and student screens
├── requirements.txt      # Python dependencies
├── .gitignore
└── src/
    ├── screens/          # Home, teacher and student screens
    ├── components/       # Reusable UI pieces (e.g. auto-enroll dialog)
    └── ui/               # Static assets (logo, etc.)
```

## 🚀 Getting Started

### Prerequisites
- Python 3.11 or higher
- A [Supabase](https://supabase.com) project

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/juveria-codes/AttendIQ.git
cd AttendIQ

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Configuration

Create `.streamlit/secrets.toml` (or set environment variables, depending on how your code reads them) with your Supabase credentials:

```toml
SUPABASE_URL = "your-supabase-project-url"
SUPABASE_KEY = "your-supabase-anon-key"
```

> ⚠️ Never commit secrets to GitHub. Make sure `.streamlit/secrets.toml` is listed in `.gitignore`.

### Run the app

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

## 🔄 How It Works

1. **Teacher** signs up, creates a class and gets a QR code and join link.
2. **Student** scans the QR code or opens the link, logs in and is auto-enrolled in the class.
3. **Attendance** is marked by verifying the student's face (and voice) against their enrolled profile.
4. Records are stored in Supabase and available to the teacher.

## 📸 Screenshots

_Add screenshots of the home screen, teacher dashboard and student view here._

## 🔮 Future Improvements

- Attendance analytics and exportable reports (CSV/PDF)
- Liveness detection to prevent photo spoofing
- Email/SMS notifications for low attendance
- Mobile-friendly PWA experience

## 👩‍💻 Author

**Juveria**
GitHub: [@juveria-codes](https://github.com/juveria-codes)

---

⭐ If you found this project useful, consider giving it a star!
