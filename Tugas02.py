from selenium import webdriver

driver = webdriver.Chrome(executable_path='C://Program Files//chromedriver//chromedriver.exe')


link = "https://demoqa.com/webtables"
driver.get(link)
driver.maximize_window()
#PerulanganDictionary

#Data=[key:value]
dictInput = {
    'Data1':{'firstName':'Aria',
            'lastName':'Suseno', 
            'userEmail':'uno@noobtest.id',
            'age':'200',
            'salary':'9999999999',
            'department':'Store'
            },
    'Data2':{'firstName':'Ari',
            'lastName':'Susen', 
            'userEmail':'un@noobtest.id',
            'age':'20',
            'salary':'999999999',
            'department':'Stor'
            },
    'Data3':{'firstName':'Ar',
            'lastName':'Suse', 
            'userEmail':'u@noobtest.id',
            'age':'2',
            'salary':'99999999',
            'department':'Sto'
            }
        }


for data, value in dictInput.items():
    driver.find_element_by_id('addNewRecordButton').click()
    for key in value:
        driver.find_element_by_id(key).send_keys(value[key])

    driver.find_element_by_id('submit').click()

#driver.find_element_by_id('lastName').send_keys("Suseno")
#driver.find_element_by_id('userEmail').send_keys("uno@noobtest.id")
#driver.find_element_by_id('age').send_keys("200")
#driver.find_element_by_id('salary').send_keys("9999999999")
#driver.find_element_by_id('department').send_keys("Store")

#driver.close()
