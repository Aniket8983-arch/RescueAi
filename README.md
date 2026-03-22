# 🚑 RescueAI – First Aid Assistant

> Instant help when every second matters.

---

## 📌 Overview

RescueAI is an AI-powered emergency assistant that provides instant first aid guidance and helps users locate nearby hospitals in real time.

It is designed to assist users during the critical moments before professional medical help arrives.

---

## ✨ Features

* 🧠 AI-generated first aid instructions
* ⚡ Quick emergency buttons (Burn, Choking, Heart Attack, etc.)
* 🗺️ Interactive hospital map
* 📍 Clickable hospital details (address + phone)
* 👤 Simple login system
* 🎯 Fast and user-friendly interface

---

## 🧰 Tech Stack

* Python
* Streamlit
* Groq API (LLM)
* OpenStreetMap
* Overpass API
* Folium
* Streamlit-Folium

---

## 🏗️ Architecture Diagram

```text
User Input
   ↓
Streamlit UI
   ↓
AI Engine (Groq API)
   ↓
First Aid Response

User Location Input
   ↓
Geocoding (Coordinates)
   ↓
Overpass API
   ↓
Hospital Data
   ↓
Map Display (Folium)
```

---

## 🔄 Workflow

```text
User selects emergency
        ↓
AI generates first aid instructions
        ↓
User searches city
        ↓
Nearby hospitals displayed on map
        ↓
User clicks hospital marker
        ↓
Hospital details shown
```

---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/rescue-ai.git
cd rescue-ai
pip install -r requirements.txt
streamlit run app.py
```

---

## 📸 Demo Flow

1. Select emergency (e.g., choking)
2. Get instant AI guidance
3. Search city
4. View hospitals on map
5. Click hospital → see details

---

## ⚠️ Disclaimer

This application provides first aid guidance only and is not a substitute for professional medical assistance.

---

## 🚀 Future Improvements

* Voice-based emergency input
* Real-time GPS location detection
* Ambulance integration
* Multilingual support
* Mobile app version

---

## 👨‍💻 Author

Aniket Patil , Kartik Madukar

---

## ⭐ Support

If you like this project, consider giving it a star ⭐
