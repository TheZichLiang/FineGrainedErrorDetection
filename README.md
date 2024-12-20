# FineGrainedErrorDetection

Our project is adapted from a shared task hosted by the ninth Conference on Machine Translation (WMT). The task is listed as 2024 Quality Estimation Shared Task 2[1]. 

The goal of our project is to improve on a method proposed by the authors of CometKiwi designed to estimate the quality of machine translations without referencing the original source. For instance, given a German text in which the original source was not written in German, we wish to identify the segments of that text that are incorrectly translated (start and end indices) and label these segments as minor or major translation errors. In other words, we are aiming for highly granular quality estimations at a word-by-word scale, or “Error spans”.

## Setup
Create an environment with python>=3.8 and run the following command

`pip3 install -r requirements.txt`

Next, log into huggingface using:

`huggingface-cli login`

Next, ensure you have access to the necessary repository by going to the Huggingface page for the model and accepting access.