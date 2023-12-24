from ui_dashboard import *
from graphs import Graphs
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("InsightFlow Manager")

        # Hide / Show Sidebar
        self.ui.sidebar.hide()
        self.ui.button_sidebar.clicked.connect(self.hide_sidebar)

        # Change temperature / humidity graph tab
        self.ui.button_temperature.setStyleSheet("border-bottom: 2px solid #E60540;")
        self.ui.button_temperature.clicked.connect(self.style_tab_temperature)
        self.ui.button_humidity.clicked.connect(self.style_tab_humidity)

        # Change electricity / devices graph tab
        self.ui.button_electricity_consumption.setStyleSheet("border-bottom: 2px solid #E60540;")
        self.ui.button_electricity_consumption.clicked.connect(self.style_tab_electricity_consumption)
        self.ui.button_devices.clicked.connect(self.style_tab_devices)

        # Plot Traffic Consumption Graph
        traffic_consumption_graph = Graphs.traffic_consumption()
        self.ui.verticalLayout_5.addWidget(traffic_consumption_graph)

        # Plot Energy Consumption Graph
        electricity_consumption_graph = Graphs.energy_consumption()
        self.ui.verticalLayout_4.addWidget(electricity_consumption_graph)

    def hide_sidebar(self):
        sidebar_container = self.ui.sidebar
        if sidebar_container.isVisible():
            sidebar_container.hide()
            self.ui.button_sidebar.setIcon(QIcon("icons/align-justify.svg"))
        else:
            sidebar_container.show()
            self.ui.button_sidebar.setIcon(QIcon("icons/chevron-left.svg"))

    def style_tab_temperature(self):
        style_button_temperature = "border-bottom: 2px solid #E60540;"
        style_button_humidity = "border: none"
        electricity_consumption_graph = Graphs.energy_consumption()

        # Clear layout to plot a new graph
        for i in reversed(range(self.ui.verticalLayout_6.count())):
            self.ui.verticalLayout_6.itemAt(i).widget().setParent(None)
        self.ui.button_temperature.setStyleSheet(style_button_temperature)
        self.ui.button_humidity.setStyleSheet(style_button_humidity)

    def style_tab_humidity(self):
        style_button_temperature = "border: none"
        style_button_humidity = "border-bottom: 2px solid #E60540;"
        electricity_consumption_graph = Graphs.energy_consumption()

        # Clear layout to plot a new graph
        for i in reversed(range(self.ui.verticalLayout_6.count())):
            self.ui.verticalLayout_6.itemAt(i).widget().setParent(None)
        self.ui.button_temperature.setStyleSheet(style_button_temperature)
        self.ui.button_humidity.setStyleSheet(style_button_humidity)

    def style_tab_electricity_consumption(self):
        style_button_electricity_consumption = "border-bottom: 2px solid #E60540;"
        style_button_devices = "border: none;"
        electricity_consumption_graph = Graphs.energy_consumption()

        # Clear layout to plot a new graph
        for i in reversed(range(self.ui.verticalLayout_4.count())):
            self.ui.verticalLayout_4.itemAt(i).widget().setParent(None)
        self.ui.button_electricity_consumption.setStyleSheet(style_button_electricity_consumption)
        self.ui.button_devices.setStyleSheet(style_button_devices)
        self.ui.verticalLayout_4.addWidget(electricity_consumption_graph)

    def style_tab_devices(self):
        style_button_electricity_consumption = "border: none;"
        style_button_devices = "border-bottom: 2px solid #E60540;"
        devices_graph = Graphs.devices()

        # Clear layout to plot a new graph
        for i in reversed(range(self.ui.verticalLayout_4.count())):
            self.ui.verticalLayout_4.itemAt(i).widget().setParent(None)
        self.ui.button_electricity_consumption.setStyleSheet(style_button_electricity_consumption)
        self.ui.button_devices.setStyleSheet(style_button_devices)
        self.ui.verticalLayout_4.addWidget(devices_graph)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()