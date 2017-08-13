## Modul eq_mail_extension

#### 20.07.2017
#### Version 1.0.12
##### FIX/CHG
- BugFix aus Odoo 10 Version übernommen (Wenn kein Standard-Mailserver vorhanden ist)

#### 20.06.2017
#### Version 1.0.11
##### FIX/CHG
- Jira Issue OBA-30: Return-Path, email_from und reply_to werden nach dem Mail Server entsprechend gesetzt (nach der Emailadresse, welcher bei dem User hinterlegt ist).

#### 10.05.2017
#### Version 1.0.10
##### CHG
- Bei einem Cronjob oder einem manuellen "Sofort senden" durch den Administrator, wird jetzt über die author_id der zu sendeten Mail der Benutzer und dementsprechend der entsprechende Mail-Server ermittelt.

#### 25.11.2016
#### Version 1.0.9
##### CHG
- Modulicon und Beschreibung angepasst. 

#### 24.11.2016
#### Version 1.0.8
##### FIX
- Print Statement entfernt.

#### 24.11.2016
#### Version 1.0.7
##### FIX
- BugFix: es wird jetzt danach abgefragt, ob der in der Datenbank (ir_values) vordefinierte Mail Server überhaupt noch vorhanden ist, bevor die Send-Methode ausgeführt wird.


#### 15.11.2016
#### Version 1.0.6
##### FIX
- Print Statement entfernt.

#### 15.11.2016
#### Version 1.0.5
##### FIX
- Übernahme einer Abfrage aus dem Equitania-Modul (siehe ReleaseNotes Equitania-Modul vom 15.01.2016: - Anpassung des Mailversandes: gültige E-Mailadresse für Return-Path)
- Durch Übernahme dieser Abfrage wird nun wieder gewährleistet, dass bei installiertem eq_mail_extension Modul auch die dazugehörige send Methode ausgeführt wird (vorher wurde die def send Methode vom Equitania Modul ausgeführt, diese ist nun aber nicht mehr vorhanden, da Übernahme der Logik in die def send des eq_mail_extension Moduls).

#### 13.07.2016
#### Version 1.0.4
##### FIX
- Übersetzungsfehler beseitigt: "The two new passwords do not match." ----> "Die neuen (vorher: alten) Passwörter stimmen nicht überein."

#### 22.06.2016
#### Version 1.0.2
##### CHG
- Abhängigkeit zum Equitania-Modul entfernt (Funktion load_translation wird nun nicht mehr aufgerufen).

#### 21.04.2016
#### Version 1.0.1
##### ADD
- Je nach ausgewählten "Default Mail Server" wird der entsprechende Benutzername direkt in die "Default Mails Server Address" eingesetzt. 
- Das Feld + Label "Alias Domain" wird nun ausgeblendet und falls ein Wert drin Stand wird dieser entfernt.

