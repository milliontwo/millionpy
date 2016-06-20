# MSQ file format

## Introduction
MSQ (**M**illion **S**e**Q**uence) files are used for storing milliontwo sequences. These are sequences of states for all clocks on the milliontwo. Think of the sequence as an *animation* or a *video*. They have the extension `.msq`.

## Format
MSQ is a binary format that starts with a header:

### Header

Bytes		  | Meaning
------------|---------------------------------------------------
0..6		  | `MILLION` as ASCII (`4d 49 4c 4c 49 4f 4e` in HEX)
7			  | Version currently fixed to `0x01`
8			  | Number of clock columns (x-direction) *nColumns*
9			  | Number of clock row (y-direction) *nRows*
10			  | Framerate (frames per second)
11			  | Fixed to `0xFF`

The header is follwed by the body, always starting from byte 12

### Body

#### State representation
The state of a single clock is represented by two bytes. The first byte represents the state of the clocks a-hand, the second byte the state of the clocks b-hand.

Each hand may be positioned at 200 positions. This leads to a range of allowed values from 0 (`0x00`) to 199 (`0xC7`) for every byte in the body.

#### Frame representation
A frame consists of all the state representations for all clocks, one after another. The order is from left to right, from top down (reading direction).
Every frame gets terminated by `0xFF`. The end of a frame can be detected by scanning for `0xFF`. However, since all frames are of a fixed length, the length should alwayz be checked as well to prevent buffer overflows. 

**Thus, a Frame is always exactly (2 * nRow * nColumns) + 1 bytes long!**

### Total length
A MSQ file is thus always length(header) + length(body) = 11 + nFrames * (1 + 2 * nRow * nColumn)