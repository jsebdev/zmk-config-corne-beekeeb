import asyncio
from bleak import BleakScanner, BleakClient

DEVICE_ADDRESS = "D5:0D:4F:71:ED:4F"  # Replace with your device's MAC address
BATTERY_CHARACTERISTIC_UUID = "00002a19-0000-1000-8000-00805f9b34fb"

async def read_battery_level(address):
    async with BleakClient(address) as client:
        battery_level = await client.read_gatt_char(BATTERY_CHARACTERISTIC_UUID)
        print(f"Battery Level: {int(battery_level[0])}%")

async def main():
    devices = await BleakScanner.discover()
    for device in devices:
        print(f"15: device.address >>>\n{device.address}")
        if device.address == DEVICE_ADDRESS:
            print(f"Found device {device.name} - {device.address}")
            await read_battery_level(device.address)
            return
    print("Device not found")

if __name__ == "__main__":
    asyncio.run(main())