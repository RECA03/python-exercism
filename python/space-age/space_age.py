class SpaceAge:

    seconds_earthyear = 31557600
    earthdays_oneearthyear = 365.25
    planet_periods = {"Mercury": 0.2408467,"Venus": 0.61519726,"Earth": 1.0,"Mars": 1.8808158,
                        "Jupiter": 11.862615,"Saturn": 29.447498,"Uranus": 84.016846,"Neptune": 164.79132}

    def __init__(self, seconds):
        self.age_earthyears = seconds/SpaceAge.seconds_earthyear

    def on_mercury(self):
        return round((self.age_earthyears / SpaceAge.planet_periods["Mercury"]), 2)

    def on_venus(self):
        return round(self.age_earthyears / SpaceAge.planet_periods["Venus"], 2)

    def on_earth(self):
        return round(self.age_earthyears / SpaceAge.planet_periods["Earth"], 2)

    def on_mars(self):
        return round(self.age_earthyears / SpaceAge.planet_periods["Mars"], 2)

    def on_jupiter(self):
        return round(self.age_earthyears / SpaceAge.planet_periods["Jupiter"], 2)

    def on_saturn(self):
        return round(self.age_earthyears / SpaceAge.planet_periods["Saturn"], 2)

    def on_uranus(self):
        return round(self.age_earthyears / SpaceAge.planet_periods["Uranus"], 2)

    def on_neptune(self):
        return round(self.age_earthyears / SpaceAge.planet_periods["Neptune"], 2)