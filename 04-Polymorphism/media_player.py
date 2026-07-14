class MediaPlayer:
    """The Parent Class representing a generic media file."""
    def __init__(self, filename):
        self.filename = filename

    def play(self):
        # This will be overridden by the child classes below
        print("Playing standard media...")


class AudioPlayer(MediaPlayer):
    """Child Class 1: Specialized in music/audio streams."""
    def __init__(self, filename, bitrate="320kbps"):
        super().__init__(filename)
        self.bitrate = bitrate

    def play(self):
        """Polymorphism: Customizing how music tracks are booted up."""
        print(f"🎵 Audio Stream Active: '{self.filename}'")
        print(f"   Audio Quality Preset: {self.bitrate} | Playing through system speakers...")


class VideoPlayer(MediaPlayer):
    """Child Class 2: Specialized in high-definition video displays."""
    def __init__(self, filename, resolution="1080p"):
        super().__init__(filename)
        self.resolution = resolution

    def play(self):
        """Polymorphism: Customizing how video files are opened with screen visuals."""
        print(f"🎬 Video Stream Active: '{self.filename}'")
        print(f"   Screen Resolution Mode: {self.resolution} | Rendering frames on visual display...")


# --- The Polymorphic Function ---
# This core engine takes any player object and taps the single .play() button
def click_play_button(media_object):
    media_object.play()
    print("-" * 60)


# --- Testing the Media Hub ---

print("=== 🍿 SYSTEM MEDIA PLAYER BOOTING ===\n")

# 1. Load and play an audio track
song = AudioPlayer(filename="dil_ko_karaar_aaya.mp3", bitrate="320kbps")
click_play_button(song)

# 2. Load and play a movie file
movie = VideoPlayer(filename="interstellar_trailer.mp4", resolution="4K UltraHD")
click_play_button(movie)