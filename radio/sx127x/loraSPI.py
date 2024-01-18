
import spidev, typing as t
from core.utils import utils


# -- bus_dev / 6 --
SPI_SPEED: int = 3_900_000


class loraSPI(object):

   def __init__(self, bus: int = 0, bus_dev: int = 0
         , bus_hz: int = SPI_SPEED, keep_open: bool = False):
      try:
         super().__init__()
         self.bus = bus
         self.bus_dev = bus_dev
         self.bus_hz = bus_hz
         self.mode: int = 0
         self.lsbfst: bool = False
         self.sysspi: spidev.SpiDev = spidev.SpiDev()
         # -- not used yet --
         self.keep_open: bool = keep_open
         self.is_opened: bool = False
      except Exception as e:
         utils.log_err(e)
      finally:
         pass

   def dump(self):
      self.sysspi.open(bus=self.bus, device=self.bus_dev)
      self.sysspi.max_speed_hz = self.bus_hz
      print(f"lsbfst: {self.sysspi.lsbfirst} | mode: {self.mode} "
         f"| hz: {self.max_speed_hz}")
      self.sysspi.close()

   def init(self):
      self.sysspi.open(bus=self.bus, device=self.bus_dev)
      self.max_speed_hz = self.bus_hz
      print((f"lsbfst: {self.sysspi.lsbfirst} | mode: {self.mode} "
         f"| hz: {self.max_speed_hz}"))
      self.sysspi.close()

   def xtfr2(self, buff: t.Iterable) -> tuple:
      try:
         self.sysspi.open(bus=self.bus, device=self.bus_dev)
         self.sysspi.max_speed_hz = self.bus_hz
         self.sysspi.lsbfirst = self.lsbfst
         self.sysspi.mode = self.mode
         return self.sysspi.xfer2(buff)
      except Exception as e:
         utils.log_err(e)
      finally:
         try:
            self.sysspi.close()
         finally:
            pass
