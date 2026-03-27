*** Settings ***
Documentation  action-chains
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***

Handling drag & drop
    [Documentation]  action-chains
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Sleep    1s

    Click Element    xpath = //a[text() = "Drag and Drop"]
    Sleep    1
    Drag And Drop    id = column-a    id = column-b
    Sleep    2

    Close Browser