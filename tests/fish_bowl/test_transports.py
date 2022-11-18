import pytest
from sardine import FishBowl

from . import EventLoggingHandler, fish_bowl


@pytest.mark.asyncio
async def test_transports(fish_bowl: FishBowl):
    logger = EventLoggingHandler(("start", "stop", "pause", "resume"))
    fish_bowl.add_handler(logger)

    # No-ops
    fish_bowl.stop()
    fish_bowl.pause()
    fish_bowl.resume()

    # Regular
    fish_bowl.start()
    fish_bowl.pause()
    fish_bowl.stop()

    fish_bowl.start()
    fish_bowl.resume()  # no-op
    fish_bowl.pause()
    fish_bowl.stop()

    event_names = [e.event for e in logger.events]
    assert event_names == [
        "start", "pause", "stop",
        "start", "pause", "stop",
    ]
