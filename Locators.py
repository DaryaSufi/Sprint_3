from selenium.webdriver.common.by import By

class Locators:
    BUTTON_PERS_ACC=(By.LINK_TEXT, "Личный Кабинет")
    LINK_REG=(By.XPATH, "//a[@class='Auth_link__1fOlj']")
    INPUT_NAME=(By.XPATH,"//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")  #не смогла найти поиск по уникальному атрибуту, поэтому исплльзую нумерацию
    INPUT_EMAIL=(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input") #не смогла найти поиск по уникальному атрибуту, поэтому исплльзую нумерацию
    INPUT_PASSWORD=(By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='password']")
    BUTTON_REG=(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    BUTTON_ENTRANCE=(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    ERROR_TEXT=(By.XPATH, "//p[@class='input__error text_type_main-default']")
    BUTTON_ENTRANCE_TO_ACC=(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    INPUT_EMAIL_ENTRANCE=(By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='text']")
    INPUT_PASWWORD_ENTRANCE=(By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='password']")
    CHECKOUT_BUTTON=(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    BUTTON_PASSWORD_RECOVERY=(By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/forgot-password']")
    INPUT_EMAIL_FOR_PASS_RECOV=(By.XPATH, "//input[@class='text input__textfield text_type_main-default']")
    BUTTON_RECOVERY=(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    BUTTON_DESIGNER=(By.LINK_TEXT, "Личный Кабинет")
    TEXT_DESIGN_BURGER=(By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")
    LOGO=(By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    BUTTON_EXIT=(By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")
    BUTTON_ROLLS = (By.LINK_TEXT, "Булки")
    BUTTON_SAUCES = (By.LINK_TEXT, "Соусы")
    BUTTON_FILLINGS = (By.LINK_TEXT, "Начинки")
    LIST_OF_ROLLS = (By.LINK_TEXT, "Флюоресцентная булка")
    LIST_OF_SAUCES = (By.LINK_TEXT, "Соус Spicy-X")
    LIST_OF_FILLINGS = (By.LINK_TEXT, "Мясо бессмертных моллюсков Protostomia")
