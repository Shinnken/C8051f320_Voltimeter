from USBXpress.USBXpress import Usbxp

def main():
    print("Hello World!")
    # List USBXpress devices
    u = Usbxp()
    print (u._number())
    l = u.list()
    print (l)
    # Open USBXpress device
    u.open()
    while 1:
        # Write to USBXpress
        i = input("Enter:")
        u.write(i)
        # Read from USBXpress
        print (u.read(10))
        if i == "q": break
    # Close USBXpress
    u.close()


if __name__ == "__main__":
    main()