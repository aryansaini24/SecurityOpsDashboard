from flask import Flask, jsonify, render_template
import json
from datetime import datetime

app = Flask(__name__, static_folder='.', static_url_path='')

# Load security events from JSON file
def load_security_events():
    try:
        with open('security_events.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Automated incident prioritization logic
def prioritize_incidents(events):
    priority_scores = {
        'critical': 4,
        'high': 3,
        'medium': 2,
        'low': 1
    }
    
    for event in events:
        # Calculate priority score based on severity and threat indicators
        base_score = priority_scores.get(event.get('severity', 'low').lower(), 1)
        
        # Increase priority for specific threat types
        threat_type = event.get('threat_type', '').lower()
        if 'ransomware' in threat_type or 'breach' in threat_type:
            base_score += 2
        elif 'malware' in threat_type or 'intrusion' in threat_type:
            base_score += 1
        
        # Add priority score to event
        event['priority_score'] = min(base_score, 5)  # Cap at 5
        
        # Assign priority label
        if event['priority_score'] >= 4:
            event['priority'] = 'Critical'
        elif event['priority_score'] == 3:
            event['priority'] = 'High'
        elif event['priority_score'] == 2:
            event['priority'] = 'Medium'
        else:
            event['priority'] = 'Low'
    
    # Sort by priority score (descending)
    events.sort(key=lambda x: x['priority_score'], reverse=True)
    return events

# Aggregate threat alerts
def aggregate_threats(events):
    stats = {
        'total_events': len(events),
        'critical_count': 0,
        'high_count': 0,
        'medium_count': 0,
        'low_count': 0,
        'threat_types': {},
        'top_sources': {}
    }
    
    for event in events:
        # Count by severity
        severity = event.get('severity', 'low').lower()
        stats[f'{severity}_count'] = stats.get(f'{severity}_count', 0) + 1
        
        # Count threat types
        threat_type = event.get('threat_type', 'Unknown')
        stats['threat_types'][threat_type] = stats['threat_types'].get(threat_type, 0) + 1
        
        # Track top sources
        source_ip = event.get('source_ip', 'Unknown')
        stats['top_sources'][source_ip] = stats['top_sources'].get(source_ip, 0) + 1
    
    return stats

@app.route('/')
def index():
    return app.send_static_file('dashboard.html')

@app.route('/api/events')
def get_events():
    events = load_security_events()
    prioritized_events = prioritize_incidents(events)
    return jsonify(prioritized_events)

@app.route('/api/stats')
def get_stats():
    events = load_security_events()
    prioritized_events = prioritize_incidents(events)
    stats = aggregate_threats(prioritized_events)
    return jsonify(stats)

@app.route('/api/health')
def health_check():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    print('Starting Security Operations Dashboard...')
    print('Dashboard available at: http://localhost:5000')
    app.run(debug=True, host='0.0.0.0', port=5000)
