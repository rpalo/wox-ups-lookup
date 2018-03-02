"""Wox Plugin class for ups tracking lookup"""

import webbrowser

from wox import Wox

class UPSLookup(Wox):
    """Opens UPS tracking page, interfaces with Wox"""

    def query(self, query):
        """Looks up pasted tracking number"""
        
        
        result = [{
            "Title": "UPS Lookup",
            "SubTitle": f"Look up {query} on UPS",
            "IcoPath": "Images\\app.png",
            "JsonRPCAction": {
                "method": "openUPS",
                "parameters": [query],
                "dontHideAfterAction": False
            }
        }]
        return result

    def openUPS(self, tracking):
        open_new_tab_if_possible = 2
        url = f"https://wwwapps.ups.com/WebTracking/track?track=yes&trackNums={tracking}"
        webbrowser.open(url, new=open_new_tab_if_possible)


if __name__ == "__main__":
    UPSLookup()
