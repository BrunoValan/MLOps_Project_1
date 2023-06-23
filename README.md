# [![Python build for application](https://github.com/BrunoValan/MLOps_Project_1/actions/workflows/project_build.yml/badge.svg)](https://github.com/BrunoValan/MLOps_Project_1/actions/workflows/project_build.yml)

# MLOPS Project 1 - Text Summarization with Hugging Face
This is a  repository for the class AIPI 561 that focuses of applying DevOps principles to machine learning. The goal of this project is to build a command line prediction tool that uses continuous integration with GitHub Actions. I decided to use a pretrained hugging face model that is specifcially architected to summarize long strings of text. You can learn more by visiting the website [here](pszemraj/led-base-book-summary). One use case I thought for this type of model is summarizing the transcript of the coursera videos we have assigned for this class. Using this command line tool you can get a quick summary of the content the video contains - then you can gauge whether the information contained is new and important or review that you may be able to skip. It can also act as a primer on the information that may help it stick better. As this class centers on using the tools/infrastructure of DevOps I focused on this as opposed to solving a complicated prediction task. 

--
## Project Scaffold
- ### .github
contains github actions workflow for the project build

- ### Makefile
contains instructions for environment set up as well as testing and formatting the command line script

- ### notebooks
contains jupyter notebooks I used to experiment with the hugging face model zoo during the exploratory phase of the project

- ### cli.py
contains the script for the command line summarization task. Prompts user for input and prints the summarization to the users terminal

- ### test_cli.py 
contains the tests for the command line script 

-- 
### Running the Project
running this project is incredibly simple. You can either open the repository in codespaces or locally. Once cloned simply navigate to the directory or environment you want to run it in and type 'make install' into your terminal. Then type 'python cli.py' to run the script. You will be prompted to enter a string of text to be summarized. 




