"""Extension that prevents the machine running the server from going to sleep
while the server is running.
"""

from contextlib import nullcontext
from trio import sleep_forever


async def run(app, configuration, logger):
    keep_display_on = bool(configuration.get("keep_display_on", False))

    try:
        from adrenaline import prevent_sleep

        context = prevent_sleep(display=keep_display_on)
    except Exception:
        context = nullcontext()
        logger.warn("Cannot prevent sleep mode on this platform")

    with context:
        await sleep_forever()