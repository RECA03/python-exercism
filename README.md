# Python Exercism

My solutions for the [Exercism Python track](https://exercism.org/tracks/python).

Each exercise lives in its own folder under `python/` with the solution, tests, and Exercism-provided docs.

## Downloading exercises

Point the Exercism CLI at this repo (one-time setup, run from the repo root):

```bash
exercism configure -w .
```

Download a new exercise:

```bash
exercism download --track=python --exercise=<exercise-slug>
```

Submit from the exercise folder:

```bash
cd python/<exercise-slug>
exercism submit <exercise_slug>.py
```

## Running tests

From an exercise folder:

```bash
python -m unittest discover
```

Or with pytest:

```bash
pytest
```

## Note

Exercise descriptions and test suites come from [Exercism](https://exercism.org). See each folder's `README.md` for the problem statement.
