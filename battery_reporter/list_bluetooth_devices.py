import asyncio
from smtpd import DebuggingServer
from bleak import BleakScanner

def device_info(device):
    print(f"5: device.name >>>\n{device.name}")
    print(f"6: device.address >>>\n{device.address}")
    print(f"8: device.metadata >>>\n{device.metadata}")
    print(f"9: device.AdvertisementData >>>\n{device.AdvertisementData}")
    print(" .         ")
    print(" .         ")

async def list_connected_devices():
    devices = await BleakScanner.discover()
    if devices:
        print("Connected Bluetooth devices:")
        for device in devices:
            device_info(device)
    else:
        print("No Bluetooth devices found.")

if __name__ == "__main__":
    asyncio.run(list_connected_devices())
