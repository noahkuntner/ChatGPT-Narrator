# Morgan Freeman - ChatGPT-Narrator


Following along what has been posted by @cbh123 in his repo: https://github.com/cbh123/narrator

- Main changes:
1. Produced Morgan Freeman voice in Elevenlabs
2. Change prompt to reflect a more direct view from Morgan Freeman
3. Open generated file up in Quicktime

Terminal Instructions
## add personal keys
export OPENAI_API_KEY=“<your key>”
export ELEVEN_API_KEY=“<your key>”
export ELEVENLABS_VOICE_ID=“<your morgan freeman voice key>”

# Morgan Freeman folder
cd /Users/noah_/Documents/Development/PersonalProjects/narrator_morgan/

source venv/bin/activate
pip install -r requirements.txt

# Circumvent packaging issues
export PYTHONPATH=$PWD/venv/lib/python3.11/site-packages

# Run scripts in separate Terminal
python capture.py

python narrator.py
