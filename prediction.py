import sys

def main():
    theta_file = "thetas.txt"
    try:
        with open(theta_file) as f:
            try:
                t0, t1, mi, ma = [float(i.strip()) for i in f.readlines()]
            except ValueError:
                sys.exit("The file was ill-formed, please relaunch training")
            mil = int(input("Mileage : ").strip())
            print ("Estimated price is: ", t0 + t1*(((mil - mi) / (ma - mi))))
    except FileNotFoundError:
        print ("No training was done before, the result will be 0")
        input("Mileage : ")
        print ("Estimated price is: 0")

if __name__ == '__main__':
    main()