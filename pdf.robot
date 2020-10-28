***Settings***
Library             mypdf.py


***Test Cases***
open pdf file
    ${ThePFD}       read pdf      A Sample PDF.pdf
    Log             ${ThePFD}