class TV:
    def __init__(self):
        self.channel = 1 # Default channel is 1
        self.volumeLevel = 1 # default volume level is 1
        self.on = False # Initially, TV is off

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

    def getChannel(self): # Gives you the channel you are on
        return self.channel

    def setChannel(self, channel): # Sets the channel. TV has to be
        if self.on and 1 <= self.channel <= 120: # on and w/in channel
            self.channel = channel # range

    def getVolumeLevel(self): # Gives you the volume that the
        return self.volumeLevel # TV has

    def setVolume(self, volumeLevel): # Allows you to change the volume
        if self.on and \
            1 <= self.volumeLevel <= 7: # Granted, TV has to be on and
            self.volumeLevel = volumeLevel #volume must be in range

    def channelUp(self): # Raises the channel by +1
        if self.on and self.channel < 120:
            self.channel += 1

    def channelDown(self): # Lowers the channel
        if self.on and self.channel > 1:
            self.channel -= 1

    def volumeUp(self): # raises the volume
        if self.on and self.volumeLevel < 7:
            self.volumeLevel += 1

    def volumeDown(self): # Lowers the volume
        if self.on and self.volumeLevel > 1:
            self.volumeLevel -= 1