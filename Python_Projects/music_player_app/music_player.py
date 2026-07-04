import os
import time

class Track:
    """Models a single audio asset, encapsulating metadata properties."""
    def __init__(self, title, artist, album, duration_seconds):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration_seconds = duration_seconds

    def get_formatted_duration(self):
        """Converts raw seconds into a standard MM:SS string representation."""
        minutes = self.duration_seconds // 60
        seconds = self.duration_seconds % 60
        return f"{minutes:02d}:{seconds:02d}"


class AudioQueueManager:
    """Manages playback pipeline states, playlist indexing, and track navigation."""
    def __init__(self, tracks):
        self.playlist = tracks
        self.current_index = 0
        self.is_playing = False
        self.simulated_progress = 0  # Tracks elapsed time in seconds

    def get_current_track(self):
        """Safely extracts the active track object from the queue array."""
        if 0 <= self.current_index < len(self.playlist):
            return self.playlist[self.current_index]
        return None

    def display_player_interface(self):
        """Renders an interactive playback matrix terminal layout dashboard."""
        track = self.get_current_track()
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("=" * 50)
        print("         STREAMING MEDIA CORE ARCHITECTURE        ")
        print("=" * 50)
        
        if not track:
            print("[!] Queue Empty: No media assets currently buffered.")
            print("=" * 50)
            return

        state_symbol = "▶ PLAYING" if self.is_playing else "❚❚ PAUSED"
        print(f" Status: {state_symbol}")
        print(f" Track:  {track.title}")
        print(f" Artist: {track.artist}")
        print(f" Album:  {track.album}")
        print("-" * 50)
        
        # Build a dynamic, visual progress meter bar
        total_seconds = track.duration_seconds
        progress_ratio = self.simulated_progress / total_seconds if total_seconds > 0 else 0
        bar_length = 20
        filled_blocks = int(progress_ratio * bar_length)
        empty_blocks = bar_length - filled_blocks
        progress_bar = "█" * filled_blocks + "░" * empty_blocks
        
        # Format times nicely
        current_time_str = f"{self.simulated_progress // 60:02d}:{self.simulated_progress % 60:02d}"
        print(f" {current_time_str} [{progress_bar}] {track.get_formatted_duration()}")
        print("=" * 50)
        print(" Controls: (1) Play/Pause  (2) Next  (3) Prev  (4) Stop  (5) Exit")

    def toggle_play_pause(self):
        """Modulates active stream execution states."""
        if not self.playlist:
            return
        self.is_playing = not self.is_playing
        if self.is_playing and self.simulated_progress == 0:
            self.simulated_progress = 3  # Advance slightly to simulate instant audio buffering

    def advance_track(self):
        """Steps the pointer forward cleanly to the next item in the collection array."""
        if self.current_index < len(self.playlist) - 1:
            self.current_index += 1
            self.simulated_progress = 0
            print(f"\n[~] Advancing track index pointer to item {self.current_index + 1}...")
        else:
            print("\n[-] End of Queue: No subsequent pipeline tracks available.")
            time.sleep(1.5)

    def regress_track(self):
        """Steps the pointer backward to the previous item in the array."""
        if self.current_index > 0:
            self.current_index -= 1
            self.simulated_progress = 0
            print(f"\n[~] Regressing track index pointer to item {self.current_index + 1}...")
        else:
            print("\n[-] Head of Queue: Already processing initial index track entity.")
            time.sleep(1.5)

    def stop_playback(self):
        """Resets stream progress variables and halts engine states."""
        self.is_playing = False
        self.simulated_progress = 0


def main():
    """Builds the asset database and kicks off the execution loop inside Pydroid 3."""
    # Data Layer: Seeding track instances into our management registry list
    audio_database = [
        Track("Code Optimization Symphony", "The Tech Synthesizers", "Algorithms Vol. 1", 185),
        Track("Database Migration Blues", "Query Operators", "Structured Protocols", 240),
        Track("Asynchronous Love Story", "Callback Stack", "Runtime Loops", 192)
    ]
    
    manager = AudioQueueManager(audio_database)
    
    while True:
        manager.display_player_interface()
        choice = input("\nEnter menu command index (1-5): ").strip()
        
        if choice == "1":
            manager.toggle_play_pause()
        elif choice == "2":
            manager.advance_track()
        elif choice == "3":
            manager.regress_track()
        elif choice == "4":
            manager.stop_playback()
        elif choice == "5":
            print("\nMedia Pipeline Detached. Audio Core Systems Offline.")
            break
        else:
            # Simulate a small playback advancement block if the engine is running
            if manager.is_playing:
                current_track = manager.get_current_track()
                if current_track and manager.simulated_progress < current_track.duration_seconds:
                    manager.simulated_progress = min(manager.simulated_progress + 15, current_track.duration_seconds)

if __name__ == "__main__":
    main()
