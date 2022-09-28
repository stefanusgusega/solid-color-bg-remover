"""
Main program
"""
import argparse
from src.remover import remove_solid_color_bg

parser = argparse.ArgumentParser()
parser.add_argument("--imgpath")
parser.add_argument("--solidcolor")
parser.add_argument("--tosave")
args = parser.parse_args()

remove_solid_color_bg(args.imgpath, args.solidcolor, args.tosave)
