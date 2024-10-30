<img width="1280" alt="readme-banner" src="https://github.com/user-attachments/assets/35332e92-44cb-425b-9dff-27bcf1023c6c">

# GuitarMate


## Basic Details
### Team Name: CodeCrocodilezzz


### Team Members
- Team Lead: Joseph Shibu - Albertian Institute of Science And Technology
- Member 2: Suha Shajahan - Albertian Institute of Science And Technology
- Member 3: Riya Sabu - Albertian Institute of Science And Technology

### Project Description
GuitarMate is an AI-powered guitar practice app that listens to your playing and provides real-time feedback on chords, notes, rhythm, and technique. It helps beginners learn songs, tracks progress, and offers practice routines, while advanced players can refine their skills and explore challenges.
### The Problem (that doesn't exist)
Based on your skill level and goals, the app generates a daily practice plan (e.g., warm-up exercises, scales, song challenges).
Tracks your progress and adjusts difficulty over time.
Jam Mode with Backing Tracks:

Play along with various backing tracks in genres like blues, rock, funk, and jazz.
The app can suggest scales and modes that fit each track to encourage improvisation.

### The Solution (that nobody asked for)
Clap or play in time with a metronome or rhythm track, and the AI scores your accuracy.
Perfect for mastering timing and rhythm, essential for ensemble playing.

## Technical Details
### Technologies/Components Used
For Software:
#### Languages Used

JavaScript – Frontend (React, Web Audio API, TensorFlow.js)
Python – Backend (Flask API, AI logic for pitch/chord detection)
HTML/CSS – For web styling and UI
Dart (Optional, if using Flutter) – Mobile app development

#### Frameworks Used

React.js – Web frontend framework
Flask – Backend framework for API logic
Flutter (Optional) – Mobile app frontend
Node.js – For backend and real-time leaderboard API (if used)

#### Libraries Used

TensorFlow.js – For chord and pitch recognition in the browser
MediaPipe Hands – Hand tracking for chord detection
Web Audio API – Audio input and analysis
librosa – For audio analysis in Python (e.g., pitch detection)
Mongoose/SQLite – Database management for storing leaderboard scores and user progress
WebXR – For AR chord guide visualization
OpenCV – (Optional) Hand tracking and analysis on video feeds
Yin Pitch Detection Algorithm – For advanced note recognition (integrated with librosa or TensorFlow)

#### Tools Used

GitHub Codespaces – Development environment
Visual Studio Code – Code editing (via Codespaces or locally)
Git – Version control and collaboration
Postman – Testing backend APIs
Vuforia (Optional) – AR tool for advanced chord visualization
npm (Node Package Manager) – Managing JavaScript dependencies
pip – Managing Python dependencies


# Installation
sudo apt update && sudo apt install -y nodejs npm python3-pip
npm install -g create-react-app
pip install Flask

npx create-react-app frontend
cd frontend
npm install @tensorflow/tfjs @mediapipe/hands

# Run
Frontend (React)
Navigate to the frontend directory:

cd frontend

Install dependencies:

npm install
Start the React app:

npm start
Access the frontend in your browser at:
http://localhost:3000

Backend (Flask)

Navigate to the backend directory:

cd backend
Install dependencies:
pip install Flask librosa tensorflow

Run the Flask server:

python app.py
Access the API at:
http://localhost:5000


### Project Documentation

# Diagrams
Frontend (React.js) <--> Backend API (Flask) <--> AI Models (TensorFlow, MediaPipe)
|
+---> Web Audio API (Chord Recognition)
|
+---> AR Visualization (WebXR)




## Team Contributions
- Joseph Shibu : Backend
- Suha Shajahan: Documentation, Research, Idea.
- Riya Sabu: Design, Frontend, Poster.

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProject--24-24?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)



