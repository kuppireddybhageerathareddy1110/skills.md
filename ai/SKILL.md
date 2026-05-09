---
name: ai
description: "for my ai domain projects"
---


---
title: "AI/ML Engineering Skill Reference"
version: "2024.2"
author: "AI Engineering Team"
date: "2024"
description: "Comprehensive guide for research-grade ML engineering with explainability focus"
tags: ["machine-learning", "deep-learning", "ai", "pytorch", "transformers", "explainable-ai"]
license: "MIT"
python_version: "3.10.12"
cuda_version: "12.2"
focus: "Build, Understand, Explain, Extend"
---

# AI/ML Engineering - SKILL.md

## Command Reference

### `question`
Direct answer • Mathematical explanation • No code

### `implementation guide`
Architecture • Training pipeline • Model selection • No full code

### `folder structure`
Project structure • Dataset organization • Model checkpoints

### `correct code`
Fix errors • Dependency issues • Version conflicts

### `fullprojectwithcode`
Complete ML pipeline • Training + Inference • Deployment ready

### `information`
Theory • Math (Linear Algebra, Statistics) • Research papers

### `design`
Model architecture • Data flow • System design

### `just training`
Training loop • Loss functions • Optimization

### `just inference`
Model loading • Prediction • API serving

### `just preprocessing`
Data cleaning • Feature engineering • Augmentation

### `from scratch`
Build without libraries • Pure NumPy/Python • Educational

### `explainable ai`
Interpretability • SHAP/LIME • Attention visualization

### `architecture comparison`
Multiple approaches • Benchmarks • Trade-offs

---

## Python Environment (2024)

### **Stable Stack**
```bash
Python: 3.10.12  # Colab default, max compatibility
CUDA: 12.2
cuDNN: 8.9
```

### **Core ML Libraries**
```python
# Deep Learning Frameworks
torch==2.1.0+cu121
torchvision==0.16.0+cu121
tensorflow==2.15.0
jax[cuda12_pip]==0.4.23

# Hugging Face Ecosystem
transformers==4.36.2
datasets==2.16.1
tokenizers==0.15.0
accelerate==0.25.0
peft==0.7.1  # LoRA, QLoRA
bitsandbytes==0.41.3  # Quantization

# Training & Optimization
pytorch-lightning==2.1.3
wandb==0.16.2
optuna==3.5.0

# Computer Vision
timm==0.9.12  # SOTA models
opencv-python==4.8.1.78
albumentations==1.3.1

# NLP Specific
sentence-transformers==2.2.2
spacy==3.7.2
nltk==3.8.1

# MLOps
mlflow==2.9.2
dvc==3.37.0
onnx==1.15.0
onnxruntime-gpu==1.16.3

# Explainability
shap==0.44.0
lime==0.2.0.1
captum==0.7.0  # PyTorch interpretability
```

### **Math & Stats**
```python
numpy==1.24.3
pandas==2.0.3
scipy==1.11.4
scikit-learn==1.3.2
statsmodels==0.14.1
```

### **Visualization**
```python
matplotlib==3.8.2
seaborn==0.13.1
plotly==5.18.0
tensorboard==2.15.1
```

---

## Development Environments

### **Google Colab** (Primary)
```python
# Auto-setup script
!nvidia-smi
!python --version
!pip install -q -U <package>

# Mount Drive
from google.colab import drive
drive.mount('/content/drive')

# GPU Check
import torch
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))
```

### **Jupyter Notebook**
```bash
# Local setup
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install jupyter notebook
pip install ipykernel
python -m ipykernel install --user --name=ml_env

jupyter notebook
```

### **VS Code**
```json
// .vscode/settings.json
{
  "python.defaultInterpreterPath": "./venv/bin/python",
  "jupyter.notebookFileRoot": "${workspaceFolder}",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black"
}
```

---

## Model Architecture Stack

### **Vision Models (2024)**
```python
# Classification
"google/vit-base-patch16-224"      # Vision Transformer
"facebook/convnext-base"           # ConvNeXt
"timm/eva02_large_patch14_448"     # EVA-02

# Object Detection
"facebook/detr-resnet-50"          # DETR
"microsoft/yolos-tiny"             # YOLO-Transformer
"hustvl/yolos-small"

# Segmentation
"facebook/mask2former-swin-base"
"nvidia/segformer-b5-finetuned"

# From Scratch Implementations
- ResNet (PyTorch)
- Vision Transformer (NumPy + PyTorch)
- U-Net
```

### **NLP Models (2024)**
```python
# LLMs (Open Source)
"mistralai/Mistral-7B-v0.1"
"meta-llama/Llama-2-7b-hf"
"microsoft/phi-2"                   # 2.7B, efficient
"TinyLlama/TinyLlama-1.1B"

# Embeddings
"BAAI/bge-large-en-v1.5"           # Best open embedding
"sentence-transformers/all-MiniLM-L6-v2"

# Multimodal
"Salesforce/blip2-opt-2.7b"
"microsoft/git-base"

# From Scratch
- Transformer (Attention is All You Need)
- BERT (Masked LM)
- GPT (Causal LM)
```

### **Audio Models**
```python
"openai/whisper-large-v3"
"facebook/wav2vec2-base"
"suno/bark"                         # Text-to-Speech
```

### **Multimodal**
```python
"openai/clip-vit-base-patch32"
"laion/CLIP-ViT-H-14-laion2B"
```

---

## Project Structure

```
ml-project/
├── data/
│   ├── raw/                    # Original data
│   ├── processed/              # Cleaned data
│   ├── external/               # External datasets
│   └── interim/                # Intermediate transformations
├── notebooks/
│   ├── 01_eda.ipynb           # Exploratory analysis
│   ├── 02_preprocessing.ipynb
│   ├── 03_baseline_model.ipynb
│   ├── 04_advanced_model.ipynb
│   └── 05_evaluation.ipynb
├── src/
│   ├── data/
│   │   ├── dataset.py         # Custom Dataset classes
│   │   ├── augmentation.py
│   │   └── preprocessing.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── transformer.py     # From scratch
│   │   ├── resnet.py          # From scratch
│   │   └── custom_model.py
│   ├── training/
│   │   ├── trainer.py         # Training loop
│   │   ├── losses.py
│   │   └── metrics.py
│   ├── inference/
│   │   ├── predict.py
│   │   └── serve.py           # FastAPI/Gradio
│   ├── explainability/
│   │   ├── shap_analysis.py
│   │   ├── attention_viz.py
│   │   └── feature_importance.py
│   └── utils/
│       ├── config.py
│       ├── logger.py
│       └── helpers.py
├── configs/
│   ├── model_config.yaml
│   ├── training_config.yaml
│   └── data_config.yaml
├── tests/
│   ├── test_data.py
│   ├── test_model.py
│   └── test_training.py
├── checkpoints/               # Saved models
├── logs/                      # Training logs
├── outputs/                   # Predictions, visualizations
├── requirements.txt
├── setup.py
├── README.md
└── LICENSE (MIT/Apache 2.0)
```

---

## Mathematical Foundations

### **Linear Algebra**
```python
# Essential Concepts
- Matrix Operations (NumPy)
- Eigenvalues/Eigenvectors (PCA)
- SVD (Dimensionality Reduction)
- Tensor Operations (PyTorch)

# Implementation
import numpy as np

def matrix_multiply_from_scratch(A, B):
    """Pure Python matrix multiplication"""
    return [[sum(a*b for a,b in zip(row,col)) 
             for col in zip(*B)] for row in A]
```

### **Statistics**
```python
# Core Topics
- Probability Distributions
- Hypothesis Testing
- Bayesian Inference
- Statistical Significance

# Libraries
from scipy import stats
import statsmodels.api as sm
```

### **Calculus (Backpropagation)**
```python
# Gradient Descent from Scratch
def gradient_descent(X, y, lr=0.01, epochs=1000):
    m, n = X.shape
    theta = np.zeros(n)
    
    for _ in range(epochs):
        predictions = X.dot(theta)
        errors = predictions - y
        gradient = (1/m) * X.T.dot(errors)
        theta -= lr * gradient
    
    return theta
```

---

## From Scratch Implementations

### **Neural Network (Pure NumPy)**
```python
class NeuralNetwork:
    def __init__(self, layers):
        self.weights = []
        self.biases = []
        for i in range(len(layers)-1):
            self.weights.append(np.random.randn(layers[i], layers[i+1]) * 0.01)
            self.biases.append(np.zeros((1, layers[i+1])))
    
    def forward(self, X):
        self.activations = [X]
        for w, b in zip(self.weights, self.biases):
            z = self.activations[-1].dot(w) + b
            a = self.relu(z)
            self.activations.append(a)
        return self.activations[-1]
    
    def backward(self, X, y, lr=0.01):
        # Backpropagation implementation
        pass
```

### **Transformer Attention (PyTorch)**
```python
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.d_model = d_model
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads
        
        self.qkv = nn.Linear(d_model, 3 * d_model)
        self.proj = nn.Linear(d_model, d_model)
    
    def forward(self, x):
        B, N, C = x.shape
        qkv = self.qkv(x).reshape(B, N, 3, self.num_heads, self.head_dim)
        q, k, v = qkv.unbind(2)
        
        attn = (q @ k.transpose(-2, -1)) / (self.head_dim ** 0.5)
        attn = attn.softmax(dim=-1)
        
        x = (attn @ v).transpose(1, 2).reshape(B, N, C)
        return self.proj(x)
```

---

## Explainable AI Patterns

### **SHAP Values**
```python
import shap

# For tree models
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)

# For deep learning
explainer = shap.DeepExplainer(model, X_train[:100])
shap_values = explainer.shap_values(X_test)
```

### **Attention Visualization**
```python
def visualize_attention(model, tokenizer, text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs, output_attentions=True)
    
    attention = outputs.attentions[-1][0].mean(0)  # Average heads
    tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
    
    plt.figure(figsize=(10, 10))
    sns.heatmap(attention.detach().numpy(), 
                xticklabels=tokens, yticklabels=tokens)
```

### **Grad-CAM (Vision)**
```python
from pytorch_grad_cam import GradCAM

cam = GradCAM(model=model, target_layers=[model.layer4[-1]])
grayscale_cam = cam(input_tensor=input_tensor, targets=targets)
```

---

## Training Architectures

### **Standard Training Loop**
```python
def train_epoch(model, dataloader, optimizer, criterion, device):
    model.train()
    total_loss = 0
    
    for batch in tqdm(dataloader):
        inputs, labels = batch
        inputs, labels = inputs.to(device), labels.to(device)
        
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
    
    return total_loss / len(dataloader)
```

### **Mixed Precision Training**
```python
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()

for inputs, labels in dataloader:
    with autocast():
        outputs = model(inputs)
        loss = criterion(outputs, labels)
    
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
```

### **Distributed Training (Multi-GPU)**
```python
from torch.nn.parallel import DistributedDataParallel as DDP

model = DDP(model, device_ids=[local_rank])
```

### **LoRA Fine-tuning**
```python
from peft import LoraConfig, get_peft_model

config = LoraConfig(
    r=8,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none"
)

model = get_peft_model(model, config)
```

---

## Research-Grade Features

### **Experiment Tracking**
```python
import wandb

wandb.init(project="my-research", config={
    "learning_rate": 1e-4,
    "architecture": "Transformer",
    "dataset": "ImageNet"
})

# Log during training
wandb.log({"loss": loss, "accuracy": acc})
```

### **Hyperparameter Optimization**
```python
import optuna

def objective(trial):
    lr = trial.suggest_loguniform('lr', 1e-5, 1e-1)
    batch_size = trial.suggest_categorical('batch_size', [16, 32, 64])
    
    model = create_model()
    accuracy = train_and_evaluate(model, lr, batch_size)
    return accuracy

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=100)
```

### **Model Versioning**
```python
import mlflow

with mlflow.start_run():
    mlflow.log_params({"lr": 1e-4, "epochs": 10})
    mlflow.log_metrics({"accuracy": 0.95})
    mlflow.pytorch.log_model(model, "model")
```

---

## Deployment Patterns

### **ONNX Export**
```python
dummy_input = torch.randn(1, 3, 224, 224)
torch.onnx.export(model, dummy_input, "model.onnx",
                  input_names=['input'], output_names=['output'],
                  dynamic_axes={'input': {0: 'batch_size'},
                               'output': {0: 'batch_size'}})
```

### **FastAPI Serving**
```python
from fastapi import FastAPI
import torch

app = FastAPI()
model = torch.load("model.pth")

@app.post("/predict")
async def predict(data: dict):
    inputs = preprocess(data)
    with torch.no_grad():
        outputs = model(inputs)
    return {"predictions": outputs.tolist()}
```

### **Gradio Interface**
```python
import gradio as gr

def predict(image):
    return model(preprocess(image))

gr.Interface(fn=predict, 
             inputs=gr.Image(), 
             outputs="label").launch()
```

---

## Multi-Architecture Comparison

### **Template**
```python
architectures = {
    "ResNet50": timm.create_model('resnet50', pretrained=True),
    "ViT": timm.create_model('vit_base_patch16_224', pretrained=True),
    "ConvNeXt": timm.create_model('convnext_base', pretrained=True),
    "EfficientNet": timm.create_model('efficientnet_b0', pretrained=True)
}

results = {}
for name, model in architectures.items():
    acc, params, flops = evaluate_model(model, test_loader)
    results[name] = {"accuracy": acc, "params": params, "flops": flops}

# Compare
pd.DataFrame(results).T.plot(kind='bar')
```

---

## Free Model Zoo (Hugging Face)

### **Vision**
```python
# Classification
google/vit-base-patch16-224
facebook/dinov2-base
microsoft/resnet-50

# Detection
facebook/detr-resnet-50
hustvl/yolos-small

# Segmentation
nvidia/segformer-b0-finetuned-ade-512-512
```

### **NLP**
```python
# Small LLMs (< 10B)
TinyLlama/TinyLlama-1.1B-Chat-v1.0
microsoft/phi-2
stabilityai/stablelm-2-1_6b

# Embeddings
BAAI/bge-base-en-v1.5
sentence-transformers/all-mpnet-base-v2
```

### **Multimodal**
```python
openai/clip-vit-base-patch32
Salesforce/blip2-opt-2.7b
microsoft/git-base-coco
```

### **Audio**
```python
openai/whisper-base
facebook/wav2vec2-base-960h
```

---

## Common Fixes

### **CUDA Out of Memory**
```python
# Gradient accumulation
accumulation_steps = 4
for i, batch in enumerate(dataloader):
    loss = model(batch) / accumulation_steps
    loss.backward()
    if (i + 1) % accumulation_steps == 0:
        optimizer.step()
        optimizer.zero_grad()

# Clear cache
torch.cuda.empty_cache()
```

### **Dependency Conflicts**
```bash
# Create clean environment
conda create -n ml python=3.10
conda activate ml

# Install PyTorch first
pip install torch==2.1.0 torchvision==0.16.0 --index-url https://download.pytorch.org/whl/cu121

# Then other packages
pip install transformers datasets accelerate
```

### **Version Pinning**
```txt
# requirements.txt
torch==2.1.0
transformers==4.36.2
datasets==2.16.1
# Lock all versions
```

---

## Research Paper Implementation

### **Standard Flow**
1. Read paper + supplementary
2. Find official code (GitHub)
3. Replicate architecture
4. Verify with paper's metrics
5. Ablation studies
6. Document differences

### **Example: Implementing "Attention is All You Need"**
```python
# 1. Positional Encoding
class PositionalEncoding(nn.Module):
    # ...based on paper formula

# 2. Multi-Head Attention
class MultiHeadAttention(nn.Module):
    # ...exact paper specs

# 3. Full Transformer
class Transformer(nn.Module):
    # ...N encoder/decoder layers

# 4. Verify on WMT dataset
# 5. Compare BLEU scores
```

---

## Open Source Checklist

- [ ] MIT/Apache 2.0 License
- [ ] Comprehensive README
- [ ] Requirements.txt + environment.yml
- [ ] Model cards (Hugging Face)
- [ ] Jupyter notebooks with examples
- [ ] Unit tests (pytest)
- [ ] CI/CD (GitHub Actions)
- [ ] Documentation (Sphinx/MkDocs)
- [ ] Pre-trained weights (Hugging Face Hub)
- [ ] Reproducibility (random seeds, configs)

---

## Usage Examples

```bash
# Full training pipeline
"fullprojectwithcode: Image classification with ViT from scratch + explainability"

# Architecture comparison
"architecture comparison: ResNet vs ViT vs ConvNeXt on CIFAR-100"

# From scratch
"from scratch: Implement BERT tokenizer + model in pure PyTorch"

# Debugging
"correct code: CUDA OOM during fine-tuning Llama-2"

# Research replication
"implementation guide: Replicate 'FlashAttention' paper"

# Explainability
"explainable ai: SHAP + Grad-CAM for medical image classifier"
```

---

## Quick Start Templates

### **Colab Notebook Header**
```python
# Setup
!nvidia-smi
!pip install -q transformers datasets accelerate wandb

# Mount Drive
from google.colab import drive
drive.mount('/content/drive')

# Login to HF
from huggingface_hub import login
login()

# Verify GPU
import torch
print(f"GPU: {torch.cuda.get_device_name(0)}")
print(f"CUDA: {torch.version.cuda}")
```

### **VS Code Notebook**
```python
# Cell 1: Imports
import torch
import numpy as np
import pandas as pd
from transformers import AutoModel, AutoTokenizer

# Cell 2: Config
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name = "microsoft/phi-2"

# Cell 3: Load model
model = AutoModel.from_pretrained(model_name).to(device)
```

---

## Additional Resources

### **Learning Paths**
- **Linear Algebra**: 3Blue1Brown "Essence of Linear Algebra"
- **Deep Learning**: fast.ai, Stanford CS231n/CS224n
- **Papers**: arXiv.org, Papers with Code
- **Practice**: Kaggle, Hugging Face Spaces

### **Communities**
- Hugging Face Discord
- r/MachineLearning
- ML Twitter (#NLP, #ComputerVision)
- Papers with Code

### **Tools**
- **Notebooks**: Colab, Kaggle, Paperspace
- **Compute**: Lambda Labs, RunPod, Vast.ai
- **Datasets**: Hugging Face Datasets, Kaggle, UCI ML Repository

---

**Philosophy**: Build, Understand, Explain, Extend  
**License**: Open source everything  
**Community**: Share knowledge, cite sources, collaborate
