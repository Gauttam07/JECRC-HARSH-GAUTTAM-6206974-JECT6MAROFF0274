*** Settings ***
Documentation  handling Screenshot
Library  SeleniumLibrary

*** Variables ***
${url}  https://in.bookmyshow.com/explore/home/jaipur

*** Test Cases ***
Screenshots
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Set Screenshot Directory    ${CURDIR}/Screenshots
    Capture Page Screenshot    ss1.png
    Sleep    2s
    Mouse Over    xpath=//img[@alt="Dhurandhar The Revenge"]
    Sleep    2s
    Capture Element Screenshot    xpath=//img[@alt="Dhurandhar The Revenge"]  Dhurandhar.png
    Close Browser