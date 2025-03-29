# Django Template Project

This is a pre-prepared Django template designed to help you quickly set up your project with essential configurations and integrations.

---

## Key Features

- **Static and Media Settings**: The template includes pre-configured static and media file settings with proper URLs.
- **Database Integration**: Ready to connect to your PostgreSQL database by reading configurations from an `.env` file.
- **Cloudinary Support**: Media hosting is configured with Cloudinary; simply provide your Cloudinary connection data in the `.env` file.
- **Custom User Model**: Includes a custom user model that you can easily modify to suit your project's needs.
- **Front-End Structure**: Contains a structured front-end directory ready for development.
- **Easy Setup Shell Script**: A PowerShell script (`pyrun.ps1`) is included to simplify migrations and running the server on Windows.

---

## Getting Started

### 1. Install Dependencies
First, make sure to install all required packages:
```bash
pip install -r requirements.txt
```
### 2. Create an .env File
Create an `.env` file in the project's root directory and include the following configuration:
```bash

# Database Configuration
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port

# Cloudinary Configuration
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```
### 3. Use the Shell Script for Easy Setup (Windows)
To make migrations and running the project easier, a PowerShell script (`pyrun.ps1`) is provided. Follow these steps:

Set up an alias for the script:
```bash
set-alias -Name pyr -Value .\pyrun.ps1
```
Use the alias pyr to run the script, which will handle migrations and start the server:
```bash
pyr
```
The script will:

Apply migrations.
Start the development server at http://127.0.0.1:5000.


### Project Structure
```
Template/
├── mainapp/                  # Contains the main application files
│   ├── models.py             # Custom user model
│   ├── views.py
│   └── ...
├── static/                   # Static files (CSS, JavaScript, images)
├── templates/                # HTML templates
├── media/                    # Media files (local development)
├── Template/                 # Project settings and configurations
│   ├── settings.py           # Django settings file
│   └── ...
├── pyrun.ps1                 # PowerShell script for easy setup
├── requirements.txt          # Python package requirements
├── .env                      # Configuration file (ignored by Git)
└── .gitignore                # Git ignore file

```
