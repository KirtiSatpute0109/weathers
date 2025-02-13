import streamlit as st
import requests

# Set up API key and base URL
api_key = "1b27c49212cb298bda55509515f1f688"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Function to get weather icon URL
def get_icon_url(icon_id):
    return f"http://openweathermap.org/img/wn/{icon_id}@2x.png"

# Create Streamlit interface
st.markdown("""
    <style>
    .title {
        font-size: 42px;
        color: #4CAF50;
        text-align: center;
        font-weight: bold;
    }
    .subtitle {
        font-size: 28px;c
        color: #FFA500;
        text-align: center;
        margin-bottom: 20px;
    }
    .info {
        font-size: 22px;
        color: #2E86C1;
    }
    .icon {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    .error {
        font-size: 24px;
        color: red;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="title">🌤️ Welcome to the Weather Forecast App</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Get real-time weather updates for any city in the world</p>', unsafe_allow_html=True)

city_name = st.text_input("Enter the city name below:", "")

if city_name:
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"] - 273.15  # Convert from Kelvin to Celsius
        pressure = main["pressure"]
        humidity = main["humidity"]
        description = weather["description"]
        icon_id = weather["icon"]
        icon_url = get_icon_url(icon_id)
        
        st.markdown(f'<p class="subtitle">Weather in {city_name.capitalize()}</p>', unsafe_allow_html=True)
        st.image(icon_url, width=100)
        st.markdown(f'<p class="info"><b>Temperature:</b> {temperature:.2f}°C</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="info"><b>Pressure:</b> {pressure} hPa</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="info"><b>Humidity:</b> {humidity}%</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="info"><b>Description:</b> {description.capitalize()}</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="error">City not found. Please enter a valid city name.</p>', unsafe_allow_html=True)
