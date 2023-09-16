class FlooStateMachineDelegate:
    def deviceDetected(self, flag: bool, port: str):
        """Called when FlooGoo device connection state changes."""
        pass

    def audioModeInd(self, mode: int):
        """Called when FlooGoo device reports current audio mode."""
        pass

    def sourceStateInd(self, state: int):
        """Called when FlooGoo device reports current source state."""
        pass

    def leAudioStateInd(self, state: int):
        """Called when FlooGoo device reports current LE audio state."""
        pass

    def broadcastModeInd(self, state: int):
        """Called when FlooGoo device reports current broadcast mode."""
        pass

    def preferLeaInd(self, state: int):
        """Called when FlooGoo device reports current preferLea mode."""
        pass

    def broadcastNameInd(self, name):
        """Called when FlooGoo device reports current LE audio state."""
        pass

    def pairedDevicesUpdateInd(self, pairedDevices):
        """Called when FlooGoo device reports current paired devices list"""
        pass

    def audioCodecInUseInd(self, codec):
        """Called when FlooGoo device reports current in use audio codec"""
        pass



