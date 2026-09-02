import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QLineEdit, QPushButton, QVBoxLayout
)
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather App")
        self.setGeometry(500, 200, 300, 250)

        self.city = QLineEdit()
        self.city.setPlaceholderText("Enter city name")

        self.button = QPushButton("Get Weather")
        self.button.clicked.connect(self.get_weather)

        self.result = QLabel("Enter a city")
        self.result.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.city)
        layout.addWidget(self.button)
        layout.addWidget(self.result)

        self.setLayout(layout)

    def get_weather(self):
        city = self.city.text()

        api_key = "6ef014d09246e3f614e76ef32a6b0dbb"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            data = requests.get(url).json()

            if data["cod"] == 200:
                temp = data["main"]["temp"]
                weather = data["weather"][0]["description"]

                self.result.setText(
                    f"{city}\n\nTemperature: {temp}°C\nWeather: {weather}"
                )
            else:
                self.result.setText("City not found!")

        except Exception:
            self.result.setText("Something went wrong!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = WeatherApp()
    window.show()

    sys.exit(app.exec_())