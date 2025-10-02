# Install Detectron2 v0.6(GPU) on Windows
Install the latest version of Detecteron2 on Windows with the least steps

# What is detectron2
Detectron2 is a PyTorch-based computer vision library developed by Facebook AI Research.
It provides state-of-the-art models for object detection, instance/semantic/panoptic segmentation, and keypoint detection.
https://github.com/facebookresearch/detectron2
# Needs
cuda11.3 + cudnn8.2.1 + vs build tools 2019
# Create a conda environment
```bash
conda create -n detectron2 python=3.9 -y
conda activate detectron2
```
# Install PyTorch with CUDA 11.3 Support
```bash
pip install torch==1.10.1+cu113 torchvision==0.11.2+cu113 torchaudio==0.10.1 -f https://download.pytorch.org/whl/torch_stable.html
```
# Get Detectron2 v0.6
https://github.com/facebookresearch/detectron2/releases/tag/v0.6
# Edit setup.py
Insert this after line 79
```bash
"-DWITH_CUDA"
```
After modification

<img width="439" height="246" alt="image" src="https://github.com/user-attachments/assets/5c64f821-c9e3-4cbc-a98a-42decc8eec6e" />

# Install detectron2
Execute under your working directory
```bash
pip install -e.
```
# Install fixed versions of numpy, Pillow and opencv
```bash
pip install numpy==1.26.4
pip install pillow==9.5.0
pip install opencv-python==4.9.0.80
```
# Test
```bash
python test.py --image demo.jpg
```
The detection result

![test_result](https://github.com/user-attachments/assets/d18f1d2e-6fb0-4471-a595-70688b7c57a1)

