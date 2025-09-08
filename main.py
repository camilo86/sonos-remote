from soco import discover
from soco.events import event_listener
from queue import Empty


def main_dev():
    device = discover().pop()
    subscription = device.renderingControl.subscribe()

    if not device:
        print("No device found")
        exit(1)

    print(f"Listening for events in speaker: {device.player_name}")

    while True:
        try:
            event = subscription.events.get(timeout=0.5)

            if "volume" in event.variables:
                print(f"Volume: {event.variables['volume']['Master']}")
        except Empty:
            pass
        except KeyboardInterrupt:
            subscription.unsubscribe()
            event_listener.stop()
            break


if __name__ == "__main__":
    main()
