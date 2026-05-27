FROM nvidia/cuda:12.4.1-cudnn-runtime-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive
ARG BIOREASON_PRO_REF=main

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      ca-certificates \
      curl \
      git \
      gnupg \
      lsb-release \
      python3.11 \
      python3.11-dev \
      python3-pip \
      python3-venv \
      build-essential && \
    rm -rf /var/lib/apt/lists/*

RUN install -d -m 0755 /usr/share/keyrings && \
    curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | \
      gpg --dearmor -o /usr/share/keyrings/google-cloud-cli.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/google-cloud-cli.gpg] https://packages.cloud.google.com/apt cloud-sdk main" > /etc/apt/sources.list.d/google-cloud-cli.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends google-cloud-cli && \
    rm -rf /var/lib/apt/lists/*

RUN ln -sf /usr/bin/python3.11 /usr/local/bin/python && \
    ln -sf /usr/bin/pip3 /usr/local/bin/pip

RUN python -m pip install --upgrade pip setuptools wheel

# Install the CUDA-enabled PyTorch wheel first so downstream runtime packages
# land on a GPU-capable base.
RUN python -m pip install --no-cache-dir \
      --index-url https://download.pytorch.org/whl/cu124 \
      torch torchvision torchaudio

# This is a smoke-test image, not a locked production build. Expect to retune
# versions if upstream BioReason-Pro or vLLM changes.
RUN python -m pip install --no-cache-dir \
      accelerate \
      datasets \
      goatools \
      google-cloud-storage \
      huggingface_hub \
      networkx \
      obonet \
      pandas \
      pyyaml \
      safetensors \
      sentence-transformers \
      torch-geometric \
      transformers \
      vllm \
      "esm>=3.2.0"

RUN git clone --depth 1 --branch "${BIOREASON_PRO_REF}" \
      https://github.com/bowang-lab/BioReason-Pro.git /opt/BioReason-Pro

WORKDIR /app
COPY . /app

ENV BIOREASON_PRO_DIR=/opt/BioReason-Pro
ENV PYTHONPATH=/opt/BioReason-Pro:/opt/BioReason-Pro/gogpt/src
ENV HF_HOME=/workdir/hf-cache
ENV TRANSFORMERS_CACHE=/workdir/hf-cache
ENV HUGGINGFACE_HUB_CACHE=/workdir/hf-cache
ENV PYTHONUNBUFFERED=1

RUN chmod +x /app/run_smoketest.sh

ENTRYPOINT ["/bin/bash", "/app/run_smoketest.sh"]
