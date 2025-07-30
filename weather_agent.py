import requests
from datetime import datetime

class WeatherAgent:
    def extract_weather_summary(self, lat, lon, forecast_days=1):
        try:
            # Prepare the API URL
            url = "https://api.open-meteo.com/v1/forecast"
            params = {
                "latitude": lat,
                "longitude": lon,
                "current_weather": True,
                "daily": "temperature_2m_max,temperature_2m_min,weathercode",
                "forecast_days": forecast_days,
                "timezone": "auto"
            }

            resp = requests.get(url, params=params)
            data = resp.json()

            if forecast_days == 1:
                current = data.get("current_weather", {})
                return {
                    "current_weather": {
                        "weather_description": self._weather_code_to_description(current.get("weathercode")),
                        "temperature": {
                            "value": round(current.get("temperature", 0)),
                            "unit": "°C"
                        }
                    }
                }
            else:
                dates = data["daily"]["time"]
                min_temps = data["daily"]["temperature_2m_min"]
                max_temps = data["daily"]["temperature_2m_max"]
                codes = data["daily"]["weathercode"]

                forecast = []
                for i in range(min(forecast_days, len(dates))):
                    forecast.append({
                        "date": dates[i],
                        "weather_description": self._weather_code_to_description(codes[i]),
                        "temperature": {
                            "min": {"value": round(min_temps[i]), "unit": "°C"},
                            "max": {"value": round(max_temps[i]), "unit": "°C"}
                        }
                    })
                return {"daily_forecast": forecast}

        except Exception as e:
            print("Weather API error:", e)
            return {}

    def _weather_code_to_description(self, code):
        code_map = {
            0: "clear sky",
            1: "mainly clear",
            2: "partly cloudy",
            3: "overcast",
            45: "fog",
            48: "depositing rime fog",
            51: "light drizzle",
            61: "light rain",
            71: "light snow",
            80: "light rain showers",
            95: "thunderstorm",
        }
        return code_map.get(code, "unknown")
