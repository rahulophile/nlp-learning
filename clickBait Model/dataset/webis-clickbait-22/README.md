# Webis Clickbait Spoiling Corpus

The Webis Clickbait Spoiling Corpus 2022 (Webis-Clickbait-22) contains 5,000 spoiled clickbait posts crawled from Facebook, Reddit, and Twitter.
This corpus supports the task of clickbait spoiling, which deals with generating a short text that satisfies the curiosity induced by a clickbait post.

This dataset contains the clickbait posts and manually cleaned versions of the linked documents, and extracted spoilers for each clickbait post.
Additionally, the spoilers are categorized into three types: short phrase spoilers, longer passage spoilers, and multiple non-consecutive pieces of text. The test set of this dataset was used for the [SemEval-2023 clickbait spoiling task](https://www.tira.io/task-overview/clickbait-spoiling). You can re-execute and adopt the software submissions made through for this SemEval task, please see the instructions and overview of approaches in [TIRA](https://www.tira.io/task-overview/clickbait-spoiling).


## Overview

The dataset comes with predefined train/validation/test splits:

- [3,200 posts for training](training.jsonl)
- [800 posts for validation](validation.jsonl)
- [1,000 posts for testing](test.jsonl)
  - The test set was used for the [SemEval-2023 clickbait spoiling task](https://www.tira.io/task-overview/clickbait-spoiling). This shared task was organized with [TIRA.io](https://www.tira.io/) and participants submitted Docker software during the task. Please see the instructions in [TIRA](https://www.tira.io/task-overview/clickbait-spoiling) to re-execute or modify the approaches.
