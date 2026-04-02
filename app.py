from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'accom-questionnaire-secret-key'

# Directory to store submissions
SUBMISSIONS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'submissions')
os.makedirs(SUBMISSIONS_DIR, exist_ok=True)


@app.route('/')
def index():
    """Serve the questionnaire form."""
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    """Handle form submission — save data as JSON."""
    try:
        data = request.get_json()
        
        # Add timestamp
        data['submitted_at'] = datetime.now().isoformat()
        
        # Generate filename from residence name or timestamp
        residence_name = data.get('residenceName', 'unnamed')
        safe_name = "".join(c if c.isalnum() or c in (' ', '-', '_') else '' for c in residence_name).strip()
        safe_name = safe_name.replace(' ', '_') or 'submission'
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{safe_name}_{timestamp}.json"
        
        # Save to file
        filepath = os.path.join(SUBMISSIONS_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"[+] Submission saved: {filename}")
        return jsonify({'success': True, 'message': 'Submission saved successfully', 'file': filename})
    
    except Exception as e:
        print(f"[!] Error saving submission: {e}")
        return jsonify({'success': False, 'message': str(e)}), 500


@app.route('/submissions')
def view_submissions():
    """List all saved submissions (admin view)."""
    files = []
    for f in sorted(os.listdir(SUBMISSIONS_DIR), reverse=True):
        if f.endswith('.json'):
            filepath = os.path.join(SUBMISSIONS_DIR, f)
            with open(filepath, 'r', encoding='utf-8') as fh:
                data = json.load(fh)
            files.append({
                'filename': f,
                'residence': data.get('residenceName', 'N/A'),
                'submitted': data.get('submitted_at', 'N/A'),
            })
    return jsonify(files)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug, host='0.0.0.0', port=port)
