from setuptools import setup, find_packages

setup(
    name="muse-maskgit-pytorch",
    packages=find_packages(exclude=[]),
    version="0.1.0",
    license="MIT",
    description="MUSE - Text-to-Image Generation via Masked Generative Transformers, in Pytorch",
    author="Phil Wang",
    author_email="lucidrains@gmail.com",
    long_description_content_type="text/markdown",
    url="https://github.com/lucidrains/muse-maskgit-pytorch",
    keywords=[
        "artificial intelligence",
        "deep learning",
        "transformers",
        "attention mechanism",
        "text-to-image",
    ],
    install_requires=[
        "accelerate",
        "diffusers",
        "datasets",
        "beartype",
        "einops>=0.6",
        "ema-pytorch",
        "omegaconf>=2.3.0",
        "pillow",
        "sentencepiece",
        "torch>=2.0",
        "torchmetrics<0.8.0",
        "pytorch-lightning>=2.0.0",
        "taming-transformers @ git+https://github.com/neggles/taming-transformers.git@v0.0.2",
        "transformers",
        "torchvision",
        "torch_optimizer",
        "tqdm",
        "vector-quantize-pytorch>=0.10.14",
        "lion-pytorch",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
)
