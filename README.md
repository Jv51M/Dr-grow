# 🌱 Dr-Grow

**Dr-Grow** is an AI-powered plant identification web app built by **Akshay, Winnie, Vishnu and Me**.
It helps users identify different plant species using an image of a plant’s leaf and also includes an **offline AI chatbot** for interactive guidance.

> 💡 *We hope our hard work proves useful to you!*

---

## 🧠 Project Overview

The development process was divided into two major stages:

1. **Model Development** – Creating an image recognition model in Python using TensorFlow and Scikit-learn.
2. **Frontend Development** – Building a user-friendly interface with Streamlit for smooth interaction.

Currently, the model supports **7 plant classes**, due to limited high-quality dataset availability.
The app also features an **offline chatbot**, powered by **Ollama**, supporting models like `llama3.2:1b` and Microsoft’s `phi`.

---

## ⚙️ Tech Stack & Libraries

The project uses the following key Python libraries:

* **Streamlit** – for building the web app interface
* **TensorFlow** – for deep learning model training and prediction
* **Scikit-learn** – for model evaluation and preprocessing
* **Ngrok** – for secure tunneling and public access
* **Ollama** – for offline AI chatbot support

  * *Models used:* `llama3.2:1b` and `phi`
  * [🧩 Setup Tutorial (YouTube)](https://youtu.be/xZL-WQLodDE)
* **QRCode** – for generating QR codes
* **OpenCV** – for image processing
* **Matplotlib** – for data visualization
* **NumPy** – for numerical computation
* **Pandas** – for data handling
* **PIL (Pillow)** – for image manipulation
* **Datetime** – for date/time utilities

---

## 🧩 System Requirements

* **Python version:** 3.12.9

  > ⚠️ Note: TensorFlow may have compatibility issues with newer Python versions. If you face errors, try running the project on **Python 3.12.9**.

---

## 🚀 How to Run

1. Clone the repository

   ```bash
   git clone https://github.com/yourusername/Dr-Grow.git
   cd Dr-Grow
   ```
2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app

   ```bash
   streamlit run app.py
   ```
4. (Optional) Start the Ollama chatbot server

   ```bash
   ollama run llama3.2:1b
   ```

---

## 🌿 Features

* Leaf-based plant identification using a deep learning model
* Interactive, user-friendly web interface
* Offline chatbot integration
* QR code support for easy sharing
* Local and online access via Ngrok

---

## 🧾 License

This project is open source and available under the **MIT License**.

---


* ✅ make a `README.md` file version of this (formatted with markdown emojis and code blocks ready to upload), or
* 🪶 make a **short portfolio version** (for resume/project showca
