from dotenv import load_dotenv
from soco import discover
from time import sleep
from gpiozero import MCP3008
from utils.volume_control import VolumeControl


def main():
    speakers = list(discover())  # type: ignore
    pot = MCP3008(channel=0)
    speaker_volume = VolumeControl(pot, speakers)

    while True:
        speaker_volume.control()
        sleep(1)


def t_volume(value: int):
    return round(value * 100)


if __name__ == "__main__":
    load_dotenv()
    main()
