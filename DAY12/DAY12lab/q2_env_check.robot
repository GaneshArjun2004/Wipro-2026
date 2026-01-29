*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Test Cases ***
Verify Environment
    Run Keyword And Continue On Failure    Check Python
    Run Keyword And Continue On Failure    Check Robot
    Log To Console    Environment verification completed

*** Keywords ***
Check Python
    ${out}=    Run    python --version
    Log To Console    Python: ${out}

Check Robot
    ${out}=    Run    robot --version
    Log To Console    Robot: ${out}
