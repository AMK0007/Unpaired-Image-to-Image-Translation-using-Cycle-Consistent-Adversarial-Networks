# 🖼️ Converting Images to Cartoon Form using CycleGAN

This project demonstrates the use of CycleGAN to transform real-world images into cartoon-style images using unpaired image-to-image translation.

## 📁 Project Overview

CycleGAN is a type of Generative Adversarial Network (GAN) that learns to perform image translation without paired examples. This notebook walks through the process of training and using a CycleGAN model to convert images from the real domain to a cartoon domain.

## 📌 Features

- Load and preprocess unpaired datasets (real images and cartoon images)
- Build the Generator and Discriminator architectures based on the original CycleGAN paper
- Train the CycleGAN model on the dataset
- Evaluate and visualize the output of the model on test images

## 🧠 Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Matplotlib
- PIL (Python Imaging Library)

## 🗂️ Directory Structure

📦CartoonGAN
┣ 📜Converting_Images_to_Cartoon_Form_using_Cycle_GAN.ipynb
┣ 📁datasets
┃ ┣ 📁trainA (e.g., real photos)
┃ ┣ 📁trainB (e.g., cartoon images)
┃ ┣ 📁testA (real images for inference)
┣ 📁outputs (generated cartoon images)
┣ 📜README.md


## 🚀 Getting Started

### Prerequisites

Install required packages:

```bash
pip install tensorflow numpy matplotlib pillow


Run the Notebook

Open Converting_Images_to_Cartoon_Form_using_Cycle_GAN.ipynb in Jupyter Notebook or VS Code.

Run all cells to:

Load the dataset

Train the CycleGAN model

Generate cartoon-style images from input images

Dataset

Make sure you place your datasets in the following format:

datasets/
  trainA/
    real_image1.jpg
    real_image2.jpg
    ...
  trainB/
    cartoon_image1.jpg
    cartoon_image2.jpg
    ...
  testA/
    test_real_image1.jpg
    test_real_image2.jpg

📊 Results
Sample input and generated cartoon-style images are displayed at the end of the notebook.

📖 References
Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks
(https://arxiv.org/pdf/1703.10593)

TensorFlow GAN Tutorial

📜 License
This project is licensed under the MIT License.
