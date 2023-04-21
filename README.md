# Makrukthai Fen Analysis

This Python script is an interface to interact with the Fairy-Stockfish chess engine. It is designed to analyze a given chess position in the Makrukthai (Thai Chess) and output the analysis results into a text file.

## Requirements

- Python 3.9 or later
- Fairy-Stockfish chess variant engine: [Download](https://github.com/ianfab/Fairy-Stockfish)

## Features

- Analyze a makrukthai position from FEN (Forsyth–Edwards Notation) input
- Save the analysis results to a text file
- Customize the engine options such as the number of threads, hash size, and search depth

## Usage

1. Clone this repository or download the `chess_engine_interface.py` script.
2. Place the Fairy-Stockfish engine binary in the `engine` directory or update the path to the engine binary in the script.
3. Run the script:

```bash
python makrukthai_fen_analyzer.py
```

```bash
Please enter the FEN string of the position you want to analyze:
```

4. Input makrukthai fen you want for example startposition

```bash
rnsmksnr/8/pppppppp/8/8/PPPPPPPP/8/RNSKMSNR w - - 0 1
```

5. Wait until the engine output successfully

```bash
Engine Output: output.txt file created successfully
```
