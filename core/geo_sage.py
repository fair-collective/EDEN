import geocoder
import requests

class GeoSage:
    def __init__(self, contract):
        self.parents = [p['phone'] for p in contract['parents']]
        self.kin = contract.get('next_of_kin', {}).get('phone')

    def get_location(self):
        g = geocoder.ip('me')
        return {"lat": g.lat, "lng": g.lng, "address": g.address}

    def send_pin(self, child_name):
        loc = self.get_location()
        maps_link = f"https://maps.google.com/?q={loc['lat']},{loc['lng']}"
        message = f"{child_name} is here: {maps_link}"
        
        for phone in self.parents + ([self.kin] if self.kin else []):
            requests.post("https:// sms-api", json={"to": phone, "msg": message})
        
        return f"Pin sent to family: {maps_link}"

    def guide_home(self, home_address):
        loc = self.get_location()
        return f"You're at {loc['address']}. Walk north to {home_address}. You're 300m away."
