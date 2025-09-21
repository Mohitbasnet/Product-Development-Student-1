# AI-Solutions Website

## How to Run the Project

### Prerequisites
- Python 3.13 or higher
- Virtual environment (already created as `ai_solutions_env`)

### Steps to Run

1. **Activate Virtual Environment**:
   ```bash
   ai_solutions_env\Scripts\activate
   ```

2. **Install Dependencies** (if not already installed):
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Database Migrations** (if not already done):
   ```bash
   python manage.py migrate
   ```

4. **Create Superuser** (if not already created):
   ```bash
   python manage.py createsuperuser
   ```

5. **Run Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Website**:
   - Main website: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
   - Analytics dashboard: http://127.0.0.1:8000/admin/dashboard/analytics/

### Default Admin Credentials
- Username: `admin`
- Password: `admin123`

### Project Features
- Professional AI-themed website
- Admin panel with analytics dashboard
- Contact form functionality
- News and events management
- Services showcase
- Photo gallery
- Customer testimonials