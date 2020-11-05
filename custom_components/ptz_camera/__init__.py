import requests
import time

DOMAIN = "ptz_camera"

ATTR_HOST = "host"
ATTR_PROFILE = "profile"
DEFAULT_HOST = "192.168.1.244"
DEFAULT_PROFILE = "Profile_1"
ATTR_PAN_TIME = "pan_time"
DEFAULT_PANT_TIME = 10
ATTR_MOVE_TIME = "move_time"
DEFAULT_MOVE_TIME = 0.3
DEFAULT_HEADERS = {'Content-Type':'application/soap+xml;charset=UTF8'}

def setup(hass, config):
    
    def stop(call):
        host = call.data.get(ATTR_HOST, DEFAULT_HOST)
        profile = call.data.get(ATTR_PROFILE, DEFAULT_PROFILE)

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

    def move_left(call):
        host = call.data.get(ATTR_HOST, DEFAULT_HOST)
        profile = call.data.get(ATTR_PROFILE, DEFAULT_PROFILE)
        move_time = call.data.get(ATTR_MOVE_TIME, DEFAULT_MOVE_TIME)

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
        time.sleep(move_time)
        stop(call)

    def move_right(call):
        host = call.data.get(ATTR_HOST, DEFAULT_HOST)
        profile = call.data.get(ATTR_PROFILE, DEFAULT_PROFILE)
        move_time = call.data.get(ATTR_MOVE_TIME, DEFAULT_MOVE_TIME)

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
        time.sleep(move_time)
        stop(call)
   
    def move_up(call):
        host = call.data.get(ATTR_HOST, DEFAULT_HOST)
        profile = call.data.get(ATTR_PROFILE, DEFAULT_PROFILE)
        move_time = call.data.get(ATTR_MOVE_TIME, DEFAULT_MOVE_TIME)

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
        time.sleep(move_time)
        stop(call)

    def move_down(call):
        host = call.data.get(ATTR_HOST, DEFAULT_HOST)
        profile = call.data.get(ATTR_PROFILE, DEFAULT_PROFILE)
        move_time = call.data.get(ATTR_MOVE_TIME, DEFAULT_MOVE_TIME)

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
        time.sleep(move_time)
        stop(call)

    def move_origin_pan(call):
        host = call.data.get(ATTR_HOST, DEFAULT_HOST)
        profile = call.data.get(ATTR_PROFILE, DEFAULT_PROFILE)

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

    def move_origin_tilt(call):
        host = call.data.get(ATTR_HOST, DEFAULT_HOST)
        profile = call.data.get(ATTR_PROFILE, DEFAULT_PROFILE)

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

    def move_origin(call):
        pan_time = call.data.get(ATTR_PAN_TIME, DEFAULT_PANT_TIME)
        move_origin_pan(call)
        time.sleep(pan_time)
        move_origin_tilt(call)


    hass.services.register(DOMAIN, "move_left", move_left)
    hass.services.register(DOMAIN, "move_right", move_right)
    hass.services.register(DOMAIN, "move_up", move_up)
    hass.services.register(DOMAIN, "move_down", move_down)
    hass.services.register(DOMAIN, "stop", stop)
    hass.services.register(DOMAIN, "move_origin", move_origin)
    hass.services.register(DOMAIN, "move_origin_pan", move_origin_pan)
    hass.services.register(DOMAIN, "move_origin_tilt", move_origin_tilt)

    # Return boolean to indicate that initialization was successfully.
    return True
