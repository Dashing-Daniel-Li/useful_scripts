import argparse
from pydub import AudioSegment
import os
import openai
import pyperclip
import nltk
from nltk.tokenize import sent_tokenize

def transcribe_audio(input_filepath, output_filepath):
    if not os.getenv('OPENAI_API_KEY'):
        raise Exception('OPENAI_API_KEY is required. Set this environment variable')

    client = openai.Client(api_key=os.getenv('OPENAI_API_KEY'))
    audio = AudioSegment.from_mp3(input_filepath)

    chunk_length_ms = 10 * 60 * 1000  # 10 minutes in milliseconds
    chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]

    full_transcription = ""
    count = 0

    for i, chunk in enumerate(chunks):
        count += 1
        print('Processing chunk', count)
        chunk_filename = f'temp_chunk_{i}.mp3'
        chunk.export(chunk_filename, format='mp3')

        with open(chunk_filename, 'rb') as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="text",
            )
            full_transcription += transcription + " "

        # Remove the temporary chunk file after processing
        os.remove(chunk_filename)

    pyperclip.copy(full_transcription)
    formatted_text = split_text_into_sentences_nltk(full_transcription)

    with open(output_filepath, 'w') as f:
        f.write(formatted_text)

    print('Transcription complete:', output_filepath)

def split_text_into_sentences_nltk(text):
    nltk.download('punkt')
    sentences = sent_tokenize(text)
    return "\n\n".join(sentences)

def main():
    parser = argparse.ArgumentParser(description="Transcribe an audio file to text.")
    parser.add_argument("-i", "--input_filepath", type=str, help="Path to the input MP3 file")
    parser.add_argument("-o", "--output_filepath", type=str, help="Path to the output text file")
    args = parser.parse_args()

    transcribe_audio(args.input_filepath, args.output_filepath)

if __name__ == "__main__":
    main()

