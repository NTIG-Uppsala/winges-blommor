from seleniumbase import BaseCase
from selenium import webdriver
import time

#Path to the site..
website = "file:/home/runner/work/florist-website/florist-website/florist-celeber/index.html"

#Path to subpage Kiruna
kirunaPage = "file:/home/runner/work/florist-website/florist-website/florist-celeber/kiruna/index.html"

#Path to subpage Luleå
luleaPage = "file:/home/runner/work/florist-website/florist-website/florist-celeber/lulea/index.html"


#----TESTS----

class chrome_test_mainpage(BaseCase):
    def test(self):
        self.open(website)
        #Find website Title
        self.assert_title("Florist Celeber")

        #Find welcome message 
        self.assert_text("Välkommen till")
        self.assert_text("FLORIST CELEBER")

        #Find header Info
        self.assert_text("BUTIKER")
        self.assert_text("HEM")
        self.assert_text("PRODUKTER")
        self.assert_text("TJÄNSTER")

        #Find footer Info
        self.assert_text("Copyright © Florist Celeber 2021")

        #Find products
        self.assert_text("PRODUKTER")
        self.assert_text("Sommarbuketter")
        self.assert_text("Från")
        self.assert_text("200 kr")
        self.assert_text("Bröllopsbuketter")
        self.assert_text("1200 kr")
        self.assert_text("Begravningskrans")
        self.assert_text("800 kr")
        self.assert_text("Höstbuketter")
        self.assert_text("400 kr")
        self.assert_text("Rosor 10-pack")
        self.assert_text("150 kr")
        self.assert_text("Tulpaner 10-pack")
        self.assert_text("100 kr")

        #Find products images
        self.assert_element('img[alt="Sommarbuketter"]')
        self.assert_element('img[alt="Bröllopsbuketter"]')
        self.assert_element('img[alt="Begravningskrans"]')
        self.assert_element('img[alt="Höstbuketter"]')
        self.assert_element('img[alt="Rosor 10-pack"]')
        self.assert_element('img[alt="Tulpaner 10-pack"]')

        #Find services image and text
        self.assert_text("Konsultation 30 min")
        self.assert_text("250 kr")

        #Find social media links
        self.assert_element('a[href="https://www.facebook.com/ntiuppsala"]') #Find Facebook link
        self.click('a[href="https://www.facebook.com/ntiuppsala"]')    #Click link
        self.go_back()    #Go back to main site

        self.assert_element('a[href="https://twitter.com/ntiuppsala"]') #Find Twitter link
        self.click('a[href="https://twitter.com/ntiuppsala"]')    #Click link
        self.go_back()    #Go back to main site

        self.assert_element('a[href="https://instagram.com/ntiuppsala"]') #Find Instagram link
        self.click('a[href="https://instagram.com/ntiuppsala"]')    #Click link
        self.go_back()    #Go back to main site


class chrome_test_kiruna(BaseCase):
    def test(self):
        self.open(kirunaPage)
        self.assert_text("KIRUNA")
        self.assert_text("Måndagar")
        self.assert_text("Tisdagar")
        self.assert_text("Onsdagar")
        self.assert_text("Torsdagar")
        self.assert_text("Fredagar")
        self.assert_text("Lördag")
        
        self.assert_text("Fjällgatan 32H")
        self.assert_text("981 39")
        self.assert_text("Kiruna")

        self.assert_text("063-055 55 55")
        self.assert_text("info@ntig-uppsala.github.io")
        self.assert_text("Fredrik Örtqvist")
        self.assert_text("Ägare")
        self.assert_text("Örjan Johansson")
        self.assert_text("Florist")
        self.assert_text("Anna Pettersson")
        self.assert_text("Hortonom")

        self.find_element("//img[@alt='Fredrik Örtqvist']") #Locates The Alt @ in all Image @ If the alt Is correct the image shall be there. Proof can be seen In screenshot
        self.find_element("//img[@alt='Anna Pettersson']")
        self.find_element("//img[@alt='Örjan Johansson']")
        
        '''dates = [
            ["new Date('13 Sep 2021 9:25:00 GMT')", "Öppnar idag kl. 10"], #monday more than 30 minutes before opening
            ["new Date('13 Sep 2021 9:55:00 GMT')", "Öppnar snart"], #monday less than 30 minutes before opening
            ["new Date('13 Sep 2021 10:05:00 GMT')", "Öppet just nu"], #monday just after opening
            ["new Date('13 Sep 2021 15:05:00 GMT')", "Stänger snart"], #monday less than 1 hour before closing
            ["new Date('13 Sep 2021 16:05:00 GMT')", "Öppnar imorgon kl. 10"], #monday just after closing

            ["new Date('14 Sep 2021 9:25:00 GMT')", "Öppnar idag kl. 10"], #tuesday more than 30 minutes before opening
            ["new Date('14 Sep 2021 9:55:00 GMT')", "Öppnar snart"], #tuesday less than 30 minutes before opening
            ["new Date('14 Sep 2021 10:05:00 GMT')", "Öppet just nu"], #tuesday just after opening
            ["new Date('14 Sep 2021 15:05:00 GMT')", "Stänger snart"], #tuesday less than 1 hour before closing
            ["new Date('14 Sep 2021 16:05:00 GMT')", "Öppnar imorgon kl. 10"], #tuesday after closing

            ["new Date('15 Sep 2021 9:25:00 GMT')", "Öppnar idag kl. 10"], #wednesday more than 30 minutes before opening
            ["new Date('15 Sep 2021 9:55:00 GMT')", "Öppnar snart"], #wednesday less than 30 minutes before opening
            ["new Date('15 Sep 2021 10:05:00 GMT')", "Öppet just nu"], #wednesday just after opening
            ["new Date('15 Sep 2021 15:05:00 GMT')", "Stänger snart"], #wednesday less than 1 hour before closing
            ["new Date('15 Sep 2021 16:05:00 GMT')", "Öppnar imorgon kl. 10"], #wednesday after closing

            ["new Date('16 Sep 2021 9:25:00 GMT')", "Öppnar idag kl. 10"], #thursday more than 30 minutes before opening
            ["new Date('16 Sep 2021 9:55:00 GMT')", "Öppnar snart"], #thursday less than 30 minutes before opening
            ["new Date('16 Sep 2021 10:05:00 GMT')", "Öppet just nu"], #thursday just after opening
            ["new Date('16 Sep 2021 15:05:00 GMT')", "Stänger snart"], #thursday less than 1 hour before closing
            ["new Date('16 Sep 2021 16:05:00 GMT')", "Öppnar imorgon kl. 10"], #thursday after closing

            ["new Date('17 Sep 2021 9:25:00 GMT')", "Öppnar idag kl. 10"], #friday more than 30 minutes before opening
            ["new Date('17 Sep 2021 9:55:00 GMT')", "Öppnar snart"], #friday less than 30 minutes before opening
            ["new Date('17 Sep 2021 10:05:00 GMT')", "Öppet just nu"], #friday just after opening
            ["new Date('17 Sep 2021 15:05:00 GMT')", "Stänger snart"], #friday less than 1 hour before closing
            ["new Date('17 Sep 2021 18:05:00 GMT')", "Öppnar imorgon kl. 12"], #friday after closing

            ["new Date('18 Sep 2021 11:25:00 GMT')", "Öppnar idag kl. 12"], #saturday more than 30 minutes before opening
            ["new Date('18 Sep 2021 11:55:00 GMT')", "Öppnar snart"], #saturday less than 30 minutes before opening
            ["new Date('18 Sep 2021 12:05:00 GMT')", "Öppet just nu"], #saturday just after opening
            ["new Date('18 Sep 2021 14:05:00 GMT')", "Stänger snart"], #saturday less than 1 hour before closing
            ["new Date('18 Sep 2021 15:05:00 GMT')", "Öppnar på måndag kl. 10"], #saturday after closing
            ["new Date('19 Sep 2021 9:25:00 GMT')", "Öppnar imorgon kl. 10"], #sunday more than 30 minutes before normal opening time
            ["new Date('19 Sep 2021 9:55:00 GMT')", "Öppnar imorgon kl. 10"], #sunday less than 30 minutes before normal opening time
            ["new Date('19 Sep 2021 10:05:00 GMT')", "Öppnar imorgon kl. 10"], #sunday just after normal opening time
            ["new Date('19 Sep 2021 15:05:00 GMT')", "Öppnar imorgon kl. 10"], #sunday less than 1 hour before normal closing time
            ["new Date('19 Sep 2021 16:05:00 GMT')", "Öppnar imorgon kl. 10"], #sunday after normal closing time

            ["new Date('13 Sep 2021 00:00:00 GMT')", "Öppnar idag kl. 10"], # monday midnight
            ["new Date('14 Sep 2021 00:00:00 GMT')", "Öppnar idag kl. 10"], # tuesday midnight
            ["new Date('15 Sep 2021 00:00:00 GMT')", "Öppnar idag kl. 10"], # wednesday midnight
            ["new Date('16 Sep 2021 00:00:00 GMT')", "Öppnar idag kl. 10"], # thursday midnight
            ["new Date('17 Sep 2021 00:00:00 GMT')", "Öppnar idag kl. 10"], # friday midnight
            ["new Date('18 Sep 2021 00:00:00 GMT')", "Öppnar idag kl. 12"], # saturday midnight
            ["new Date('19 Sep 2021 00:00:00 GMT')", "Öppnar imorgon kl. 10"] # sunday midnight
            ]
        for i in range(len(dates)):
            codeToExecute = "liveOpeningHours("+ dates[i][0] +")"
            self.execute_script(codeToExecute)
            self.assert_text(dates[i][1])
            print("index: " + str(i))'''

class chrome_test_lulea(BaseCase):
    def test(self):
        self.open(luleaPage)
        self.assert_text("LULEÅ")
        self.assert_text("Måndagar")
        self.assert_text("Tisdagar")
        self.assert_text("Onsdagar")
        self.assert_text("Torsdagar")
        self.assert_text("Fredagar")
        self.assert_text("Lördag")

        self.assert_text("Färjledsvägen 38")
        self.assert_text("961 93")
        self.assert_text("Luleå")
        self.assert_text("Södra Sunderbyn")

        self.assert_text("064-055 53 33")
        self.assert_text("info@ntig-uppsala.github.io")

        self.assert_text("Anna Andersson")
        self.assert_text("Florist")
        self.assert_text("Johan Olsson")
        self.assert_text("Florist")
        self.assert_text("Elin Nygård")
        self.assert_text("Hortonom")

        self.find_element("//img[@alt='Anna Andersson']") #Locates The Alt @ in all Image @ If the alt Is correct the image shall be there. Proof can be seen In screenshot
        self.find_element("//img[@alt='Johan Olsson']")
        self.find_element("//img[@alt='Elin Nygård']")
        

        '''dates = [
                ["new Date('13 Sep 2021 9:25:00 GMT')", "Öppnar idag kl. 10"], #monday more than 30 minutes before opening
                ["new Date('13 Sep 2021 9:55:00 GMT')", "Öppnar snart"], #monday less than 30 minutes before opening
                ["new Date('13 Sep 2021 10:05:00 GMT')", "Öppet just nu"], #monday just after opening
                ["new Date('13 Sep 2021 16:05:00 GMT')", "Stänger snart"], #monday less than 1 hour before closing
                ["new Date('13 Sep 2021 17:05:00 GMT')", "Öppnar imorgon kl. 10"], #monday just after closing

                ["new Date('14 Sep 2021 9:25:00 GMT')", "Öppnar idag kl. 10"], #tuesday more than 30 minutes before opening
                ["new Date('14 Sep 2021 9:55:00 GMT')", "Öppnar snart"], #tuesday less than 30 minutes before opening
                ["new Date('14 Sep 2021 10:05:00 GMT')", "Öppet just nu"], #tuesday just after opening
                ["new Date('14 Sep 2021 15:05:00 GMT')", "Stänger snart"], #tuesday less than 1 hour before closing
                ["new Date('14 Sep 2021 16:05:00 GMT')", "Öppnar imorgon kl. 10"], #tuesday after closing

                ["new Date('15 Sep 2021 9:25:00 GMT')", "Öppnar idag kl. 10"], #wednesday more than 30 minutes before opening
                ["new Date('15 Sep 2021 9:55:00 GMT')", "Öppnar snart"], #wednesday less than 30 minutes before opening
                ["new Date('15 Sep 2021 10:05:00 GMT')", "Öppet just nu"], #wednesday just after opening
                ["new Date('15 Sep 2021 14:05:00 GMT')", "Stänger snart"], #wednesday less than 1 hour before closing
                ["new Date('15 Sep 2021 15:05:00 GMT')", "Öppnar imorgon kl. 10"], #wednesday after closing

                ["new Date('16 Sep 2021 9:25:00 GMT')", "Öppnar idag kl. 10"], #thursday more than 30 minutes before opening
                ["new Date('16 Sep 2021 9:55:00 GMT')", "Öppnar snart"], #thursday less than 30 minutes before opening
                ["new Date('16 Sep 2021 10:05:00 GMT')", "Öppet just nu"], #thursday just after opening
                ["new Date('16 Sep 2021 15:05:00 GMT')", "Stänger snart"], #thursday less than 1 hour before closing
                ["new Date('16 Sep 2021 16:05:00 GMT')", "Öppnar imorgon kl. 10"], #thursday after closing

                ["new Date('17 Sep 2021 9:25:00 GMT')", "Öppnar idag kl. 10"], #friday more than 30 minutes before opening
                ["new Date('17 Sep 2021 9:55:00 GMT')", "Öppnar snart"], #friday less than 30 minutes before opening
                ["new Date('17 Sep 2021 10:05:00 GMT')", "Öppet just nu"], #friday just after opening
                ["new Date('17 Sep 2021 15:05:00 GMT')", "Stänger snart"], #friday less than 1 hour before closing
                ["new Date('17 Sep 2021 18:05:00 GMT')", "Öppnar imorgon kl. 12"], #friday after closing

                ["new Date('18 Sep 2021 11:25:00 GMT')", "Öppnar idag kl. 12"], #saturday more than 30 minutes before opening
                ["new Date('18 Sep 2021 11:55:00 GMT')", "Öppnar snart"], #saturday less than 30 minutes before opening
                ["new Date('18 Sep 2021 12:05:00 GMT')", "Öppet just nu"], #saturday just after opening
                ["new Date('18 Sep 2021 14:05:00 GMT')", "Stänger snart"], #saturday less than 1 hour before closing
                ["new Date('18 Sep 2021 15:05:00 GMT')", "Öppnar på måndag kl. 10"], #saturday after closing
                #SUNDAY SHOULD BE CLOSED ALL DAY!!
                ["new Date('19 Sep 2021 9:25:00 GMT')", "Öppnar imorgon kl. 10"], #sunday more than 30 minutes before normal opening time
                ["new Date('19 Sep 2021 9:55:00 GMT')", "Öppnar imorgon kl. 10"], #sunday less than 30 minutes before normal opening time
                ["new Date('19 Sep 2021 10:05:00 GMT')", "Öppnar imorgon kl. 10"], #sunday just after normal opening time
                ["new Date('19 Sep 2021 15:05:00 GMT')", "Öppnar imorgon kl. 10"], #sunday less than 1 hour before normal closing time
                ["new Date('19 Sep 2021 16:05:00 GMT')", "Öppnar imorgon kl. 10"], #sunday after normal closing time

                ["new Date('13 Sep 2021 00:00:00 GMT')", "Öppnar idag kl. 10"], # monday midnight
                ["new Date('14 Sep 2021 00:00:00 GMT')", "Öppnar idag kl. 10"], # tuesday midnight
                ["new Date('15 Sep 2021 00:00:00 GMT')", "Öppnar idag kl. 10"], # wednesday midnight
                ["new Date('16 Sep 2021 00:00:00 GMT')", "Öppnar idag kl. 10"], # thursday midnight
                ["new Date('17 Sep 2021 00:00:00 GMT')", "Öppnar idag kl. 10"], # friday midnight
                ["new Date('18 Sep 2021 00:00:00 GMT')", "Öppnar idag kl. 12"], # saturday midnight
                ["new Date('19 Sep 2021 00:00:00 GMT')", "Öppnar imorgon kl. 10"] # sunday midnight

            ]
        for i in range(len(dates)):
            codeToExecute = "liveOpeningHours("+ dates[i][0] +")"
            self.execute_script(codeToExecute)
            self.assert_text(dates[i][1])
            print("index: " + str(i))'''
