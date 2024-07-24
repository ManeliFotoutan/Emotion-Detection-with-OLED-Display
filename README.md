# Emotion Detection with OLED

This project demonstrates how to detect emotions in real-time using a webcam and display corresponding facial expressions on an OLED screen controlled by an Arduino. The setup involves a Python script for emotion detection and an Arduino sketch to display emotions on the OLED display.

## Project Overview

The project uses OpenCV and DeepFace to perform real-time emotion detection from a webcam feed. The detected emotion is then sent to an Arduino via serial communication. The Arduino controls an OLED display to show different expressions based on the detected emotion.

### Components Required

- Arduino UNO or MEGA
- 128x64 OLED Display
- Webcam
- Connecting cables

### Python Script

The Python script (`eye.py`) captures video from the webcam, detects faces, and analyzes emotions using DeepFace. The detected emotion is sent to the Arduino over serial communication.

### Arduino Sketch

The Arduino sketch (`eye.ino`) receives the emotion data from the Python script and displays corresponding graphics on the OLED screen. The sketch currently supports three emotions: happy, sad, and angry.

## Adding New Emotions

To add new emotions to your project, follow these steps:

1. **Create C File Arrays for New Emotions:**
   Use an 'Image to C Array Converter' to generate C file arrays for your new emotion images. 

   - **LVGL Online Image Converter:** [LVGL Image Converter](https://lvgl.io/tools/imageconverter)
   - **Image to C Array Converter Tutorial:** [Tutorial](https://ctmprojectsblog.wordpress.com/2022/02/10/arduino-oled-eyes/)

2. **Update the Arduino Sketch:**
   - Add new C file arrays to the Arduino sketch for the new emotions.
   - Modify the `loop` function to handle the new emotions. You will need to add `else if` conditions for each new emotion and display the corresponding bitmap.

   For example:
   ```cpp
   else if (incomingEmotion == "new_emotion") {
     display.clearDisplay();  // Clear the buffer
     display.drawBitmap(0, 0, image_data_NEW_EMOTION, 128, 64, 1);
     display.display();    // Action for "new_emotion"
   }
