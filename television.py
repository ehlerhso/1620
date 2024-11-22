class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Initiate TV Variables"""
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
    def power(self):
        """Turn the TV on and Off"""
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False
    def mute(self):
        """Mute the TV volume or Unmute"""
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False
    def channel_up(self):
        """Change the channel up, change the channel to the minimum channel value if channel exceeds max channel"""
        if self.__status:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = self.MIN_CHANNEL
    def channel_down(self):
        """Change the channel down, change the channel to the maximum channel value if channel goes below minimum channel"""
        if self.__status:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.MAX_CHANNEL
    def volume_up(self):
        """Increase the TV volume only if the TV is powered on"""
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1
    def volume_down(self):
        """Decrease the TV volume only if the TV is powered on"""
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1
    def __str__(self):
        """Return the TV variables as a string"""
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {0 if self.__muted == True else self.__volume}"

