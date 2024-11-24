# bjfu_digital_video
# License Plate Recognition Project

## Overview

This project implements a license plate recognition system that processes videos containing vehicles to extract and identify license plate numbers. The solution utilizes image processing techniques and machine learning algorithms to achieve accurate recognition under various conditions.

## Features

- **Video Input**: Accepts videos captured by users or sourced from online resources.
- **Image Preprocessing**: Enhances video frames for improved recognition accuracy.
- **License Plate Localization**: Identifies and isolates the license plate area in the video frames.
- **Character Segmentation**: Segments individual characters from the license plate.
- **Character Recognition**: Utilizes machine learning models to accurately identify characters.
- **User Interface**: Developed using QT for an intuitive and visual experience.

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - OpenCV for image processing
  - scikit-learn for support vector machine (SVM) implementation
  - TensorFlow/Keras for deep learning (if applicable)
  - QT for building the graphical user interface

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/license-plate-recognition.git
   cd license-plate-recognition
   ```

2. **Install Dependencies**:
   Make sure you have Python installed. Then, install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up QT Environment**:
   Ensure that QT and QT Designer are installed. Configure the QT environment in your IDE.

## Usage

1. **Run the Application**:
   Launch the application using the following command:
   ```bash
   python main.py
   ```

2. **Load Video**:
   Use the interface to load a video file containing vehicles.

3. **Start Recognition**:
   Click the "Start Recognition" button to begin processing the video. The system will display the recognized license plate numbers along with the original frames.

## Contributing

Contributions are welcome! If you have suggestions for improvements or want to report a bug, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to all libraries and resources that made this project possible.
- Acknowledgment of the support from peers and mentors during the development of this project.

---

Feel free to modify this template according to your project's specific details and requirements!