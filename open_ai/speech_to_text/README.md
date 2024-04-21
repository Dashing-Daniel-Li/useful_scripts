
# Audio Transcription Script

This script transcribes audio files to text using the OpenAI API, specifically leveraging the Whisper model. It is designed to handle MP3 files, splitting them into manageable chunks for transcription, and outputs the transcribed text with sentence segmentation.

## Prerequisites

Before you can run the script, you need to ensure you have Python installed on your system (Python 3.6+ recommended). You also need an OpenAI API key set as an environment variable.

See here: https://platform.openai.com/api-keys
## Installation

1. **Clone the Repository**
   ```bash
   git clone https://yourrepository.com/audio_transcription.git
   cd audio_transcription
   ```

2. **Set up a Python virtual environment (Optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variable**
   Make sure to set your `OPENAI_API_KEY` in your environment variables:
   ```bash
   export OPENAI_API_KEY='your_openai_api_key_here'  # On Windows use `set OPENAI_API_KEY=your_openai_api_key_here`
   ```

## Usage

To run the script, you need to provide the path to the input MP3 file and the desired path for the output text file:

```bash
python transcribe_audio.py -i path/to/your/input.mp3 -o path/to/your/output.txt
```

### Example

Transcribe the audio file `example.mp3` and output the transcription to `transcript.txt`:

```bash
python transcribe_audio.py -i example.mp3 -o transcript.txt
```

## Features

- **MP3 Audio Processing:** The script accepts MP3 files, splitting them into 10-minute chunks for efficient processing.


