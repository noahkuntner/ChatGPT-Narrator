# Morgan Freeman narrates Life

Inspired by the David Attenborough narrates your life implementation. ->
https://twitter.com/charliebholtz/status/1724815159590293764

# Example of desired output:
![image](https://github.com/user-attachments/assets/890246c7-bf0b-4032-bf25-c97d07e9cfdd)

- ChatGPT-4 generates script based on what is being seen.
- ElevenLabs cloned voice is used.

## Setup -> 

Clone this repo, and setup and activate a virtualenv:

```bash
python3 -m pip install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
```

Then, install the dependencies:
`pip install -r requirements.txt`



Make a new voice in Eleven and get the voice id of that voice using their [get voices](https://elevenlabs.io/docs/api-reference/voices) API, or by clicking the flask icon next to the voice in the VoiceLab tab.

## Run it!

In on terminal, run the webcam capture:
```bash
python capture.py
```
In another terminal, run the narrator:

```bash
python narrator.py
```

