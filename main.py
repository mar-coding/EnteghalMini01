from line_code import plot_schemes as pl
from line_decode import decode as dl

def main():
    print("\n===================== Menu ======================")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit.")
    ch = int(input("Choice: "))
    if ch == 3:
        quit()
    if ch == 1:
        print("\n===================== Sub-Menu(Encode) ======================")
        print("1. Unipolar NRZ;")
        print("2. Polar NRZ-L;")
        print("3. Polar NRZ-I;")
        print("4. Polar RZ;")
        print("5. Biphase Manchester;")
        print("6. Biphase Differential Manchester")
        print("7. Bipolar AMI;")
        print("8. Pseudoternary;")
        print("9. Exit")
        print("=================================================")
        ch = int(input("Choice: "))
        if ch == 9:
            quit()
        elif ch>=1 and ch<=8:
            bits = input("Input Bits:(1/0 only)")
            if ch == 4 or ch== 8:
                while len(bits) == 4:
                    print("wrong input bits\n")
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
    elif ch == 2:
        print("\n===================== Sub-Menu(Decode) ======================")
        print("1. Unipolar NRZ(0,1)")
        print("2. Polar NRZ-L(0,1)")
        print("3. Polar NRZ-I(0,1)")
        print("4. Polar RZ(+0,-0)")
        print("5. Biphase Manchester(01,10)")
        print("6. Biphase Differential Manchester")
        print("7. Bipolar AMI(0,+,-)")
        print("8. Pseudoternary(0,+,-)")
        print("9. Exit")
        print("=================================================")
        ch = int(input("Choice: "))
        if ch == 9:
            quit()
        elif ch>=1 and ch<=8:
            bits = input("Input Bits:(1/0 or +/- only)")
            if ch == 1:
                # Unipolar NRZ
                try:
                    print(dl.decode_unipolar_nrz_to_input(bits))
                except ValueError as e:
                    print(e)
                    
            elif ch == 2:
                # Polar NRZ-L
                try:
                    print(dl.decode_nrzl_to_input(bits))
                except ValueError as e:
                    print(e)
            elif ch == 3:
                # Polar NRZ-I
                try:
                    print(dl.decode_nrzi_to_input(bits))
                except ValueError as e:
                    print(e)
            elif ch == 4:
                # Polar RZ
                try:
                    print(dl.decode_polar_rz_to_input(bits))
                except ValueError as e:
                    print(e)
            elif ch == 5:
                # Biphase Manchester
                try:
                    print(dl.decode_manchester_to_input(bits))
                except ValueError as e:
                    print(e)
            elif ch == 6:
                # Biphase Differential Manchester
                try:
                    print(dl.decode_differential_manchester_to_input(bits))
                except ValueError as e:
                    print(e)
            elif ch == 7:
                # Bipolar AMI
                try:
                    print(dl.decode_ami_to_input(bits))
                except ValueError as e:
                    print(e)
            elif ch == 8:
                # Pseudoternary
                try:
                    print(dl.decode_pseudoternary_to_input(bits))
                except ValueError as e:
                    print(e)
        else:
            print("Invalid choice!")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()