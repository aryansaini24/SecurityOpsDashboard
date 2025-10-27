# 🛡️ Security Operations Dashboard

A real-time security operations dashboard that provides unified visibility into security threats, automated incident prioritization, and comprehensive threat visualization. Built with Python Flask backend and interactive HTML/JavaScript frontend.

## 🎯 Overview

This Security Operations Dashboard is a full-featured prototype that aggregates security threat alerts from log files, applies intelligent prioritization logic, and displays real-time threat data through an intuitive web interface.

## ✨ Key Features

### 🔍 **Threat Visualization Dashboard**
- Interactive, real-time security event monitoring
- Color-coded severity indicators (Critical, High, Medium, Low)
- Responsive grid layout with visual threat cards
- Auto-refresh every 30 seconds for live updates
- Modern dark-themed UI with gradient effects

### 📊 **Automated Incident Prioritization**
- Python-based intelligent priority scoring algorithm
- Multi-factor analysis considering:
  - Base severity levels (Critical/High/Medium/Low)
  - Threat type classifications (Ransomware, Malware, Intrusion, etc.)
  - Automatic escalation for high-risk threats
- Dynamic priority assignment with score capping
- Sorted event display by priority level

### 📈 **Threat Analytics & Aggregation**
- Real-time statistics dashboard
- Event counting by severity level
- Threat type distribution analysis
- Source IP tracking and monitoring
- Top threat sources identification

### 🔧 **Python Flask Backend API**
- RESTful API endpoints:
  - `/api/events` - Prioritized security events
  - `/api/stats` - Aggregated threat statistics
  - `/api/health` - System health check
- JSON data processing and manipulation
- Efficient file-based data loading
- CORS-ready for frontend integration

### 📝 **Sample Security Data**
- 12 realistic security event scenarios
- Diverse threat types:
  - Ransomware attacks
  - Data breach attempts
  - Brute force attacks
  - Malware detection
  - DDoS attacks
  - SQL injection attempts
  - Insider threats
  - And more...
- Complete event metadata (IPs, systems, timestamps, status)

## 🚀 Installation

### Prerequisites

- **Python 3.7+** installed on your system
- **pip** (Python package installer)
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Step 1: Clone the Repository

```bash
git clone https://github.com/aryansaini24/SecurityOpsDashboard.git
cd SecurityOpsDashboard
```

### Step 2: Install Dependencies

Install Flask and required Python packages:

```bash
pip install flask
```

Or use a virtual environment (recommended):

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install flask
```

### Step 3: Verify Files

Ensure all required files are present:

```
SecurityOpsDashboard/
├── app.py                    # Flask backend application
├── security_events.json      # Sample security event data
├── dashboard.html            # Frontend interface
└── README.md                 # This file
```

## 🎬 Launch Instructions

### Starting the Dashboard

1. **Navigate to the project directory:**

```bash
cd SecurityOpsDashboard
```

2. **Start the Flask server:**

```bash
python app.py
```

You should see output similar to:

```
Starting Security Operations Dashboard...
Dashboard available at: http://localhost:5000
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://0.0.0.0:5000
```

3. **Access the dashboard:**

Open your web browser and navigate to:

```
http://localhost:5000
```

4. **View real-time threat data:**

The dashboard will automatically load and display:
- Summary statistics (total events, counts by severity)
- Prioritized security events list
- Detailed threat information for each event

### Stopping the Server

Press `Ctrl+C` in the terminal where Flask is running.

## 📖 Usage Guide

### Dashboard Interface

**Statistics Cards (Top Section):**
- **Total Events**: Overall count of security incidents
- **Critical**: High-priority threats requiring immediate attention
- **High Priority**: Significant threats needing quick response
- **Medium Priority**: Notable events for investigation
- **Low Priority**: Informational or minor events

**Security Events List:**
- Each event displays:
  - Event type and current status
  - Priority badge (Critical/High/Medium/Low)
  - Detailed description
  - Event ID and threat classification
  - Source and destination IP addresses
  - Affected systems
  - Timestamp

**Refresh Button:**
- Manual refresh to reload latest data
- Auto-refresh occurs every 30 seconds

### API Endpoints

#### Get All Events (Prioritized)
```bash
GET http://localhost:5000/api/events
```
Returns: JSON array of security events sorted by priority

#### Get Statistics
```bash
GET http://localhost:5000/api/stats
```
Returns: JSON object with aggregated threat statistics

#### Health Check
```bash
GET http://localhost:5000/api/health
```
Returns: System health status and timestamp

## 🔧 Customization

### Adding Your Own Security Events

Edit `security_events.json` to add custom events:

```json
{
  "id": "EVT-XXX",
  "timestamp": "2025-10-27T12:00:00Z",
  "event_type": "Your Event Type",
  "severity": "critical",
  "threat_type": "Threat Classification",
  "source_ip": "xxx.xxx.xxx.xxx",
  "destination_ip": "xxx.xxx.xxx.xxx",
  "description": "Event description",
  "affected_systems": ["SYSTEM-01"],
  "status": "active"
}
```

### Modifying Prioritization Logic

Edit the `prioritize_incidents()` function in `app.py` to adjust:
- Base severity scores
- Threat type weightings
- Priority thresholds
- Sorting criteria

### Customizing the UI

Modify `dashboard.html` to change:
- Color schemes and styling
- Layout and grid configurations
- Auto-refresh intervals
- Data visualization formats

## 🏗️ Architecture

### Backend (Python Flask)

**app.py** - Main application file containing:
- Flask server configuration
- API route handlers
- Data loading functions
- Incident prioritization algorithm
- Threat aggregation logic

### Data Layer

**security_events.json** - Sample data file with:
- Realistic security event scenarios
- Complete event metadata
- Various threat types and severities

### Frontend (HTML/JavaScript)

**dashboard.html** - Single-page application featuring:
- Responsive CSS Grid layout
- Vanilla JavaScript for API calls
- Real-time data rendering
- Auto-refresh functionality
- Interactive event cards

## 🔐 Security Considerations

This is a **prototype/demonstration** application. For production use, consider:

- Implementing authentication and authorization
- Adding HTTPS/TLS encryption
- Securing API endpoints
- Input validation and sanitization
- Rate limiting and DDoS protection
- Database integration instead of JSON files
- Logging and audit trails
- Error handling and monitoring

## 📦 Technologies Used

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Data Format**: JSON
- **Architecture**: RESTful API

## 🚀 Future Enhancements

- Database integration (PostgreSQL, MongoDB)
- User authentication and role-based access
- Real-time WebSocket updates
- Advanced data visualization (Chart.js, D3.js)
- Alert notifications (email, SMS, Slack)
- Integration with SIEM tools
- Machine learning-based threat detection
- Export functionality (PDF, CSV)
- Historical data analysis and trends
- Multi-tenancy support

## 📝 License

This project is for educational and demonstration purposes.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements!

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Built with ❤️ for cybersecurity professionals**
