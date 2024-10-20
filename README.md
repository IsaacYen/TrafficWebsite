
# Traffic Scene Detection Web Service

This repository contains a web service built with Flask and YOLOv5 for detecting objects in traffic scene images. It provides a simple REST API for uploading images and receiving detection results.

## Prerequisites  

Before you begin, ensure you have Python installed on your system. The web service is designed to work with Python 3.8 or later.

## Setup

**Clone the Repository:**

```
git clone https://github.com/yourusername/traffic-scene-detection.git
```

**Create a Virtual Environment:**

```
cd traffic-scene-detection

python -m venv venv
```

**Activate the Virtual Environment:**

**On Windows:**

```
.\venv\Scripts\activate
```

**On macOS and Linux:**

```
source venv/bin/activate
```

**Install Dependencies:**

```
pip install -r requirements.txt
```

**Run the Web Service:**

```
python -m flask run
```
