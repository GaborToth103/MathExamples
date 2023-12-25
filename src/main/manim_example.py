import sys
from manim import *
import logging
import shutil

folder_path = r'C:\Workspace\Projects\MathExamples\media'

# Use shutil.rmtree to delete the entire folder and its contents
shutil.rmtree(folder_path)

class ContinuousMotion(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(func, stroke_width=2, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)

def main(arguments: list[str]):
    ContinuousMotion().construct()

def argument_selector(arguments: list[str]):
    logging.basicConfig(level=logging.WARNING, format='%(message)s', handlers=[logging.StreamHandler(), logging.FileHandler('test_results.log')])
    match len(sys.argv):
        case 1:
            main(sys.argv)
        case default:
            raise Exception("Non-valid arguments provided")

if __name__ == "__main__":
    argument_selector(sys.argv)
