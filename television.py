class Television:
    """
    Represents a Television with functionality to control power, mute,
    channel, and volume. The television starts off powered down with the minimum
    channel and volume set.
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initialize the Television object with default settings:
        - Powered off
        - Not muted
        - Volume set to the minimum (MIN_VOLUME)
        - Channel set to the minimum (MIN_CHANNEL)
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggle the power status of the television.
        If the television is powered off, it also unmutes the volume.
        """
        self.__status = not self.__status
        if not self.__status:
            self.__muted = False  # Reset mute when powered off

    def mute(self) -> None:
        """
        Toggle the mute status of the television if it is powered on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increase the channel by 1 if the television is powered on.
        Wrap around to MIN_CHANNEL if the channel is at MAX_CHANNEL.
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decrease the channel by 1 if the television is powered on.
        Wrap around to MAX_CHANNEL if the channel is at MIN_CHANNEL.
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increase the volume by 1 if the television is powered on and not muted.
        If the volume is muted, unmute it. The volume does not exceed MAX_VOLUME.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease the volume by 1 if the television is powered on and not muted.
        If the volume is muted, unmute it. The volume does not go below MIN_VOLUME.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Return the string representation of the television's current state.
        If muted, the volume is displayed as 0.
        """
        # Volume may be cause for not showing False on 4th test. Change.
        if self.__status:
            volume = 0 if self.__muted else self.__volume
            return f"Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{volume}]"
        else:
            return f"Power = [False], Channel = [{self.__channel}], Volume = [{self.__volume}]"
