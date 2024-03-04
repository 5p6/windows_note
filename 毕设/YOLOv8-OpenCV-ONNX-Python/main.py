import argparse

import cv2.dnn
import numpy as np
from utility import *
from ultralytics.utils import ASSETS, yaml_load
from ultralytics.utils.checks import check_yaml




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', default='../../best.onnx', help='Input your ONNX model.')
    parser.add_argument('--img', default="E:\\code\\python\\ultralytics\\ultralytics\\assets\\bus.jpg", help='Path to input image.')
    args = parser.parse_args()
    # main(args.model, args.img)
    main_video(args.model)
