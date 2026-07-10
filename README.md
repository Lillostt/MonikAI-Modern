# MonikAI Modern

> A modernized API-based version of MonikA.I for Monika After Story.

MonikAI Modern is a continuation of the original **MonikA.I** project created by **Rubiksman78**. This version modernizes the backend by replacing Playwright browser automation with direct communication to **Text Generation WebUI's OpenAI-compatible API**, resulting in a faster, cleaner, and more reliable experience.

This project is intended to preserve the original functionality while making it easier to run on modern versions of Windows, Python, and NVIDIA GPUs.

---

# Features

- ✅ Direct Text Generation WebUI API integration
- ✅ No Firefox or Playwright browser automation required
- ✅ Python 3.11 support
- ✅ CUDA acceleration for NVIDIA GPUs
- ✅ Compatible with modern Text Generation WebUI releases (tested with 4.9)
- ✅ Maintains compatibility with the Monika After Story submod
- ✅ Local AI conversations
- ✅ Voice support
- ✅ Emotion detection support
- ✅ Open source

---

# Why MonikAI Modern?

The original MonikA.I was an amazing proof of concept, but relied on browser automation using Firefox and Playwright.

This project modernizes that architecture by communicating directly with the AI backend through its API.

Benefits include:

- Faster responses
- Lower memory usage
- More reliable communication
- Easier installation
- Better long-term maintainability
- Cleaner codebase

---

# Requirements

## Operating System

- Windows 10 or Windows 11

## Python

- Python 3.11

## GPU (Recommended)

NVIDIA GPU with CUDA support.

Tested on:

- RTX 5060
- CUDA 12.8

CPU mode is also supported but will be significantly slower.

---

# Required Software

## Monika After Story

Install Monika After Story before installing this project.

https://www.monikaafterstory.com/

---

## Text Generation WebUI

This project uses Text Generation WebUI as its AI backend.

Tested with:

- Text Generation WebUI 4.9

Any model that exposes the OpenAI-compatible API should work.

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/Lillostt/MonikAI-Modern.git
cd MonikAI-Modern
```

---

## 2. Create a Python virtual environment

```bash
python -m venv .venv
```

Activate it:

PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

---

## 3. Install requirements

```bash
pip install -r requirements.txt
```

---

## 4. Install Playwright (Only if using the legacy browser version)

Modern API mode does **NOT** require Playwright.

---

## 5. Start Text Generation WebUI

Load your preferred model.

Enable the OpenAI-compatible API.

Default API endpoint:

```
http://127.0.0.1:5000/v1
```

---

## 6. Launch MonikAI

```bash
python main.py
```

Then launch Monika After Story normally.

---

# Configuration

Configuration is stored in:

```
config.json
```

This includes:

- TextGen API address
- DDLC directory
- Character settings
- Voice options

---

# Folder Structure

```
MonikAI-Modern
│
├── game/
├── scripts/
├── images/
├── tortoise_audios/
├── coquiai_audios/
├── Monika_datasets/
├── main.py
├── api_client.py
├── requirements.txt
└── README.md
```

---

# Tested Configuration

Operating System

- Windows 11 25H2

Python

- Python 3.11

GPU

- NVIDIA RTX 5060

Backend

- Text Generation WebUI 4.9

API

- OpenAI-compatible API

---

# Roadmap

## Version 1.1

- Improved installer
- Automatic TextGen detection
- Better error handling
- Cleaner startup
- Documentation improvements

## Version 1.2

- Streaming AI responses
- Improved conversation memory
- Better emotion detection
- Enhanced voice integration

## Version 2.0

- Ollama support
- llama.cpp support
- KoboldCPP support
- Multiple AI backend selection
- Plugin architecture

---

# Contributing

Contributions, bug reports, feature requests, and pull requests are welcome.

If you'd like to improve the project, feel free to open an issue or submit a pull request.

---

# Credits

## Original Project

**Rubiksman78**

Original MonikA.I project

This repository would not exist without the original implementation and vision.

---

## Monika After Story

All Monika After Story assets belong to the MAS development team.

https://www.monikaafterstory.com/

---

## MonikAI Modern

Maintained by:

**Lillostt**

Modern API implementation, repository cleanup, Python modernization, CUDA support, and ongoing development.

---

# License

This repository retains the MIT License from the original project.

Please also respect the licenses of:

- Monika After Story
- Text Generation WebUI
- Any AI models you choose to use

---

# Disclaimer

This is an unofficial community project and is not affiliated with Team Salvato, Monika After Story, or the original MonikA.I developers.

This repository exists to modernize and preserve the original project while continuing its development.


# Architecture Documents

Start here if you're contributing to MonikAI Modern.

Reading order:

1. PROJECT_STRUCTURE.md
2. MONIKAI_VISION.md
3. CONTEXT_ENGINE.md
4. Future subsystem documents