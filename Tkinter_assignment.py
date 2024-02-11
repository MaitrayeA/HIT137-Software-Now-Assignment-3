import tkinter as tk
from tkinter import ttk

class YouTubeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube-like Interface")

        # Header
        header_frame = ttk.Frame(root)
        header_frame.pack(side=tk.TOP, fill=tk.X)

        title_label = ttk.Label(header_frame, text="YouTube-like Interface", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # Video List
        video_list_frame = ttk.Frame(root)
        video_list_frame.pack(side=tk.LEFT, fill=tk.Y)

        video_list_label = ttk.Label(video_list_frame, text="Video List", font=("Helvetica", 12, "bold"))
        video_list_label.pack(pady=5)

        video_listbox = tk.Listbox(video_list_frame, height=15, width=30)
        video_listbox.pack(padx=10, pady=10)
        self.populate_video_list(video_listbox)

        # Video Player
        video_player_frame = ttk.Frame(root)
        video_player_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        video_player_label = ttk.Label(video_player_frame, text="Video Player", font=("Helvetica", 12, "bold"))
        video_player_label.pack(pady=5)

        video_canvas = tk.Canvas(video_player_frame, bg="black", height=300, width=500)
        video_canvas.pack(padx=10, pady=10)

        play_button = ttk.Button(video_player_frame, text="Play", command=self.play_video)
        play_button.pack(pady=5)

    def populate_video_list(self, listbox):
        # Fetch video titles from a database or a file
        video_titles = ["Video 1", "Video 2", "Video 3", "Video 4", "Video 5"]

        for title in video_titles:
            listbox.insert(tk.END, title)

    def play_video(self):
        # Implement video playback functionality 
        print("Video is playing.")

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeApp(root)
    root.mainloop()
