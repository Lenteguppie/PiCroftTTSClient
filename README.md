# PiCroftTTSClient
In this little project I am going to create a web based TTS client for MyCroft assistant devices. There are a couple of requirements that I need to keep to, but it is possible for everyone to follow this steps to create your own TTS client.

### Software used:
- [PiCroft (Custom OS to run the MyCroft Assistant)](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/get-mycroft/picroft)
- [Balena Etcher](https://www.balena.io/etcher/)
- Your preffered code editor

### Hardware used:
- Raspberry Pi 3b+ or Raspberry Pi 4
- SD card (8GB or higher)
- Computer screen
- Speaker with 3,5 mm jack (HDMI cable works fine)
- Keyboard
### Requirements:
- This project needs to be mobile user friendly.
- This program must run on a raspberry pi with at least a speaker connected

## Raspberry pi setup
In order to let the MyCroft assistant run on a Raspberry Pi, you need to burn a custom Linux Distribution called PiCroft on a sd card which you later use to boot your Raspberry Pi with. To set everything up you can follow the steps on the official PiCroft Wiki (https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/get-mycroft/picroft)

### Speaker setup
Once you followed the setup from the site they reccommend to use an analog speaker (a speaker which is connected with an 3,5mm jack). If you connect your raspberry pi via HDMI with a tv or monitor with speakers it also works fine, but maybe not so practical of you want to use MyCroft daily.
