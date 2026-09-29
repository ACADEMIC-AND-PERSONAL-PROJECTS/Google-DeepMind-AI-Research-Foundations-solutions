<center>
<img src="assets/brand/banner.svg" width="100%" alt="Google DeepMind AI Research Foundations — research field notes">
</center>

<center>
<img src="assets/brand/hero-study-frame.png" width="100%" alt="A centered photograph with rounded corners, showing a student silhouette working at several screens in a purple-lit room">
<br>
<img src="assets/brand/badges.svg" width="100%" alt="Full learning path, course notes, lab solutions, research, and Google DeepMind">
</center>

**Google DeepMind: AI Research Foundations — Solutions** is my archive for coursework, lab solutions, research notes, and experiments from the [full Google Skills learning path](https://www.skills.google/paths/3135). It is organized course by course; the first materials here come from **Train a Small Language Model**.

<center>
<img src="assets/brand/divider.svg" width="100%" alt="Purple research-notes divider">
</center>

## Origins

This repository is intended to collect my work across the **Google DeepMind: AI Research Foundations** learning path, not just a single course. I am adding the material course by course; the current notebooks document the [Train a Small Language Model](https://www.skills.google/paths/3135/course_templates/1453) course, including hands-on coding activities, solutions, and text-generation experiments. These are personal study notes and solutions, not an official Google or DeepMind repository.

## Current collection

### Course 1 · Train a Small Language Model

These are the Course 1 materials currently in the repository. Open each notebook on GitHub or launch it directly in Google Colab.

| Lab | Notebook | What you'll explore |
|---|---|---|
| 1.2 | [Experiment with N-Gram Models](course_1/gdm_lab_1_2_experiment_with_n_gram_models.ipynb) · [Colab](https://colab.research.google.com/github/ACADEMIC-AND-PERSONAL-PROJECTS/Google-DeepMind-AI-Research-Foundations-solutions/blob/main/course_1/gdm_lab_1_2_experiment_with_n_gram_models.ipynb) | Tokenize a corpus, build n-grams, count occurrences, estimate probabilities, and generate text. |
| 1.4 | [Prepare the Dataset for an SLM](course_1/gdm_lab_1_4_prepare_the_dataset_for_training_a_slm.ipynb) · [Colab](https://colab.research.google.com/github/ACADEMIC-AND-PERSONAL-PROJECTS/Google-DeepMind-AI-Research-Foundations-solutions/blob/main/course_1/gdm_lab_1_4_prepare_the_dataset_for_training_a_slm.ipynb) | Build a vocabulary and token/index mappings, then encode and decode sequences. |
| 1.5 | [Train Your Own Small Language Model](course_1/gdm_lab_1_5_train_your_own_small_language_model.ipynb) · [Colab](https://colab.research.google.com/github/ACADEMIC-AND-PERSONAL-PROJECTS/Google-DeepMind-AI-Research-Foundations-solutions/blob/main/course_1/gdm_lab_1_5_train_your_own_small_language_model.ipynb) | Prepare and pad sequences, create batches, train an SLM, and inspect its predictions and generated text. |

### After Course 1 · Build a SLM Lab

Continue with the [Build a SLM Lab notebook](Train%20A%20Small%20Language%20Model%20lab/notebook.ipynb) in `Train A Small Language Model lab/`, or [open it in Colab](https://colab.research.google.com/github/ACADEMIC-AND-PERSONAL-PROJECTS/Google-DeepMind-AI-Research-Foundations-solutions/blob/main/Train%20A%20Small%20Language%20Model%20lab/notebook.ipynb). This follow-up lab covers helper functions and data loading, character-level tokenization, and text generation with an n-gram model.

<details>
<summary>Open the companion lab and field notes</summary>

| File | Purpose |
|---|---|
| [`main.py`](Train%20A%20Small%20Language%20Model%20lab/main.py) | Python entry point for the local project. |
| [`simple_word_tokenization.py`](course_1/simple_word_tokenization.py) | Educational word tokenizer with encoding and decoding methods. |
| [Diagram notes](assets/NOTES.md) | Context for the reasoning diagrams created with Excalidraw. |
| [N-gram diagram](assets/probleme_ngrammes.png) · [final version](assets/probleme_ngrammes_final_version.png) | Two visual notes exploring the n-gram problem. |

</details>

<center>
<img src="assets/brand/divider.svg" width="100%" alt="Purple research-notes divider">
</center>

## Research flow

The labs move from a simple text representation to a first training and evaluation loop.

<center>
<img src="assets/brand/research-flow.svg" width="100%" alt="Centered diagram showing a text corpus branching into n-gram text generation and small language model training, ending with evaluation">
</center>

<details>
<summary>View the Mermaid source</summary>

```mermaid
%%{init: {"theme":"dark", "themeVariables": {"primaryColor":"#15085F", "primaryTextColor":"#C4A9F2", "primaryBorderColor":"#5336A6", "lineColor":"#9965F4"}}}%%
flowchart LR
    corpus["Corpus"] --> tokens["Tokenization"]
    tokens --> ngrams["N-grams"]
    ngrams --> probs["Counts and probabilities"]
    probs --> generation["Text generation"]
    tokens --> encoded["Vocabulary and token IDs"]
    encoded --> batches["Sequences, padding, and batches"]
    batches --> model["Small language model"]
    model --> evaluate["Predictions and evaluation"]
```

</details>

## The toolkit

The course notebooks run in Google Colab. The companion local lab declares its dependencies in `pyproject.toml` and pins them in `uv.lock`.

| Layer | Tool / declared version |
|---|---|
| Language | Python `>=3.12` |
| Notebooks | Jupyter / IPython kernel |
| Kernel | `ipykernel 7.3.0` |
| Numerical computing | `NumPy 2.5.3` · `pandas 3.0.6` |
| Models | `Keras 3.15.1` · `TensorFlow 2.21.0` |
| Environment | `uv` with `pyproject.toml` and `uv.lock` |

## Quick start

To get started without installing anything, open one of the notebooks in Colab using its link in the grimoire table.

To run the companion lab locally, install [uv](https://docs.astral.sh/uv/), then:

```bash
git clone https://github.com/ACADEMIC-AND-PERSONAL-PROJECTS/Google-DeepMind-AI-Research-Foundations-solutions.git
cd Google-DeepMind-AI-Research-Foundations-solutions
cd "Train A Small Language Model lab"
uv sync
uv run --with jupyter jupyter lab notebook.ipynb
```

## Reading notes

This is a learning repository: exercises and solutions live in the notebooks, alongside a standalone Python tokenizer. No automated test suite is configured; experiment results and examples are available in the notebooks.

<center>
<img src="assets/brand/divider.svg" width="100%" alt="Purple research-notes divider">
</center>

Research notes and learning experiments by <b><a href="https://github.com/khadimmbaye0">@khadimmbaye0</a></b>
