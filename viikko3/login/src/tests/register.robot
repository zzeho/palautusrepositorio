*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username    newuser
    Set Password    password123
    Set Password Confirmation    password123
    Click    button >> text=Register
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username    ab
    Set Password    password123
    Set Password Confirmation    password123
    Click    button >> text=Register
    Registration Should Fail    Username must be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username    newuser
    Set Password    12345
    Set Password Confirmation    12345
    Click    button >> text=Register
    Registration Should Fail    Password must be at least 8 characters

Register With Username That Is Already In Use
    Set Username    kalle
    Set Password    password123
    Set Password Confirmation    password123
    Click    button >> text=Register
    Registration Should Fail    Username already exists

*** Keywords ***

Registration Should Succeed
    Get Title    ==    Welcome to Ohtu Application!

Registration Should Fail
    [Arguments]    ${message}
    Register Page Should Be Open
    Get Text    body    *=    ${message}

Set Username
    [Arguments]    ${username}
    Fill Text    id=username    ${username}

Set Password
    [Arguments]    ${password}
    Fill Secret    id=password    $password

Set Password Confirmation
    [Arguments]    ${password}
    Fill Secret    id=password_confirmation    $password

Reset Application Create User And Go To Register Page
    Reset Application
    Create User    kalle    kalle123
    Go To    ${REGISTER_URL}