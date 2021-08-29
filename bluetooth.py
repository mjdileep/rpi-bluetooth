# -*- coding:utf-8 -*-
# (c) All Rights Reserved
#  Dileep Jayamal

import subprocess
import time


def scan(scan_timeout=20):
    """ scan
        Scan for devices

        Parameters
        ----------
        scan_timeout : int
            Timeout to run the scan
        Returns
        ----------
        devices : dict
            set of discovered devices as MAC:Name pairs
    """
    p = subprocess.Popen(["bluetoothctl", "scan", "on"])
    time.sleep(scan_timeout)
    p.terminate()
    return __devices()


def __devices():
    """ devices
        List discovered devices

        Returns
        ----------
        devices : dict
            set of discovered devices as MAC:Name pairs
    """
    devices_s = subprocess.check_output("bluetoothctl devices", shell=True).decode().split("\n")[:-1]
    devices = {}
    for each in devices_s:
        devices[each[7:24]] = each[25:]
    return devices


def info():
    """ Info

        Returns
        ----------
        info : str
            information about the device connected currently if any
    """
    return subprocess.check_output("bluetoothctl info", shell=True).decode()


def pair(mac_address):
    """ pair
        Pair with a device

        Parameters
        ----------
        mac_address : str
           mac address of the device tha you need to pair
    """
    subprocess.check_output("bluetoothctl pair {}".format(mac_address), shell=True)


def remove(mac_address):
    """ remove
        Remove a connected(paired) device

        Parameters
        ----------
        mac_address : str
           mac address of the device tha you need to remove
    """
    subprocess.check_output("bluetoothctl remove {}".format(mac_address), shell=True)


def connect(mac_address):
    """ connect
        Connect to a device

        Parameters
        ----------
        mac_address : str
           mac address of the device tha you need to connect
    """
    subprocess.check_output("bluetoothctl connect {}".format(mac_address), shell=True)


def disconnect():
    """ disconnect
        Disconnects for currently connected device

    """
    subprocess.check_output("bluetoothctl disconnect", shell=True)


def paired_devices():
    """ paired_devices
            Return a list of paired devices

    """
    return subprocess.check_output("bluetoothctl paired-devices", shell=True).decode()

