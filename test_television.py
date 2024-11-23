import pytest
from television import Television

def tv():
    return Television()

def test_initialization(tv):
    assert tv._Television__status is False
    assert tv._Television__muted is False
    assert tv._Television__volume == Television.MIN_VOLUME
    assert tv._Television__channel == Television.MIN_CHANNEL

def test_power(tv):
    tv.power()
    assert tv._Television__status is True
    tv.power()
    assert tv._Television__status is False

def test_mute(tv):
    tv.power()
    tv.volume_up()
    tv.mute()
    assert tv._Television__muted is True
    tv.mute()
    assert tv._Television__muted is False
    tv.power()
    assert tv._Television__muted is False

def test_channel_up(tv):
    tv.channel_up()
    assert tv._Television__channel == Television.MIN_CHANNEL
    tv.power()
    tv.channel_up()
    assert tv._Television__channel == 1
    tv._Television__channel = Television.MAX_CHANNEL
    tv.channel_up()
    assert tv._Television__channel == Television.MIN_CHANNEL

def test_channel_down(tv):
    tv.channel_down()
    assert tv._Television__channel == Television.MIN_CHANNEL
    tv.power()
    tv._Television__channel = Television.MIN_CHANNEL
    tv.channel_down()
    assert tv._Television__channel == Television.MAX_CHANNEL

def test_volume_up(tv):
    tv.volume_up()
    assert tv._Television__volume == Television.MIN_VOLUME
    tv.power()
    tv.volume_up()
    assert tv._Television__volume == 1
    tv.volume_up()
    assert tv._Television__volume == 2
    tv.volume_up()
    assert tv._Television__volume == Television.MAX_VOLUME
    tv.mute()
    tv.volume_up()
    assert tv._Television__muted is False
    assert tv._Television__volume == 2

def test_volume_down(tv):
    tv.volume_down()
    assert tv._Television__volume == Television.MIN_VOLUME
    tv.power()
    tv.volume_down()
    assert tv._Television__volume == Television.MIN_VOLUME
    tv.volume_up()
    tv.volume_down()
    assert tv._Television__volume == 0





        