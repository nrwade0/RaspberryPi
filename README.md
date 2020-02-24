# RaspberryPi


## Timelapse

Run `get_images.py` to collect the sequence of images (see script to determine frames/interval/duration) and then run `timelapse.py` in order to build the timelapse mp4. Makes use of RaspberryPi Camera module


## Blackjack

Script to read playing card images in the works. Part of a larger blackjack simulation project. Test image is `img008.jpg`

Estimated checklist for completion:

- [ ] Reading and displaying the test image using `opencv`.
- [ ] Read the value of cards on a table. May need a better camera (?).
- [ ] Showing card values back thru command line in rpi program.
- [ ] Building a static (or dynamic, if easier) card detecting and reading system.
- [ ] Convert card-reading to real-time video using [camshift](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_video/py_meanshift/py_meanshift.html#meanshift) to follow cards on the table. Not yet sure of the limitations.
