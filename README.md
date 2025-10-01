# Install Detectron2 v0.6(GPU) on Windows
Install the latest version of Detecteron2 on Windows with the least steps

# what is detectron2
Detectron2 is a PyTorch-based computer vision library developed by Facebook AI Research.
It provides state-of-the-art models for object detection, instance/semantic/panoptic segmentation, and keypoint detection.
https://github.com/facebookresearch/detectron2
# Step by step 
cuda11.3+cudnn8.2.1+vs build tools 2019
# Create a conda environment
`conda create -n detectron2 python=3.9 -y`
`conda activate detectron2`
# Install PyTorch with CUDA 11.3 Support
`pip install torch==1.10.1+cu113 torchvision==0.11.2+cu113 torchaudio==0.10.1 -f https://download.pytorch.org/whl/torch_stable.html`
# Get Detectron2 v0.6
https://github.com/facebookresearch/detectron2/releases/tag/v0.6
# Edit setup.py
Insert this line of code after line 79
`"-DWITH_CUDA"`
after modification
<img width="439" height="246" alt="image" src="https://github.com/user-attachments/assets/5c64f821-c9e3-4cbc-a98a-42decc8eec6e" />
# Install detectron2
Execute in the working directory
`pip install -e.`

