import moviepy
from faster_whisper import WhisperModel

# I USED THIS TO EXTRACT THE AUDIO FROM THE VIDEO!!!
# if __name__ == '__main__':
    # video = 'video-test.mp4'
    # content = moviepy.VideoFileClip(video)
    # content.audio.write_audiofile('test_audio.mp3')

# audio_path = "test_audio.mp3"
# model = WhisperModel('base', device='cpu', compute_type='int8')

# model.transcribe() returns the actual transcript content stored in "segments" and any extra information stored in "info"
# segments, info = model.transcribe(audio_path) 

# full_text = ""
# for segment in segments:
#     full_text += segment.text + " "

# full_text = full_text.strip()

# with open("transcript.txt", "w", encoding="utf-8") as f:
#     f.write(full_text)

# print('Language:', info.language)
# print(info)

def extract_audio(video_path, output_audio_path='audio.mp3'):
    audio_content = moviepy.VideoFileClip(video_path)
    audio_content.audio.write_audiofile(output_audio_path)
    return output_audio_path


def transcribe_audio(audio_path):
    model = WhisperModel('base', device='cpu', compute_type='int8')
    
    # model.transcribe() returns the actual transcript content stored in "segments" and any extra information stored in "info"
    segments, info = model.transcribe(audio_path) 
    
    full_text = ""
    for segment in segments:
        full_text += segment.text + " "

    full_text = full_text.strip()
    return full_text


def save_transcript(transcript, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(transcript)


def main():
    video_path = input('Please enter the video file name (including .mp4): ')
    audio_path = extract_audio(video_path)
    transcript = transcribe_audio(audio_path)
    save_transcript(transcript, 'transcript.txt')
    print('Transcript was successfully generated from ' + video_path + '!')


if __name__ == '__main__':
    main()