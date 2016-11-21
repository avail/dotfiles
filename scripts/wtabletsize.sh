#! /bin/sh

# Wacom Intous CTH-680 Config

# Buton Mapping:
#
# -----------------------------
# | 3                       8 |
# ------                 ------
# | 1                       9 |
# -----------------------------

## Inital Settings

# This allows it to destinguish when it's connected to the usb or when 
# I'm using the wireless kit when I'm traveling.

w="`xsetwacom --list | grep -c "WL"`"

wired="Wacom Intuos PT M"
wireless="Wacom Intuos PT M (WL)"

if [ $w = 4 ]; then
    device=$wireless
else
    device=$wired
fi

## Muti-Monitor Setup

# This is set up for my muti-monitor setup. This allows it to detect
# when my HDMI port is connected and sets the default monitor to map to. 
# Also allows it to switch Monitors if a button on the Wacom is pressed.

p=`xrandr | grep -c "HDMI-1 connected"`

if [ $p = 1 ]; then
  primary="HDMI-1"
  secondary="eDP-1"
else
  primary="eDP-1"
  secondary="eDP-1"
fi


## List Devices into varriables to simplify commands.

stylus="Pen stylus"    
eraser="Pen eraser"    
pad="Pad pad"
touch="Finger touch"

set="xsetwacom --set "


#Stylus
$set "$device $stylus" Area 0 0 12165 9000
$set "$device $stylus" Mode Absolute
$set "$device $stylus" MapToOutput $primary

#Eraser
$set "$device $eraser" Area 0 0 12165 9000
$set "$device $eraser" Mode Absolute
$set "$device $eraser" MapToOutput $secondary

#Pad
$set "$device $pad" Button 1 "key ctl z"
$set "$device $pad" Button 3 "key ctl shift z"
$set "$device $pad" Button 8 "key ["
$set "$device $pad" Button 9 "key ]"

echo "Tablet is configured unless there are errors about"
sleep 10
