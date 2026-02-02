*** Settings ***
Library    RequestsLibrary

Suite Setup       Setup Suite
Suite Teardown    Teardown Suite
Test Setup        Setup Test
Test Teardown     Teardown Test

*** Variables ***
${baseurl}    http://127.0.0.1:5000

*** Keywords ***
Setup Suite
    Log    Suite setup started

Teardown Suite
    Log    Suite teardown completed

Setup Test
    Create Session    mysession    ${baseurl}

Teardown Test
    Log    Test teardown completed

*** Test Cases ***
Verify Get_User
    [Tags]    smoke    api
    ${response}=    GET On Session    mysession    /users
    Status Should Be    200    ${response}
    ${res_json}=    To Json    ${response.content}
    Log To Console    ${res_json}
