# AccomForm | Student Accommodation Website Questionnaire

A modern, responsive Flask-based web application designed to collect detailed website requirements for student residences. This form helps streamline the process of gathering branding, room details, facilities, location, and safety information from property owners.

## 🚀 Features
- **Multi-step Form**: Organized into Branding, Rooms, Media, Location, and Extras.
- **Dynamic Entries**: Add multiple room types and student testimonials.
- **Responsive Design**: Works perfectly on mobile and desktop.
- **Flask Backend**: Handles submissions and saves them as JSON for review.
- **Deployable**: Configured for priority deployment to **Render** with `Procfile` and `requirements.txt` included.

## 🛠️ Installation (Local)

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd webquestion
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**:
   ```bash
   python app.py
   ```
   The app will be available at `http://127.0.0.1:5001`.

## 📦 Deployment to Render

1. Create a new **Web Service** on Render.
2. Connect your GitHub repository.
3. Use the following settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

## 📁 Project Structure
- `app.py`: Flask application routes and logic.
- `templates/`: HTML5 templates (Jinja2).
- `static/`: CSS styling and JavaScript form logic.
- `submissions/`: Folder where form data is saved as JSON.

---
*Developed for efficient student accommodation onboarding.*
