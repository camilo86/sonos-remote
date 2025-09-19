from dotenv import load_dotenv
from signal import pause
from gpiozero import LED


def main():
    green_led = LED(17)
    green_led.blink()


if __name__ == "__main__":
    load_dotenv()
    main()
    pause()
