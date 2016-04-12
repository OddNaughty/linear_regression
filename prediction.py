def main():
    theta_file = "thetas.txt"
    with open(theta_file) as f:
        t1, t0 = [float(i.strip()) for i in f.readlines()]
        print ("I follow the linear function: '{} * x + {}'".format(t0, t1))
        mil = int(input("Mileage : ").strip())
        print ("Estimated price is: ", t0 + t1*mil)

if __name__ == '__main__':
    main()