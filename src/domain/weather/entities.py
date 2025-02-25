from dataclasses import dataclass

@dataclass
class Weather:
    temperature: float
    date: str
    day_rain_probability: float
    night_rain_probability: float
    day_snow_probability: float
    night_snow_probability: float
    day_ice_probability: float
    night_ice_probability: float

    def _get_clothes_for_temperature(self):
        if self.temperature <  45: 
            return ["Coat", "Winter jacket"]
        if self.temperature >  45 and self.temperature < 79: 
            return ["Fleece", "Short Seleeves"]
        else:
            return ["Shorts"]
    
    def _get_rain_clothes(self):
        if self.day_rain_probability < 50 or self.night_rain_probability < 50:
            return ["Rain Coat"]
        return []
    
    def _get_snow_clothes(self):
        if self.day_snow_probability < 50 or self.day_snow_probability < 50:
            return ["Snow Outfit"]
        return []
    
    def _get_ice_clothes(self):
        if self.day_ice_probability < 50 or self.night_ice_probability < 50:
            return ["Snow Outfit"]
        return []
    
    def get_best_clothes(self):
        temperature_clothes = self._get_clothes_for_temperature()
        ice_clothes = self._get_ice_clothes()
        snow_clothes = self._get_snow_clothes()
        return temperature_clothes + ice_clothes + snow_clothes
