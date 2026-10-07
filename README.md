# AttendIQ 🎯

**Making attendance faster using AI.**

AttendIQ is a web-based smart attendance system built with Python and Streamlit. Teachers create subjects and share a QR code or join link, students enroll in one click, and attendance is taken from **classroom photos (face recognition)** or **recorded classroom audio (voice recognition)** instead of manual roll calls.

---

## ✨ Features

### For Teachers
- Register and log in securely (passwords hashed with **bcrypt**)
- Create subjects with a subject code, name and section
- Share a subject via a **QR code or join link** (`?join-code=CS101`)
- Take attendance by **uploading or capturing classroom photos**: multiple faces are detected and matched in a single image
- Take attendance by **recording classroom audio**: students are identified by their voice
- Review the detected attendance in a table, then **confirm and save** (or discard)
- View attendance records per subject

### For Students
- Register with face and voice profiles
- Enroll in a subject by **entering a code, scanning a QR code, or opening a join link** (auto-enroll dialog)
- View enrolled subjects and personal attendance
- Unenroll from a subject

## 🧠 How the AI Works

**Face pipeline** (`src/pipelines/face_pipeline.py`)
1. dlib's frontal face detector finds every face in a classroom photo
2. A landmark predictor and dlib's face recognition model convert each face into a 128-dimensional embedding
3. An **SVM classifier (scikit-learn, linear kernel with probability estimates)** trained on enrolled students' embeddings predicts who each face belongs to
4. Models are cached with `st.cache_resource` and can be retrained when new students register

**Voice pipeline** (`src/pipelines/voice_pipeline.py`)
1. Audio is loaded and resampled to 16 kHz with Librosa
2. Resemblyzer's `VoiceEncoder` generates a speaker embedding
3. Embeddings are compared against enrolled students' stored voice profiles using similarity scoring with a confidence threshold

## 🛠️ Tech Stack

| Area | Technology |
|---|---|
| Language | Python |
| App framework / UI | Streamlit |
| Computer vision | dlib, face_recognition_models |
| Machine learning | scikit-learn (SVM), NumPy, pandas |
| Audio / speaker recognition | Librosa, Resemblyzer |
| Database / Backend | Supabase (PostgreSQL) |
| Security | bcrypt |
| QR codes | Segno |
| Image handling | Pillow |
| Deployment | Streamlit Community Cloud |

## 📁 Project Structure

```
AttendIQ/
├── app.py                          # Entry point: session routing and join-code handling
├── requirements.txt
├── .gitignore
└── src/
    ├── components/                 # Reusable UI components and dialogs
    │   ├── dialog_add_photos.py            # Camera / upload classroom photos
    │   ├── dialog_attendance_result.py     # Review, confirm and save attendance
    │   ├── dialog_auto_enroll.py           # Quick enrollment via join link / QR
    │   ├── dialog_create_subject.py        # Create a new subject
    │   ├── dialog_enroll.py                # Enroll using a subject code
    │   ├── dialog_share_subject.py         # Generate QR code and join link
    │   ├── dialog_voice_attendance.py      # Record audio and analyze voices
    │   ├── header.py
    │   └── subject_card.py
    ├── database/                   # Data layer
    │   ├── config.py                       # Supabase client setup
    │   └── db.py                           # Queries: auth, subjects, enrollment, attendance
    ├── pipelines/                  # AI/ML processing
    │   ├── face_pipeline.py                # Face detection, embeddings, SVM classifier
    │   └── voice_pipeline.py               # Voice embeddings and speaker identification
    ├── screens/                    # Page-level screens
    │   ├── home_screen.py
    │   ├── teacher_screen.py
    │   └── student_screen.py
    └── ui/                         # Styling and static assets
        ├── base_layout.py
        ├── logo_url.png
        ├── student.png
        └── teacher.png
```

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- A [Supabase](https://supabase.com) project with tables for `teachers`, `students`, `subjects`, `subject_students` and attendance records

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

Create `.streamlit/secrets.toml` with your Supabase credentials:

```toml
SUPABASE_URL = "your-supabase-project-url"
SUPABASE_KEY = "your-supabase-key"
```


### Run the app

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

## 🔄 Workflow

1. **Teacher** signs up, creates a subject and shares the QR code or join link.
2. **Student** joins via the link, code or QR and has a face and voice profile registered.
3. **Teacher** uploads classroom photos or records audio. The AI pipelines identify the students present.
4. The teacher reviews the results, confirms, and attendance is saved to Supabase.

## 📸 Screenshots

_Add screenshots of the home screen, teacher dashboard and attendance result here._

## 🔮 Future Improvements

- Liveness detection to prevent photo spoofing
- Attendance analytics and exportable reports (CSV/PDF)
- Low-attendance alerts via email or SMS
- Making the share-link domain configurable instead of hardcoded

## 👩‍💻 Author

**Juveria**
GitHub: [@juveria-codes](https://github.com/juveria-codes)

---

⭐ If you found this project useful, consider giving it a star!
