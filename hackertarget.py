#!/usr/bin/env python
# -*- coding: utf-8 -*-

from source import hackertarget_api
import time

hackertarget_logo = """
██████╗░███╗░░██╗░██████╗  ██████╗░███████╗░█████╗░░█████╗░███╗░░██╗
██╔══██╗████╗░██║██╔════╝  ██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗░██║
██║░░██║██╔██╗██║╚█████╗░  ██████╔╝█████╗░░██║░░╚═╝██║░░██║██╔██╗██║
██║░░██║██║╚████║░╚═══██╗  ██╔══██╗██╔══╝░░██║░░██╗██║░░██║██║╚████║
██████╔╝██║░╚███║██████╔╝  ██║░░██║███████╗╚█████╔╝╚█████╔╝██║░╚███║
╚═════╝░╚═╝░░╚══╝╚═════╝░  ╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚══╝
Shubham ROoter | github.com/shubham-rooter
"""
menu = """
[1] DNS Lookup
[2] Reverse DNS
[3] Find DNS Host
[4] Find Shared DNS
[5] Zone Transfer
[6] IP Location Lookup
[7] Subnet Lookup
[8] Exit
"""

print(hackertarget_logo)
print(menu)

def run():

    try:
        choice = input("Which option number : ")

        if choice == '1':
            print("\n")
            print("[+] DNS Lookup script running..")
            target = input("[+] Target : ")
            print("\n")
            txt = hackertarget_api.hackertarget_api(3, target)
            print(txt)

        elif choice == '2':
            print("\n")
            print("[+] Reverse DNS script running..")
            target = input("[+] Target : ")
            print("\n")
            txt = hackertarget_api.hackertarget_api(4, target)
            print(txt)

        elif choice == '3':
            print("\n")
            print("[+] Find DNS Host script running..")
            target = input("[+] Target : ")
            print("\n")
            txt = hackertarget_api.hackertarget_api(5, target)
            print(txt)

        elif choice == '4':
            print("\n")
            print("[+] Find Shared DNS script running..")
            target = input("[+] Target : ")
            print("\n")
            txt = hackertarget_api.hackertarget_api(6, target)
            print(txt)

        elif choice == '5':
            print("\n")
            print("[+] Zone Transfer script running..")
            target = input("[+] Target : ")
            print("\n")
            txt = hackertarget_api.hackertarget_api(7, target)
            print(txt)

        elif choice == '6':
            print("\n")
            print("[+] IP Location Lookup script running..")
            target = input("[+] Target : ")
            print("\n")
            txt = hackertarget_api.hackertarget_api(9, target)
            print(txt)

        elif choice == '7':
            print("\n")
            print("[+] Subnet Lookup script running..")
            target = input("[+] Target : ")
            print("\n")
            txt = hackertarget_api.hackertarget_api(12, target)
            print(txt)


        elif choice == '8':
            exit()

    except KeyboardInterrupt:
        print("\nAborted!")
        quit()
    except:
        print("Invalid Option !\n")
        return run()
run()
