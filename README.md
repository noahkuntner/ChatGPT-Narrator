# Morgan Freeman narrates Life

Forked from David Attenborough narrates your life. ->
https://twitter.com/charliebholtz/status/1724815159590293764

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

