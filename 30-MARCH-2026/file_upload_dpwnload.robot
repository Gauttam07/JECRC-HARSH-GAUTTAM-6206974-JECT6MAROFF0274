*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${check-download}  C:/Users/hp5cd/Downloads/file.txt
*** Test Cases ***
Upload
    Open Browser  ${url}  chrome
    Maximize Browser Window
    
    Click Element    xpath=//a[@href="/upload"]
    Sleep    2s

    ${path}  Normalize Path  C:/Users/hp5cd/Downloads/bleh 3.jpeg

    Choose File    id=file-upload    ${path}
    Sleep    2s

    Click Button    id=file-submit

Download
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Click Element    xpath=//a[@href="/download"]
    Sleep  2s

    Click Element    xpath=//a[@href="download/file.txt"]
    Sleep    2s

    Wait Until Created    ${check-download}   timeout=10s

    File Should Exist    ${check-download}
    Log To Console    it downloaded successfully

    Close Browser

