import streamlit as st
import qrcode
import subprocess
import time
import requests

st.title('Please Scan the QR Code to access the mobile version of Dr.Grow!')
with st.spinner('Setting up ngrok...'):
    ngrok_process = subprocess.Popen(["ngrok", "http", "8501"], stdout=subprocess.DEVNULL)
    time.sleep(3)
    try:
        ngrok_api_url = "http://127.0.0.1:4040/api/tunnels"
        tunnels = requests.get(ngrok_api_url).json()
        public_url = tunnels['tunnels'][0]['public_url']
        print(f"🔗 Ngrok public URL: {public_url}")
    except Exception as e:
        print("❌ Failed to get ngrok public URL:", e)
        public_url = None
st.success("✅ Tunnel established successfully!")
st.write("🔗 Ngrok public URL:", public_url)
with st.spinner('Generating QR code...'):
    qr = qrcode.make(public_url).get_image()
    st.image(qr, caption="📱 Scan to Open")

    
