from line_code import plot_schemes as pl

def main():
    print("\n===================== Menu ======================")
    print("1. Unipolar NRZ")
    print("2. Polar NRZ-L")
    print("3. Polar NRZ-I")
    print("4. Polar RZ")
    print("5. Biphase Manchester")
    print("6. Biphase Differential Manchester")
    print("7. Bipolar AMI")
    print("8. Pseudoternary")
    print("9. Exit")
    print("=================================================")
    ch = int(input("Choice: "))
    if ch == 9:
        quit()
    elif ch>=1 and ch<=8:
        bits = input("Input Bits:(1/0 only)")
        if ch == 1:
            # Unipolar NRZ
            print("Plotting figure...Done!\nOpening figure window...")
            pl.plot_UNRZ(bits)
        elif ch == 2:
            # Polar NRZ-L
            print("Plotting figure...Done!\nOpening figure window...")
            pl.plot_PNRZ(bits,"nrzl")
        elif ch == 3:
            # Polar NRZ-I
            print("Plotting figure...Done!\nOpening figure window...")
            pl.plot_PNRZ(bits,"nrzi")
        elif ch == 4:
            # Polar RZ
            print("Plotting figure...Done!\nOpening figure window...")
            pl.plot_PRZ(bits)
        elif ch == 5:
            # Biphase Manchester
            print("Plotting figure...Done!\nOpening figure window...")
            pl.plot_Biphase(bits,"man")
        elif ch == 6:
            # Biphase Differential Manchester
            print("Plotting figure...Done!\nOpening figure window...")
            pl.plot_Biphase(bits,"diff")
        elif ch == 7:
            # Bipolar AMI
            print("Plotting figure...Done!\nOpening figure window...")
            pl.plot_Bipolar(bits,"ami")
        elif ch == 8:
            # Pseudoternary
            print("Plotting figure...Done!\nOpening figure window...")
            pl.plot_Bipolar(bits,"pseudo")
        print("Closing figure window...Done!")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()