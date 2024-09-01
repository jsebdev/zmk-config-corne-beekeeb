import asyncio
from bleak import BleakScanner

async def discover_devices():
    devices = await BleakScanner.discover()
    for device in devices:
        print(f"Name: {device.name or 'Unknown'}, Address: {device.address}")

if __name__ == "__main__":
    asyncio.run(discover_devices())