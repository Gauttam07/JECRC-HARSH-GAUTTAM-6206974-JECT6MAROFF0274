*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***
Iframe Window Handling'
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Click Element    xpath=//a[text()='Iframe with in an Iframe']
    Select Frame    xpath=//iframe[@src='MultipleFrames.html']

    Select Frame    xpath=//iframe[@src='SingleFrame.html']
    Sleep    2s
    Input Text    xpath=//input[@type="text"]    HG

    Unselect Frame
    Unselect Frame
    
    Click Element    locator
    Sleep    5s
    
    


    Close Browser