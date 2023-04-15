# Object Detection with OpenCV and YOLOv4

This is a Python project that uses OpenCV and YOLOv4 for object detection. It allows the user to select certain objects to be detected in real-time using the GUI buttons. 

## Installation

1. Clone this repository to your local machine.
2. Install the required packages by running `pip install -r requirements.txt` in your command prompt or terminal.
3. Download the pre-trained YOLOv4-tiny model from the [YOLO website](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights) and save it in the `dnn_model` folder.
4. Download the YOLOv4-tiny configuration file from the [YOLO website](https://github.com/AlexeyAB/darknet/blob/master/cfg/yolov4-tiny.cfg) and save it in the `dnn_model` folder.
5. Create a file named `classes.txt` in the `dnn_model` folder and write the names of the objects you want to detect in separate lines.

## Usage

1. Run the `main.py` file.
2. Select the objects you want to detect by clicking on the GUI buttons.
3. Press the `Esc` key to exit the program.

## Contributing

Contributions are welcome! If you find any issues or have any suggestions, please open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
