Idee: Inhalt der Poster im NDEF-Format auf einem EEPROM mit RFID/NFC und I2C Schnittstelle (M24LR) ablegen um den Inhalt mit einem Handy auslesen und ihn mit einem Arduino bzw. Raspberry Pi dynamisch ändern zu können. 

* Überblick M24LR: http://www.st.com/st-web-ui/static/active/en/resource/sales_and_marketing/promotional_material/flyer/FLM24LR6400213.pdf

## Ermittlung I2C-Adressen

    sudo apt-get install i2c-tools
    sudo i2cdetect -y 1