def main():
    theta_file = "thetas.txt"
    with open(theta_file) as f:
        t0, t1, mi, ma = [float(i.strip()) for i in f.readlines()]
        print ("I follow the linear function: '{} * x + {}'".format(t0, t1))
        mil = int(input("Mileage : ").strip())
        print ("Estimated price is: ", t0 + t1*(((mil - mi) / (ma - mi))))

if __name__ == '__main__':
    main()