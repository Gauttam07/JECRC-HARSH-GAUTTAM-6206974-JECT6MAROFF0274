*** Settings ***
Documentation  handling dropdowns
Library  SeleniumLibrary

*** Variables ***
${url}  https://inc.in/

*** Test Cases ***
handle dropdown
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  3s

    Execute Javascript  window.scrollTo(0,document.body.scrollHeight)
    Sleep    3s

    Execute Javascript  window.scrollTo(0,0)

    Sleep    2s

    Execute Javascript  window.scrollBy(0,500)

    Sleep    2s

    Execute Javascript  window.scrollBy(0,-100)

    Sleep    2s

    Close Browser

    Close Browser