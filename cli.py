#!/usr/bin/env python
import torch
from transformers import pipeline

summary_model = "pszemraj/led-base-book-summary"
summary_generator = pipeline(
    "summarization", model=summary_model, device=0 if torch.cuda.is_available() else -1
)


def generate_summary(text_body):
    # raise type error if input is not a string
    if not isinstance(text_body, str):
        raise TypeError("Input must be a string.")

    result = summary_generator(
        text_body,
        min_length=8,
        max_length=100,
        no_repeat_ngram_size=3,
        encoder_no_repeat_ngram_size=3,
        repetition_penalty=3.5,
        num_beams=4,
        do_sample=False,
        early_stopping=True,
    )
    summary_text = result[0]["summary_text"]
    print("Your summary is:")
    print(summary_text)
    return summary_text


if __name__ == "__main__":
    # prompt user for text input
    text_body = input("Please enter the text you want to summarize: ")
    generate_summary(text_body)
