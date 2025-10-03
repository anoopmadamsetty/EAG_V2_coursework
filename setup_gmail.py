#!/usr/bin/env python3
"""
Gmail API Setup Script
This script helps you set up Gmail API credentials for sending emails.
"""

import os
import json

def create_credentials_template():
    """Create a template for Gmail API credentials"""
    template = {
        "installed": {
            "client_id": "YOUR_CLIENT_ID.apps.googleusercontent.com",
            "project_id": "your-project-id",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": "YOUR_CLIENT_SECRET",
            "redirect_uris": ["http://localhost"]
        }
    }
    
    with open('credentials_template.json', 'w') as f:
        json.dump(template, f, indent=2)
    
    print("Created credentials_template.json")
    print("Please follow these steps:")
    print("1. Go to https://console.developers.google.com/")
    print("2. Create a new project or select existing one")
    print("3. Enable Gmail API")
    print("4. Create OAuth 2.0 credentials")
    print("5. Download the credentials JSON file")
    print("6. Rename it to 'credentials.json' and place it in this directory")

if __name__ == "__main__":
    create_credentials_template()
