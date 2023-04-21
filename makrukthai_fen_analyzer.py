from collections.abc import Iterable
import subprocess
import threading


class Engine():
    INFO_KEYWORDS = {'depth': int, 'seldepth': int, 'multipv': int,
                     'nodes': int, 'nps': int, 'time': int, 'score': list, 'pv': list}

    def __init__(self, args, options=None):
        self.process = subprocess.Popen(
            args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        self.lock = threading.Lock()
        self.options = options
        self.paused = False

    def write(self, message):
        with self.lock:
            self.process.stdin.write(message)
            self.process.stdin.flush()

    def setoption(self, name, value):
        self.write('setoption name {} value {}\n'.format(name, value))

    def initialize(self):
        message = 'uci\n'
        for option, value in self.options.items():
            message += 'setoption name {} value {}\n'.format(option, value)
        self.write(message)

    def newgame(self):
        self.write('ucinewgame\n')

    def position(self, fen=None, moves=None):
        fen = 'fen {}'.format(fen) if fen else 'startpos'
        moves = 'moves {}'.format(' '.join(moves)) if moves else ''
        self.write('position {} {}\n'.format(fen, moves))

    def analyze(self):
        # self.write('go depth 10\n')
        self.write('go movetime 1000\n')
        self.paused = False

    def stop(self):
        self.write('stop\n')
        self.paused = True

    def toggle(self):
        if self.paused:
            self.analyze()
        else:
            self.stop()

    def quit(self):
        self.write('quit\n')

    def read(self):
        while self.process.poll() is None:
            yield self.process.stdout.readline()

    def wait_for_bestmove(self):
        """ # Show Only bestmove
        for line in self.read():
            if 'bestmove' in line:
                return line.split()[1] """
        info_list = []
        for line in self.read():
            info = self.process_line(line)
            if info is not None:
                info_list.append(info)
            if 'bestmove' in line:
                return info_list
        return None

    @classmethod
    def process_line(cls, line):
        items = line.split()
        if len(items) > 1 and items[0] == 'info' and items[1] != 'string':
            key = None
            values = []
            info = {}
            for i in items[1:] + ['']:
                if not i or i in cls.INFO_KEYWORDS:
                    if key:
                        if values and not issubclass(cls.INFO_KEYWORDS[key], Iterable):
                            values = values[0]
                        info[key] = cls.INFO_KEYWORDS[key](values)
                    key = i
                    values = []
                else:
                    values.append(i)
            return info
        return None


if __name__ == '__main__':
    print("Please enter the FEN string of the position you want to analyze:")
    input_fen = input().strip()

    engine = Engine('engine/fairy-stockfish_x86-64-bmi2.exe', options={
        'UCI_Variant': 'makruk',
        'MultiPV': 6,
        'Threads': 4,
        'Hash': 4096,
        'Use NNUE': True,
        # 'EvalFile': 'engine/makruk-a8c621e24a8c.nnue',
    })
    engine.initialize()
    engine.position(
        fen=input_fen)
    engine.analyze()

    output = engine.wait_for_bestmove()
    print(f'Engine Output: output.txt file created successfully')
    with open('output.txt', 'w') as file:
        file.write('FEN : ' + input_fen + '\n\n')
        file.write('Depth\t\tSelDepth\tMultipv\t\tScore\t\t\tPV\n')
        for info in output:
            depth = str(info.get('depth'))
            seldepth = str(info.get('seldepth'))
            multipv = str(info.get('multipv'))
            score = ' '.join(info.get('score', []))
            pv = ' '.join(info.get('pv', []))
            file.write(
                f'{depth}\t\t\t{seldepth}\t\t\t{multipv}\t\t\t{score}\t\t\t{pv}\n')

    engine.quit()
