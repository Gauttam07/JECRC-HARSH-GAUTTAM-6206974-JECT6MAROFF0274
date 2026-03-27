*** Settings ***
Documentation  Opening of browsers
Library  SeleniumLibrary
*** Variables ***
${url}  https://www.cricbuzz.com/
## scalar variable

@{bikes}    ktm  kawasaki   honda  pulsar
## list variable

&{cars}  nissan=gtr  honda=civic  bmw=m5
## dict variables

*** Test Cases ***

# robot -d reports -t "Opening Chrome Browser" open_browser.robot
# headless work for chrome and firefox
Opening headless Chrome Browser
    [Documentation]  Chrome browser navigating to https://www.cricbuzz.com/
    [Tags]  smoke
    # group to run a specific or intial test case
#     robot -d reports -i "smoke" open_browser.robot
    Open Browser  ${url}  headlesschrome
    # if we dont use double space it use default as firefox
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    ${bikes}[1]
    ## when i calling dict or list we have to chnde to scaler
    Log To Console    ${cars.nissan} ${bikes}[2]
    Sleep    3s

#    Close Browser

Opening Chrome Browser
    [Documentation]  Chrome browser navigating to https://www.cricbuzz.com/
    Open Browser  https://www.cricbuzz.com/  chrome
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    navigated to cricbuzz
    Sleep    3s

#    Close Browser

Opening Edge Browser
    Opening Edge Browser
#    Close Browser
Opening Firefox Browser
    [Documentation]  Firefox browser navigating to https://www.cricbuzz.com/
    Open Browser  https://www.cricbuzz.com/  firefox
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    navigated to cricbuzz
    Sleep    3s

    Close All Browsers
*** Keywords ***

Opening Edge Browser
    [Documentation]  Edge browser navigating to https://www.cricbuzz.com/
    Open Browser  https://www.cricbuzz.com/  edge
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    navigated to cricbuzz
    Sleep    3s
