import tkinter as tk
from tkVideoPlayer import TkinterVideo

class VideoGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo Interativo")
        self.root.geometry("800x600")

        self.video_player = TkinterVideo(master=root, scaled=True)
        self.video_player.pack(expand=True, fill="both")

        self.choice_frame = tk.Frame(root)
        
        self.play_video("video_inicial.mp4")  # Substitua pelo caminho do primeiro vídeo

        self.video_player.bind("<<Ended>>", self.exibir_opcoes)

    def play_video(self, video_path):
        self.video_player.load(video_path)
        self.video_player.play()

    def exibir_opcoes(self, event):
        self.choice_frame.pack(pady=20)
        
        opcao1 = tk.Button(self.choice_frame, text="Opção 1", command=lambda: self.escolher("video_opcao1.mp4"))
        opcao2 = tk.Button(self.choice_frame, text="Opção 2", command=lambda: self.escolher("video_opcao2.mp4"))
        
        opcao1.pack(side="left", padx=10)
        opcao2.pack(side="right", padx=10)

    def escolher(self, novo_video):
        self.choice_frame.pack_forget()
        self.play_video(novo_video)

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoGameApp(root)
    root.mainloop()
