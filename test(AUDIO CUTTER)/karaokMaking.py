from spleeter.separator import Separator
from pydub import AudioSegment
import os

# === CONFIGURATION ===
input_song = "/Users/rahulraj/Desktop/Natural Language Processing (NLP)/test/Pallavimusic.mp3"
output_folder = "/Users/rahulraj/Desktop/Natural Language Processing (NLP)/test/output"
final_output = "/Users/rahulraj/Desktop/Natural Language Processing (NLP)/test/output/final_karaoke.wav"

# Times in milliseconds
skip_start = 30000  # 00:30
skip_end = 46000    # 00:46

# Step 1: Separate using Spleeter (2 stems: vocals + accompaniment)
separator = Separator('spleeter:2stems')
separator.separate_to_file(input_song, output_folder)

# Step 2: File path setup
song_name = os.path.splitext(os.path.basename(input_song))[0]
accompaniment_path = os.path.join(output_folder, song_name, "accompaniment.wav")
original_path = os.path.join(output_folder, song_name, "mix.wav")

# Step 3: Load audio segments
karaoke_audio = AudioSegment.from_wav(accompaniment_path)
original_audio = AudioSegment.from_wav(original_path)

# Step 4: Merge final output
part1 = karaoke_audio[:skip_start]            # karaoke till 00:30
part2 = original_audio[skip_start:skip_end]   # keep vocals from 00:30 to 00:46
part3 = karaoke_audio[skip_end:]              # karaoke after 00:46

final_audio = part1 + part2 + part3

# Step 5: Export the final audio
final_audio.export(final_output, format="wav")
print(f"✅ Final karaoke exported at: {final_output}")
