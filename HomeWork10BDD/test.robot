*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           Selenium2Library

*** Variables ***
${LOGIN URL}      https://demo23.opencart.pro/
${ADMIN URL}      https://demo23.opencart.pro/admin
${BROWSER}        Chrome
${admin}     demo
${password}     demo
${user}       demo
${email}        Akuma@gmail.com
${message}      such robot much framework

*** Test Cases ***
Buy iMac
   Open Browser To User
    Go To Mac
    Add To Cart
    Checkout
    [Teardown]    Close Browser

Contact Us
    Open Browser To User
    Go To Contact Us
    Fill Contact Form
    Submit
    Continue From Submit
    [Teardown]    Close Browser

Login Admin
    Open Browser To Admin Page
    Login Admin
    Zoom Map
    Select Country
    [Teardown]    Close Browser


*** Keywords ***
Zoom Map
    Wait Until Page Contains Element    //*[@id="vmap"]/div[1]
    Click Element    //*[@id="vmap"]/div[1]
    Click Element    //*[@id="vmap"]/div[1]
    Click Element    //*[@id="vmap"]/div[1]

Select Country
    Click Element   //*[@id="jqvmap1_ne"]

Login Admin
    Input Text    input-username    ${admin}
    Input Text    input-password    ${password}
    Submit Form
    Title Should Be    Панель состояния

Open Browser To Admin Page
    Open Browser    ${ADMIN URL}    ${BROWSER}
    Title Should Be    Авторизация

Open Browser To User
     Open Browser    ${LOGIN URL}    ${BROWSER}

Submit
    Click Button        Применить

Continue From Submit
    Click Element    //*[@id="content"]/div/div/a

Go To Contact Us
    Click Element       //*[@id="menu"]/div[2]/ul/li[12]/a
    Title Should Be     Связаться с нами

Fill Contact Form
    Input Text    input-name    ${user}
    Input Text    input-email    ${email}
    Input Text    input-enquiry    ${message}


Go To Mac
    Click Element     //*[@id="menu"]/div[2]/ul/li[1]/a
    Click Element     //*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[1]/a
    Title Should Be     Mac

Add To Cart
    Click Element      //*[@id="content"]/div[5]/div/div/div[1]/a/img
    Click Element       //*[@id="button-cart"]


Checkout
    Title Should Be    iMac