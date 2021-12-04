import random as rnd

SWITCH_A = {
    'A0': ['B0', 'B4'],
    'A1': ['B1', 'B5'],
    'A2': ['B2', 'B6'],
    'A3': ['B3', 'B7'],
    'A4': ['B0', 'B4'],
    'A5': ['B1', 'B5'],
    'A6': ['B2', 'B6'],
    'A7': ['B3', 'B7']
}

SWITCH_B = {
    'B0': ['C0', 'C2'],
    'B1': ['C1', 'C3'],
    'B2': ['C0', 'C2'],
    'B3': ['C1', 'C3'],
    'B4': ['C4', 'C6'],
    'B5': ['C5', 'C7'],
    'B6': ['C4', 'C6'],
    'B7': ['C5', 'C7'],
}

SWITCH_C = {
    'C0': ['D0', 'D1'],
    'C1': ['D0', 'D1'],
    'C2': ['D2', 'D3'],
    'C3': ['D2', 'D3'],
    'C4': ['D4', 'D5'],
    'C5': ['D4', 'D5'],
    'C6': ['D6', 'D7'],
    'C7': ['D6', 'D7']
}

SWITCH_D = {
    'D0': [0, 1],
    'D1': [2, 3],
    'D2': [4, 5],
    'D3': [6, 7],
    'D4': [8, 9],
    'D5': [10, 11],
    'D6': [12, 13],
    'D7': [14, 15]
}

class BatcherBanyanNetwork:
    def __init__(self, inputs):
        self.inputs = sorted(inputs)
        self.binary = list(map('{:04b}'.format, self.inputs))
        self.routes = []

    def route(self):
        for i in range(len(self.inputs)):
            a = 'A' + str(i) if i <= 7 else 'A' + str(i-8)
            b = SWITCH_A[a][0] if self.binary[i][0] == '0' else SWITCH_A[a][1]
            c = SWITCH_B[b][0] if self.binary[i][1] == '0' else SWITCH_B[b][1]
            d = SWITCH_C[c][0] if self.binary[i][2] == '0' else SWITCH_C[c][1]
            out = SWITCH_D[d][0] if self.binary[i][3] == '0' else SWITCH_D[d][1]
            self.routes.append((self.inputs[i], a, b, c, d, out))
    
    def print_routes(self):
        for route in self.routes:
            print(f'{route[0]} --> {route[1]} --> {route[2]} --> {route[3]} --> {route[4]} --> {route[5]}')
    


if __name__ == '__main__':
    inputs = [rnd.randint(0,15) for i in range(15)]
    print(f'Original inputs: {inputs}')
    bnn = BatcherBanyanNetwork(inputs)
    bnn.route()
    print('\nROUTES')
    bnn.print_routes()


