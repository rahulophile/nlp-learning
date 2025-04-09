from pydub import AudioSegment

# Load the audio file
audio = AudioSegment.from_mp3("/Users/rahulraj/Desktop/Natural Language Processing (NLP)/test/GHAR_MORE.mp3")


# Define start and end times in milliseconds
remove_start = 1 * 60 * 1000 + 34 * 1000 + 0  # 01:34:00
remove_end = 2 * 60 * 1000 + 30 * 1000 + 700    # 02:31:50

# Create the new audio by removing the unwanted part
edited_audio = audio[:remove_start] + audio[remove_end:]

# Export the edited audio
output_path = "/Users/rahulraj/Desktop/Natural Language Processing (NLP)/test/Pallavimusic.mp3"
edited_audio.export(output_path, format="mp3")


output_path
