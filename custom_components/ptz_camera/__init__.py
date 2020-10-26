import requests
import time

DOMAIN = "ptz_camera"

ATTR_HOST = "host"
ATTR_PROFILE = "profile"
DEFAULT_HOST = "192.168.1.244"
DEFAULT_PROFILE = "Profile_1"
DEFAULT_HEADERS = {'Content-Type':'application/soap+xml;charset=UTF8'}

def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""
    
    def stop(call):
        host = call.data.get(ATTR_HOST, DEFAULT_HOST)

        xml = """<?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
         xmlns:tptz="http://www.onvif.org/ver20/ptz/wsdl">
         <soap:Body>
         <tptz:Stop>
         <tptz:ProfileToken>Profile_1</tptz:ProfileToken>
         <tptz:PanTilt>true</tptz:PanTilt>
         <tptz:Zoom>true</tptz:Zoom>
         </tptz:Stop>
         </soap:Body>
        </soap:Envelope> """

        r = requests.post('http://'+host+'/onvif/PTZ', data=xml, headers=DEFAULT_HEADERS)
        print (r.content)

    def move_left(call):
        """Handle the service call."""
        host = call.data.get(ATTR_HOST, DEFAULT_HOST)

        xml = """<?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
         xmlns:tptz="http://www.onvif.org/ver20/ptz/wsdl"
         xmlns:tt="http://www.onvif.org/ver10/schema">
         <soap:Body>
         <tptz:ContinuousMove>
         <tptz:ProfileToken>Profile_1</tptz:ProfileToken>
         <tptz:Velocity>
         <tt:PanTilt x="-0.5" y="0"/>
         <tt:Zoom x="1"/>
         </tptz:Velocity>
         </tptz:ContinuousMove>
         </soap:Body>
        </soap:Envelope>"""

        r = requests.post('http://'+host+'/onvif/PTZ', data=xml, headers=DEFAULT_HEADERS)
        print (r.content)
        time.sleep(0.3)
        stop(call)

    def move_rigth(call):
        host = call.data.get(ATTR_HOST, DEFAULT_HOST)

        xml = """<?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
         xmlns:tptz="http://www.onvif.org/ver20/ptz/wsdl"
         xmlns:tt="http://www.onvif.org/ver10/schema">
         <soap:Body>
         <tptz:ContinuousMove>
         <tptz:ProfileToken>Profile_1</tptz:ProfileToken>
         <tptz:Velocity>
         <tt:PanTilt x="0.5" y="0"/>
         <tt:Zoom x="1"/>
         </tptz:Velocity>
         </tptz:ContinuousMove>
         </soap:Body>
        </soap:Envelope>"""

        r = requests.post('http://'+host+'/onvif/PTZ', data=xml, headers=DEFAULT_HEADERS)
        print (r.content)
        time.sleep(0.3)
        stop(call)
   
    def move_up(call):
        host = call.data.get(ATTR_HOST, DEFAULT_HOST)

        xml = """<?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
         xmlns:tptz="http://www.onvif.org/ver20/ptz/wsdl"
         xmlns:tt="http://www.onvif.org/ver10/schema">
         <soap:Body>
         <tptz:ContinuousMove>
         <tptz:ProfileToken>Profile_1</tptz:ProfileToken>
         <tptz:Velocity>
         <tt:PanTilt x="0" y="0.5"/>
         <tt:Zoom x="1"/>
         </tptz:Velocity>
         </tptz:ContinuousMove>
         </soap:Body>
        </soap:Envelope>"""

        r = requests.post('http://'+host+'/onvif/PTZ', data=xml, headers=DEFAULT_HEADERS)
        print (r.content)
        time.sleep(0.3)
        stop(call)

    def move_down(call):
        host = call.data.get(ATTR_HOST, DEFAULT_HOST)

        xml = """<?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
         xmlns:tptz="http://www.onvif.org/ver20/ptz/wsdl"
         xmlns:tt="http://www.onvif.org/ver10/schema">
         <soap:Body>
         <tptz:ContinuousMove>
         <tptz:ProfileToken>Profile_1</tptz:ProfileToken>
         <tptz:Velocity>
         <tt:PanTilt x="0" y="-0.5"/>
         <tt:Zoom x="1"/>
         </tptz:Velocity>
         </tptz:ContinuousMove>
         </soap:Body>
        </soap:Envelope>"""

        r = requests.post('http://'+host+'/onvif/PTZ', data=xml, headers=DEFAULT_HEADERS)
        print (r.content)
        time.sleep(0.3)
        stop(call)

    hass.services.register(DOMAIN, "move_left", move_left)
    hass.services.register(DOMAIN, "move_rigth", move_rigth)
    hass.services.register(DOMAIN, "move_up", move_up)
    hass.services.register(DOMAIN, "move_down", move_down)
    hass.services.register(DOMAIN, "stop", stop)

    # Return boolean to indicate that initialization was successfully.
    return True
