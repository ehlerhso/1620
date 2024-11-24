class Television:
    """Television Class that holds functions like a regular TV does"""
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3
    def __init__(self) -> None:
        """Regular TV values before the TV turns on"""
        self.__status: bool = False
        self.__muted:bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL
    def power(self) -> None:
        """Powers on the TV or powers off the TV"""
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False
    def mute(self) -> None:
        """Mutes the TV or unmutes the TV"""
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False
    def channel_up(self) -> None:
        """
        ONLY WORKS IF TV IS POWERED ON
        Increases the channel value, if the value exceeds the maximum channel value
        Reset the channel value to the minimum channel value
        """
        if self.__status:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = self.MIN_CHANNEL
    def channel_down(self) -> None:
        """
        ONLY WORKS IF TV IS POWERED ON
        Decreases the channel value, if the value exceeds the minimum channel value
        Reset the channel value to the maximum channel value
        """
        if self.__status:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.MAX_CHANNEL
    def volume_up(self) -> None:
        """
        ONLY WORKS IF TV IS POWERED ON
        Increases the TV Volume, If the TV is muted, unmute the TV.
        Volume cannot exceed the maximum volume value
        """
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1
    def volume_down(self) -> None:
        """
        ONLY WORKS IF THE TV IS POWERED ON
        Decreases the TV Volume, if the TV is muted, unmute the TV.
        Volume cannot go below the minimum volume value
        """
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1
    def __str__(self) -> str:
        """
        Returns the state of the TV values including the TV power, TV channel, and TV volume in the form of string
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {0 if self.__muted == True else self.__volume}"

