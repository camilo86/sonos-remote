from dotenv import load_dotenv
from soco import discover
from gpiozero import MCP3008
from utils.volume_control import VolumeControl


def main():
    speakers = list(discover())  # type: ignore
    mid = len(speakers) // 2
    speakers_group_a = speakers[:mid]
    speakers_group_b = speakers[mid:]

    pot_1 = MCP3008(channel=0)
    pot_2 = MCP3008(channel=1)
    speaker_volume_a = VolumeControl(pot_1, speakers_group_a)
    speaker_volume_b = VolumeControl(pot_2, speakers_group_b)

    while True:
        speaker_volume_a.control()
        speaker_volume_b.control()


def t_volume(value: int):
    return round(value * 100)


if __name__ == "__main__":
    load_dotenv()
    main()
