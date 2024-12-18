#Door Daniël van Belzen

from machine import Pin
import time

# Invoer pinnen instellen met ingebouwde pull-down weerstanden om zwevende waardes te voorkomen
led1 = Pin(15, Pin.IN, Pin.PULL_DOWN)  # LED-sensor 1 op pin 15
state1 = False  # Variabele om de status van led1 bij te houden

led2 = Pin(19, Pin.IN, Pin.PULL_DOWN)  # LED-sensor 2 op pin 19
state2 = False  # Variabele om de status van led2 bij te houden

led3 = Pin(22, Pin.IN, Pin.PULL_DOWN)  # LED-sensor 3 op pin 22
state3 = False  # Variabele om de status van led3 bij te houden

Button = Pin(16, Pin.IN, Pin.PULL_DOWN)  # Startknop op pin 16

# Relais instellen als uitvoer
Relay1 = Pin(17, Pin.OUT)  # Relais 1 op pin 17
Relay1.value(1)  # Zet relais 1 in de uitgeschakelde toestand
Relay2 = Pin(18, Pin.OUT)  # Relais 2 op pin 18
Relay2.value(1)  # Zet relais 2 in de uitgeschakelde toestand
Relay3 = Pin(20, Pin.OUT)  # Relais 3 op pin 20
Relay3.value(1)  # Zet relais 3 in de uitgeschakelde toestand

start_gun = False  # Variabele om aan te geven of het systeem is gestart

# Hoofdlus
while True:
    # Controleer de status van led1 en werk state1 bij
    if led1.value() == 1:  # Als led1 een signaal detecteert
        state1 = True
    else:  # Als led1 geen signaal detecteert
        state1 = False

    # Controleer de status van led2 en werk state2 bij
    if led2.value() == 1:  # Als led2 een signaal detecteert
        state2 = True
    else:  # Als led2 geen signaal detecteert
        state2 = False

    # Controleer de status van led3 en werk state3 bij
    if led3.value() == 1:  # Als led3 een signaal detecteert
        state3 = True
    else:  # Als led3 geen signaal detecteert
        state3 = False

    # Controleer of de startknop is ingedrukt
    if Button.value() == 1:
        start_gun = True  # Zet start_gun op True om het systeem te starten
        Relay1.value(0)  # Schakel relais 1 in
        Relay2.value(1)  # Zorg ervoor dat relais 2 uitgeschakeld blijft
        Relay3.value(1)  # Zorg ervoor dat relais 3 uitgeschakeld blijft

    # Als het systeem is gestart, controleer de sensoren
    if start_gun:
        if state1 == False:  # Als led1 geen signaal meer detecteert
            Relay1.value(1)  # Schakel relais 1 uit
            Relay2.value(0)  # Schakel relais 2 in
            Relay3.value(1)  # Zorg ervoor dat relais 3 uitgeschakeld blijft
        elif state2 == False:  # Als led2 geen signaal meer detecteert
            Relay1.value(1)  # Schakel relais 1 uit
            Relay2.value(1)  # Schakel relais 2 uit
            Relay3.value(0)  # Schakel relais 3 in
            start_gun = False  # Zet start_gun uit om het proces te stoppen
        elif state3 == False:  # Als led3 geen signaal meer detecteert
            Relay1.value(1)  # Schakel relais 1 uit
            Relay2.value(1)  # Schakel relais 2 uit
            Relay3.value(0)  # Schakel relais 3 in
