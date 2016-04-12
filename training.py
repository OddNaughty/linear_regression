import csv
import matplotlib.pyplot as plt

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
    print ("t0 and t1: ", (t0, t1))
    for i in range(30000):
        t0, t1 = regression_one(km, price, t0, t1, a)
    plt.plot(price, km, 'yo', price, [t0 + t1 * x for x in price], '--k')
    plt.show()
    return (t0, t1)

def scaling(values):
    for k, v in values.items():
        mi, ma = min(v), max(v)
        values[k] = [(x - mi) / (ma - mi) for x in v]
    return values

def main():
    with open('dataset.csv') as f:
        reader = csv.DictReader(f)
        values = {key: [] for key in reader.fieldnames}
        for row in reader:
            for k, v in row.items():
                values[k].append(int(v))
        values = scaling(values)
        t0, t1 = train_algo(values['price'], values['km'])
        with open('thetas.txt', 'w') as thetas:
            thetas.write("{}\n{}\n".format(t0, t1))

if __name__ == '__main__':
    main()