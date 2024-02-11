import tkinter as tk
from tkinter import ttk

class Video:
    def __init__(self, title, url):
        self.title = title
        self.url = url

# Base class for UI components

class UIComponent:
    def __init__(self, master=None):
        self.master = master

class Header(UIComponent):
    def __init__(self, master=None):
        super().__init__(master)
        self.header_frame = ttk.Frame(master)
        self.header_frame.pack(side=tk.TOP, fill=tk.X)

        self.title_label = ttk.Label(self.header_frame, text="YouTube-like Interface", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)


class VideoList(UIComponent):
    def __init__(self, master=None, video_player=None):
        super().__init__(master)
        self.video_player = video_player

        self.video_list_frame = ttk.Frame(master)
        self.video_list_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.video_list_label = ttk.Label(self.video_list_frame, text="Video List", font=("Helvetica", 12, "bold"))
        self.video_list_label.pack(pady=5)

        self.video_listbox = tk.Listbox(self.video_list_frame, height=15, width=30)
        self.video_listbox.pack(padx=10, pady=10)
        self.populate_video_list()

        self.video_listbox.bind("<<ListboxSelect>>", self.play_selected_video)

    def populate_video_list(self):
        # Modified to fetch video titles and URLs from a database or a file
        self.videos = [
            Video("Disney Intro", "https://www.youtube.com/watch?v=cv6ncEYLRlk"),
            Video("Warner Bros Intro", "https://www.youtube.com/watch?v=OT9HsNszYCI"),
            Video("Sony Intro", "https://www.youtube.com/watch?v=q4T4vdAV5Vk"),
        
        ]

        for video in self.videos:
            self.video_listbox.insert(tk.END, video.title)

    def play_selected_video(self, event):
        selected_index = self.video_listbox.curselection()
        if selected_index:
            selected_video = self.video_listbox.get(selected_index[0])
            self.video_player.play_video(selected_video)

# Base class for Videoplayer

class VideoPlayer(UIComponent):
    def __init__(self, master=None):
        super().__init__(master)
        self.video_player_frame = ttk.Frame(master)
        self.video_player_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.video_player_label = ttk.Label(self.video_player_frame, text="Video Player", font=("Helvetica", 12, "bold"))
        self.video_player_label.pack(pady=5)

        self.video_canvas = tk.Canvas(self.video_player_frame, bg="black", height=300, width=500)
        self.video_canvas.pack(padx=10, pady=10)

        self.play_button = ttk.Button(self.video_player_frame, text="Play", command=self.play_video)
        self.play_button.pack(pady=5)

    def play_video(self, video_title):
        # You can implement video playback functionality here
        # For simplicity, we'll just print the selected video title and URL
        selected_video = next((video for video in app.videos if video.title == video_title), None)
        if selected_video:
            print(f"Playing Video: {selected_video.title} - {selected_video.url}")
            # Implement actual video playback here using a multimedia library or an external tool

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoList(root, VideoPlayer(root))
    root.mainloop()
