import pytest

from pyfitstat.fitstat import FitStat


@pytest.fixture()
def fstat():
    return FitStat()


@pytest.fixture()
def mocked_ser_write(mocker):  # mocker is pytest-mock fixture
    mocker.patch("serial.Serial.write", return_value="Testing")


def test_pyfitstat():
    """Verify that FitStat object can be created"""
    fstat = FitStat()


def test_get_uuid(fstat):
    """The serial command for this is broken, but the host system should know it"""
    uuid = fstat.get_uuid()
    assert uuid == "test-uuid"


def test_set_color(fstat, mocked_ser_write):
    """Verify that the set color string is written to the serial port, formatted as '#FF0000'"""
    colorhex = "FF0000"
    colortuple = (0, 255, 0)

    fstat.set_color(colorhex)
    mocked_ser_write.assert_called_with(b"#FF0000\n")

    fstat.set_color(colortuple)
    mocked_ser_write.assert_called_with(b"#00FF00\n")


def test_get_color(fstat, mocked_ser_write):
    """Verify that 'G' is written to the serial port and valid data is returned"""
    color = fstat.get_color()
    mocked_ser_write.assert_called_with(b"G\n")
    assert color


def test_set_fade_time(fstat, mocked_ser_write):
    """Verify that 'Fxxxxx' is written to the serial port"""
    fstat.set_fade_time(1234)
    mocked_ser_write.assert_called_with(b"F1234\n")


def test_set_color_sequence(fstat, mocked_ser_write):
    """TODO"""
    fstat.set_color_sequence("FF0000", 200, "00FF00", 300, "0000FF", 400)
    mocked_ser_write.assert_called_with(b"B#FF0000-200#00FF00-300#0000FF-400\n")
