from typing import List
from gpiozero import AnalogInputDevice
from soco import SoCo


class VolumeControl:
    def __init__(self, analog_device: AnalogInputDevice, speakers: List[SoCo]):
        self.device = analog_device
        self.speakers = speakers
        self.volume = -1

    def value(self):
        return VolumeControl.to_volume(self.device.value)

    def control(self):
        value = self.value()

        if self.volume != value:
            self.volume = value

            for speaker in self.speakers:
                speaker.volume = self.volume

            print(self.volume)

    @staticmethod
    def to_volume(value: int):
        return round((value * 100))
