import os
from openai import OpenAI
import base64
import json
import time
import simpleaudio as sa
import errno
from elevenlabs import generate, play, set_api_key, voices
import subprocess


# Your Open AI API-key
api_key = ""
client = OpenAI(api_key=api_key)


# Your ElevenLabs API-key
set_api_key("")

def encode_image(image_path):
    while True:
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode("utf-8")
        except IOError as e:
            if e.errno != errno.EACCES:
                # Not a "file in use" error, re-raise
                raise
            # File is being written to, wait a bit and retry
            time.sleep(0.1)


def play_audio(text):
    audio = generate(text, voice="q7lZ63jPhYTOL2rU2Auh")

    # Create a unique directory for each audio file
    unique_id = base64.urlsafe_b64encode(os.urandom(30)).decode("utf-8").rstrip("=")
    dir_path = os.path.join("narration", unique_id)
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, "audio.wav")

    with open(file_path, "wb") as f:
        f.write(audio)

    open_with_quicktime(file_path)  # Open the audio file with QuickTime


def open_with_quicktime(file_path):
    quicktime_path = "/System/Applications/QuickTime Player.app"
    subprocess.run(["open", "-a", quicktime_path, "-j", file_path])

# Example usage:
latest_file_path = None

# Play the latest recording
if latest_file_path is not None:
    open_with_quicktime(latest_file_path)


def generate_new_line(base64_image):
    return [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe this image"},
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                },
            ],
        },
    ]


# Narration Function calling ChatGPT and sending it over to Elevenlabs for voice.
def analyze_image(base64_image, script):
    image_description = "A human is sitting at a desk with multiple screens open on Saturday around noon."

    # Ensure script is a list of strings
    script_messages = [{"role": "user", "content": str(script_content)} for script_content in script]  # Convert to string if needed

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": """
                You are Morgan Freeman. Narrate a human, as if you are describing a good friend with a bright future ahead. Do not give him a name. 
                Talk about the background you are seeing. If I do anything remotely unexpected, describe how this ties into my greater aspiring character. However, focus on the dangers this person is facing and how his character needs to push through it. Make it punchy and concise, and make it sound like you care about this person and his endearing tasks at hand. Maximum thirty seconds to read. Don't repeat yourself. If 
                """,
            },

        # Ensure all content is properly formatted
        ] + script_messages + [{"role": "user", "content": image_description}],  
        max_tokens=500,
    )

    response_text = response.choices[0].message.content
    script.clear()  # Clear the script after usage
    return response_text


def main():
    script = []

    while True:
        # path to your image
        image_path = os.path.join(os.getcwd(), "./frames/frame.jpg")

        # getting the base64 encoding
        base64_image = encode_image(image_path)

        # analyze posture
        print("\n👀 Morgan Freeman is watching...")
        analysis = analyze_image(base64_image, script=script)

        print("\n🎙️ Morgan Freeman says:")
        print(analysis)

        play_audio(analysis)

        script = script + [{"role": "assistant", "content": analysis}]

        # wait for 30 seconds
        time.sleep(60)


if __name__ == "__main__":
    main()
