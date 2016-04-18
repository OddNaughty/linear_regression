import csv, argparse
import matplotlib.pyplot as plt

def estimate_error(km, price, t0, t1):
    totalError = 0
    for i in range(len(km)):
        x = km[i]
        y = price[i]
        totalError += (y - (t1 * x + t0)) ** 2
    return totalError / float(len(km))

def regression_one(price, km, t0, t1, learningRate):
    new_t0 = new_t1 = 0
    for i in range(len(km)):
        new_t0 += estimate_price(km[i], t0, t1) - price[i]
        new_t1 += km[i] * (estimate_price(km[i], t0, t1) - price[i])
    new_t0 = t0 - (learningRate * new_t0 * 1/len(km))
    new_t1 = t1 - (learningRate * new_t1 * 1/len(km))
    return [new_t0, new_t1]

def estimate_price(mileage, t0, t1):
    return t0 + (t1*mileage)

def train_algo(price, km):
    t0 = t1 = 0
    a = 0.005
    for _ in range(30000):
        t0, t1 = regression_one(price, km, t0, t1, a)
    return (t0, t1)

def scaling(values):
    mi, ma = min(values['km']), max(values['km'])
    new_values = {'km': [((x - mi) / (ma - mi)) for x in values['km']], 'price': values['price'], 'min': mi, 'max': ma}
    return new_values

def print_graph(km, price, hypothesis):
    plt.ylabel('Price')
    plt.xlabel('Mileage')
    plt.plot(price, km, 'yo')
    plt.plot(price, hypothesis)
    plt.show()

def main(show):
    with open('dataset.csv') as f:
        reader = csv.DictReader(f)
        values = {key: [] for key in reader.fieldnames}
        for row in reader:
            for k, v in row.items():
                values[k].append(int(v))
        values2 = scaling(values)
        t0, t1 = train_algo(values2['price'], values2['km'])
        if show:
            print_graph(values['price'], values['km'], [t0 + (t1 * ((x - values2['min']) / (values2['max'] - values2['min']))) for x in values['km']])
        # print("The margin of error is: ", estimate_error(values['km'], values['price'], t0, t1))
        with open('thetas.txt', 'w') as thetas:
            thetas.write("{}\n{}\n{}\n{}\n".format(t0, t1, values2['min'], values2['max']))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--show', action="store_const", const=True)
    args = parser.parse_args()
    main(args.show)