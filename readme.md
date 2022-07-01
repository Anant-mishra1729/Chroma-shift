# Fast image color transfer

Image color transfer is a technique of transferring color texture of one image to another image.

# Description

## Lαβ color space
Lαβ color space is a **3-axis color system** 

<img src = "lab-color-space.png" width = 400>

* L represents lightness and α and β for the color dimensions. .
* Lαβ is the most exact representation or most **natural representation** of colors just like we humans see them.

This algorithm of color transfer was proposed in 
<a href="https://www.cs.tau.ac.il/~turkel/imagepapers/ColorTransfer.pdf">Color Transfer between images</a>

## Getting Started

### Dependencies 

* Dependencies are listed in requirements.txt

### Executing program

* Clone this repository

```
git clone https://github.com/Anant-mishra1729/Color-transfer.git
```
* Run python file color_transfer.py
```
python color_transfer.py 

--source or -s : Path to source image (Image to be used for transferring color)

--target or -t : Path to target image (Image on which color is transferred)

--result or -r : Path to resulting image
```

## Results
Images are taken from google images
|Source|Target|Result|
|---|---|---|
|<img align = "center`" src = "source/evening.jpg" width = 270 height = 250>|<img align = "center`" src = "target/colosseum.jpg" width = 270 height = 250>|<img align = "center`" src = "result/colosseum_evening.jpg" width = 270 height = 250>|
|<img align = "center`" src = "source/beach.jpg" width = 270 height = 250>|<img align = "center`" src = "target/evening.jpg" width = 270 height = 250>|<img align = "center`" src = "result/evening_morning.jpg" width = 270 height = 250>|

## Contributors

<a href="https://github.com/Anant-mishra1729">Anant Mishra</a>

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
<a href="https://www.cs.tau.ac.il/~turkel/imagepapers/ColorTransfer.pdf">Color Transfer between images</a>
