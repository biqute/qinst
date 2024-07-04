"""
Controller of the R&S FSV3030 Spectrum Analyzer.

.. module:: RS_FSV3030.py
"""

from qtics.instruments import NetworkInst


class FSV3030(NetworkInst):
    def clear(self):
        """Clear the output buffer."""
        self.write("*CLS")

    def wait(self):
        """Wait for command to be finished.

        Prevents servicing of the subsequent commands until all preceding
        commands have been executed and all signals have settled.
        """
        self.write("*WAI")

    @property
    def is_completed(self) -> bool:
        """Check if last command is completed.

        Return bool 0 (1) in the event status register (output buffer)
        when all preceding commands have been executed.
        """
        return self.query("*OPC?") == "1"

    def set_freq_span(self, min, max):
        self.write(f"SOUR:FREQ:STAR {min}")
        self.write(f"SOUR:FREQ:STOP {max}")

    def acquire_amplitude(self):
        self.query()
