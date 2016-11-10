from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.gridlayout import GridLayout
from anti_freeze.anti_freeze import AntiFreeze


class MainScreen(GridLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 2
        self.humidity_description = Label(text="Humedad: ", font_size=40)
        self.wind_description = Label(text="Viento: ", font_size=40)
        self.none_ = Label(text="")
        self.none = Label(text="")

        # Add sliders to control wind speed
        self.wind_slider = Slider(min=0, max=60, value=30)
        self.wind_label = Label(text=str(self.wind_slider.value)+".00 Km/h", font_size=40)

        # Same with humidity percentage
        self.humidity_slider = Slider(min=0, max=100, value=50)
        self.humidity_label = Label(text=str(self.humidity_slider.value)+".00 %", font_size=40)

        # Bind Sliders value to a function
        self.wind_slider.bind(value=self.__wind_slider__)
        self.humidity_slider.bind(value=self.__humidity_slider__)

        # Fuzzy output labels
        self.inference_label = Label(font_size=40, text="Inferencia:")
        self.inference = Label(font_size=40)
        self.wind_value = Label(font_size=20)
        self.humidity_value = Label(font_size=20)

        # Window order
        self.add_widget(self.wind_description)
        self.add_widget(self.none)
        self.add_widget(self.wind_slider)
        self.add_widget(self.wind_label)
        self.add_widget(self.humidity_description)
        self.add_widget(self.none_)
        self.add_widget(self.humidity_slider)
        self.add_widget(self.humidity_label)
        self.add_widget(self.inference_label)
        self.add_widget(self.inference)
        self.add_widget(self.wind_value)
        self.add_widget(self.humidity_value)
        self.anti_freeze = AntiFreeze()
        self.__update_screen__()

    def __wind_slider__(self, instance, value):
        self.wind_label.text = "%.2f Km/h" % value
        self.__update_screen__()

    def __humidity_slider__(self, instance, value):
        self.humidity_label.text = "%.2f %%" % value
        self.__update_screen__()

    def __update_screen__(self):
        """
        Executes the fuzzy function with the actual values obtained from the sliders and updates
        all the labels from the screen
        """
        vals = self.anti_freeze.fuzzy(
            humidity=self.humidity_slider.value,
            wind=self.wind_slider.value,
        )

        self.inference.text = vals['inference']
        self.wind_value.text = "Viento: %s con %f" % (vals['wind'], vals['wind_value'])
        self.humidity_value.text = "Humedad: %s con %f" % (vals['humidity'], vals['humidity_value'])


class MyApp(App):

    def build(self):
        self.title = 'Anti Freeze System'
        return MainScreen()


if __name__ == '__main__':
    MyApp().run()
