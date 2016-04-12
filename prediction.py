def main():
    theta_file = "thetas.txt"
    with open(theta_file) as f:
        t0, t1 = [int(i.strip()) for i in f.readlines()]
        print (t0, t1)
        mil = int(input("Mileage :"))
        print ("Estimated price is: ", t0 + t1*mil)

if __name__ == '__main__':
    main()