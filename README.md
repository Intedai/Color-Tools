
<p align="center">
  <img src="https://github.com/Intedai/Color-Tools/blob/main/assets/LOGO.png", width="1600">
  An app that offers a wide variety of color tools for designers
</p>

## Overview
The app offers the following tools: 

* RGB and HSV Sliders
* Color picker
* Copying HEX, RGB, HSV with customizable formats
* Random color generator

## Assets  
All of the assets in this project were made by me, feel free to use them in any project you want.

## Installation
clone the repository:  
```bash
git clone https://github.com/Intedai/Color-Tools.git
```
install the required libraries
```bash
pip install -r requirements.txt
```
and run `app.py`

## Demo
### RGB, HSV Sliders and modifiable HEX
https://github.com/Intedai/Color-Tools/assets/69306633/eedd24df-7540-49c7-a994-0e790bec6711


### Color Picker
Click on the Color picker symbol and then press `k`
you can change this, look at **Editing settings** below  

https://github.com/Intedai/Color-Tools/assets/69306633/70bb85b7-d3b5-49a5-ab4f-bbf65379c157

### Random color
https://github.com/Intedai/Color-Tools/assets/69306633/0aed3843-5a40-4145-a716-0fbc103ea2dd

### Copying HEX, RGB, HSV with customizable formats  
To see how the copy formats look  at **Editing settings** below  

https://github.com/Intedai/Color-Tools/assets/69306633/f639bce5-eb14-475c-824a-acf3217ca11d

## Editing settings:
![Settings](https://github.com/Intedai/Color-Tools/assets/69306633/da93ed25-ef8f-4876-a8c1-b9da88be90c5)  

You can change the color picker keybind from `k` to any alphanumeric character  

You can choose if you want the HEX characters to be uppercase or lowercase by ticking the `Uppercase for HEX characters` option on or off  
  
You can change the copy formats of every color representation:  
`{}` is a placeholder where the first one is `R` the second one is `G` and the third one is `B` (same with HSV and HEX)  
and then you can use the format `RGB ({}, {}, {}` for example  
  
you can use maximum three `{}` if you use less you will only get R,G in RGB and HEX or H,S in hsv  
  
if you use more than three you will get an error:  
![ERROR](https://github.com/Intedai/Color-Tools/assets/69306633/d051492b-f5d3-4596-8460-3b7419f58090)

## License
Distributed under the MIT license. See `LICENSE` for more information.



