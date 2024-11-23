import pytest
from television import Television
def test_init():
    tv_1 = Television()
    assert str(tv_1) == "Power = False, Channel = 0, Volume = 0"
    tv_1.power()
    assert str(tv_1) == "Power = True, Channel = 0, Volume = 0"
    tv_1.power()
    assert str(tv_1) == "Power = False, Channel = 0, Volume = 0"
    tv_1.volume_up()
    assert str(tv_1) == "Power = False, Channel = 0, Volume = 0"
    tv_1.power()
    tv_1.volume_up()
    assert str(tv_1) == "Power = True, Channel = 0, Volume = 1"
    tv_1.mute()
    assert str(tv_1) == "Power = True, Channel = 0, Volume = 0"
    tv_1.power()
    tv_1.mute()
    assert str(tv_1) == "Power = False, Channel = 0, Volume = 0"
    tv_1.channel_up()
    assert str(tv_1) == "Power = False, Channel = 0, Volume = 0"
    tv_1.power()
    tv_1.channel_up()
    assert str(tv_1) == "Power = True, Channel = 1, Volume = 0"
    tv_1.channel_up()
    tv_1.channel_up()
    tv_1.channel_up()
    tv_1.channel_up()
    assert str(tv_1) == "Power = True, Channel = 1, Volume = 0"
    tv_1.channel_down()
    tv_1.channel_down()
    assert str(tv_1) == "Power = True, Channel = 3, Volume = 0"
    tv_1.power()
    tv_1.channel_down()
    assert str(tv_1) == "Power = False, Channel = 3, Volume = 0"
    tv_1.volume_up()
    assert str(tv_1) == "Power = False, Channel = 3, Volume = 0"
    tv_1.power()
    tv_1.volume_up()
    assert str(tv_1) == "Power = True, Channel = 3, Volume = 2"
    tv_1.mute()
    tv_1.volume_up()
    assert str(tv_1) == "Power = True, Channel = 3, Volume = 2"
    tv_1.power()
    tv_1.volume_down()
    assert str(tv_1) == "Power = False, Channel = 3, Volume = 2"
    tv_1.power()
    tv_1.volume_down()
    assert str(tv_1) == "Power = True, Channel = 3, Volume = 1"
    tv_1.volume_down()
    tv_1.volume_down()
    tv_1.volume_down()
    tv_1.volume_down()
    tv_1.volume_down()
    assert str(tv_1) == "Power = True, Channel = 3, Volume = 0"
    tv_1.volume_up()
    tv_1.mute()
    tv_1.volume_down()
    assert str(tv_1) == "Power = True, Channel = 3, Volume = 0"
