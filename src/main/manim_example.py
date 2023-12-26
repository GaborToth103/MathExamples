import sys
from manim import *
import logging
import shutil
import os
import subprocess

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square
        circle2 = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency
        square.rotate(PI / 4)  # rotate a certain amount
        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation0
        circle2.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle2))  # show the circle on screen
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(func, stroke_width=2, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)

class ManimCreator:
    def __init__(self, arguments: list[str]):
        logging.basicConfig(level=logging.WARNING, format='%(message)s', handlers=[logging.StreamHandler(), logging.FileHandler('test_results.log')])
        match len(sys.argv):
            case 1:
                self.folder_path = r'C:\Workspace\Projects\MathExamples\media\videos\1080p60\partial_movie_files\CreateCircle'
            case 2:
                self.folder_path = arguments[1]
            case default:
                raise Exception("Non-valid arguments provided")    
        self.main(sys.argv)

    def concat(self):
        output_file = self.folder_path + r"\output.mp4"
        file_list = [f for f in os.listdir(self.folder_path) if f.endswith('.mp4')]
        file_list.sort()  # Sort the files to concatenate in the correct order

        with open('file_list.txt', 'w') as file_list_file:
            for file_name in file_list:
                file_list_file.write(f"file '{os.path.join(self.folder_path, file_name)}'\n")

        subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'file_list.txt', '-c', 'copy', output_file])

        # Clean up the temporary file_list.txt
        os.remove('file_list.txt')

    def initialization(self):
        if os.path.exists(self.folder_path) and os.path.isdir(self.folder_path):
            shutil.rmtree(self.folder_path)

    def main(self, arguments: list[str]):
        self.initialization()
        self.CreateCircle().construct()
        self.concat()

if __name__ == "__main__":
    ManimCreator(sys.argv)
