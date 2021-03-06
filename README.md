# PiCroftTTSClient
This project I have created a web-based TTS client for Mycroft assistant devices. There are a couple of requirements that I need to keep to, but everyone can follow these steps to create your own TTS client.

### Software used:
- [PiCroft (Custom OS to run the Mycroft Assistant)](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/get-mycroft/picroft)
- [Balena Etcher](https://www.balena.io/etcher/)
- Your preferred code editor

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
To let the Mycroft assistant run on a Raspberry Pi, you need to burn a custom Linux Distribution called PiCroft on an sd card which you later use to boot your Raspberry Pi with. To set everything up you can follow the steps on the official PiCroft Wiki (https://mycroft-ai.gitbook.io/docs/using-Mycroft-ai/get-mycroft/picroft)

### Speaker setup
Once you followed the setup from the site they recommend using an analog speaker (a speaker which is connected with a 3,5mm jack). If you connect your raspberry pi via HDMI with tv or monitor with speakers it also works fine, but maybe not so practical if you want to use Mycroft daily.

## Software

### Mobile friendly
Since one of the requirements is to make the program mobile-friendly. I decided to create a simple website using PHP. It has a form where you can fill in your text that you want to hear and a button to send the text to your Mycroft instance.

If I wanted to, I could also make it in Android studio so I can run it as an android app instead of making it run from the browser, which eventually is more professional, but then Apple and Windows phone users are not able to use it since I need to rewrite the app later.

### Communication
When I was browsing through some documentation of some Mycroft skills. I found out that they had a MessageBusClient pre-installed.  

The MessageBusClient has a very good Python library which you can use to connect and send messages to your local Mycroft device. Since I was using PHP I was not able to use that library. So I went to their GitHub repository [which can be found here](https://github.com/MycroftAI/mycroft-messagebus-client) since Mycroft is an open-source project and was looking for the source code of the MessageBusClient.

They established a connection via WebSockets. Websockets is a protocol built on the HTTP protocol. With WebSockets, you can open a connection with another device that uses WebSockets and you can hold on to that connection to send data until you close the connection. While you are connected you can send and receive data asynchronously. Since you only close the connection when you want, you receive and send the data (almost) realtime which is also called a stream.

To let Mycroft speak out your message, you need to send a message in JSON format via the WebSocket connection. The JSON message looks something like this:
```json
{"type": "speak", "data": {"utterance":"YOUR DATA"} } 
```
To let Mycroft speak the message the type must be "speak". After the utterance tag, you need to put your message.

The default address where you need to send the JSON message to is 
``` 
ws://[YOUR LOCAL MYCROFT IP]:8181/core
```
You can find your local Mycroft IP in your router.

## Result:
[![Mycroft mobile TTS client](https://yt-embed.herokuapp.com/embed?v=Ey4miKTGQSc)](https://www.youtube.com/watch?v=Ey4miKTGQSc)


