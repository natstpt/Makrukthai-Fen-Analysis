# Makrukthai Fen Analysis

This Python script is an interface to interact with the Fairy-Stockfish chess engine. It is designed to analyze a given fen position in the Makrukthai (Thai Chess) and output the analysis results into a text file.

## Requirements

- Python 3.9 or later
- Fairy-Stockfish chess variant engine: [Download](https://github.com/ianfab/Fairy-Stockfish) store in engine directory

## Features

- Analyze a makrukthai position from FEN (Forsyth–Edwards Notation) input
- Save the analysis results to a text file
- Customize the engine options such as the number of threads, hash size, and search depth

## Usage

1. Clone this repository or download the `makrukthai_fen_analyzer.py` script.
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

6. Open output.txt file

```bash
FEN : rnsmksnr/8/pppppppp/8/8/PPPPPPPP/8/RNSKMSNR w - - 0 1

Depth		SelDepth	Multipv		Score			PV
1			1			1			cp 2			d1c2
1			1			2			cp 1			e3e4
1			1			3			cp 0			e1f2
1			1			4			cp 0			b1d2
1			1			5			cp 0			e1d2
1			1			6			cp 0			d1e2
2			2			1			cp 8			d1c2 a6a5
2			2			2			cp 3			e3e4 c6c5
2			2			3			cp 2			e1f2 a6a5
2			2			4			cp 0			b1d2 c6c5
2			2			5			cp 0			e1d2 c6c5
```
