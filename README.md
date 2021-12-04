# PTZ-YCC365

This custom component allows you to use the Pan and Tilt functions of Chinese cameras that do not fully comply with the ONVIF protocol.

For some reason, the Home Assistant ONVIF integration does not work with my cameras that use the YCC365 Plus app for their configuration.

I've used the ONVIF Device Manager application and from this PC application I can use the pan and tilt functions.

Apparently, these cameras do not fully comply with the ONVIF protocol and the Home Assistant integration cannot integrate them at the moment.

I have looked for a solution to be able to use in Home Assistant with the pan and tilt option.

Using the Wireshark application I was able to obtain information to use these cameras.

In order to use this custom component, I recommend that you integrate the signal from your cameras with motionEye. **This component does not integrate the video signal of your cameras, only the pan and tilt function.**

### Tested cameras

  - [YCC365 Plus IP Camera 1080P 360°](https://es.aliexpress.com/item/4000055767917.html)
  
![](camara360.jpg)
  
      - rtsp: // IP: 554 1280x720 h264 no audio
      - rtsp: // IP: 554/0 / av0 1280x720 h264 mono audio 8000Hz 16 bits
      - rtsp: // IP: 554/0 / av1 640x352 h264 mono audio 8000Hz 16 bits

  - [YCC365 Plus IP Outdoor Camera°](https://es.aliexpress.com/item/4001201258483.html)
  
![](camaraExterior.jpg)
  
      - rtsp: // IP: 554 1280x720 h264 no audio
      - rtsp: // IP: 554/0 / av0 1280x720 h264 mono audio 8000Hz 16 bits
      - rtsp: // IP: 554/0 / av1 640x352 h264 mono audio 8000Hz 16 bits

## Installation
You just need to install the custom component as usual. Copy the otz_camera folder from this project to your `/config/custom_components/` Home Assistant directory.

## Setting
In your configuration.yaml:
```yaml
ptz_camera:
```
## Services
This custom component creates multiple services with domain ptz_camera. To get information about these services you can use “Developer Tools”> Services. You will have detailed information about the arguments to call each service.

## Camera Entity

You can create a camera in the usual way. I recommend using the [motionEye](https://addons.community/) addon  and creating a mjpeg camera. It is the best setting I have found with a low delay. An example of a configuration would be:

```yaml
camera:
  - platform: mjpeg
    name: living-room
    mjpeg_url: http://192.168.1.111:8083
```

## Card with controls
An easy way to use the pan and tilt controls is to layer the controls on top of a camera image. Replace the IP address in this example with the IP address of your camera.

```yaml
type: picture-elements
camera_view: live
camera_image: camera.salon
elements:
  - type: icon
    icon: 'mdi:arrow-left-drop-circle'
    tap_action:
      action: call-service
      service: ptz_camera.move_left
      service_data:
        host: 192.168.1.244
    style:
      bottom: 45%
      left: 5%
      color: white
      opacity: 0.5
      transform: 'scale(1.5, 1.5)'
  - type: icon
    icon: 'mdi:arrow-right-drop-circle'
    tap_action:
      action: call-service
      service: ptz_camera.move_right
      service_data:
        host: 192.168.1.244
    style:
      bottom: 45%
      right: 5%
      color: white
      opacity: 0.5
      transform: 'scale(1.5, 1.5)'
  - type: icon
    icon: 'mdi:arrow-up-drop-circle'
    tap_action:
      action: call-service
      service: ptz_camera.move_up
      service_data:
        host: 192.168.1.244
    style:
      top: 10%
      left: 46%
      color: white
      opacity: 0.5
      transform: 'scale(1.5, 1.5)'
  - type: icon
    icon: 'mdi:arrow-down-drop-circle'
    tap_action:
      action: call-service
      service: ptz_camera.move_down
      service_data:
        host: 192.168.1.244
    style:
      bottom: 10%
      left: 46%
      color: white
      opacity: 0.5
      transform: 'scale(1.5, 1.5)'
  - type: icon
    icon: 'mdi:arrow-expand-all'
    tap_action:
      action: more-info
    entity: camera.salon
    style:
      top: 5%
      right: 5%
      color: white
      opacity: 0.5
      transform: 'scale(1.5, 1.5)'

```
      
![](tarjeta.jpg)
