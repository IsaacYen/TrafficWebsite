
# Traffic Scene Detection Web Service

This repository contains a web service built with Flask and YOLOv5 for detecting objects in traffic scene images. It provides a simple REST API for uploading images and receiving detection results.

## Prerequisites
Before you begin, ensure you have Python installed on your system. The web service is designed to work with Python 3.8 or later.

## Setup
**Clone the Repository:**

bash
git clone https://github.com/yourusername/traffic-scene-detection.git
**Create a Virtual Environment:**

bash
cd traffic-scene-detection
python -m venv venv
**Activate the Virtual Environment:**

**On Windows:**
bash
.\venv\Scripts\activate
**On macOS and Linux:**
bash
source venv/bin/activate
**Install Dependencies:**

bash
pip install -r requirements.txt
**Run the Web Service:**

bash
python -m flask run
