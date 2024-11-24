import pytest
from television import Television
class TestTelevision:
    """Test all the methods for the TV"""
    #Creating one TV instance
    tv = Television()
    def test_init(self):
        """Testing the functionality of the tv remote."""
        #Testing original TV values before it powers on
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"
    def test_power(self):
        #Testing the state of the TV power after turning it on
        self.tv.power()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"
        #Turning off the TV and the TV power value should be set to False
        self.tv.power()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"
    def test_mute(self):
        #Testing the TV values after turning the TV on, increased volume, then mute, Volume should be 0 after mute
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"
        #Unmuting the TV, Volume should be back at 1
        self.tv.mute()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1"
        #Turning TV off and attempting to lower volume, volume should stay same since TV is off
        self.tv.power()
        self.tv.mute()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 1"
        #Attempting to Increase volume, volume should stay same since TV is off
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 1"
    def test_channel_up(self):
        #Attempting to increase channel while TV is off, channel should not go Up
        self.tv.channel_up()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 1"
        #Turning on the TV and increasing channel, channel should go up
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == "Power = True, Channel = 1, Volume = 1"
        #Going to max channel
        self.tv.channel_up()
        self.tv.channel_up()
        #Increasing the channel value after hitting the max, channel should be back at 0
        self.tv.channel_up()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1"
    def test_channel_down(self):
        """Testing the channel down method"""
        #Powering off TV and decreasing channel, channel should stay the same
        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 1"
        #Turning the TV back on and decreasing past the minimum channel Value, channel value should be at 3
        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == "Power = True, Channel = 3, Volume = 1"
    def test_volume_up(self):
        """Testing the volume up method"""
        #Testing while the tv is off and volume has been increased, volume should stay same
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = False, Channel = 3, Volume = 1"
        #Turning TV on and volume has been increased
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = True, Channel = 3, Volume = 2"
        #Decreasing Volume, Muting, and Increasing volume, volume should be at Max
        self.tv.volume_down()
        self.tv.mute()
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = True, Channel = 3, Volume = 2"
        #Trying to increase volume at the max volume, volume should stay same
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = True, Channel = 3, Volume = 2"
    def test_volume_down(self):
        """Testing the volume down method"""
        #Testing when the TV is off and volume has decreased, volume should stay same since TV is off
        self.tv.power()
        self.tv.volume_down()
        assert self.tv.__str__() == "Power = False, Channel = 3, Volume = 2"
        #powering on TV and decreasing the volume
        self.tv.power()
        self.tv.volume_down()
        assert self.tv.__str__() == "Power = True, Channel = 3, Volume = 1"
        #Muting and decreasing volume, volume should be at 0
        self.tv.mute()
        self.tv.volume_down()
        assert self.tv.__str__() == "Power = True, Channel = 3, Volume = 0"
        #attempting to decrease volume past minimum, volume should be at 0
        self.tv.volume_down()
        self.tv.volume_down()
        self.tv.volume_down()
        assert self.tv.__str__() == "Power = True, Channel = 3, Volume = 0"