import requests

def fetch_weather_data(city_name, api_key):
    """Connects to the OpenWeatherMap API pipeline to fetch geographic metrics safely."""
    # Use standard metric units for Celsius temperature readouts
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=10)
        
        # Explicit evaluation of network status codes
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return {"error": f"City '{city_name}' could not be located in the global database."}
        elif response.status_code == 401:
            return {"error": "Authentication failed: Invalid API Key provided."}
        else:
            return {"error": f"Server connection anomaly. HTTP Status: {response.status_code}"}
            
    except requests.exceptions.Timeout:
        return {"error": "Network Timeout: The external server took too long to respond."}
    except requests.exceptions.RequestException:
        return {"error": "Connection Failure: Check your mobile internet link or network permissions."}

def display_weather_report(data):
    """Parses JSON payload structure cleanly into formatted console tables."""
    if "error" in data:
        print(f"\n[!] System Alert: {data['error']}")
        return
        
    # Parsing targeted multi-layered data arrays out of JSON payload
    city = data.get("name")
    country = data.get("sys", {}).get("country")
    temp = data.get("main", {}).get("temp")
    feels_like = data.get("main", {}).get("feels_like")
    humidity = data.get("main", {}).get("humidity")
    wind_speed = data.get("wind", {}).get("speed")
    description = data.get("weather", [{}])[0].get("description", "N/A").title()
    
    print("\n" + "=" * 45)
    print(f" WEATHER PROTOCOL METRICS: {city.upper()}, {country}")
    print("=" * 45)
    print(f"{'Atmospheric State:':<22} {description}")
    print(f"{'Current Temperature:':<22} {temp}°C")
    print(f"{'Apparent Sensation:':<22} {feels_like}°C")
    print(f"{'Relative Humidity:':<22} {humidity}%")
    print(f"{'Wind Velocity Rate:':<22} {wind_speed} m/s")
    print("=" * 45)

def main():
    """Main execution frame for mobile operations."""
    print("=" * 45)
    print("      REAL-TIME GLOBAL WEATHER TERMINAL      ")
    print("=" * 45)
    
    # Portfolio best practice guidance: Instruct users clearly how to feed credentials safely
    print("[INFO] Requires an active OpenWeatherMap API Key to fetch live streams.")
    api_key = input("Paste your OpenWeather API Key here: ").strip()
    
    if not api_key:
        print("\n[!] Critical Termination: Key variable cannot be empty.")
        return

    while True:
        city_name = input("\nEnter target city name (or type 'exit' to quit): ").strip()
        
        if city_name.lower() == 'exit':
            print("\nShutting down Weather Terminal. Connections closed.")
            break
            
        if not city_name:
            continue
            
        print(f"\n[~] Querying remote server nodes for '{city_name}'...")
        weather_payload = fetch_weather_data(city_name, api_key)
        display_weather_report(weather_payload)

if __name__ == "__main__":
    main()
